"""Digital PDF text extraction with line-level bounding boxes (PyMuPDF).

Returns embedded text only. Scanned pages yield no text, which tells callers to
fall back to OCR instead of trusting a partial extraction.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

REPLACEMENT_CHAR = "�"
MAX_PAGES = 500


@dataclass(frozen=True)
class PageLayout:
    page_number: int
    width: float
    height: float
    text: str
    lines: tuple[tuple[str, tuple[float, float, float, float]], ...]


def extract_digital_pdf_layout(source_path: Path) -> list[PageLayout]:
    """Return per-page text and normalized line boxes, or [] when unreadable."""

    try:
        import fitz  # PyMuPDF
    except ImportError:
        return []
    try:
        document = fitz.open(str(source_path))
    except Exception:
        return []

    pages: list[PageLayout] = []
    try:
        if document.needs_pass or document.page_count > MAX_PAGES:
            return []
        for index, page in enumerate(document, 1):
            width, height = float(page.rect.width), float(page.rect.height)
            if width <= 0 or height <= 0:
                return []
            lines: list[tuple[str, tuple[float, float, float, float]]] = []
            for block in page.get_text("dict").get("blocks", ()):
                for line in block.get("lines", ()):
                    text = "".join(span.get("text", "") for span in line.get("spans", ())).strip()
                    if not text:
                        continue
                    x0, y0, x1, y1 = line["bbox"]
                    box = (
                        max(0.0, min(1.0, x0 / width)),
                        max(0.0, min(1.0, y0 / height)),
                        max(0.0, min(1.0, x1 / width)),
                        max(0.0, min(1.0, y1 / height)),
                    )
                    lines.append((text, box))
            pages.append(
                PageLayout(
                    page_number=index,
                    width=width,
                    height=height,
                    text="\n".join(text for text, _ in lines),
                    lines=tuple(lines),
                )
            )
    except Exception:
        return []
    finally:
        document.close()
    return pages


def digital_pdf_ocr_pages(source_path: Path):
    """Return OCRPage objects (with line boxes) for a fully digital PDF, else None."""

    from .ocr_result import OCRLine, OCRPage

    layouts = extract_digital_pdf_layout(source_path)
    if not _is_usable(layouts):
        return None
    return tuple(
        OCRPage(
            page_number=layout.page_number,
            text=layout.text,
            confidence=0.98,
            lines=tuple(OCRLine(text=text, bbox=box) for text, box in layout.lines),
        )
        for layout in layouts
    )


def extract_digital_pdf_pages(source_path: Path) -> list[str]:
    """Return page texts only when every page has real embedded text, else []."""

    layouts = extract_digital_pdf_layout(source_path)
    return [page.text for page in layouts] if _is_usable(layouts) else []


def _is_usable(layouts: list[PageLayout]) -> bool:
    if not layouts or any(len(page.text.strip()) < 10 for page in layouts):
        return False
    joined = "".join(page.text for page in layouts)
    return joined.count(REPLACEMENT_CHAR) <= max(3, len(joined) // 50)
