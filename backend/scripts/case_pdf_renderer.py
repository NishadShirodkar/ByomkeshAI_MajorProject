"""Renders a structured record (nested dict/list/scalars) as a PDF in the same layout as the
pre-existing CASE-002-Byomkesh sample documents: a repeating "DELHI POLICE / OFFICIAL DOCUMENT"
header on every page, a title block, and the data flattened into labelled fields and "Item N:"
list entries. Used by scripts/generate_detailed_case_pdfs.py.
"""

from __future__ import annotations

import io
from datetime import datetime
from xml.sax.saxutils import escape

from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.platypus import BaseDocTemplate, Frame, HRFlowable, PageTemplate, Paragraph, Spacer

HEADER_HEIGHT = 44 * mm


def _humanize(key: str) -> str:
    return key.replace("_", " ").strip()


def flatten(data) -> list[tuple[str, str]]:
    """Recursively turn a dict/list/scalar record into (kind, text) lines: header, item or field."""

    lines: list[tuple[str, str]] = []

    def walk(value, key: str | None) -> None:
        if isinstance(value, dict):
            if key is not None:
                lines.append(("header", _humanize(key).upper()))
            for sub_key, sub_value in value.items():
                walk(sub_value, sub_key)
        elif isinstance(value, (list, tuple)):
            if key is not None:
                lines.append(("header", _humanize(key).upper()))
            for index, item in enumerate(value, 1):
                lines.append(("item", f"Item {index}:"))
                if isinstance(item, (dict, list, tuple)):
                    walk(item, None)
                else:
                    lines.append(("value", str(item)))
        else:
            text = str(value)
            lines.append(("field", f"{_humanize(key).title()}: {text}" if key else text))

    walk(data, None)
    return lines


def _header_drawer(station_name: str, case_number: str):
    def draw(canvas_obj, _doc) -> None:
        canvas_obj.saveState()
        left, right = 18 * mm, A4[0] - 18 * mm
        y = A4[1] - 14 * mm
        canvas_obj.setFont("Helvetica-Bold", 10.5)
        canvas_obj.drawString(left, y, "DELHI POLICE")
        canvas_obj.setFont("Helvetica", 8)
        canvas_obj.drawRightString(right, y, station_name)
        y -= 5 * mm
        canvas_obj.setFont("Helvetica", 8.5)
        canvas_obj.drawString(left, y, f"Case: {case_number}")
        canvas_obj.drawRightString(right, y, f"Page {canvas_obj.getPageNumber()}")
        y -= 4.6 * mm
        canvas_obj.drawString(left, y, "OFFICIAL DOCUMENT")
        y -= 4.6 * mm
        canvas_obj.setFont("Helvetica-Oblique", 7.5)
        canvas_obj.setFillColor(colors.HexColor("#555555"))
        canvas_obj.drawString(left, y, "This document is a true copy of the original record")
        y -= 3.8 * mm
        canvas_obj.drawString(left, y, f"Generated: {datetime.now():%d-%m-%Y %H:%M}")
        y -= 3.8 * mm
        canvas_obj.drawString(left, y, "Confidential - For Official Use Only")
        y -= 2.2 * mm
        canvas_obj.setStrokeColor(colors.HexColor("#999999"))
        canvas_obj.setLineWidth(0.6)
        canvas_obj.line(left, y, right, y)
        canvas_obj.restoreState()

    return draw


def _styles():
    styles = getSampleStyleSheet()
    styles.add(ParagraphStyle("DocTitle", parent=styles["Title"], fontSize=13, leading=16, spaceAfter=1 * mm))
    styles.add(ParagraphStyle("Meta", parent=styles["Normal"], fontSize=9, leading=11.5))
    styles.add(ParagraphStyle("SectionHeader", parent=styles["Normal"], fontName="Helvetica-Bold", fontSize=9.6, leading=12, spaceBefore=3 * mm, spaceAfter=1 * mm, textColor=colors.HexColor("#1a1a1a")))
    styles.add(ParagraphStyle("ItemLabel", parent=styles["Normal"], fontName="Helvetica-Bold", fontSize=9, leading=12, spaceBefore=1.5 * mm))
    styles.add(ParagraphStyle("Field", parent=styles["Normal"], fontSize=9.2, leading=12.5, spaceAfter=0.6 * mm))
    return styles


def render_record_pdf(doc_title: str, station_name: str, case_number: str, fields: dict) -> bytes:
    """Render ``fields`` (plain Python dict/list/scalar values) as a CASE-002-style PDF."""

    buffer = io.BytesIO()
    styles = _styles()
    document = BaseDocTemplate(
        buffer, pagesize=A4,
        leftMargin=18 * mm, rightMargin=18 * mm, topMargin=HEADER_HEIGHT + 4 * mm, bottomMargin=16 * mm,
        title=doc_title,
    )
    frame = Frame(document.leftMargin, document.bottomMargin, document.width, document.height, id="body")
    document.addPageTemplates(PageTemplate(id="record", frames=[frame], onPage=_header_drawer(station_name, case_number)))

    story = [
        Paragraph(escape(doc_title), styles["DocTitle"]),
        Paragraph(f"Case: {escape(case_number)}", styles["Meta"]),
        Paragraph(f"Date: {datetime.now():%d-%m-%Y}", styles["Meta"]),
        HRFlowable(width="100%", thickness=0.6, color=colors.black),
        Spacer(1, 1.5 * mm),
    ]
    style_for = {"header": "SectionHeader", "item": "ItemLabel", "field": "Field", "value": "Field"}
    for kind, text in flatten({doc_title: fields}):
        story.append(Paragraph(escape(text), styles[style_for[kind]]))

    document.build(story)
    return buffer.getvalue()
