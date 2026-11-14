"""Seeds two demo cases into the API storage so every feature can be shown without a live LLM.

  1. DEMO_COMPLETED_KarolBagh_Robbery : fully processed, approved, finalized, signed, QR-verifiable.
  2. DEMO_DRAFT_Dwarka_HitAndRun      : processed draft with planted contradictions and evidence gaps.

Both run through the real nine-stage pipeline. Only document *parsing* is scripted (it replaces the
Gemini call), so results are identical on every run. Re-running recreates the two demo cases only.

Usage (from the backend folder):  python scripts/seed_demo_cases.py [--storage-root PATH]
"""

from __future__ import annotations

import argparse
import io
import json
import os
import sys
from dataclasses import dataclass, field
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from fastapi import UploadFile  # noqa: E402
from reportlab.lib.pagesizes import A4  # noqa: E402
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet  # noqa: E402
from reportlab.lib.units import mm  # noqa: E402
from reportlab.platypus import Paragraph, SimpleDocTemplate, Spacer  # noqa: E402
from starlette.datastructures import Headers  # noqa: E402

from src.api.config import api_config  # noqa: E402
from src.api.schemas.review import AddNoteRequest, CorrectionRequest, DecisionRequest  # noqa: E402
from src.api.services.case_review_service import CaseReviewService  # noqa: E402
from src.api.services.case_service import CaseService, parse_safe_case_id  # noqa: E402
from src.extraction.mock_client import MockOCRClient  # noqa: E402
from src.intake.storage_layout import CaseStorageLayout  # noqa: E402
from src.intake.upload_manager import IncomingUpload  # noqa: E402
from src.parsers.base_parser import ParserClient, ParserError  # noqa: E402
from src.rag.embedding_provider import NoOpEmbeddingProvider  # noqa: E402
from src.workflow.production import create_workflow_context, run_production_workflow  # noqa: E402

COMPLETED_ID = "DEMO_COMPLETED_KarolBagh_Robbery"
DRAFT_ID = "DEMO_DRAFT_Dwarka_HitAndRun"
IO_ID, IO_NAME = "IO-SI-DEEPAK-RAWAT", "SI Deepak Rawat"


@dataclass
class DemoDocument:
    filename: str
    model_title: str
    needle: str
    heading: str
    fields: list[tuple[str, str]]
    paragraphs: list[str]
    payload: dict = field(default_factory=dict)


# ----------------------------------------------------------------------------- PDF rendering
def render_pdf(doc: DemoDocument, station: str) -> bytes:
    styles = getSampleStyleSheet()
    header = ParagraphStyle("hdr", parent=styles["Normal"], fontName="Helvetica-Bold", fontSize=9, textColor="#475569")
    title = ParagraphStyle("ttl", parent=styles["Title"], fontSize=15, spaceAfter=6)
    body = ParagraphStyle("body", parent=styles["Normal"], fontSize=10, leading=14, spaceAfter=4)
    buffer = io.BytesIO()
    template = SimpleDocTemplate(buffer, pagesize=A4, leftMargin=20 * mm, rightMargin=20 * mm, topMargin=18 * mm, bottomMargin=18 * mm)
    story = [Paragraph("GOVERNMENT OF NCT OF DELHI - DELHI POLICE", header), Paragraph(station, header), Spacer(1, 4 * mm), Paragraph(doc.heading, title), Spacer(1, 3 * mm)]
    for label, value in doc.fields:
        story.append(Paragraph(f"<b>{label}:</b> {value}", body))
    story.append(Spacer(1, 3 * mm))
    for paragraph in doc.paragraphs:
        story.append(Paragraph(paragraph, body))
    template.build(story)
    return buffer.getvalue()


# ----------------------------------------------------------------------------- scripted parser
class ScriptedParserClient(ParserClient):
    """Returns the authored structured payload for each document instead of calling an LLM."""

    def __init__(self, documents: list[DemoDocument]) -> None:
        self.documents = documents

    def generate_json(self, prompt: str) -> dict:
        schema = json.loads(prompt.split("Schema: ", 1)[1].split("\n\n<document_text>", 1)[0])
        text = prompt.split("<document_text>", 1)[1].rsplit("</document_text>", 1)[0].casefold()
        for doc in self.documents:
            if doc.model_title == schema["title"] and doc.needle.casefold() in text:
                return {**doc.payload, "confidence": 0.96, "warnings": []}
        raise ParserError(f"No scripted payload for {schema['title']}")


# ----------------------------------------------------------------------------- Case A: completed
A_STATION = "Karol Bagh Police Station, Central District, New Delhi"
A_NARRATIVE = (
    "On 14 August 2025 at about 10:30 pm, the complainant Neha Arora was walking home along Ajmal Khan Road, Karol Bagh, "
    "when two men on a motorcycle DL3SCX4821 stopped near Metro Pillar 112. The accused Rakesh Yadav threatened her with a knife "
    "and demanded her gold chain and mobile phone. When she resisted, the accused deliberately attacked her and slashed her on the "
    "left forearm with the knife, causing grievous hurt. The accused then robbed her of a gold chain and an iPhone 14 and fled towards "
    "Rani Jhansi Road with the second accused Sunil Chauhan."
)
A_PLACE = "Ajmal Khan Road, near Metro Pillar 112, Karol Bagh, New Delhi"


def completed_case() -> list[DemoDocument]:
    complaint_text = (
        "On the night of 14 August 2025 at about 10:30 pm I was walking home along Ajmal Khan Road near Metro Pillar 112 when two men on a "
        "motorcycle DL3SCX4821 stopped in front of me. One of them held a knife to my face and demanded my gold chain and phone. I was in "
        "great fear. When I tried to step back he slashed my left arm with the knife. They took my gold chain and my iPhone 14 without my "
        "consent and rode away towards Rani Jhansi Road. I request that strict legal action be taken against the two men."
    )
    w1 = (
        "I run a tea stall near Metro Pillar 112 on Ajmal Khan Road. On 14 August 2025 at about 10:30 pm I saw two men on a motorcycle "
        "number DL3SCX4821 stop in front of a young woman. One of the men, whom I later identified as Rakesh Yadav, pointed a knife at her. "
        "She shouted for help and he slashed her arm. The two men took her gold chain and phone without her consent and fled towards "
        "Rani Jhansi Road."
    )
    w2 = (
        "I live above the shops on Ajmal Khan Road. On 14 August 2025 at about 10:30 pm I heard a woman screaming from the street and looked "
        "down from my balcony. I saw a man with a knife and the woman bleeding from her left arm. The second man on the motorcycle DL3SCX4821 "
        "kept the engine running. The attackers rode away towards Rani Jhansi Road."
    )
    return [
        DemoDocument(
            "fir.pdf", "FIR", "0287/2025", "FIRST INFORMATION REPORT (Section 173 BNSS)",
            [("FIR No", "0287/2025"), ("Date of FIR", "15 August 2025"), ("Police Station", "Karol Bagh"), ("District", "Central Delhi"),
             ("Complainant", "Neha Arora"), ("Accused", "Rakesh Yadav, Sunil Chauhan"), ("Victim", "Neha Arora"), ("Vehicle", "DL3SCX4821"),
             ("Date and time of occurrence", "14 August 2025, 10:30 pm"), ("Place of occurrence", A_PLACE),
             ("Sections", "Section 309(4) BNS, Section 118(2) BNS"), ("Court", "Metropolitan Magistrate, Tis Hazari Courts, Delhi")],
            [f"<b>Brief facts:</b> {A_NARRATIVE}"],
            {"fir_number": "0287/2025", "crime_number": "0287/2025", "registration_date": "2025-08-15", "police_station": "Karol Bagh",
             "complainant_name": "Neha Arora", "accused_names": ["Rakesh Yadav", "Sunil Chauhan"], "victim_names": ["Neha Arora"],
             "vehicle_registrations": ["DL3SCX4821"], "occurrence_datetime": "2025-08-14T22:30:00+05:30", "occurrence_location": A_PLACE,
             "jurisdiction": "Central Delhi", "court": "Metropolitan Magistrate, Tis Hazari Courts, Delhi",
             "reported_sections": ["Section 309(4) BNS", "Section 118(2) BNS"], "narrative_text": A_NARRATIVE},
        ),
        DemoDocument(
            "complaint.pdf", "Complaint", "iPhone 14 without my", "WRITTEN COMPLAINT",
            [("Date", "15 August 2025"), ("To", "The SHO, Karol Bagh Police Station"), ("Complainant", "Neha Arora, R/o 21 Idgah Road, Karol Bagh, New Delhi"),
             ("Victim", "Neha Arora"), ("Vehicle of offenders", "DL3SCX4821")],
            [complaint_text],
            {"complaint_date": "2025-08-15", "complainant_name": "Neha Arora", "complainant_address": "21 Idgah Road, Karol Bagh, New Delhi",
             "person_complained_against_names": [], "victim_names": ["Neha Arora"], "vehicle_registrations": ["DL3SCX4821"], "complaint_text": complaint_text},
        ),
        DemoDocument(
            "witness_statement_01.pdf", "WitnessStatement", "tea stall", "STATEMENT OF WITNESS UNDER SECTION 180 BNSS",
            [("Date", "15 August 2025"), ("Witness", "Mohan Lal"), ("Age", "46"), ("Occupation", "Tea stall owner"), ("Recorded by", IO_NAME)],
            [w1],
            {"statement_date": "2025-08-15", "witness_name": "Mohan Lal", "recorded_by": IO_NAME, "age": "46", "occupation": "Tea stall owner", "statement_text": w1},
        ),
        DemoDocument(
            "witness_statement_02.pdf", "WitnessStatement", "balcony", "STATEMENT OF WITNESS UNDER SECTION 180 BNSS",
            [("Date", "15 August 2025"), ("Witness", "Pooja Sharma"), ("Age", "38"), ("Occupation", "Homemaker"), ("Recorded by", IO_NAME)],
            [w2],
            {"statement_date": "2025-08-15", "witness_name": "Pooja Sharma", "recorded_by": IO_NAME, "age": "38", "occupation": "Homemaker", "statement_text": w2},
        ),
        DemoDocument(
            "medical_report.pdf", "MedicalReport", "Neha Arora", "MEDICO-LEGAL EXAMINATION REPORT (MLC)",
            [("MLC No", "MLC/RML/2025/08841"), ("Date", "14 August 2025"), ("Hospital", "Dr. Ram Manohar Lohia Hospital, New Delhi"),
             ("Patient", "Neha Arora"), ("Age / Sex", "29 / Female"), ("Examining doctor", "Dr. Anil Kapoor")],
            ["<b>Findings:</b> Deep stab wound 6 cm long on the left forearm with injury to the extensor tendons.",
             "Fracture of the shaft of the left ulna. Patient conscious and stable, admitted for surgery.",
             "<b>Opinion:</b> The injury is grievous hurt caused by a sharp-edged weapon such as a knife. The patient is alive and under treatment."],
            {"report_number": "MLC/RML/2025/08841", "report_date": "2025-08-14", "patient_name": "Neha Arora", "doctor_name": "Dr. Anil Kapoor",
             "hospital_name": "Dr. Ram Manohar Lohia Hospital, New Delhi", "age": "29", "gender": "Female",
             "observations": ["Deep stab wound 6 cm long on the left forearm with injury to the extensor tendons", "Fracture of the shaft of the left ulna", "Patient conscious and stable, admitted for surgery"],
             "opinion_text": "The injury is grievous hurt caused by a sharp-edged weapon such as a knife. The patient is alive and under treatment."},
        ),
        DemoDocument(
            "spot_panchnama.pdf", "SpotPanchnama", "SP/KB/0087/2025", "SPOT INSPECTION MEMO (PANCHNAMA)",
            [("Memo No", "SP/KB/0087/2025"), ("Date and time", "15 August 2025, 12:40 am"), ("Place", A_PLACE), ("Panch witnesses", "Mohan Lal, Pooja Sharma")],
            ["Blood stains were found on the footpath about three metres from Metro Pillar 112.",
             "One broken gold-coloured chain link was recovered from the footpath.",
             "A CCTV camera on the opposite shop covers the spot."],
            {"memo_number": "SP/KB/0087/2025", "inspection_datetime": "2025-08-15T00:40:00+05:30", "location": A_PLACE,
             "observations": ["Blood stains were found on the footpath about three metres from Metro Pillar 112", "One broken gold-coloured chain link was recovered from the footpath", "A CCTV camera on the opposite shop covers the spot"],
             "witnesses": ["Mohan Lal", "Pooja Sharma"]},
        ),
        DemoDocument(
            "arrest_memo.pdf", "ArrestMemo", "AM/KB/0059/2025", "ARREST MEMO",
            [("Memo No", "AM/KB/0059/2025"), ("Date and time", "16 August 2025, 09:30 am"), ("Arrested person", "Rakesh Yadav"), ("Father's name", "Ramesh Yadav"),
             ("Age", "27"), ("Address", "H.No. 14, Anand Parbat, New Delhi"), ("Occupation", "Delivery rider"), ("Place of arrest", "Anand Parbat, New Delhi"),
             ("Arresting officer", IO_NAME)],
            ["The arrested person was informed of the grounds of arrest and of his right to inform a relative."],
            {"memo_number": "AM/KB/0059/2025", "arrest_datetime": "2025-08-16T09:30:00+05:30", "arrested_person_name": "Rakesh Yadav", "father_name": "Ramesh Yadav",
             "age": "27", "address": "H.No. 14, Anand Parbat, New Delhi", "occupation": "Delivery rider", "arrest_location": "Anand Parbat, New Delhi", "arresting_officer_name": IO_NAME},
        ),
        DemoDocument(
            "seizure_memo.pdf", "SeizureMemo", "SM/KB/0112/2025", "SEIZURE MEMO",
            [("Memo No", "SM/KB/0112/2025"), ("Date and time", "16 August 2025, 11:45 am"), ("Place", "Anand Parbat, New Delhi"), ("Prepared by", IO_NAME)],
            ["The following articles were recovered from the accused Rakesh Yadav at his instance and seized:",
             "EX-1: Knife with a black plastic handle and a 22 cm blade.",
             "EX-2: Gold chain (22 carat, about 18 grams), stolen property recovered from the accused.",
             "EX-3: iPhone 14, stolen property knowingly retained by the accused.",
             "EX-4: Motorcycle DL3SCX4821 (Hero Splendor)."],
            {"memo_number": "SM/KB/0112/2025", "seizure_datetime": "2025-08-16T11:45:00+05:30", "seizure_location": "Anand Parbat, New Delhi", "prepared_by": IO_NAME,
             "seized_items": [{"description": "Knife with a black plastic handle and a 22 cm blade", "exhibit_mark": "EX-1"},
                              {"description": "Gold chain (22 carat, about 18 grams), stolen property recovered from the accused", "exhibit_mark": "EX-2"},
                              {"description": "iPhone 14, stolen property knowingly retained by the accused", "exhibit_mark": "EX-3"},
                              {"description": "Motorcycle DL3SCX4821 (Hero Splendor)", "exhibit_mark": "EX-4"}]},
        ),
        DemoDocument(
            "fsl_report.pdf", "FSLReport", "FSL/DEL/2025/BIO/3318", "FORENSIC SCIENCE LABORATORY REPORT",
            [("Report No", "FSL/DEL/2025/BIO/3318"), ("Date", "28 August 2025"), ("Laboratory", "Forensic Science Laboratory, Rohini, Delhi"),
             ("Items examined", "Knife (EX-1); blood-stained clothing of the complainant")],
            ["Human blood was detected on the knife blade (EX-1).",
             "The DNA profile from the knife matches the blood of the complainant Neha Arora.",
             "<b>Opinion:</b> The blood on EX-1 is of human origin and matches the complainant."],
            {"report_number": "FSL/DEL/2025/BIO/3318", "report_date": "2025-08-28", "laboratory_name": "Forensic Science Laboratory, Rohini, Delhi",
             "examined_items": ["Knife (EX-1)", "Blood-stained clothing of the complainant"],
             "findings": ["Human blood was detected on the knife blade (EX-1)", "The DNA profile from the knife matches the blood of the complainant Neha Arora"],
             "opinion_text": "The blood on EX-1 is of human origin and matches the complainant."},
        ),
        DemoDocument(
            "case_diary.pdf", "CaseDiary", "CD/KB/0287/2025", "CASE DIARY",
            [("Diary No", "CD/KB/0287/2025"), ("Investigating officer", IO_NAME)],
            ["<b>Entry 1 (15 August 2025):</b> FIR registered and investigation taken up. Spot inspected and witnesses examined.",
             "<b>Entry 2 (16 August 2025):</b> Accused Rakesh Yadav arrested. Knife, chain, phone and motorcycle recovered at his instance.",
             "<b>Entry 3 (28 August 2025):</b> FSL report received confirming the complainant's blood on the knife. Efforts continue to trace the second accused Sunil Chauhan."],
            {"diary_number": "CD/KB/0287/2025", "officer_name": IO_NAME,
             "entries": [{"entry_number": "1", "entry_datetime": "2025-08-15T18:00:00+05:30", "text": "FIR registered and investigation taken up. Spot inspected and witnesses examined."},
                         {"entry_number": "2", "entry_datetime": "2025-08-16T14:00:00+05:30", "text": "Accused Rakesh Yadav arrested. Knife, chain, phone and motorcycle recovered at his instance."},
                         {"entry_number": "3", "entry_datetime": "2025-08-28T17:00:00+05:30", "text": "FSL report received confirming the complainant's blood on the knife. Efforts continue to trace the second accused Sunil Chauhan."}]},
        ),
    ]


# ----------------------------------------------------------------------------- Case B: incomplete draft with planted problems
B_STATION = "Dwarka Sector 23 Police Station, South West District, New Delhi"
B_NARRATIVE = (
    "On 3 September 2025 at about 11:10 pm, the complainant's brother Rohit Mehta was riding his motorcycle on Sector 10 Road near Dwarka Mor "
    "Metro Station when a speeding Maruti Swift car DL8CAF7712, driven in a rash and negligent manner by the accused Vikram Sethi, hit his "
    "motorcycle from behind. Rohit Mehta fell on the road and sustained a fracture of the right leg and head injuries. The accused did not stop "
    "the car and drove away towards Najafgarh."
)
B_PLACE = "Sector 10 Road, near Dwarka Mor Metro Station, New Delhi"


def draft_case() -> list[DemoDocument]:
    complaint_text = (
        "My brother Rohit Mehta was hit by a speeding Maruti Swift car DL8CAF7712 on Sector 10 Road in Dwarka on the night of 3 September 2025. "
        "I request legal action against Vikas Malhotra, the owner of the Maruti Swift DL8CAF7712, for the rash and negligent driving."
    )
    witness_text = (
        "I run a paan shop near the metro station in Dwarka. The accident happened at about 8:00 am when I was opening my shop. "
        "A white Maruti Swift came speeding and hit a motorcyclist, who fell on the road. The car did not stop."
    )
    return [
        DemoDocument(
            "fir.pdf", "FIR", "0412/2025", "FIRST INFORMATION REPORT (Section 173 BNSS)",
            [("FIR No", "0412/2025"), ("Date of FIR", "4 September 2025"), ("Police Station", "Dwarka Sector 23"), ("District", "South West Delhi"),
             ("Complainant", "Anil Mehta"), ("Accused", "Vikram Sethi"), ("Victim", "Rohit Mehta"), ("Vehicle", "DL8CAF7712"),
             ("Date and time of occurrence", "3 September 2025, 11:10 pm"), ("Place of occurrence", B_PLACE),
             ("Sections", "Section 281 BNS, Section 125 BNS")],
            [f"<b>Brief facts:</b> {B_NARRATIVE}"],
            {"fir_number": "0412/2025", "crime_number": "0412/2025", "registration_date": "2025-09-04", "police_station": "Dwarka Sector 23",
             "complainant_name": "Anil Mehta", "accused_names": ["Vikram Sethi"], "victim_names": ["Rohit Mehta"], "vehicle_registrations": ["DL8CAF7712"],
             "occurrence_datetime": "2025-09-03T23:10:00+05:30", "occurrence_location": B_PLACE, "jurisdiction": "South West Delhi",
             "reported_sections": ["Section 281 BNS", "Section 125 BNS"], "narrative_text": B_NARRATIVE},
        ),
        DemoDocument(
            "complaint.pdf", "Complaint", "Vikas Malhotra", "WRITTEN COMPLAINT",
            [("Date", "4 September 2025"), ("To", "The SHO, Dwarka Sector 23 Police Station"), ("Complainant", "Anil Mehta, R/o Sector 12, Dwarka, New Delhi"),
             ("Victim", "Rohit Mehta"), ("Person complained against", "Vikas Malhotra"), ("Vehicle", "DL8CAF7712")],
            [complaint_text],
            {"complaint_date": "2025-09-04", "complainant_name": "Anil Mehta", "complainant_address": "Sector 12, Dwarka, New Delhi",
             "person_complained_against_names": ["Vikas Malhotra"], "victim_names": ["Rohit Mehta"], "vehicle_registrations": ["DL8CAF7712"], "complaint_text": complaint_text},
        ),
        DemoDocument(
            "witness_statement_01.pdf", "WitnessStatement", "paan shop", "STATEMENT OF WITNESS UNDER SECTION 180 BNSS",
            [("Date", "1 September 2025"), ("Witness", "Sanjay Kumar"), ("Age", "41"), ("Occupation", "Shopkeeper"), ("Recorded by", "ASI Ramesh Chand")],
            [witness_text],
            {"statement_date": "2025-09-01", "witness_name": "Sanjay Kumar", "recorded_by": "ASI Ramesh Chand", "age": "41", "occupation": "Shopkeeper", "statement_text": witness_text},
        ),
        DemoDocument(
            "medical_report.pdf", "MedicalReport", "Rohit Mehta", "MEDICO-LEGAL EXAMINATION REPORT (MLC)",
            [("MLC No", "MLC/VH/2025/5127"), ("Date", "3 September 2025"), ("Hospital", "Venkateshwar Hospital, Dwarka, New Delhi"),
             ("Patient", "Rohit Mehta"), ("Age / Sex", "34 / Male"), ("Examining doctor", "Dr. Meera Iyer")],
            ["<b>Findings:</b> Fracture of the shaft of the right femur. Scalp laceration 5 cm over the right parietal region.",
             "Patient conscious and oriented, admitted to the orthopaedic ward, condition stable.",
             "<b>Opinion:</b> The injuries are grievous in nature (fracture). The patient is alive and under treatment."],
            {"report_number": "MLC/VH/2025/5127", "report_date": "2025-09-03", "patient_name": "Rohit Mehta", "doctor_name": "Dr. Meera Iyer",
             "hospital_name": "Venkateshwar Hospital, Dwarka, New Delhi", "age": "34", "gender": "Male",
             "observations": ["Fracture of the shaft of the right femur", "Scalp laceration 5 cm over the right parietal region", "Patient conscious and oriented, admitted to the orthopaedic ward, condition stable"],
             "opinion_text": "The injuries are grievous in nature (fracture). The patient is alive and under treatment."},
        ),
        DemoDocument(
            "spot_panchnama.pdf", "SpotPanchnama", "SP/DW/0143/2025", "SPOT INSPECTION MEMO (PANCHNAMA)",
            [("Memo No", "SP/DW/0143/2025"), ("Date and time", "4 September 2025, 12:30 am"), ("Place", "Najafgarh Road, near Uttam Nagar East Metro Station, New Delhi")],
            ["Skid marks about 12 metres long were found on the road surface.", "Broken pieces of a motorcycle headlight were found near the divider."],
            {"memo_number": "SP/DW/0143/2025", "inspection_datetime": "2025-09-04T00:30:00+05:30", "location": "Najafgarh Road, near Uttam Nagar East Metro Station, New Delhi",
             "observations": ["Skid marks about 12 metres long were found on the road surface", "Broken pieces of a motorcycle headlight were found near the divider"], "witnesses": []},
        ),
        DemoDocument(
            "vehicle_inspection.pdf", "VehicleInspection", "VI/DW/0211/2025", "MOTOR VEHICLE INSPECTION REPORT",
            [("Report No", "VI/DW/0211/2025"), ("Date", "5 September 2025"), ("Vehicle registration", "UP16BK3305"), ("Inspected by", "Motor Vehicle Inspector, Dwarka")],
            ["Front bumper and bonnet are damaged. Paint transfer consistent with a red motorcycle was found on the bumper."],
            {"report_number": "VI/DW/0211/2025", "inspection_date": "2025-09-05", "vehicle_registration": "UP16BK3305", "inspected_by": "Motor Vehicle Inspector, Dwarka",
             "observations": ["Front bumper and bonnet are damaged", "Paint transfer consistent with a red motorcycle was found on the bumper"]},
        ),
    ]


# ----------------------------------------------------------------------------- pipeline plumbing
def upload_file(data: bytes, filename: str) -> UploadFile:
    return UploadFile(file=io.BytesIO(data), filename=filename, headers=Headers({"content-type": "application/pdf"}))


def seed_case(storage_root: Path, case_id: str, title: str, station: str, documents: list[DemoDocument]) -> None:
    cases = CaseService(storage_root)
    try:
        cases.delete_case(case_id)
    except Exception:
        pass
    cases.create_case(case_id=case_id, title=title, description="Demo case generated by scripts/seed_demo_cases.py")
    result = cases.upload_documents(case_id, [upload_file(render_pdf(doc, station), doc.filename) for doc in documents])
    if result.failed_count:
        raise RuntimeError(f"{case_id}: {result.failed_count} document(s) were rejected on upload")

    case_uuid, _ = parse_safe_case_id(case_id)
    layout = CaseStorageLayout(storage_root, case_uuid)
    index = json.loads((layout.case_directory / "uploads" / "upload_index.json").read_text(encoding="utf-8"))
    uploads = tuple(
        IncomingUpload(source_path=layout.case_directory / "uploads" / item["stored_filename"], original_filename=item["original_filename"])
        for item in index
    )
    context = create_workflow_context(case_uuid, uploads, resume=False, storage_root=storage_root)
    outcome = run_production_workflow(
        storage_root,
        context,
        legal_reference_path=api_config.legal_reference_path,
        legal_reference_version=api_config.legal_reference_version,
        resume=False,
        ocr_client=MockOCRClient(),
        parser_client=ScriptedParserClient(documents),
        embedding_provider=NoOpEmbeddingProvider(),
    )
    if not outcome.report.successful:
        failed = next((r for r in outcome.report.stage_records if r.exception), None)
        raise RuntimeError(f"{case_id}: pipeline failed at {failed.stage_name if failed else '?'}: {failed.exception.message if failed else ''}")


def finalize_completed_case(storage_root: Path) -> None:
    review = CaseReviewService(storage_root)
    review.apply_corrections(
        COMPLETED_ID,
        CorrectionRequest(
            reviewer_id=IO_ID,
            reviewer_name=IO_NAME,
            comments="Final opinion and signature block recorded by the investigating officer.",
            corrections={
                "final_opinion": (
                    "On the evidence collected, a prima facie case is made out against accused Rakesh Yadav under Sections 309(4) and 118(2) BNS "
                    "for armed robbery causing grievous hurt. The knife, chain, phone and motorcycle were recovered at his instance and the FSL report "
                    "links the knife to the complainant. He is forwarded for trial. The second accused, Sunil Chauhan, is absconding and "
                    "investigation against him is continuing under Section 193(9) BNSS."
                ),
                "signature": f"{IO_NAME}, Investigating Officer, Karol Bagh Police Station",
            },
        ),
    )
    review.record_decision(COMPLETED_ID, DecisionRequest(decision="approve", reviewer_id=IO_ID, reviewer_name=IO_NAME, comments="Reviewed against source documents; approved."))
    review.record_decision(COMPLETED_ID, DecisionRequest(decision="finalize", reviewer_id=IO_ID, reviewer_name=IO_NAME))


def annotate_draft_case(storage_root: Path) -> None:
    CaseReviewService(storage_root).add_note(
        DRAFT_ID,
        AddNoteRequest(
            author_id="IO-ASI-RAMESH-CHAND",
            author_name="ASI Ramesh Chand",
            note_text="FSL, arrest memo and seizure memo are still awaited. Statement date, vehicle number and spot location need to be reconciled before this can go forward.",
        ),
    )


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--storage-root", type=Path, default=None, help="Defaults to the API storage root (OUTPUT_DIR).")
    parser.add_argument("--public-base-url", default=None, help="Address encoded in the QR code, e.g. http://192.168.1.20:8000 so a phone can scan it.")
    args = parser.parse_args()
    if args.public_base_url:
        os.environ["PUBLIC_BASE_URL"] = args.public_base_url
    storage_root = (args.storage_root or api_config.storage_root).resolve()
    storage_root.mkdir(parents=True, exist_ok=True)
    print(f"Storage root: {storage_root}")

    print("Seeding completed case ...")
    seed_case(storage_root, COMPLETED_ID, "Armed robbery with grievous hurt, Karol Bagh", A_STATION, completed_case())
    finalize_completed_case(storage_root)
    print("Seeding incomplete draft case ...")
    seed_case(storage_root, DRAFT_ID, "Rash driving causing grievous hurt, Dwarka", B_STATION, draft_case())
    annotate_draft_case(storage_root)

    print("\nDone. Restart nothing: the running API reads these from disk.")
    print(f"  Completed : {COMPLETED_ID}   (approved, finalized, signed, QR verification)")
    print(f"  Draft     : {DRAFT_ID}   (contradictions, evidence gaps, awaiting officer)")


if __name__ == "__main__":
    main()
