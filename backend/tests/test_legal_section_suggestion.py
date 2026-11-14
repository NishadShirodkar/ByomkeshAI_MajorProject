"""Section suggestion: candidate selection, negation, ingredient evidence, readiness and gaps."""

from __future__ import annotations

from datetime import datetime, timezone
from pathlib import Path
from uuid import uuid4

from src.context.case_context import CaseContext
from src.domain.common import SourceLocation, SourceReference
from src.knowledge_graph.graph_models import GraphProvenance
from src.legal.ingredient_matcher import match_element, mentions
from src.legal.legal_findings import EvidenceMapping, IngredientStatus, LegalFindingStatus
from src.legal.legal_reasoner import LegalReasoner
from src.legal.legal_rules import LocalLegalReferenceProvider
from src.normalization.canonical_models import CanonicalFact

DATASET = Path(__file__).resolve().parent.parent / "references" / "legal" / "bns_sections.json"
VERSION = "bns-2023-2024-07-01"


def _fact(value: str, path: str = "medical.injuries") -> CanonicalFact:
    doc_id = uuid4()
    prov = GraphProvenance(
        document_id=doc_id,
        confidence=0.85,
        parser_name="fixture",
        timestamp=datetime.now(timezone.utc),
        source_reference=SourceReference(document_id=doc_id, location=SourceLocation(page_number=1)),
    )
    return CanonicalFact(
        value=value,
        source_document_ids=(doc_id,),
        references=(prov,),
        source_path=path,
        confidence=0.85,
        extraction_method="fixture",
        timestamp=prov.timestamp,
    )


def _narrative(*sentences: str) -> tuple[EvidenceMapping, ...]:
    doc_id = uuid4()
    return tuple(
        EvidenceMapping(
            source_document_id=doc_id,
            field_path="witness_statement.statement_text",
            description=sentence,
            source_references=(SourceReference(document_id=doc_id, excerpt=sentence),),
        )
        for sentence in sentences
    )


def _reason(context: CaseContext, narrative=()):
    provider = LocalLegalReferenceProvider.load(DATASET, VERSION)
    return LegalReasoner(provider).reason(context, narrative_evidence=narrative)


def _by_section(findings):
    return {f.proposed_section: f for f in findings.findings}


def test_single_shared_word_no_longer_establishes_an_ingredient():
    assert not match_element(
        "manner so rash or negligent as to endanger human life", (), "A person was seen near the road"
    ).supports


def test_negation_is_respected():
    assert not mentions("the injury was not fatal", ("fatal",))
    assert not mentions("non-fatal injury", ("fatal",))
    assert mentions("he died on the spot", ("died",))
    assert match_element("hurt", ("injur",), "No hurt or injury was caused").negated


def test_theft_case_suggests_theft_with_ingredient_quotes_and_gaps():
    context = CaseContext(
        case_id=uuid4(),
        medical_findings=(),
        legal_section_references=(_fact("Section 303 BNS", "fir.sections"),),
        validation_disposition="draft_allowed",
    )
    narrative = _narrative(
        "The accused stole a gold chain and a mobile phone from the shop counter.",
        "The complainant did not give permission for anyone to take the items.",
    )
    findings = _reason(context, narrative)
    sections = _by_section(findings)

    theft = sections["303"]
    assert theft.status in (LegalFindingStatus.SUPPORTED, LegalFindingStatus.REVIEW_REQUIRED)
    assert all(a.status == IngredientStatus.SUPPORTED for a in theft.ingredient_assessments)
    assert all(a.evidence_quote for a in theft.ingredient_assessments)
    assert theft.court_readiness == 1.0
    assert theft.cognizable is True and theft.bailable is False
    assert any("seizure memo" in gap for gap in theft.evidence_gaps)

    # Unrelated offences are not even proposed.
    assert "103" not in sections and "64" not in sections


def test_murder_not_suggested_for_survived_victim_and_ipc_crosswalk_note():
    context = CaseContext(
        case_id=uuid4(),
        medical_findings=(_fact("Victim alive, fracture of femur, grievous hurt, discharged after treatment"),),
        legal_section_references=(_fact("IPC 307, IPC 323", "fir.sections"),),
        validation_disposition="draft_allowed",
    )
    findings = _reason(context, _narrative("The accused stabbed the victim twice with a knife during the quarrel."))
    sections = _by_section(findings)

    assert "109" in sections  # IPC 307 crosswalks to BNS 109
    assert "115" in sections  # IPC 323 crosswalks to BNS 115
    if "103" in sections:
        assert sections["103"].status != LegalFindingStatus.SUPPORTED
    assert findings.reasoning_summary and "IPC section" in findings.reasoning_summary


def test_zero_element_reference_is_never_supported(tmp_path: Path):
    import json

    from src.legal.legal_rules import FixtureLegalReferenceProvider, LegalReference

    data = json.loads(DATASET.read_text(encoding="utf-8"))["references"][0]
    ref = dict(data)
    ref.update(required_elements=[], keywords=[])
    ref["source_reference"] = SourceReference(document_id=uuid4())
    reference = LegalReference.model_validate(ref)
    context = CaseContext(
        case_id=uuid4(),
        medical_findings=(_fact("Victim sustained injury"),),
        validation_disposition="draft_allowed",
    )
    findings = LegalReasoner(FixtureLegalReferenceProvider((reference,))).reason(context)
    assert findings.findings[0].status != LegalFindingStatus.SUPPORTED
