"""Serves source-document pages and text locations for click-to-source tracing."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any
from uuid import UUID

from ...extraction.ocr_result import OCRResult
from ...intake.storage_layout import CaseStorageLayout
from ...tracing.locator import locate
from ..config import api_config
from ..exceptions import ArtifactNotFoundError, CaseNotFoundError
from .case_service import parse_safe_case_id

RENDER_DPI = 130


class SourceService:
    def __init__(self, storage_root: Path | None = None) -> None:
        self.storage_root = (storage_root or api_config.storage_root).resolve()

    def _layout(self, case_id: str) -> CaseStorageLayout:
        case_uuid, _ = parse_safe_case_id(case_id)
        layout = CaseStorageLayout(self.storage_root, case_uuid)
        if not layout.case_directory.is_dir():
            raise CaseNotFoundError(case_id)
        return layout

    @staticmethod
    def _document_uuid(document_id: str) -> UUID:
        try:
            return UUID(document_id)
        except ValueError:
            raise ArtifactNotFoundError("Source document was not found.") from None

    def load_ocr(self, case_id: str, document_id: str) -> OCRResult:
        layout = self._layout(case_id)
        doc_uuid = self._document_uuid(document_id)
        ocr_directory = layout.processed_directory / "ocr"
        for path in sorted(ocr_directory.glob(f"*_{doc_uuid.hex[:8]}_OCRResult.json")):
            try:
                payload = json.loads(path.read_text(encoding="utf-8"))
                payload.pop("page_count", None)
                result = OCRResult.model_validate(payload)
            except (OSError, ValueError):
                continue
            if result.document_id == doc_uuid:
                return result
        raise ArtifactNotFoundError("OCR output for this source document was not found.")

    def _original_path(self, case_id: str, document_id: str) -> Path:
        layout = self._layout(case_id)
        doc_uuid = self._document_uuid(document_id)
        for path in layout.originals_directory.glob(f"{doc_uuid}.*"):
            if path.is_file():
                return path
        raise ArtifactNotFoundError("Original source file was not found.")

    def _manifest_entry(self, case_id: str, document_id: str) -> dict[str, Any]:
        layout = self._layout(case_id)
        try:
            manifest = json.loads((layout.processed_directory / "upload_manifest.json").read_text(encoding="utf-8"))
        except (OSError, ValueError):
            return {}
        for entry in manifest.get("entries", ()):
            source = entry.get("source_document", {})
            if str(source.get("id")) == str(self._document_uuid(document_id)):
                return source
        return {}

    def info(self, case_id: str, document_id: str) -> dict[str, Any]:
        ocr = self.load_ocr(case_id, document_id)
        source = self._manifest_entry(case_id, document_id)
        return {
            "document_id": str(ocr.document_id),
            "filename": source.get("original_filename"),
            "document_type": source.get("detected_type"),
            "page_count": ocr.page_count,
            "language": ocr.language,
            "ocr_provider": ocr.metadata.provider,
            "ocr_confidence": ocr.confidence,
            "has_line_boxes": any(page.lines for page in ocr.pages),
        }

    def render_page(self, case_id: str, document_id: str, page_number: int) -> bytes:
        path = self._original_path(case_id, document_id)
        try:
            import fitz
        except ImportError as exc:  # pragma: no cover - dependency declared in requirements
            raise ArtifactNotFoundError("Page rendering requires PyMuPDF.") from exc
        try:
            document = fitz.open(str(path))
        except Exception:
            raise ArtifactNotFoundError("This source file cannot be rendered as a page image.") from None
        try:
            if page_number < 1 or page_number > document.page_count:
                raise ArtifactNotFoundError(f"Page {page_number} does not exist in this document.")
            return document[page_number - 1].get_pixmap(dpi=RENDER_DPI).tobytes("png")
        finally:
            document.close()

    def locate(self, case_id: str, document_id: str, text: str, page: int | None) -> list[dict[str, Any]]:
        ocr = self.load_ocr(case_id, document_id)
        return [
            {
                "page_number": match.page_number,
                "boxes": [list(box) for box in match.boxes],
                "matched_text": match.matched_text,
                "score": match.score,
            }
            for match in locate(ocr, text, page=page)
        ]
