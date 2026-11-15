"""Generates two detailed, multi-document sample cases in the same layout as the pre-existing
CASE-002-Byomkesh sample ("DELHI POLICE / OFFICIAL DOCUMENT" header, flattened record fields).

Each case has the same 19 document types as CASE-002-Byomkesh: fir, complaint, two witness
statements, medical report, postmortem report, FSL report, seizure memo, spot panchnama, vehicle
inspection, arrest memo, accused statement, CCTV report, evidence list, annexures, timeline, site
plan, case diary and a master case file.

These are plain PDFs with no scripted parser behind them: upload them through the frontend and
click "Process Case" to run real Gemini OCR and parsing end to end.

Usage (from the backend folder):
    python scripts/generate_detailed_case_pdfs.py [--out-dir PATH]
"""

from __future__ import annotations

import argparse
import shutil
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from scripts.case_pdf_renderer import render_record_pdf  # noqa: E402

SAMPLE_CASES_DIR = Path(__file__).resolve().parents[1] / "sample_cases"

# Common document type -> (output filename, title shown on the PDF)
DOC_TYPES: list[tuple[str, str]] = [
    ("fir", "FIRST INFORMATION REPORT"),
    ("complaint", "COMPLAINT UNDER SECTION 154 CRPC"),
    ("witness_statement_1", "WITNESS STATEMENT - 161 CRPC"),
    ("witness_statement_2", "WITNESS STATEMENT - 161 CRPC"),
    ("medical_report", "MEDICO-LEGAL EXAMINATION REPORT (MLC)"),
    ("postmortem_report", "POST-MORTEM EXAMINATION STATUS REPORT"),
    ("fsl_report", "FORENSIC SCIENCE LABORATORY REPORT"),
    ("seizure_memo", "SEIZURE MEMO"),
    ("spot_panchnama", "SPOT INSPECTION MEMO (PANCHNAMA)"),
    ("vehicle_inspection", "MOTOR VEHICLE / CONVEYANCE INSPECTION REPORT"),
    ("arrest_memo", "ARREST MEMO"),
    ("accused_statement", "ACCUSED STATEMENT - 161 CRPC"),
    ("cctv_report", "CCTV ANALYSIS REPORT"),
    ("evidence_list", "EVIDENCE INVENTORY"),
    ("annexures", "ANNEXURE LIST - DOCUMENTS INDEX"),
    ("timeline", "INVESTIGATION TIMELINE RECONSTRUCTION"),
    ("site_plan", "SITE PLAN"),
    ("case_diary", "CASE DIARY"),
    ("master_case", "MASTER CASE FILE"),
]


# --------------------------------------------------------------------------------------------
# Case 1: chain snatching with grievous hurt, Lajpat Nagar
# --------------------------------------------------------------------------------------------
def lajpat_nagar_case() -> dict:
    station = {
        "name": "Lajpat Nagar Police Station",
        "address": "Ring Road, Lajpat Nagar-IV, New Delhi - 110024",
        "district": "South East Delhi",
        "state": "Delhi",
        "phone": "011-26341122",
        "email": "sho-lajpatnagar-dl@delhipolice.gov.in",
    }
    case_number = "FIR/2025/DL/PSLJN/0531"
    place = "Central Market, near Shiv Mandir Gate, Lajpat Nagar-II, New Delhi"

    return {
        "case_number": case_number,
        "station": station,
        "fir": {
            "fir_number": case_number,
            "fir_book_serial_no": "531",
            "date_of_fir": "2025-10-09",
            "time_of_fir": "20:15",
            "police_station": station,
            "act_and_sections": {"bns": ["Section 304", "Section 115"], "other_acts": []},
            "complainant_name": "Priya Nair",
            "complainant_address": "C-42, Lajpat Nagar-III, New Delhi - 110024",
            "accused_names": ["Suresh Pal", "Deepak Thakur"],
            "victim_name": "Priya Nair",
            "property_involved": ["Gold chain, approximately 15 grams", "Samsung Galaxy S23 mobile phone"],
            "date_time_of_occurrence": "2025-10-09 19:45",
            "place_of_occurrence": place,
            "distance_and_direction_from_ps": "1.2 km, north-east of Lajpat Nagar Police Station",
            "brief_facts": (
                "On 9 October 2025 at about 7:45 pm, the complainant Priya Nair was walking out of a shop in the "
                "Central Market, Lajpat Nagar-II, near the Shiv Mandir Gate, when two men on a motorcycle bearing "
                "registration DL7SCB9034 approached her from behind. The pillion rider, later identified as Suresh "
                "Pal, snatched her gold chain weighing about 15 grams from her neck and, in the act of snatching, "
                "pushed her, causing her to fall and sustain a fracture of the right wrist. The rider of the "
                "motorcycle, later identified as Deepak Thakur, sped away towards Ring Road. The complainant's "
                "mobile phone, a Samsung Galaxy S23, fell from her hand during the struggle and was also taken by "
                "the accused."
            ),
            "action_taken": "FIR registered under Section 173 BNSS. Investigation taken up by SI Vikas Tomar.",
            "fir_contents_read_over_to_complainant": True,
            "signature_of_complainant": "Signed",
            "copy_dispatched_to_court": True,
        },
        "complaint": {
            "date": "2025-10-09", "time": "19:50", "police_station": station["name"],
            "section": "Section 173 of the Bharatiya Nagarik Suraksha Sanhita, 2023",
            "complainant_details": {
                "name": "Priya Nair", "age": "31", "occupation": "Marketing Executive, private firm",
                "address": "C-42, Lajpat Nagar-III, New Delhi - 110024", "contact": "9810276453",
                "relation_to_victim": "Self (complainant is the victim)",
            },
            "complaint_text": (
                "I was coming out of a shop in the Central Market near the Shiv Mandir Gate at about 7:45 pm on 9 "
                "October 2025 when two men on a black motorcycle, registration DL7SCB9034, came close to me from "
                "behind. The man sitting behind pulled my gold chain from my neck so hard that I fell on the ground "
                "and my right wrist was badly hurt. My phone, a Samsung Galaxy S23, fell on the road and they took "
                "that too before riding away towards Ring Road. I could not see their faces clearly in the evening "
                "crowd but I could read part of the number plate. I request strict action against the culprits."
            ),
            "verbal_complaint_recorded_by": "SI Vikas Tomar, Duty Officer, PS Lajpat Nagar",
            "complaint_read_and_verified": True, "time_of_complaint": "19:50 hours",
            "signature_thumb_impression": "Signed by complainant",
        },
        "witness_statement_1": {
            "statement_id": "WS/PSLJN/0531/001", "date_of_recording": "2025-10-09", "time_of_recording": "21:10",
            "place": "PS Lajpat Nagar", "recorded_by": "SI Vikas Tomar",
            "witness_details": {
                "witness_id": "WIT-001", "name": "Ramesh Gupta", "age": "44", "occupation": "Shop owner, garment store",
                "address": "Shop No. 14, Central Market, Lajpat Nagar-II, New Delhi", "contact": "9891022331",
            },
            "statement_under_section": "Section 180 of the Bharatiya Nagarik Suraksha Sanhita, 2023",
            "statement_text": (
                "I run a garment shop in the Central Market, Lajpat Nagar-II, right next to the Shiv Mandir Gate. "
                "On 9 October 2025 at about 7:45 pm I heard a woman scream outside my shop. When I came out I saw a "
                "lady, whom I later came to know as Priya Nair, lying on the ground near the gate. A black "
                "motorcycle with registration DL7SCB9034 was speeding away towards Ring Road. I helped the lady get "
                "up and called for an auto-rickshaw to take her to the hospital. I also noticed that her phone was "
                "missing from the spot. I am willing to identify the motorcycle and give evidence if required."
            ),
        },
        "witness_statement_2": {
            "statement_id": "WS/PSLJN/0531/002", "date_of_recording": "2025-10-09", "time_of_recording": "21:40",
            "place": "PS Lajpat Nagar", "recorded_by": "SI Vikas Tomar",
            "witness_details": {
                "witness_id": "WIT-002", "name": "Baldev Singh", "age": "52", "occupation": "Security guard",
                "address": "Market Association Office, Central Market, Lajpat Nagar-II, New Delhi", "contact": "9971145590",
            },
            "statement_under_section": "Section 180 of the Bharatiya Nagarik Suraksha Sanhita, 2023",
            "statement_text": (
                "I am employed as a security guard at the Central Market, Lajpat Nagar-II, and I was on duty near "
                "the Shiv Mandir Gate on 9 October 2025. At about 7:45 pm I saw two men on a black motorcycle slow "
                "down near a woman who was walking out of a shop. One of them, sitting behind, snatched something "
                "from her neck and she fell down immediately. The motorcycle then moved fast towards Ring Road. I "
                "noted that the number plate began with DL7S but could not read the rest clearly in the dim light "
                "near the gate. I informed the market association office and they called the police."
            ),
        },
        "medical_report": {
            "mlc_no": "MLC/MAX/2025/07218", "date": "2025-10-09", "hospital_name": "Max Hospital, Saket, New Delhi",
            "patient_name": "Priya Nair", "age": "31", "gender": "Female", "examining_doctor": "Dr. Kavita Rao",
            "brought_by": "Autorickshaw driver and Ramesh Gupta (shopkeeper)",
            "findings": [
                "Fracture of the distal end of the right radius (Colles' fracture)",
                "Abrasions on the right palm and right knee consistent with a fall on a hard surface",
                "No other external injury noted",
            ],
            "patient_status": "Conscious, oriented and haemodynamically stable. Right forearm immobilised in a plaster cast.",
            "opinion": "The injury is grievous in nature on account of the fracture. The patient is alive and under outpatient treatment.",
            "injury_report_handed_to": "IO, PS Lajpat Nagar, on 2025-10-10",
        },
        "postmortem_report": {
            "report_no": "PM-NA-LJN-04", "date": "2025-10-10", "status": "Not Applicable",
            "reason": "Victim Priya Nair is alive and was discharged after outpatient treatment at Max Hospital, Saket.",
            "remarks": "Post-mortem examination is not applicable in this case.",
        },
        "seizure_memo": {
            "memo_no": "SM/LJN/0133/2025", "date_time": "2025-10-12 19:50", "place": "Jeweller's shop and accused's residence, Govindpuri, New Delhi",
            "prepared_by": "SI Vikas Tomar",
            "seized_items": [
                {"description": "Gold chain, approximately 15 grams, identified by the complainant as her stolen chain", "exhibit_mark": "EX-1"},
                {"description": "Samsung Galaxy S23 mobile phone, recovered from the accused", "exhibit_mark": "EX-2"},
                {"description": "Motorcycle bearing registration DL7SCB9034 (Bajaj Pulsar 150)", "exhibit_mark": "EX-3"},
            ],
        },
        "fsl_report": {
            "report_no": "FSL/DEL/2025/DIG/4477", "date": "2025-10-20", "laboratory_name": "Forensic Science Laboratory, Rohini, Delhi",
            "examined_items": ["Samsung Galaxy S23 mobile phone (EVD-0531-002)", "CCTV footage from Central Market and Ring Road cameras"],
            "findings": [
                "The IMEI number of the recovered phone matches the IMEI reported by the complainant as belonging to her Samsung Galaxy S23.",
                "CCTV footage extracted shows a motorcycle matching the description, with registration partially legible as DL7S..9034, at the time and place of the occurrence.",
            ],
            "opinion": "The seized mobile phone is confirmed to be the complainant's stolen device.",
        },
        "spot_panchnama": {
            "memo_no": "SP/LJN/0098/2025", "date_time": "2025-10-09 20:50", "place": place,
            "panch_witnesses": ["Ramesh Gupta", "Baldev Singh"],
            "observations": [
                "A broken gold-coloured chain clasp was recovered from the pavement near the Shiv Mandir Gate.",
                "No blood stains were found at the spot.",
                "A CCTV camera installed at the gate of the Central Market covers the point of occurrence.",
                "Tyre marks consistent with a two-wheeler braking sharply were noted near the gate.",
            ],
            "prepared_by": "SI Vikas Tomar",
        },
        "vehicle_inspection": {
            "report_no": "VI/LJN/0211/2025", "date": "2025-10-13", "vehicle_registration": "DL7SCB9034",
            "make_model": "Bajaj Pulsar 150", "inspected_by": "Motor Vehicle Inspector, Lajpat Nagar Circle",
            "observations": [
                "Vehicle recovered from the possession of accused Suresh Pal at the time of arrest.",
                "Registration certificate found to be in the name of Deepak Thakur.",
                "No visible accident damage; vehicle in roadworthy condition.",
            ],
        },
        "arrest_memo": {
            "memo_no": "AM/LJN/0071/2025", "date_time": "2025-10-12 18:15", "arrested_person_name": "Suresh Pal",
            "father_name": "Om Prakash", "age": "24", "address": "H.No. 9, Govindpuri, New Delhi - 110019",
            "occupation": "Unemployed", "place_of_arrest": "Govindpuri, New Delhi",
            "arresting_officer": "SI Vikas Tomar",
            "grounds_of_arrest_informed": True, "right_to_inform_relative_informed": True,
            "relative_informed": "Mother, Smt. Kamla Devi, informed telephonically at 18:40 hrs",
            "medical_examination_before_arrest": "Conducted at PS Lajpat Nagar, no injury noted",
        },
        "accused_statement": {
            "statement_id": "AS/PSLJN/0531/001", "date_of_recording": "2025-10-12", "time_of_recording": "19:30",
            "place": "Lock-up Room, PS Lajpat Nagar", "recorded_by": "SI Vikas Tomar",
            "witness_to_recording": "ASI Ramphal Singh, PS Lajpat Nagar",
            "accused_details": {
                "accused_id": "ACC-001", "name": "Suresh Pal", "age": "24", "father_name": "Om Prakash",
                "occupation": "Unemployed", "education": "10th Pass", "marital_status": "Unmarried",
                "address": "H.No. 9, Govindpuri, New Delhi - 110019",
                "native_place": "Village Bhadsa, District Rohtak, Haryana",
                "contact": "9871556620",
            },
            "rights_read": {
                "article_20_3_read": True, "right_to_silence": True, "right_to_legal_counsel": True,
                "accused_understood_rights": True,
            },
            "statement_text": (
                "I, Suresh Pal, s/o Om Prakash, state that on 9 October 2025 I was riding pillion on a motorcycle "
                "driven by my friend Deepak Thakur. We were passing through the Central Market area in Lajpat Nagar "
                "at around 7:45 pm. I admit that I pulled a gold chain from a woman's neck near the Shiv Mandir "
                "Gate. I did not intend for her to fall, but she lost her balance. We then rode away towards Ring "
                "Road. I later sold the chain to a known jeweller in Govindpuri for cash. I am giving this statement "
                "voluntarily and without any pressure."
            ),
        },
        "cctv_report": {
            "report_id": "CCTV/PSLJN/0531/2025", "date_of_collection": "2025-10-10", "date_of_analysis": "2025-10-10 to 2025-10-11",
            "analyzed_by": {"name": "HC Rajesh Yadav", "designation": "Head Constable, Technical Cell", "police_station": "Lajpat Nagar"},
            "cctv_sources": [
                {
                    "source_id": "CCTV-001", "location": "Central Market, Shiv Mandir Gate",
                    "camera_id": "CAM-CM-G1-02", "camera_type": "IP Camera, Dome, Hikvision",
                    "coverage_area": "Market gate and adjoining pavement",
                    "footage_duration_obtained": "19:30 to 20:00, 09-10-2025",
                    "findings": "Shows a black motorcycle approaching the victim and the pillion rider reaching towards her neck; number plate partially legible as DL7S..9034.",
                },
                {
                    "source_id": "CCTV-002", "location": "Ring Road junction, 300m from the spot",
                    "camera_id": "CAM-RR-J4-01", "camera_type": "Traffic police PTZ camera",
                    "coverage_area": "Ring Road carriageway towards Govindpuri",
                    "footage_duration_obtained": "19:40 to 19:55, 09-10-2025",
                    "findings": "Shows a motorcycle matching the description turning towards Govindpuri at high speed shortly after the incident.",
                },
            ],
        },
        "evidence_list": {
            "case_reference": case_number, "total_evidence_items": 5, "evidence_custodian": "MHC(M) - PS Lajpat Nagar",
            "list_prepared_by": "SI Vikas Tomar, IO", "date": "2025-10-13",
            "items": [
                {
                    "evidence_id": "EVD-0531-001", "type": "Physical - Jewellery",
                    "description": "Gold chain, approximately 15 grams, identified by the complainant",
                    "quantity": "1", "collected_from": "Jeweller's shop, Govindpuri (recovered on accused's instance)",
                    "collected_by": "SI Vikas Tomar", "date_time_collection": "2025-10-12, 19:50",
                    "seal_number": "VT-01", "current_location": "Malkhana, PS Lajpat Nagar",
                    "chain_of_custody": [
                        {"date": "2025-10-12", "action": "Seized on accused's instance", "by": "IO"},
                        {"date": "2025-10-13", "action": "Shown to complainant for identification", "by": "IO"},
                        {"date": "2025-10-13", "action": "Deposited in Malkhana", "by": "MHC(M)"},
                    ],
                },
                {
                    "evidence_id": "EVD-0531-002", "type": "Physical - Electronics",
                    "description": "Samsung Galaxy S23 mobile phone, recovered from the accused",
                    "quantity": "1", "collected_from": "Govindpuri, at the time of arrest",
                    "collected_by": "SI Vikas Tomar", "date_time_collection": "2025-10-12, 18:20",
                    "seal_number": "VT-02", "current_location": "Malkhana, PS Lajpat Nagar",
                },
                {
                    "evidence_id": "EVD-0531-003", "type": "Physical - Vehicle",
                    "description": "Bajaj Pulsar 150 motorcycle, registration DL7SCB9034",
                    "quantity": "1", "collected_from": "Govindpuri, at the time of arrest",
                    "collected_by": "SI Vikas Tomar", "date_time_collection": "2025-10-12, 18:20",
                    "seal_number": "VT-03", "current_location": "Malkhana yard, PS Lajpat Nagar",
                },
                {
                    "evidence_id": "EVD-0531-004", "type": "Digital - CCTV footage",
                    "description": "CCTV footage from Central Market gate and Ring Road junction cameras",
                    "quantity": "2 clips", "collected_from": "Market association office and Traffic Police control room",
                    "collected_by": "HC Rajesh Yadav", "date_time_collection": "2025-10-10, 11:00",
                    "seal_number": "RY-01", "current_location": "Case file digital evidence folder",
                },
                {
                    "evidence_id": "EVD-0531-005", "type": "Medical document",
                    "description": "Medico-legal certificate of complainant Priya Nair",
                    "quantity": "1", "collected_from": "Max Hospital, Saket",
                    "collected_by": "SI Vikas Tomar", "date_time_collection": "2025-10-10, 10:00",
                    "seal_number": "N/A", "current_location": "Case file",
                },
            ],
        },
        "annexures": {
            "case_reference": case_number, "total_documents": 10, "prepared_by": "SI Vikas Tomar, IO", "date": "2025-10-20",
            "documents": [
                {"annexure_no": "A-1", "document_name": "First Information Report (FIR)", "document_id": case_number, "pages": 2, "filed_in_court": True, "exhibit_mark": "PW-1/A"},
                {"annexure_no": "A-2", "document_name": "Complaint under Section 173 BNSS", "document_id": "Complaint by Priya Nair dated 09-10-2025", "pages": 1, "filed_in_court": True, "exhibit_mark": "PW-1/B"},
                {"annexure_no": "A-3", "document_name": "Statement of witness Ramesh Gupta", "document_id": "WS/PSLJN/0531/001", "pages": 1, "filed_in_court": True, "exhibit_mark": "PW-2"},
                {"annexure_no": "A-4", "document_name": "Statement of witness Baldev Singh", "document_id": "WS/PSLJN/0531/002", "pages": 1, "filed_in_court": True, "exhibit_mark": "PW-3"},
                {"annexure_no": "A-5", "document_name": "Medico-legal certificate", "document_id": "MLC/MAX/2025/07218", "pages": 1, "filed_in_court": True, "exhibit_mark": "PW-4/A"},
                {"annexure_no": "A-6", "document_name": "Spot Panchnama", "document_id": "SP/LJN/0098/2025", "pages": 1, "filed_in_court": True, "exhibit_mark": "PW-1/C"},
                {"annexure_no": "A-7", "document_name": "Arrest Memo", "document_id": "AM/LJN/0071/2025", "pages": 1, "filed_in_court": True, "exhibit_mark": "PW-5/A"},
                {"annexure_no": "A-8", "document_name": "Seizure Memo", "document_id": "SM/LJN/0133/2025", "pages": 1, "filed_in_court": True, "exhibit_mark": "PW-5/B"},
                {"annexure_no": "A-9", "document_name": "CCTV Analysis Report", "document_id": "CCTV/PSLJN/0531/2025", "pages": 2, "filed_in_court": True, "exhibit_mark": "PW-6/A"},
                {"annexure_no": "A-10", "document_name": "Case Diary", "document_id": "CD/LJN/0531/2025", "pages": 2, "filed_in_court": False, "exhibit_mark": "N/A (not tendered)"},
            ],
        },
        "timeline": {
            "case_reference": case_number, "source_evidence": "CCTV footage, witness statements, hospital records, accused statement",
            "events": [
                {"time": "19:45", "event": "Accused on motorcycle DL7SCB9034 approach the complainant near the Shiv Mandir Gate.", "source": "CCTV-001", "confidence": "High"},
                {"time": "19:45", "event": "Pillion rider snatches the complainant's gold chain; complainant falls and sustains wrist injury.", "source": "CCTV-001, witness Ramesh Gupta", "confidence": "High"},
                {"time": "19:46", "event": "Accused flee on the motorcycle towards Ring Road.", "source": "CCTV-002, witness Baldev Singh", "confidence": "High"},
                {"time": "19:50", "event": "Complainant taken to Max Hospital, Saket by autorickshaw.", "source": "Hospital admission record", "confidence": "High"},
                {"time": "20:15", "event": "FIR registered at PS Lajpat Nagar.", "source": "FIR record", "confidence": "High"},
                {"time": "2025-10-10", "event": "CCTV footage collected and analysed by Technical Cell.", "source": "CCTV analysis report", "confidence": "High"},
                {"time": "2025-10-12", "event": "Accused Suresh Pal traced to Govindpuri and arrested; chain, phone and motorcycle recovered.", "source": "Arrest memo, seizure memo", "confidence": "High"},
            ],
        },
        "site_plan": {
            "plan_no": "SP-PLAN/LJN/0531/2025", "date": "2025-10-10", "prepared_by": "Draftsman, PS Lajpat Nagar",
            "location": place,
            "annotations": [
                "Point A: Shop from which the complainant exited.",
                "Point B: Spot of occurrence, near the Shiv Mandir Gate, marked with 'X'.",
                "Point C: Position of CCTV camera CAM-CM-G1-02.",
                "Arrow: Direction of the accused's flight towards Ring Road.",
            ],
            "scale": "Not to scale, approximate distances marked in metres",
        },
        "case_diary": {
            "diary_number": "CD/LJN/0531/2025", "officer_name": "SI Vikas Tomar",
            "entries": [
                {"entry_number": "1", "date": "2025-10-09", "text": "FIR registered. Spot visited and inspected. Statements of two eyewitnesses recorded. Complainant sent for medical examination."},
                {"entry_number": "2", "date": "2025-10-10", "text": "CCTV footage collected from Central Market gate and Ring Road junction cameras and sent for analysis."},
                {"entry_number": "3", "date": "2025-10-12", "text": "Accused Suresh Pal traced and arrested at Govindpuri on the basis of CCTV footage and local intelligence. Chain, mobile phone and motorcycle recovered at his instance. Accused statement recorded."},
                {"entry_number": "4", "date": "2025-10-20", "text": "Annexures and evidence list compiled. Efforts continue to trace the second accused, Deepak Thakur, who remains absconding."},
            ],
        },
        "master_case": {
            "case_identifier": {"fir_number": case_number, "crime_number": "CR/2025/DL/PSLJN/0298", "ps_case_number": "PSLJN/2025/INV/181"},
            "police_station": {"name": station["name"], "district": station["district"], "state": station["state"], "police_station_code": "PSLJN", "jurisdiction": "Lajpat Nagar, Central Market, Amar Colony"},
            "incident_details": {"date": "2025-10-09", "day": "Thursday", "time": "19:45:00", "timezone": "IST", "weather": "Clear, dry evening", "lighting": "Dusk, market lights on"},
            "location": {"address": place, "area": "Lajpat Nagar", "city": "New Delhi", "pincode": "110024"},
            "investigation_status": "Charge-sheet under preparation against arrested accused; investigation continuing against absconding co-accused",
        },
    }


# --------------------------------------------------------------------------------------------
# Case 2: residential burglary, Vasant Kunj
# --------------------------------------------------------------------------------------------
def vasant_kunj_case() -> dict:
    station = {
        "name": "Vasant Kunj Police Station",
        "address": "Pocket C, Vasant Kunj, New Delhi - 110070",
        "district": "South District",
        "state": "Delhi",
        "phone": "011-26130044",
        "email": "sho-vasantkunj-dl@delhipolice.gov.in",
    }
    case_number = "FIR/2025/DL/PSVKJ/0674"
    place = "House No. C-118, Vasant Kunj, Sector C, New Delhi"

    return {
        "case_number": case_number,
        "station": station,
        "fir": {
            "fir_number": case_number,
            "fir_book_serial_no": "674",
            "date_of_fir": "2025-11-03",
            "time_of_fir": "10:30",
            "police_station": station,
            "act_and_sections": {"bns": ["Section 305", "Section 303"], "other_acts": []},
            "complainant_name": "Rohit Malhotra",
            "complainant_address": "C-118, Vasant Kunj, Sector C, New Delhi - 110070",
            "accused_names": ["Mahesh Oraon"],
            "victim_name": "Rohit Malhotra",
            "property_involved": [
                "Cash Rs. 85,000", "Assorted gold jewellery, approximately 60 grams", "Dell laptop",
                "Sony television, 43 inch",
            ],
            "date_time_of_occurrence": "2025-11-01 night to 2025-11-02 morning (between 23:00 and 07:00)",
            "place_of_occurrence": place,
            "distance_and_direction_from_ps": "800 metres, south of Vasant Kunj Police Station",
            "brief_facts": (
                "The complainant Rohit Malhotra states that he, along with his family, had travelled to Jaipur for "
                "a wedding from 1 November 2025 evening and returned on the morning of 3 November 2025. On return, "
                "he found the rear window grill of his house broken open and the house ransacked. Cash of about Rs. "
                "85,000, assorted gold jewellery weighing approximately 60 grams, a Dell laptop and a 43-inch Sony "
                "television were found missing. He suspects his former domestic help, Mahesh Oraon, who had worked "
                "at the house for eight months until two months ago and was familiar with the household's layout "
                "and the family's travel plans."
            ),
            "action_taken": "FIR registered under Section 173 BNSS. Investigation taken up by SI Neeraj Bhandari.",
            "fir_contents_read_over_to_complainant": True,
            "signature_of_complainant": "Signed",
            "copy_dispatched_to_court": True,
        },
        "complaint": {
            "date": "2025-11-03", "time": "10:15", "police_station": station["name"],
            "section": "Section 173 of the Bharatiya Nagarik Suraksha Sanhita, 2023",
            "complainant_details": {
                "name": "Rohit Malhotra", "age": "46", "occupation": "Bank manager",
                "address": "C-118, Vasant Kunj, Sector C, New Delhi - 110070", "contact": "9811034562",
                "relation_to_victim": "Self (owner of the house)",
            },
            "complaint_text": (
                "I, Rohit Malhotra, resident of C-118, Vasant Kunj, state that my family and I had gone to Jaipur "
                "on 1 November 2025 evening for a wedding and returned on 3 November 2025 morning at about 9:30 am. "
                "On reaching home, I found the grill of the rear bedroom window broken and bent, and the house in "
                "disarray. Cash of about Rs. 85,000 kept in a cupboard, my wife's gold jewellery weighing about 60 "
                "grams, my Dell laptop and our Sony television were missing. Our neighbour Mrs. Anjali Verma told me "
                "that she noticed a scooter parked near our gate late at night on 1 November but did not think "
                "anything of it at the time. I suspect Mahesh Oraon, who worked as domestic help at our house for "
                "about eight months and left about two months ago, as he was familiar with where we kept our "
                "valuables and knew we would be travelling. I request that strict action be taken."
            ),
            "verbal_complaint_recorded_by": "SI Neeraj Bhandari, Duty Officer, PS Vasant Kunj",
            "complaint_read_and_verified": True, "time_of_complaint": "10:15 hours",
            "signature_thumb_impression": "Signed by complainant",
        },
        "witness_statement_1": {
            "statement_id": "WS/PSVKJ/0674/001", "date_of_recording": "2025-11-03", "time_of_recording": "12:00",
            "place": "C-118, Vasant Kunj, New Delhi", "recorded_by": "SI Neeraj Bhandari",
            "witness_details": {
                "witness_id": "WIT-001", "name": "Anjali Verma", "age": "39", "occupation": "Homemaker",
                "address": "C-120, Vasant Kunj, Sector C, New Delhi (neighbour)", "contact": "9899210047",
            },
            "statement_under_section": "Section 180 of the Bharatiya Nagarik Suraksha Sanhita, 2023",
            "statement_text": (
                "I live next door to Rohit Malhotra's house at C-118, Vasant Kunj. On the night of 1 November 2025, "
                "at around 11:30 pm, I was closing my balcony window when I noticed a grey scooter parked near the "
                "Malhotra house gate with a man standing beside it. I did not recognise the man clearly in the "
                "darkness and did not think it unusual at the time since the street often has parked vehicles. The "
                "next time I saw activity at the house was on the morning of 3 November when Mr. Malhotra returned "
                "and discovered the break-in. I am willing to assist in identifying the scooter if shown to me."
            ),
        },
        "witness_statement_2": {
            "statement_id": "WS/PSVKJ/0674/002", "date_of_recording": "2025-11-03", "time_of_recording": "13:30",
            "place": "PS Vasant Kunj", "recorded_by": "SI Neeraj Bhandari",
            "witness_details": {
                "witness_id": "WIT-002", "name": "Suman Lata", "age": "48", "occupation": "Domestic help",
                "address": "Rangpuri Pahari, New Delhi", "contact": "9654201177",
            },
            "statement_under_section": "Section 180 of the Bharatiya Nagarik Suraksha Sanhita, 2023",
            "statement_text": (
                "I currently work as domestic help in the C-block of Vasant Kunj. I know Mahesh Oraon, who earlier "
                "worked at the Malhotra house at C-118. About a week before the incident, Mahesh asked me casually "
                "whether the Malhotra family had any travel plans, saying he wanted to meet Mr. Malhotra about dues "
                "he claimed were pending. I did not think much of it then. I have seen Mahesh around the Vasant "
                "Kunj C-block market area occasionally even after he left the job."
            ),
        },
        "medical_report": {
            "mlc_no": "N/A", "date": "N/A", "hospital_name": "N/A",
            "patient_name": "N/A", "age": "N/A", "gender": "N/A", "examining_doctor": "N/A",
            "brought_by": "N/A",
            "findings": ["No person was injured in this incident; medical examination was not required."],
            "patient_status": "Not applicable - no injured person in this case.",
            "opinion": "Not applicable.",
            "injury_report_handed_to": "N/A",
        },
        "postmortem_report": {
            "report_no": "PM-NA-VKJ-02", "date": "2025-11-03", "status": "Not Applicable",
            "reason": "This is a case of theft in a dwelling house with no injury or death to any person.",
            "remarks": "Post-mortem examination is not applicable in this case.",
        },
        "fsl_report": {
            "report_no": "FSL/DEL/2025/FP/5541", "date": "2025-11-15", "laboratory_name": "Forensic Science Laboratory, Rohini, Delhi",
            "examined_items": ["Chance fingerprints lifted from the broken window grill and almirah handle", "Mahesh Oraon's specimen fingerprints"],
            "findings": [
                "Two chance fingerprints lifted from the window grill and almirah handle were found suitable for comparison.",
                "The chance fingerprints match the specimen fingerprints of the suspect Mahesh Oraon.",
            ],
            "opinion": "The fingerprints developed at the scene of crime are identical to the specimen fingerprints of Mahesh Oraon.",
        },
        "seizure_memo": {
            "memo_no": "SM/VKJ/0141/2025", "date_time": "2025-11-07 16:00", "place": "Mahesh Oraon's rented room, Rangpuri Pahari, New Delhi",
            "prepared_by": "SI Neeraj Bhandari",
            "seized_items": [
                {"description": "Gold jewellery (bangles and a chain, approx. 42 grams), identified by the complainant's wife", "exhibit_mark": "EX-1"},
                {"description": "Dell laptop bearing the complainant's name on the warranty sticker", "exhibit_mark": "EX-2"},
                {"description": "Pawn broker's receipt dated 02-11-2025 for the remaining jewellery pledged at a shop in Mehrauli", "exhibit_mark": "EX-3"},
            ],
        },
        "spot_panchnama": {
            "memo_no": "SP/VKJ/0102/2025", "date_time": "2025-11-03 11:00", "place": place,
            "panch_witnesses": ["Anjali Verma", "Market association representative Deepak Soni"],
            "observations": [
                "The grill of the rear bedroom window was found bent and the glass pane broken from outside.",
                "Cupboard in the bedroom found open with contents scattered.",
                "Muddy footprints were noted on the floor near the window, suggesting entry from the rear garden.",
                "Two latent fingerprints were lifted from the window grill and the almirah handle by the FSL team.",
            ],
            "prepared_by": "SI Neeraj Bhandari",
        },
        "vehicle_inspection": {
            "report_no": "VI/VKJ/0098/2025", "date": "2025-11-08", "vehicle_registration": "DL1SAB6621",
            "make_model": "Honda Activa", "inspected_by": "Motor Vehicle Inspector, Vasant Kunj Circle",
            "observations": [
                "Scooter recovered from Mahesh Oraon's rented accommodation at Rangpuri Pahari.",
                "Registration found to be in the name of the accused's brother.",
                "Tyre tread pattern is consistent with marks photographed near the complainant's gate on the night of the incident.",
            ],
        },
        "arrest_memo": {
            "memo_no": "AM/VKJ/0059/2025", "date_time": "2025-11-07 15:00", "arrested_person_name": "Mahesh Oraon",
            "father_name": "Suku Oraon", "age": "31", "address": "Rangpuri Pahari, New Delhi - 110037",
            "occupation": "Formerly domestic help; currently unemployed", "place_of_arrest": "Rangpuri Pahari, New Delhi",
            "arresting_officer": "SI Neeraj Bhandari",
            "grounds_of_arrest_informed": True, "right_to_inform_relative_informed": True,
            "relative_informed": "Wife, Smt. Sunita Oraon, informed telephonically at 15:30 hrs",
            "medical_examination_before_arrest": "Conducted at PS Vasant Kunj, no injury noted",
        },
        "accused_statement": {
            "statement_id": "AS/PSVKJ/0674/001", "date_of_recording": "2025-11-07", "time_of_recording": "17:00",
            "place": "Lock-up Room, PS Vasant Kunj", "recorded_by": "SI Neeraj Bhandari",
            "witness_to_recording": "ASI Mahendra Rawat, PS Vasant Kunj",
            "accused_details": {
                "accused_id": "ACC-001", "name": "Mahesh Oraon", "age": "31", "father_name": "Suku Oraon",
                "occupation": "Formerly domestic help", "education": "8th Pass", "marital_status": "Married",
                "address": "Rangpuri Pahari, New Delhi - 110037",
                "native_place": "Village Tapkara, District Khunti, Jharkhand",
                "contact": "9560217734",
            },
            "rights_read": {
                "article_20_3_read": True, "right_to_silence": True, "right_to_legal_counsel": True,
                "accused_understood_rights": True,
            },
            "statement_text": (
                "I, Mahesh Oraon, s/o Suku Oraon, state that I worked as domestic help at the house of Rohit "
                "Malhotra at C-118, Vasant Kunj for about eight months and left the job about two months ago over a "
                "dispute regarding unpaid wages. I knew the family was travelling to Jaipur for a wedding because "
                "Mr. Malhotra had mentioned it to me earlier. On the night of 1 November 2025, I went to the house "
                "on my brother's scooter, broke open the rear window grill, and entered the house. I took cash, "
                "some jewellery, a laptop and a television. I pledged part of the jewellery at a pawn shop in "
                "Mehrauli for money and kept the rest, the laptop and the cash with me. I am giving this statement "
                "voluntarily."
            ),
        },
        "cctv_report": {
            "report_id": "CCTV/PSVKJ/0674/2025", "date_of_collection": "2025-11-04", "date_of_analysis": "2025-11-04 to 2025-11-05",
            "analyzed_by": {"name": "HC Sandeep Kumar", "designation": "Head Constable, Technical Cell", "police_station": "Vasant Kunj"},
            "cctv_sources": [
                {
                    "source_id": "CCTV-001", "location": "C-Block market entrance, Vasant Kunj",
                    "camera_id": "CAM-CB-E1-04", "camera_type": "DVR-based dome camera",
                    "coverage_area": "Entrance road leading towards Sector C",
                    "footage_duration_obtained": "22:30 to 06:00, 01/02-11-2025",
                    "findings": "Shows a grey scooter entering the Sector C lane at 23:05 and leaving at 05:50, matching the timeframe of the incident.",
                },
            ],
        },
        "evidence_list": {
            "case_reference": case_number, "total_evidence_items": 6, "evidence_custodian": "MHC(M) - PS Vasant Kunj",
            "list_prepared_by": "SI Neeraj Bhandari, IO", "date": "2025-11-16",
            "items": [
                {
                    "evidence_id": "EVD-0674-001", "type": "Physical - Jewellery",
                    "description": "Gold jewellery, approximately 42 grams, identified by complainant's wife",
                    "quantity": "1 lot", "collected_from": "Accused's rented room, Rangpuri Pahari",
                    "collected_by": "SI Neeraj Bhandari", "date_time_collection": "2025-11-07, 16:00",
                    "seal_number": "NB-01", "current_location": "Malkhana, PS Vasant Kunj",
                    "chain_of_custody": [
                        {"date": "2025-11-07", "action": "Seized on accused's instance", "by": "IO"},
                        {"date": "2025-11-08", "action": "Shown to complainant's wife for identification", "by": "IO"},
                        {"date": "2025-11-08", "action": "Deposited in Malkhana", "by": "MHC(M)"},
                    ],
                },
                {
                    "evidence_id": "EVD-0674-002", "type": "Physical - Electronics",
                    "description": "Dell laptop, recovered from the accused's room",
                    "quantity": "1", "collected_from": "Accused's rented room, Rangpuri Pahari",
                    "collected_by": "SI Neeraj Bhandari", "date_time_collection": "2025-11-07, 16:00",
                    "seal_number": "NB-02", "current_location": "Malkhana, PS Vasant Kunj",
                },
                {
                    "evidence_id": "EVD-0674-003", "type": "Documentary",
                    "description": "Pawn broker's receipt for jewellery pledged at a Mehrauli shop",
                    "quantity": "1", "collected_from": "Accused's rented room, Rangpuri Pahari",
                    "collected_by": "SI Neeraj Bhandari", "date_time_collection": "2025-11-07, 16:00",
                    "seal_number": "NB-03", "current_location": "Case file",
                },
                {
                    "evidence_id": "EVD-0674-004", "type": "Physical - Vehicle",
                    "description": "Honda Activa scooter, registration DL1SAB6621",
                    "quantity": "1", "collected_from": "Rangpuri Pahari, at the time of arrest",
                    "collected_by": "SI Neeraj Bhandari", "date_time_collection": "2025-11-07, 15:10",
                    "seal_number": "NB-04", "current_location": "Malkhana yard, PS Vasant Kunj",
                },
                {
                    "evidence_id": "EVD-0674-005", "type": "Forensic - Fingerprints",
                    "description": "Chance fingerprints lifted from window grill and almirah handle",
                    "quantity": "2 lifts", "collected_from": "C-118, Vasant Kunj", "collected_by": "FSL mobile team",
                    "date_time_collection": "2025-11-03, 11:30", "seal_number": "FSL-LIFT-01", "current_location": "Forensic Science Laboratory, Rohini",
                },
                {
                    "evidence_id": "EVD-0674-006", "type": "Digital - CCTV footage",
                    "description": "CCTV footage from C-Block market entrance camera",
                    "quantity": "1 clip", "collected_from": "RWA office, C-Block Vasant Kunj",
                    "collected_by": "HC Sandeep Kumar", "date_time_collection": "2025-11-04, 10:00",
                    "seal_number": "SK-01", "current_location": "Case file digital evidence folder",
                },
            ],
        },
        "annexures": {
            "case_reference": case_number, "total_documents": 10, "prepared_by": "SI Neeraj Bhandari, IO", "date": "2025-11-20",
            "documents": [
                {"annexure_no": "A-1", "document_name": "First Information Report (FIR)", "document_id": case_number, "pages": 2, "filed_in_court": True, "exhibit_mark": "PW-1/A"},
                {"annexure_no": "A-2", "document_name": "Complaint under Section 173 BNSS", "document_id": "Complaint by Rohit Malhotra dated 03-11-2025", "pages": 1, "filed_in_court": True, "exhibit_mark": "PW-1/B"},
                {"annexure_no": "A-3", "document_name": "Statement of witness Anjali Verma", "document_id": "WS/PSVKJ/0674/001", "pages": 1, "filed_in_court": True, "exhibit_mark": "PW-2"},
                {"annexure_no": "A-4", "document_name": "Statement of witness Suman Lata", "document_id": "WS/PSVKJ/0674/002", "pages": 1, "filed_in_court": True, "exhibit_mark": "PW-3"},
                {"annexure_no": "A-5", "document_name": "Spot Panchnama", "document_id": "SP/VKJ/0102/2025", "pages": 1, "filed_in_court": True, "exhibit_mark": "PW-1/C"},
                {"annexure_no": "A-6", "document_name": "FSL Report (fingerprints)", "document_id": "FSL/DEL/2025/FP/5541", "pages": 2, "filed_in_court": True, "exhibit_mark": "PW-4/A"},
                {"annexure_no": "A-7", "document_name": "Arrest Memo", "document_id": "AM/VKJ/0059/2025", "pages": 1, "filed_in_court": True, "exhibit_mark": "PW-5/A"},
                {"annexure_no": "A-8", "document_name": "Seizure Memo", "document_id": "SM/VKJ/0141/2025", "pages": 1, "filed_in_court": True, "exhibit_mark": "PW-5/B"},
                {"annexure_no": "A-9", "document_name": "CCTV Analysis Report", "document_id": "CCTV/PSVKJ/0674/2025", "pages": 1, "filed_in_court": True, "exhibit_mark": "PW-6/A"},
                {"annexure_no": "A-10", "document_name": "Case Diary", "document_id": "CD/VKJ/0674/2025", "pages": 2, "filed_in_court": False, "exhibit_mark": "N/A (not tendered)"},
            ],
        },
        "timeline": {
            "case_reference": case_number, "source_evidence": "Fingerprint report, CCTV footage, witness statements, accused statement",
            "events": [
                {"time": "2025-11-01 18:00", "event": "Malhotra family leaves for Jaipur for a wedding.", "source": "Complainant's statement", "confidence": "High"},
                {"time": "2025-11-01 23:05", "event": "A grey scooter is seen entering the Sector C lane near the complainant's house.", "source": "CCTV-001", "confidence": "High"},
                {"time": "2025-11-01 23:00 to 2025-11-02 07:00", "event": "Rear window grill broken; house entered and ransacked; cash, jewellery, laptop and television taken.", "source": "Spot panchnama, accused statement", "confidence": "High"},
                {"time": "2025-11-02 05:50", "event": "The grey scooter is seen leaving the Sector C lane.", "source": "CCTV-001", "confidence": "High"},
                {"time": "2025-11-02", "event": "Accused pledges part of the jewellery at a pawn shop in Mehrauli.", "source": "Pawn broker's receipt, accused statement", "confidence": "High"},
                {"time": "2025-11-03 09:30", "event": "Malhotra family returns and discovers the break-in.", "source": "Complainant's statement", "confidence": "High"},
                {"time": "2025-11-03 10:30", "event": "FIR registered at PS Vasant Kunj.", "source": "FIR record", "confidence": "High"},
                {"time": "2025-11-07", "event": "Accused Mahesh Oraon traced and arrested; jewellery, laptop and scooter recovered.", "source": "Arrest memo, seizure memo", "confidence": "High"},
                {"time": "2025-11-15", "event": "FSL report confirms the accused's fingerprints match those lifted at the scene.", "source": "FSL report", "confidence": "High"},
            ],
        },
        "site_plan": {
            "plan_no": "SP-PLAN/VKJ/0674/2025", "date": "2025-11-03", "prepared_by": "Draftsman, PS Vasant Kunj",
            "location": place,
            "annotations": [
                "Point A: Front gate of the house.",
                "Point B: Rear bedroom window, point of entry, marked with 'X'.",
                "Point C: Position of the neighbour's balcony from which the scooter was seen.",
                "Point D: Approximate parking position of the scooter on the night of the incident.",
            ],
            "scale": "Not to scale, approximate distances marked in metres",
        },
        "case_diary": {
            "diary_number": "CD/VKJ/0674/2025", "officer_name": "SI Neeraj Bhandari",
            "entries": [
                {"entry_number": "1", "date": "2025-11-03", "text": "FIR registered. Spot visited and inspected. Statements of neighbour and a local domestic worker recorded. FSL team called to lift fingerprints."},
                {"entry_number": "2", "date": "2025-11-04", "text": "CCTV footage collected from C-Block market entrance camera and sent for analysis."},
                {"entry_number": "3", "date": "2025-11-07", "text": "Accused Mahesh Oraon traced to Rangpuri Pahari and arrested. Jewellery, laptop, pawn broker's receipt and scooter recovered at his instance. Accused statement recorded."},
                {"entry_number": "4", "date": "2025-11-15", "text": "FSL report received confirming the fingerprints lifted at the scene match the accused."},
                {"entry_number": "5", "date": "2025-11-20", "text": "Annexures and evidence list compiled. Investigation substantially complete; chargesheet under preparation."},
            ],
        },
        "master_case": {
            "case_identifier": {"fir_number": case_number, "crime_number": "CR/2025/DL/PSVKJ/0411", "ps_case_number": "PSVKJ/2025/INV/233"},
            "police_station": {"name": station["name"], "district": station["district"], "state": station["state"], "police_station_code": "PSVKJ", "jurisdiction": "Vasant Kunj Sector A to D, Rangpuri Pahari"},
            "incident_details": {"date": "2025-11-01/02", "day": "Saturday night to Sunday morning", "time": "23:00 to 07:00", "timezone": "IST", "weather": "Clear, cold night", "lighting": "Street lit, house unlit (family away)"},
            "location": {"address": place, "area": "Vasant Kunj", "city": "New Delhi", "pincode": "110070"},
            "investigation_status": "Fully resolved; accused arrested, stolen property substantially recovered, forensic match obtained; charge-sheet under preparation",
        },
    }


def _case_documents(case: dict) -> list[tuple[str, str, dict]]:
    return [(key, title, case[key]) for key, title in DOC_TYPES]


def generate(out_root: Path) -> None:
    cases = {
        "LajpatNagar_ChainSnatching": lajpat_nagar_case(),
        "VasantKunj_Burglary": vasant_kunj_case(),
    }
    for folder_name, case in cases.items():
        out_dir = out_root / folder_name
        if out_dir.is_dir():
            shutil.rmtree(out_dir)
        out_dir.mkdir(parents=True, exist_ok=True)
        station_name = case["station"]["name"]
        case_number = case["case_number"]
        for key, title, fields in _case_documents(case):
            pdf_bytes = render_record_pdf(title, station_name, case_number, fields)
            (out_dir / f"{key}.pdf").write_bytes(pdf_bytes)
        print(f"{folder_name}: {len(DOC_TYPES)} PDF(s) written to {out_dir}")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--out-dir", type=Path, default=SAMPLE_CASES_DIR, help="Parent directory for the case folders.")
    args = parser.parse_args()
    generate(args.out_dir)
    print('\nUpload each folder\'s PDFs to a new case in the frontend, then click "Process Case".')


if __name__ == "__main__":
    main()
