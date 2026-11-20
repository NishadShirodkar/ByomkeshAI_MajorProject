"""Shared building blocks for the scripted demo cases.

Each demo document carries the structured payload the parser would have produced. The source PDF is
rendered from that same payload, so the uploaded original and the parsed record never disagree.
"""

from __future__ import annotations

import io
from dataclasses import dataclass, field
from html import escape
from typing import Any, Callable

from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.platypus import HRFlowable, Paragraph, SimpleDocTemplate, Spacer


@dataclass
class DemoDocument:
    """One uploaded source document.

    ``needle`` must be a short, unique token (normally the document's own reference number) that appears
    in the rendered PDF text; the scripted parser uses it to pick this payload for the OCR'd document.
    """

    filename: str
    model_title: str
    needle: str
    heading: str
    payload: dict
    header: list[tuple[str, str]] = field(default_factory=list)


@dataclass
class DemoCase:
    case_id: str
    title: str
    station: str
    documents: Callable[[], list[DemoDocument]]
    finish: Callable[..., None] | None = None


_LABEL_OVERRIDES = {"fir": "FIR", "fsl": "FSL", "datetime": "date and time", "id": "ID"}


def _label(key: str) -> str:
    words = [_LABEL_OVERRIDES.get(word, word) for word in key.split("_")]
    text = " ".join(words)
    return text[:1].upper() + text[1:]


def _styles() -> dict[str, ParagraphStyle]:
    base = getSampleStyleSheet()
    return {
        "header": ParagraphStyle("hdr", parent=base["Normal"], fontName="Helvetica-Bold", fontSize=9, textColor="#475569"),
        "title": ParagraphStyle("ttl", parent=base["Title"], fontSize=14, leading=18, spaceAfter=6),
        "label": ParagraphStyle("lbl", parent=base["Normal"], fontName="Helvetica-Bold", fontSize=10, leading=14, spaceBefore=4, spaceAfter=2),
        "body": ParagraphStyle("body", parent=base["Normal"], fontSize=10, leading=14, spaceAfter=4),
    }


def _render_value(story: list, key: str, value: Any, styles: dict[str, ParagraphStyle]) -> None:
    if value is None or value == "" or value == [] or key in {"confidence", "warnings"}:
        return
    if isinstance(value, bool):
        story.append(Paragraph(f"<b>{escape(_label(key))}:</b> {'Yes' if value else 'No'}", styles["body"]))
    elif isinstance(value, str) and len(value) <= 140:
        story.append(Paragraph(f"<b>{escape(_label(key))}:</b> {escape(value)}", styles["body"]))
    elif isinstance(value, str):
        story.append(Paragraph(escape(_label(key)), styles["label"]))
        for paragraph in value.split("\n\n"):
            story.append(Paragraph(escape(paragraph), styles["body"]))
    elif isinstance(value, list) and value and isinstance(value[0], dict):
        story.append(Paragraph(escape(_label(key)), styles["label"]))
        for index, item in enumerate(value, 1):
            parts = "; ".join(f"<b>{escape(_label(k))}:</b> {escape(str(v))}" for k, v in item.items() if v)
            story.append(Paragraph(f"{index}. {parts}", styles["body"]))
    elif isinstance(value, list):
        story.append(Paragraph(escape(_label(key)), styles["label"]))
        for item in value:
            story.append(Paragraph(escape(str(item)), styles["body"], bulletText="•"))
    else:
        story.append(Paragraph(f"<b>{escape(_label(key))}:</b> {escape(str(value))}", styles["body"]))


def render_pdf(doc: DemoDocument, station: str) -> bytes:
    styles = _styles()
    buffer = io.BytesIO()
    template = SimpleDocTemplate(buffer, pagesize=A4, leftMargin=20 * mm, rightMargin=20 * mm, topMargin=18 * mm, bottomMargin=18 * mm)
    story: list = [
        Paragraph("GOVERNMENT OF NCT OF DELHI - DELHI POLICE", styles["header"]),
        Paragraph(escape(station), styles["header"]),
        Spacer(1, 4 * mm),
        Paragraph(escape(doc.heading), styles["title"]),
        HRFlowable(width="100%", thickness=0.5, color=colors.HexColor("#94A3B8")),
        Spacer(1, 3 * mm),
    ]
    for label, value in doc.header:
        story.append(Paragraph(f"<b>{escape(label)}:</b> {escape(value)}", styles["body"]))
    if doc.header:
        story.append(Spacer(1, 2 * mm))
    for key, value in doc.payload.items():
        _render_value(story, key, value, styles)
    template.build(story)
    return buffer.getvalue()
