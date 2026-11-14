"""Locate a piece of text inside an OCR result and return page boxes to highlight."""

from __future__ import annotations

from dataclasses import dataclass

from ..extraction.ocr_result import OCRResult
from ..text_normalization import normalize_for_match

MAX_QUERY_CHARS = 240
MAX_WINDOW_LINES = 3


@dataclass(frozen=True)
class SourceMatch:
    page_number: int
    boxes: tuple[tuple[float, float, float, float], ...]
    matched_text: str
    score: float


def locate(
    ocr: OCRResult,
    query: str,
    *,
    page: int | None = None,
    limit: int = 3,
    min_score: float = 72.0,
) -> list[SourceMatch]:
    """Return the best matches for ``query``, searching ``page`` first when given."""

    needle = normalize_for_match(query[:MAX_QUERY_CHARS])
    if len(needle) < 3:
        return []

    candidates = [p for p in ocr.pages if page is None or p.page_number == page]
    matches = _search(candidates, needle, min_score)
    if not matches and page is not None:
        matches = _search([p for p in ocr.pages if p.page_number != page], needle, min_score)
    matches.sort(key=lambda m: m.score, reverse=True)
    return matches[:limit]


def _search(pages, needle: str, min_score: float) -> list[SourceMatch]:
    found: list[SourceMatch] = []
    for ocr_page in pages:
        if ocr_page.lines:
            units = [(line.text, line.bbox) for line in ocr_page.lines]
        else:
            units = [(text, None) for text in ocr_page.text.splitlines() if text.strip()]
        best: SourceMatch | None = None
        for start in range(len(units)):
            for size in range(1, MAX_WINDOW_LINES + 1):
                window = units[start : start + size]
                if len(window) < size:
                    break
                text = " ".join(item[0] for item in window)
                score = _score(needle, normalize_for_match(text))
                if score >= min_score and (best is None or score > best.score):
                    boxes = tuple(item[1] for item in window if item[1] is not None)
                    best = SourceMatch(ocr_page.page_number, boxes, text, round(score, 1))
        if best is not None:
            found.append(best)
    return found


def _score(needle: str, haystack: str) -> float:
    if not haystack:
        return 0.0
    if needle in haystack:
        # Prefer the tightest window that still contains the whole text.
        return 90.0 + 10.0 * min(1.0, len(needle) / len(haystack))
    from rapidfuzz import fuzz

    return min(89.0, float(fuzz.partial_ratio(needle, haystack)))
