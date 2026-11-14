"""Click-to-source: locator accuracy and the source endpoints."""

from __future__ import annotations

import io
import json
from pathlib import Path
from uuid import uuid4

import pytest
from fastapi.testclient import TestClient
from reportlab.pdfgen.canvas import Canvas

from src.api.app import create_app  # noqa: F401  (module attribute check below)
from src.api.dependencies import get_storage_root
from src.extraction.ocr_result import OCRLine, OCRMetadata, OCRPage, OCRResult
from src.extraction.pdf_extractor import digital_pdf_ocr_pages
from src.intake.storage_layout import CaseStorageLayout
from src.api.services.case_service import parse_safe_case_id
from src.tracing.locator import locate

LINES = [
    "FIR No 42/2026 registered at Central Police Station",
    "Complainant Asha Devi reported theft of a motorcycle",
    "Accused Rakesh Kumar was seen fleeing towards the market",
]


def _pdf_bytes() -> bytes:
    buf = io.BytesIO()
    canvas = Canvas(buf)
    y = 780
    for line in LINES:
        canvas.drawString(50, y, line)
        y -= 20
    canvas.save()
    return buf.getvalue()


def _ocr(document_id, pages) -> OCRResult:
    return OCRResult(
        document_id=document_id,
        pages=pages,
        raw_text="\n\n".join(p.text for p in pages),
        metadata=OCRMetadata(provider="t", model="t", input_mime_type="application/pdf", processing_time_ms=1),
    )


def test_locator_finds_exact_text_and_returns_its_line_box(tmp_path: Path):
    pdf = tmp_path / "a.pdf"
    pdf.write_bytes(_pdf_bytes())
    pages = digital_pdf_ocr_pages(pdf)
    ocr = _ocr(uuid4(), pages)
    matches = locate(ocr, "Asha Devi")
    assert matches and matches[0].page_number == 1
    assert "Asha Devi" in matches[0].matched_text
    assert len(matches[0].boxes) == 1
    # second printed line sits below the first
    assert matches[0].boxes[0][1] > pages[0].lines[0].bbox[1]


def test_locator_tolerates_small_ocr_differences_and_rejects_unrelated_text():
    page = OCRPage(
        page_number=1,
        text="x",
        lines=(
            OCRLine(text="Accused Rakesh Kumar was seen fleeing", bbox=(0.1, 0.2, 0.9, 0.25)),
            OCRLine(text="towards the market", bbox=(0.1, 0.26, 0.5, 0.3)),
        ),
    )
    ocr = _ocr(uuid4(), (page,))
    assert locate(ocr, "Rakesh Kumr")  # one dropped character
    assert locate(ocr, "completely unrelated sentence about weather") == []
    assert locate(ocr, "ab") == []


def test_locator_works_on_devanagari():
    page = OCRPage(
        page_number=1,
        text="x",
        lines=(OCRLine(text="आरोपी राम कुमार फरार हो गया", bbox=(0.1, 0.1, 0.9, 0.15)),),
    )
    matches = locate(_ocr(uuid4(), (page,)), "राम कुमार")
    assert matches and matches[0].score >= 90


@pytest.fixture()
def client_and_case(tmp_path: Path):
    from src.api.app import app as fastapi_app

    root = tmp_path / "storage"
    root.mkdir()
    fastapi_app.dependency_overrides[get_storage_root] = lambda: root
    case_uuid, case_key = parse_safe_case_id("case-trace-1")
    layout = CaseStorageLayout(root, case_uuid).ensure_exists()
    doc_id = uuid4()
    pdf = layout.originals_directory / f"{doc_id}.pdf"
    pdf.write_bytes(_pdf_bytes())
    ocr = _ocr(doc_id, digital_pdf_ocr_pages(pdf))
    ocr_dir = layout.processed_directory / "ocr"
    ocr_dir.mkdir(parents=True, exist_ok=True)
    (ocr_dir / f"fir_{doc_id.hex[:8]}_OCRResult.json").write_text(
        json.dumps(ocr.model_dump(mode="json")), encoding="utf-8"
    )
    try:
        yield TestClient(fastapi_app), case_key, doc_id
    finally:
        fastapi_app.dependency_overrides.clear()


def test_source_endpoints_info_locate_and_image(client_and_case):
    client, case_key, doc_id = client_and_case
    base = f"/api/v1/cases/{case_key}/sources/{doc_id}"

    info = client.get(base).json()
    assert info["page_count"] == 1 and info["has_line_boxes"] is True

    located = client.get(f"{base}/locate", params={"text": "Central Police Station"}).json()
    assert located["matches"][0]["boxes"]

    image = client.get(f"{base}/pages/1/image")
    assert image.status_code == 200 and image.headers["content-type"] == "image/png"
    assert image.content[:8] == b"\x89PNG\r\n\x1a\n"

    assert client.get(f"{base}/pages/9/image").status_code == 404
    assert client.get(f"/api/v1/cases/{case_key}/sources/not-a-uuid").status_code == 404
    assert client.get(f"/api/v1/cases/{case_key}/sources/{uuid4()}").status_code == 404


def test_pipeline_fields_are_traceable_to_source_boxes(tmp_path: Path):
    from src.api.app import app as fastapi_app
    from src.api.dependencies import (
        get_artifact_service,
        get_case_service,
        get_job_service,
        get_review_service,
    )
    from src.api.services.artifact_service import ArtifactService
    from src.api.services.case_review_service import CaseReviewService
    from src.api.services.case_service import CaseService
    from src.api.services.job_service import JobService

    root = tmp_path.resolve()
    case_service, job_service = CaseService(root), JobService(root)
    artifact_service, review_service = ArtifactService(root), CaseReviewService(root)
    fastapi_app.dependency_overrides.update(
        {
            get_storage_root: lambda: root,
            get_case_service: lambda: case_service,
            get_job_service: lambda: job_service,
            get_artifact_service: lambda: artifact_service,
            get_review_service: lambda: review_service,
        }
    )

    def pdf(lines):
        buf = io.BytesIO()
        canvas = Canvas(buf)
        y = 780
        for line in lines:
            canvas.drawString(50, y, line)
            y -= 20
        canvas.save()
        return buf.getvalue()

    try:
        client = TestClient(fastapi_app)
        client.post("/api/v1/cases", json={"case_id": "trace-e2e", "title": "t"})
        fir = pdf(
            [
                "FIRST INFORMATION REPORT (Under Section 173 BNSS / 154 CrPC)",
                "State: Delhi District: Central Delhi Police Station: Rajinder Nagar Police Station",
                "FIR No: FIR/2024/DL/PSRKP/0452 Date Of Fir: 2024-10-15",
                "Complainant: Sunita Sharma",
                "ACCUSED DETAILS Name: Amit Verma",
                "VICTIM DETAILS Name: Rajesh Kumar Sharma",
                "Place Of Occurrence: Shankar Road T-Point, Rajinder Nagar",
                "Brief Facts: High speed collision at Shankar Road T-Point causing grievous injury.",
                "Sections: Section 281, Section 125 BNS",
            ]
        )
        upload = client.post(
            "/api/v1/cases/trace-e2e/documents", files=[("files", ("fir.pdf", fir, "application/pdf"))]
        )
        assert upload.status_code == 201
        job = job_service.wait_for_job(
            client.post("/api/v1/cases/trace-e2e/process", json={"mock_llm": True}).json()["job_id"], timeout=60.0
        )
        assert job.status == "completed"

        sheet = client.get("/api/v1/cases/trace-e2e/review").json()["charge_sheet_data"]
        traced = 0
        for field in (sheet["case_number"], sheet["police_station"]):
            ref = field["source_references"][0]
            matches = client.get(
                f"/api/v1/cases/trace-e2e/sources/{ref['document_id']}/locate",
                params={"text": field["value"]},
            ).json()["matches"]
            assert matches and matches[0]["boxes"]
            traced += 1
        assert traced == 2
    finally:
        fastapi_app.dependency_overrides.clear()
