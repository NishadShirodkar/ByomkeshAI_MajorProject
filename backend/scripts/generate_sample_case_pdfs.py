"""Generates a realistic, detailed set of case PDFs for manual upload through the frontend.

Unlike scripts/seed_demo_cases.py (which scripts the parser so the demo runs offline), this
script only writes PDF files to disk. Upload them through the UI's Document Uploader and click
"Process Case" to exercise the *real* pipeline end to end: PyMuPDF/Gemini OCR, Gemini parsing,
entity resolution, contradiction detection, legal reasoning and chargesheet generation.

Usage (from the backend folder):
    python scripts/generate_sample_case_pdfs.py [--out-dir PATH]

Requires GEMINI_API_KEY to be set in backend/.env for the "Process Case" step (not for this
script itself, which only renders PDFs).
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from scripts.seed_demo_cases import DemoDocument, render_pdf  # noqa: E402

STATION = "Lajpat Nagar Police Station, South East District, New Delhi"
PLACE = "Central Market, near Shiv Mandir Gate, Lajpat Nagar-II, New Delhi"
NARRATIVE = (
    "On 9 October 2025 at about 7:45 pm, the complainant Priya Nair was walking out of a shop in the Central Market, "
    "Lajpat Nagar-II, near the Shiv Mandir Gate, when two men on a motorcycle bearing registration DL7SCB9034 approached "
    "her from behind. The pillion rider, later identified as Suresh Pal, snatched her gold chain weighing about 15 grams "
    "from her neck and, in the act of snatching, pushed her, causing her to fall and sustain a fracture of the right wrist. "
    "The rider of the motorcycle, later identified as Deepak Thakur, sped away towards Ring Road. The complainant's mobile "
    "phone, a Samsung Galaxy S23, fell from her hand during the struggle and was also taken by the accused."
)


def build_documents() -> list[DemoDocument]:
    complaint_text = (
        "I was coming out of a shop in the Central Market near the Shiv Mandir Gate at about 7:45 pm on 9 October 2025 when "
        "two men on a black motorcycle, registration DL7SCB9034, came close to me from behind. The man sitting behind pulled "
        "my gold chain from my neck so hard that I fell on the ground and my right wrist was badly hurt. My phone, a Samsung "
        "Galaxy S23, fell on the road and they took that too before riding away towards Ring Road. I could not see their "
        "faces clearly but I could read part of the number plate. I request strict action against the culprits."
    )
    witness_shopkeeper = (
        "I run a garment shop in the Central Market, Lajpat Nagar-II, right next to the Shiv Mandir Gate. On 9 October 2025 "
        "at about 7:45 pm I heard a woman scream outside my shop. When I came out I saw a lady, whom I later came to know as "
        "Priya Nair, lying on the ground near the gate. A black motorcycle with registration DL7SCB9034 was speeding away "
        "towards Ring Road. I helped the lady get up and called for an auto to take her to the hospital. I also saw that her "
        "phone was missing from the spot."
    )
    witness_security_guard = (
        "I am employed as a security guard at the Central Market, Lajpat Nagar-II, and I was on duty near the Shiv Mandir "
        "Gate on 9 October 2025. At about 7:45 pm I saw two men on a black motorcycle slow down near a woman who was walking "
        "out of a shop. One of them, sitting behind, snatched something from her neck and she fell down immediately. The "
        "motorcycle then moved fast towards Ring Road. I noted that the number plate began with DL7S but could not read the "
        "rest clearly in the dim light near the gate."
    )
    return [
        DemoDocument(
            "FIR.pdf", "FIR", "0531/2025", "FIRST INFORMATION REPORT (Section 173 BNSS)",
            [
                ("FIR No", "0531/2025"), ("Date of FIR", "9 October 2025"), ("Police Station", "Lajpat Nagar"),
                ("District", "South East Delhi"), ("Complainant", "Priya Nair"),
                ("Accused", "Suresh Pal, Deepak Thakur"), ("Victim", "Priya Nair"), ("Vehicle", "DL7SCB9034"),
                ("Date and time of occurrence", "9 October 2025, 7:45 pm"), ("Place of occurrence", PLACE),
                ("Sections", "Section 304 BNS, Section 115 BNS"),
                ("Court", "Metropolitan Magistrate, Saket Courts, New Delhi"),
            ],
            [f"<b>Brief facts:</b> {NARRATIVE}"],
        ),
        DemoDocument(
            "Complaint.pdf", "Complaint", "Samsung Galaxy S23", "WRITTEN COMPLAINT",
            [
                ("Date", "9 October 2025"), ("To", "The SHO, Lajpat Nagar Police Station"),
                ("Complainant", "Priya Nair, R/o C-42, Lajpat Nagar-III, New Delhi"), ("Victim", "Priya Nair"),
                ("Vehicle of offenders", "DL7SCB9034"),
            ],
            [complaint_text],
        ),
        DemoDocument(
            "Witness_Statement_Shopkeeper.pdf", "WitnessStatement", "garment shop", "STATEMENT OF WITNESS UNDER SECTION 180 BNSS",
            [
                ("Date", "9 October 2025"), ("Witness", "Ramesh Gupta"), ("Age", "44"),
                ("Occupation", "Shop owner"), ("Recorded by", "SI Vikas Tomar"),
            ],
            [witness_shopkeeper],
        ),
        DemoDocument(
            "Witness_Statement_SecurityGuard.pdf", "WitnessStatement", "security guard", "STATEMENT OF WITNESS UNDER SECTION 180 BNSS",
            [
                ("Date", "9 October 2025"), ("Witness", "Baldev Singh"), ("Age", "52"),
                ("Occupation", "Security guard"), ("Recorded by", "SI Vikas Tomar"),
            ],
            [witness_security_guard],
        ),
        DemoDocument(
            "Medical_Report.pdf", "MedicalReport", "Priya Nair", "MEDICO-LEGAL EXAMINATION REPORT (MLC)",
            [
                ("MLC No", "MLC/MAX/2025/07218"), ("Date", "9 October 2025"),
                ("Hospital", "Max Hospital, Saket, New Delhi"), ("Patient", "Priya Nair"),
                ("Age / Sex", "31 / Female"), ("Examining doctor", "Dr. Kavita Rao"),
            ],
            [
                "<b>Findings:</b> Fracture of the distal end of the right radius (Colles' fracture). Abrasions on the right "
                "palm and knee consistent with a fall on a hard surface.",
                "Patient conscious, oriented and haemodynamically stable. Right forearm immobilised in a plaster cast.",
                "<b>Opinion:</b> The injury is grievous in nature on account of the fracture. The patient is alive and "
                "under outpatient treatment.",
            ],
        ),
        DemoDocument(
            "Spot_Panchnama.pdf", "SpotPanchnama", "SP/LN/0098/2025", "SPOT INSPECTION MEMO (PANCHNAMA)",
            [
                ("Memo No", "SP/LN/0098/2025"), ("Date and time", "9 October 2025, 8:50 pm"),
                ("Place", PLACE), ("Panch witnesses", "Ramesh Gupta, Baldev Singh"),
            ],
            [
                "A broken gold-coloured chain clasp was recovered from the pavement near the Shiv Mandir Gate.",
                "No blood stains were found at the spot. A CCTV camera installed at the gate of the Central Market "
                "covers the point of occurrence.",
            ],
        ),
        DemoDocument(
            "Arrest_Memo.pdf", "ArrestMemo", "AM/LN/0071/2025", "ARREST MEMO",
            [
                ("Memo No", "AM/LN/0071/2025"), ("Date and time", "12 October 2025, 6:15 pm"),
                ("Arrested person", "Suresh Pal"), ("Father's name", "Om Prakash"), ("Age", "24"),
                ("Address", "H.No. 9, Govindpuri, New Delhi"), ("Occupation", "Unemployed"),
                ("Place of arrest", "Govindpuri, New Delhi"), ("Arresting officer", "SI Vikas Tomar"),
            ],
            ["The arrested person was informed of the grounds of arrest and of his right to inform a relative or friend."],
        ),
        DemoDocument(
            "Seizure_Memo.pdf", "SeizureMemo", "SM/LN/0133/2025", "SEIZURE MEMO",
            [
                ("Memo No", "SM/LN/0133/2025"), ("Date and time", "12 October 2025, 7:30 pm"),
                ("Place", "Govindpuri, New Delhi"), ("Prepared by", "SI Vikas Tomar"),
            ],
            [
                "The following articles were recovered from the accused Suresh Pal at his instance and seized:",
                "EX-1: Gold chain (approximately 15 grams), identified by the complainant as her stolen chain.",
                "EX-2: Samsung Galaxy S23 mobile phone, recovered from the accused.",
                "EX-3: Motorcycle bearing registration DL7SCB9034 (Bajaj Pulsar).",
            ],
        ),
        DemoDocument(
            "FSL_Report.pdf", "FSLReport", "FSL/DEL/2025/DIG/4477", "FORENSIC SCIENCE LABORATORY REPORT",
            [
                ("Report No", "FSL/DEL/2025/DIG/4477"), ("Date", "20 October 2025"),
                ("Laboratory", "Forensic Science Laboratory, Rohini, Delhi"),
                ("Items examined", "Samsung Galaxy S23 (EX-2); CCTV footage from Central Market gate camera"),
            ],
            [
                "The IMEI number of the seized phone (EX-2) matches the IMEI reported by the complainant as belonging to "
                "her Samsung Galaxy S23.",
                "CCTV footage extracted shows a motorcycle matching the description, with registration partially "
                "legible as DL7SCB9034, at the time and place of the occurrence.",
                "<b>Opinion:</b> The seized mobile phone is confirmed to be the complainant's stolen device.",
            ],
        ),
        DemoDocument(
            "Case_Diary.pdf", "CaseDiary", "CD/LN/0531/2025", "CASE DIARY",
            [("Diary No", "CD/LN/0531/2025"), ("Investigating officer", "SI Vikas Tomar")],
            [
                "<b>Entry 1 (9 October 2025):</b> FIR registered. Spot visited and inspected. Statements of two "
                "eyewitnesses recorded. Complainant sent for medical examination.",
                "<b>Entry 2 (12 October 2025):</b> Accused Suresh Pal traced and arrested at Govindpuri on the basis of "
                "CCTV footage and local intelligence. Chain, mobile phone and motorcycle recovered at his instance.",
                "<b>Entry 3 (20 October 2025):</b> FSL report received confirming the recovered phone belongs to the "
                "complainant. Efforts continue to trace the second accused, Deepak Thakur, who remains absconding.",
            ],
        ),
    ]


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument(
        "--out-dir", type=Path, default=Path(__file__).resolve().parents[1] / "sample_cases" / "LajpatNagar_ChainSnatching",
        help="Directory to write the PDFs into (created if missing).",
    )
    args = parser.parse_args()
    args.out_dir.mkdir(parents=True, exist_ok=True)

    documents = build_documents()
    for doc in documents:
        path = args.out_dir / doc.filename
        path.write_bytes(render_pdf(doc, STATION))
        print(f"  wrote {path}")

    print(f"\n{len(documents)} PDF(s) written to: {args.out_dir}")
    print("Upload all of them to a new case in the frontend, then click \"Process Case\".")


if __name__ == "__main__":
    main()
