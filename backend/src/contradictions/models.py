"""Typed cross-document contradiction findings."""

from __future__ import annotations

from enum import StrEnum
from uuid import UUID, uuid4

from pydantic import Field

from ..domain.common import DomainModel, SourceReference


class ContradictionKind(StrEnum):
    TIME = "time"
    DATE = "date"
    LOCATION = "location"
    VEHICLE = "vehicle"
    ACCUSED = "accused"
    VICTIM = "victim"
    LIFE_STATUS = "life_status"
    CHRONOLOGY = "chronology"


class ContradictionSeverity(StrEnum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"


class ContradictionSide(DomainModel):
    document_id: UUID
    document_label: str
    text: str
    value: str | None = None


class Contradiction(DomainModel):
    contradiction_id: UUID = Field(default_factory=uuid4)
    kind: ContradictionKind
    severity: ContradictionSeverity
    summary: str
    why_it_matters: str
    sides: tuple[ContradictionSide, ...] = Field(min_length=2)

    @property
    def source_references(self) -> tuple[SourceReference, ...]:
        return tuple(SourceReference(document_id=side.document_id, excerpt=side.text) for side in self.sides)
