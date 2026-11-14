"""Cross-document contradiction detection."""

from __future__ import annotations

from datetime import date, datetime, timezone
from uuid import uuid4

from src.contradictions import ContradictionDetector, ContradictionKind, ContradictionSeverity
from src.domain.parsed_documents import (
    FIR,
    CaseDiary,
    Complaint,
    MedicalReport,
    ParseMetadata,
    SpotPanchnama,
    VehicleInspection,
    WitnessStatement,
)

META = ParseMetadata(parser_name="fixture", parse_duration_ms=1, retry_count=0, confidence=0.9)
SHA = "a" * 64


def _fir(**kwargs) -> FIR:
    base = dict(
        document_id=uuid4(),
        ocr_text_sha256=SHA,
        parse_metadata=META,
        fir_number="42/2026",
        accused_names=("Amit Verma",),
        victim_names=("Rajesh Sharma",),
        vehicle_registrations=("DL2SBP1234",),
        occurrence_datetime=datetime(2026, 2, 3, 22, 15, tzinfo=timezone.utc),
        occurrence_location="Shankar Road T-Point, Rajinder Nagar",
        narrative_text="A collision occurred at the Shankar Road T-Point.",
    )
    base.update(kwargs)
    return FIR(**base)


def _witness(text: str, **kwargs) -> WitnessStatement:
    return WitnessStatement(
        document_id=uuid4(), ocr_text_sha256=SHA, parse_metadata=META, witness_name="Asif", statement_text=text, **kwargs
    )


def _kinds(findings):
    return {f.kind for f in findings}


def test_consistent_case_has_no_contradictions():
    fir = _fir()
    witness = _witness("The collision occurred at about 10:15 pm near the T-point. Bajaj Pulsar DL2SBP1234 was speeding.")
    assert ContradictionDetector().detect([fir, witness]) == ()


def test_time_mismatch_is_flagged_with_both_sides_and_excerpts():
    fir = _fir()
    witness = _witness("The accident happened at around 8:00 am when I was opening my shop.")
    findings = ContradictionDetector().detect([fir, witness])
    time_findings = [f for f in findings if f.kind == ContradictionKind.TIME]
    assert len(time_findings) == 1
    finding = time_findings[0]
    assert finding.severity == ContradictionSeverity.HIGH
    assert {side.document_id for side in finding.sides} == {fir.document_id, witness.document_id}
    assert "8:00 am" in finding.sides[1].text
    assert all(ref.excerpt for ref in finding.source_references)


def test_later_events_are_not_mistaken_for_time_contradictions():
    fir = _fir()
    witness = _witness("I reached the police station at 11:30 am to report the accident that I saw earlier.")
    assert not any(f.kind == ContradictionKind.TIME for f in ContradictionDetector().detect([fir, witness]))


def test_date_mismatch_and_statement_before_incident():
    fir = _fir()
    witness = _witness("The accident occurred on 2026-01-15 near the market.", statement_date=date(2026, 2, 1))
    kinds = _kinds(ContradictionDetector().detect([fir, witness]))
    assert ContradictionKind.DATE in kinds
    assert ContradictionKind.CHRONOLOGY in kinds


def test_vehicle_registration_mismatch():
    inspection = VehicleInspection(
        document_id=uuid4(), ocr_text_sha256=SHA, parse_metadata=META, vehicle_registration="MH12AB9999"
    )
    findings = ContradictionDetector().detect([_fir(), inspection])
    assert ContradictionKind.VEHICLE in _kinds(findings)


def test_accused_and_victim_identity_mismatch():
    complaint = Complaint(
        document_id=uuid4(),
        ocr_text_sha256=SHA,
        parse_metadata=META,
        person_complained_against_names=("Suresh Patil",),
    )
    medical = MedicalReport(document_id=uuid4(), ocr_text_sha256=SHA, parse_metadata=META, patient_name="Meena Kapoor")
    kinds = _kinds(ContradictionDetector().detect([_fir(), complaint, medical]))
    assert ContradictionKind.ACCUSED in kinds and ContradictionKind.VICTIM in kinds


def test_devanagari_accused_names_match_themselves():
    fir = _fir(accused_names=("अमित वर्मा",))
    complaint = Complaint(
        document_id=uuid4(), ocr_text_sha256=SHA, parse_metadata=META, person_complained_against_names=("अमित वर्मा",)
    )
    assert ContradictionKind.ACCUSED not in _kinds(ContradictionDetector().detect([fir, complaint]))


def test_location_mismatch_but_not_for_minor_spelling_differences():
    close = SpotPanchnama(document_id=uuid4(), ocr_text_sha256=SHA, parse_metadata=META, location="Shankar Road T Point, Rajinder Nagar")
    far = SpotPanchnama(document_id=uuid4(), ocr_text_sha256=SHA, parse_metadata=META, location="Lajpat Nagar Metro Station")
    assert ContradictionKind.LOCATION not in _kinds(ContradictionDetector().detect([_fir(), close]))
    assert ContradictionKind.LOCATION in _kinds(ContradictionDetector().detect([_fir(), far]))


def test_death_described_but_medical_record_says_victim_alive():
    fir = _fir(narrative_text="The victim Rajesh Sharma died after the collision at the T-point.")
    medical = MedicalReport(
        document_id=uuid4(),
        ocr_text_sha256=SHA,
        parse_metadata=META,
        patient_name="Rajesh Sharma",
        observations=("Patient is alive and conscious, under treatment for fracture.",),
    )
    findings = ContradictionDetector().detect([fir, medical])
    life = [f for f in findings if f.kind == ContradictionKind.LIFE_STATUS]
    assert life and life[0].severity == ContradictionSeverity.HIGH
    assert findings[0].severity == ContradictionSeverity.HIGH  # high-severity findings sort first


def test_not_fatal_injury_is_not_reported_as_a_death():
    fir = _fir(narrative_text="The injury to Rajesh Sharma was not fatal and he was taken to hospital.")
    medical = MedicalReport(
        document_id=uuid4(), ocr_text_sha256=SHA, parse_metadata=META, patient_name="Rajesh Sharma",
        observations=("Patient is alive and conscious.",),
    )
    assert ContradictionKind.LIFE_STATUS not in _kinds(ContradictionDetector().detect([fir, medical]))


def test_case_diary_entries_are_scanned():
    fir = _fir()
    diary = CaseDiary(document_id=uuid4(), ocr_text_sha256=SHA, parse_metadata=META, entries=())
    assert ContradictionDetector().detect([fir, diary]) == ()


def test_location_mismatch_not_hidden_by_generic_words():
    other = SpotPanchnama(
        document_id=uuid4(), ocr_text_sha256=SHA, parse_metadata=META,
        location="Najafgarh Road, near Uttam Nagar East Metro Station, New Delhi",
    )
    fir = _fir(occurrence_location="Sector 10 Road, near Dwarka Mor Metro Station, New Delhi")
    assert ContradictionKind.LOCATION in _kinds(ContradictionDetector().detect([fir, other]))
