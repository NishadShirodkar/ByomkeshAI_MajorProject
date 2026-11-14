"""Controlled, versioned legal references used by legal reasoning."""

from __future__ import annotations

import json
import re
from abc import ABC, abstractmethod
from datetime import date
from enum import StrEnum
from pathlib import Path
from uuid import NAMESPACE_URL, UUID, uuid5

from pydantic import Field, model_validator

from ..context.case_context import CaseContext
from ..domain.common import DomainModel, SourceReference


_IPC_NUMBER = re.compile(r"(\d+[A-Za-z]?)")


class LegalReferenceConfigurationError(ValueError):
    """Raised when production legal-reference data is absent, malformed, or mismatched."""


class LegalJurisdiction(StrEnum):
    INDIA = "IN"


class LegalReferenceSource(DomainModel):
    publisher: str = Field(min_length=1)
    citation: str = Field(min_length=1)
    uri: str = Field(min_length=1)


class LegalReference(DomainModel):
    section_id: UUID
    section_number: str = Field(min_length=1)
    offence_name: str = Field(min_length=1)
    description: str = Field(min_length=1)
    required_elements: tuple[str, ...] = ()
    jurisdiction: LegalJurisdiction
    effective_from: date
    effective_to: date | None = None
    source: LegalReferenceSource
    version: str = Field(min_length=1)
    source_reference: SourceReference
    statute: str = Field(default="The Bharatiya Nyaya Sanhita, 2023")
    provision_type: str = Field(default="substantive")
    legacy_ipc_equivalent: str | None = None
    verified: bool = True
    verification_date: str | None = None
    punishment: str | None = None
    cognizable: bool | None = None
    bailable: bool | None = None
    triable_by: str | None = None
    compoundable: str | None = None
    keywords: tuple[str, ...] = ()
    element_cues: dict[str, tuple[str, ...]] = Field(default_factory=dict)
    expected_documents: tuple[str, ...] = ()

    @model_validator(mode="after")
    def effective_range_is_valid(self) -> "LegalReference":
        if self.effective_to is not None and self.effective_to < self.effective_from:
            raise ValueError("effective_to cannot be before effective_from")
        return self


class LegalReferenceDataset(DomainModel):
    version: str = Field(min_length=1)
    references: tuple[LegalReference, ...] = Field(min_length=1)

    @model_validator(mode="after")
    def records_match_dataset_version(self) -> "LegalReferenceDataset":
        if any(reference.version != self.version for reference in self.references):
            raise ValueError("Every legal reference must match the dataset version")
        return self


class LegalReferenceProvider(ABC):
    @abstractmethod
    def references_for(self, context: CaseContext) -> tuple[LegalReference, ...]: ...


class FixtureLegalReferenceProvider(LegalReferenceProvider):
    """Test-only deterministic provider; production composition never selects it."""

    def __init__(self, references: tuple[LegalReference, ...] = ()) -> None:
        self.references = references

    def references_for(self, context: CaseContext) -> tuple[LegalReference, ...]:
        return self.references


class LocalLegalReferenceProvider(LegalReferenceProvider):
    """Loads only a validated, version-pinned local reference dataset."""

    def __init__(self, dataset: LegalReferenceDataset, *, source_path: Path) -> None:
        self.dataset = dataset
        self.source_path = source_path

    @classmethod
    def load(cls, path: Path | None, expected_version: str | None) -> "LocalLegalReferenceProvider":
        if path is None or not str(path).strip():
            raise LegalReferenceConfigurationError("LEGAL_REFERENCE_PATH is required for production legal reasoning")
        if not expected_version:
            raise LegalReferenceConfigurationError("LEGAL_REFERENCE_VERSION is required for production legal reasoning")
        if not path.is_file():
            raise LegalReferenceConfigurationError(f"Configured legal reference dataset was not found: {path}")
        try:
            payload = json.loads(path.read_text(encoding="utf-8"))
            records = []
            for item in payload.get("references", []):
                controlled = dict(item)
                section_id = UUID(str(controlled["section_id"]))
                controlled["source_reference"] = SourceReference(
                    document_id=uuid5(NAMESPACE_URL, f"byomkesh-legal-reference:{section_id}:{controlled['version']}")
                )
                records.append(LegalReference.model_validate(controlled))
            dataset = LegalReferenceDataset(version=payload["version"], references=tuple(records))
        except (KeyError, TypeError, ValueError, json.JSONDecodeError) as exc:
            raise LegalReferenceConfigurationError(f"Legal reference dataset is invalid: {exc}") from exc
        if dataset.version != expected_version:
            raise LegalReferenceConfigurationError(f"Legal reference version mismatch: configured '{expected_version}', dataset '{dataset.version}'")
        return cls(dataset, source_path=path)

    def references_for(self, context: CaseContext) -> tuple[LegalReference, ...]:
        return self.dataset.references

    def lookup(self, section_number: str) -> LegalReference | None:
        return next((reference for reference in self.dataset.references if reference.section_number == section_number), None)

    def bns_for_ipc(self, ipc_section: str) -> LegalReference | None:
        """Crosswalk an IPC section number (e.g. "323") to its BNS reference."""

        wanted = ipc_section.strip().upper()
        for reference in self.dataset.references:
            numbers = {n.upper() for n in _IPC_NUMBER.findall(reference.legacy_ipc_equivalent or "")}
            if wanted in numbers:
                return reference
        return None
