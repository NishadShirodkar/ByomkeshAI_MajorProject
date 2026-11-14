"""Sealed final PDF, hash-chained audit trail and tamper detection."""

from __future__ import annotations

import json
from pathlib import Path

import pytest
from fastapi.testclient import TestClient

from src.api.app import app as fastapi_app
from src.api.dependencies import get_verification_service
from src.api.services.verification_service import VerificationService
from src.chargesheet.chargesheet_populator import ChargeSheetPopulator
from src.review.audit_chain import verify_chain
from src.review.review_service import ReviewService
from src.signing.seal import seal_path_for

from test_chargesheet import context, findings


@pytest.fixture()
def finalized(tmp_path: Path):
    service = ReviewService()
    data = ChargeSheetPopulator().populate(context(), findings())
    review = service.approve(
        service.submit_for_review(service.create_draft(data), data),
        data,
        reviewer_id="officer-1",
        reviewer_name="Officer One",
    )
    done = service.finalize(review, data, storage_root=tmp_path)
    return tmp_path, str(data.case_id), done, tmp_path / done.final_artifact_reference


def test_events_form_an_unbroken_chain(finalized):
    _, _, review, _ = finalized
    ok, message = verify_chain(review.events)
    assert ok, message
    assert all(event.event_hash for event in review.events)


def test_editing_history_breaks_the_chain(finalized):
    _, _, review, _ = finalized
    forged = list(review.events)
    forged[1] = forged[1].model_copy(update={"actor_id": "someone-else"})
    ok, message = verify_chain(forged)
    assert not ok and "altered" in message
    assert not verify_chain(review.events[:0])[0]


def test_final_pdf_is_sealed_and_verifies(finalized):
    root, case_id, _, pdf = finalized
    assert seal_path_for(pdf).is_file()
    result = VerificationService(root).verify(case_id)
    assert result["verified"], result["checks"]
    assert {check["name"] for check in result["checks"]} >= {
        "Document integrity",
        "Signature",
        "Trusted signer",
        "Audit trail",
        "Audit trail matches seal",
        "Content binding",
    }


def test_one_changed_byte_fails_document_integrity(finalized):
    root, case_id, _, pdf = finalized
    original = pdf.read_bytes()
    tampered = bytearray(original)
    tampered[len(tampered) // 2] ^= 0x01
    result = VerificationService(root).verify(case_id, bytes(tampered))
    assert not result["verified"]
    failed = {check["name"] for check in result["checks"] if not check["passed"]}
    assert "Document integrity" in failed and "Embedded PDF signature" in failed
    assert failed <= {"Document integrity", "Embedded PDF signature"}
    assert VerificationService(root).verify(case_id, original)["verified"]


def test_rewriting_audit_history_is_detected(finalized):
    root, case_id, _, _ = finalized
    state = root / f"CASE_{case_id.replace('-', '')}" / "processed" / "chargesheet" / "review_state.json"
    payload = json.loads(state.read_text(encoding="utf-8"))
    payload["events"][1]["actor_id"] = "forged-officer"
    state.write_text(json.dumps(payload), encoding="utf-8")
    result = VerificationService(root).verify(case_id)
    assert not result["verified"]
    failed = {check["name"] for check in result["checks"] if not check["passed"]}
    assert "Audit trail" in failed


def test_forged_seal_from_another_key_is_not_trusted(finalized, tmp_path_factory):
    root, case_id, _, pdf = finalized
    other_root = tmp_path_factory.mktemp("other")
    from src.signing import seal_pdf

    seal_pdf(other_root, pdf, case_id=__import__("uuid").UUID(case_id), version=1, content_hash="0" * 64, audit_head="x")
    forged = json.loads(seal_path_for(pdf).read_text(encoding="utf-8"))
    # the forger's seal replaces the genuine one on disk
    real_path = seal_path_for(pdf)
    real_path.write_text(json.dumps(forged), encoding="utf-8")
    result = VerificationService(root).verify(case_id)
    assert not result["verified"]


def test_verification_endpoints_and_public_page(finalized):
    root, case_id, _, pdf = finalized
    fastapi_app.dependency_overrides[get_verification_service] = lambda: VerificationService(root)
    try:
        client = TestClient(fastapi_app)
        page = client.get(f"/verify/{case_id}")
        assert page.status_code == 200 and "Charge sheet authenticity check" in page.text

        assert client.get(f"/api/v1/cases/{case_id}/verification").json()["verified"] is True

        good = client.post(
            f"/api/v1/cases/{case_id}/verification/upload", files={"file": ("a.pdf", pdf.read_bytes(), "application/pdf")}
        )
        assert good.json()["verified"] is True and good.json()["source"] == "uploaded copy"

        bad = client.post(
            f"/api/v1/cases/{case_id}/verification/upload",
            files={"file": ("a.pdf", pdf.read_bytes() + b"\n%edited", "application/pdf")},
        )
        assert bad.json()["verified"] is False
    finally:
        fastapi_app.dependency_overrides.pop(get_verification_service, None)


def test_unfinalized_case_has_nothing_to_verify(tmp_path: Path):
    fastapi_app.dependency_overrides[get_verification_service] = lambda: VerificationService(tmp_path)
    try:
        client = TestClient(fastapi_app)
        response = client.get("/api/v1/cases/some-case/verification")
        assert response.status_code == 404
    finally:
        fastapi_app.dependency_overrides.pop(get_verification_service, None)


def test_final_pdf_carries_a_visible_embedded_signature(finalized):
    import io

    from pyhanko.pdf_utils.reader import PdfFileReader

    _, _, _, pdf = finalized
    reader = PdfFileReader(io.BytesIO(pdf.read_bytes()))
    signatures = reader.embedded_signatures
    assert len(signatures) == 1
    assert signatures[0].field_name == "OfficerApprovalSignature"
    assert signatures[0].sig_object["/Reason"].startswith("Approved and finalized charge sheet")
    # the visible stamp sits on a real page inside the page bounds
    widget_rect = [float(v) for v in signatures[0].sig_field["/Rect"]]
    assert 0 <= widget_rect[0] < widget_rect[2] <= 600 and 0 <= widget_rect[1] < widget_rect[3] <= 850
