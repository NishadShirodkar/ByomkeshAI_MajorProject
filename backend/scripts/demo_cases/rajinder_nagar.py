"""Case C: rash riding causing grievous hurt at Shankar Road T-Point, Rajinder Nagar (FIR 0452/2024).

Rebuilt from the original 19-document bundle of case 26a276cb918e5d36ad36c6662e5c6086, whose files had
been ingested unclassified and produced an unstructured charge sheet. Investigation complete; draft charge
sheet awaiting supervisory approval.
"""

from __future__ import annotations

from .common import DemoCase, DemoDocument

CASE_ID = "26a276cb918e5d36ad36c6662e5c6086"
TITLE = "Rash riding causing grievous hurt, Rajinder Nagar"
STATION = "Rajinder Nagar Police Station, Central District, New Delhi"
IO_ID, IO_NAME = "IO-INSP-SURESH-CHANDRA", "Inspector Suresh Chandra"
PLACE = "Shankar Road T-Point, near St. Stephen's Hospital Gate No. 2, Rajinder Nagar, New Delhi"
COURT = "Metropolitan Magistrate, Tis Hazari Courts, Delhi"
PULSAR, ACTIVA = "DL2SBP1234", "DL5SCT5678"

NARRATIVE = (
    "On 15 October 2024 at about 6:20 pm, the accused Amit Verma, a food delivery rider, was riding his red Bajaj Pulsar 220F "
    f"motorcycle {PULSAR} on Shankar Road from the Karol Bagh side towards Rajinder Nagar at a speed of about 55 to 60 km/h in a "
    "40 km/h zone, in a rash and negligent manner endangering human life. The traffic signal at the T-Point near St. Stephen's "
    "Hospital Gate No. 2 was non-functional and Traffic Constable Mohammed Asif was regulating traffic by hand. Ignoring the "
    "constable's raised hand signal to stop, the accused crossed the stop line and rode into the junction, where he hit the "
    f"right side of the white Honda Activa scooter {ACTIVA} ridden by the victim Rajesh Kumar Sharma, who was lawfully completing "
    "a right turn towards Old Rajinder Nagar with his indicator on. In the accident the victim was thrown about four metres and sustained "
    "grievous injuries, including a head injury with a subdural haematoma, a comminuted fracture of the right femur, a fracture "
    "of the right clavicle, fractures of three right ribs and a liver laceration, which endangered his life. The accused tried to "
    "pick up his motorcycle and leave the spot without helping the injured, but Constable Mohammed Asif caught him at the spot "
    "with the help of members of the public. Inspector Suresh Chandra arrested the accused at the spot at about 7:15 pm and seized "
    "both vehicles. The cameras at St. Stephen's Hospital Gate No. 2 and at the Canara Bank ATM on Shankar Road recorded the "
    "motorcycle approaching at high speed, crossing the stop line against the constable's signal and striking the scooter, and the "
    "accused, who was hurrying to deliver a food order, did not stop to provide or arrange medical aid for the injured."
)


def documents() -> list[DemoDocument]:
    complaint_text = (
        "Respected Sir, I, Sunita Sharma, wife of Rajesh Kumar Sharma, resident of B-143, R.P. Bagh, Pusa Road, New Delhi, state "
        "that my husband works as an accountant at the DTC Inderlok Depot and normally reaches home by about 6:30 pm on his white "
        f"Honda Activa scooter {ACTIVA}.\n\n"
        "On 15 October 2024 a stranger called me from my husband's mobile phone and told me that my husband had met with an "
        "accident at the Shankar Road T-Point near St. Stephen's Hospital. I rushed to St. Stephen's Hospital and found my husband "
        "in the emergency ward with serious injuries to his head, right leg, right shoulder and chest. He was bleeding from the head "
        "and could not speak properly.\n\n"
        "The traffic police constable present at the hospital told me that the accident happened because a young man named Amit "
        f"Verma, riding a red Pulsar motorcycle {PULSAR} at very high speed, ignored the constable's signal to stop and hit my "
        "husband's scooter while my husband was taking a lawful turn towards Old Rajinder Nagar. The motorcycle rider was wearing "
        "the red T-shirt of a food delivery company and was caught at the spot by the constable.\n\n"
        "The doctors have told me that my husband has a blood clot in the head, a broken thigh bone, a broken collar bone, broken ribs "
        "and an injury to the liver, and that he is in the ICU and in danger. Because of the rash and negligent riding of Amit Verma "
        "my husband has suffered grievous injuries and our family is in great distress. I request that strict legal action be taken "
        "against Amit Verma. I have given this complaint of my own free will and the facts stated are true to my knowledge."
    )
    asif = (
        "I, Mohammed Asif, Traffic Police Constable, Badge No. TPC/DL/3342, posted at the Karol Bagh Traffic Circle, state that on "
        "15 October 2024 I was on duty at the Shankar Road T-Point near St. Stephen's Hospital Gate No. 2 from 4 pm to 8 pm. The "
        "traffic signal at this junction had not been working for three days and I was regulating traffic by hand. I had already "
        "reported the faulty signal to the Traffic Circle office in writing.\n\n"
        "At about 6:20 pm I was standing in the middle of the junction. Vehicles from the Rajinder Nagar side had the right of way and "
        "were turning towards Old Rajinder Nagar. A white Honda Activa scooter was making a slow right turn with its indicator on. At "
        f"that moment I saw a red Bajaj Pulsar motorcycle {PULSAR} coming very fast on Shankar Road from the Karol Bagh side. I "
        "estimate its speed at more than 55 km/h. I raised my left hand towards the rider and signalled him to stop, but he did not "
        "slow down. He was looking down at a mobile phone fixed on the handlebar of the motorcycle.\n\n"
        f"The Pulsar crossed the stop line and hit the right side of the Activa {ACTIVA} in the middle of the turn. The impact was so "
        "strong that the scooter rider was thrown off and fell on the road about four metres away near the edge of the road. He was "
        "wearing a white helmet. The Pulsar rider also fell, but he got up quickly and tried to lift his motorcycle to leave the spot "
        "without helping the injured man. I ran to him, caught his right arm and, with the help of the tea stall owner Prakash Chandra "
        "Joshi and other people, made him sit on the footpath. He told me his name was Amit Verma.\n\n"
        "I then called the PCR on 112 from my mobile phone and also asked the security staff of St. Stephen's Hospital for an "
        "ambulance. The PCR van Z-45 and the ambulance reached the spot within a few minutes and the injured man was taken to the "
        "hospital emergency. I handed over Amit Verma to the PCR staff and later to Inspector Suresh Chandra. Amit Verma was wearing "
        "a red Zomato T-shirt, blue jeans and a black helmet with a broken chin strap, and a red food delivery bag was tied to the "
        "motorcycle. I can identify him and both vehicles. I acted as a panch witness to the spot inspection, the seizure of the "
        "vehicles and the arrest. This statement is true and is given voluntarily."
    )
    joshi = (
        "My name is Prakash Chandra Joshi. I have run a tea stall at Shop No. 7, Shankar Road, opposite Gate No. 2 of St. Stephen's "
        "Hospital, for the last 22 years. My stall is about 35 metres from the T-Point.\n\n"
        "On 15 October 2024 at about 6:20 pm I was making tea for my customers when I heard the loud screech of brakes followed by "
        "a heavy crash. I immediately came out and saw that a red motorcycle had crashed into a white Activa scooter in the middle "
        "of the T-Point. The scooter rider was lying on the road near the edge of the road and the motorcycle rider was getting up. "
        "The traffic constable on duty, whom I know as Asif, ran and caught the motorcycle rider by the arm because he was trying to "
        "lift his motorcycle and go away.\n\n"
        "I went near to help. The injured scooter rider was bleeding from his head and his right leg was bent in an unnatural way. He "
        "was crying in pain. Along with the constable I moved him carefully to the side of the road so that no other vehicle would run "
        "over him, and I gave him water. The motorcycle rider was wearing the red T-shirt of a food delivery company and had a red "
        "delivery box on his motorcycle. The constable was scolding him for over-speeding and for not stopping at his signal.\n\n"
        "In my many years at this stall I have seen that vehicles from the Shankar Road side come very fast and do not stop when the "
        "signal is not working. The hospital ambulance came quickly because the hospital is just opposite, and the police arrived soon "
        "after. I gave my name and mobile number to the police and I signed the spot inspection memo and the seizure memo as a panch "
        "witness. I can identify both vehicles and the motorcycle rider. What I have stated is true."
    )
    victim = (
        "I, Rajesh Kumar Sharma, aged 42 years, son of Late Om Prakash Sharma, resident of B-143, R.P. Bagh, Pusa Road, New Delhi, "
        "state that I work as an accountant at the DTC Inderlok Depot. On 15 October 2024 I left office at about 6:05 pm on my white "
        f"Honda Activa scooter {ACTIVA} and was going home. I was wearing my ISI-marked helmet with the strap fastened and I was "
        "riding at about 30 to 35 km/h.\n\n"
        "At about 6:20 pm I reached the Shankar Road T-Point near St. Stephen's Hospital. The signal was not working and a traffic "
        "constable was controlling the traffic. He allowed the traffic from my side to turn, so I switched on my right indicator, "
        "slowed down to about 10 km/h and began turning right towards Old Rajinder Nagar. When I was in the middle of the turn, a "
        "motorcycle coming at very high speed from the Karol Bagh side suddenly hit the right side of my scooter. I was thrown off "
        "and I do not remember anything after that.\n\n"
        "When I regained full consciousness I was in the ICU of St. Stephen's Hospital. The doctors told me that I had a blood clot in "
        "my head that had to be removed by an operation, a broken right thigh bone that was fixed with a rod, a broken right collar "
        "bone, three broken ribs and an injury to my liver. I remained in hospital for 36 days. I still cannot walk without support "
        "and I need physiotherapy for at least three months. The doctors have said that my right leg may remain shorter.\n\n"
        "I did nothing wrong; I was riding slowly, wearing my helmet and turning lawfully. The accident happened only because of the "
        "rash and negligent riding of the motorcycle rider. I have spent about Rs 4.2 lakh on treatment so far and I have been on "
        "leave without pay for three months. I want strict action against the accused and compensation for my losses."
    )
    ramesh_pcr = (
        "I, HC Ramesh, am posted as In-charge of PCR Van Z-45, Central District. On 15 October 2024 at about 6:24 pm my van received a "
        "call from the control room about an accident involving two two-wheelers at the Shankar Road T-Point near St. Stephen's "
        "Hospital, with one person injured.\n\n"
        "We reached the spot at about 6:31 pm. A crowd had gathered. A red Bajaj Pulsar motorcycle and a white Honda Activa scooter "
        "were lying on their right sides in the junction. An injured man was lying near the edge of the road with a bleeding head "
        "wound and a deformed right thigh. Traffic Constable Mohammed Asif was holding a young man in a red Zomato T-shirt, who gave "
        "his name as Amit Verma and who, according to the constable, had been riding the Pulsar.\n\n"
        "The hospital ambulance reached the spot at about 6:35 pm. I helped the medical staff put the injured man on a stretcher and "
        "accompanied him to the emergency of St. Stephen's Hospital, where he was admitted. His name was found to be Rajesh Kumar "
        "Sharma from the papers in his pocket. I informed the duty officer of PS Rajinder Nagar. My colleague kept Amit Verma at the "
        "spot until Inspector Suresh Chandra arrived. The dash camera of the PCR van was recording throughout, and I handed over its "
        "memory card to the investigating officer when it was asked for. This statement is true."
    )
    thomas = (
        "I, Thomas George, am the Security In-charge of St. Stephen's Hospital, Tis Hazari. The hospital has an IP camera, CAM-SSH-G2-03, "
        "mounted above Gate No. 2. It faces Shankar Road and gives a clear and full view of the T-Point about 30 metres away. The "
        "camera records continuously to a digital video recorder kept in the security control room, and its clock is checked every "
        "week against standard time.\n\n"
        "When Inspector Suresh Chandra visited the security control room and asked for the recordings of the evening of the accident, "
        "I played back the footage in his presence. The footage shows the white scooter turning, the red motorcycle entering the "
        "junction at speed against the hand signal of the traffic constable, and the collision.\n\n"
        "At the request of the investigating officer I removed the 1 TB hard disk containing the relevant recording from the DVR and "
        "handed it over to him. He sealed it with the seal SC in my presence and I signed the seizure memo. A certificate under Section "
        "63 of the Bharatiya Sakshya Adhiniyam regarding the recording system was also issued by me. Nobody has tampered with the "
        "recording. I can identify the hard disk and my signature on the seizure memo."
    )
    venkatesh = (
        "I, S. Venkatesh, am the Branch Manager of Canara Bank, Shankar Road branch. The bank's ATM kiosk on Shankar Road, about 50 "
        "metres south of the T-Point near St. Stephen's Hospital, has a CP Plus dome camera, CAM-CB-ATM-01, that covers the ATM entrance "
        "and about 30 metres of Shankar Road on the Karol Bagh side.\n\n"
        "On a written request from Inspector Suresh Chandra I retrieved the recording of the evening of the accident from the ATM camera "
        "system and copied the relevant portion onto a pen drive in his presence. The copy shows a red motorcycle passing the ATM "
        "towards the junction at high speed with its rider in a red T-shirt and a delivery bag on the motorcycle, and a crash sound picked "
        "up by the kiosk microphone a few seconds later.\n\n"
        "The pen drive was sealed by the investigating officer and I signed the seizure memo. I have issued a certificate under Section "
        "63 of the Bharatiya Sakshya Adhiniyam for the copy. The original recording is preserved on the bank's system."
    )
    ramphal = (
        "I, ASI Ramphal Singh, am posted at Police Station Rajinder Nagar. On 15 October 2024 I joined the investigation of this case "
        "with Inspector Suresh Chandra.\n\n"
        "I was present when the accused Amit Verma was formally arrested and personally searched by the investigating officer. From "
        "his person a black Samsung Galaxy M32 mobile phone, a wallet containing Rs 850, his driving licence, a photocopy of his Aadhaar "
        "card and an SBI ATM card, the motorcycle keys and a red Zomato delivery bag were recovered. The grounds of arrest and his "
        "rights, including the right to bail and to a lawyer, were explained to him in Hindi.\n\n"
        "At about 8:15 pm on the same day I informed his father, Ramesh Verma, of the arrest by telephone. I also escorted the accused "
        "for medical examination at Dr. Ram Manohar Lohia Hospital, where his blood sample was collected and sealed. I was present as a "
        "witness when the investigating officer recorded the disclosure of the accused in the lock-up in the presence of a legal aid "
        "counsel. I can identify the accused and the articles recovered from him."
    )
    rajender = (
        "I, ASI Rajender Prasad, am posted in the Motor Transport Section and have 18 years of experience in the mechanical examination "
        "of vehicles. On 16 October 2024 I mechanically inspected the red Bajaj Pulsar 220F and the white Honda Activa 6G in the vehicle "
        "yard of PS Rajinder Nagar with the help of Constable Mohan Singh, a mechanic.\n\n"
        f"Both vehicles were roadworthy before the accident and had working brakes, tyres, lights and steering. The Pulsar {PULSAR} had "
        "heavy damage to its front and right side, its speedometer needle was jammed at the 55 km/h mark, and its front brake lever was "
        f"in the applied position, which shows that the rider braked only at the last moment. The Activa {ACTIVA} had a deep dent and "
        "scrape on its right body panel at the height of the Pulsar's front wheel and fairing, with red paint transfer.\n\n"
        "In my opinion the damage on both vehicles matches a near right-angle collision in which the front of the Pulsar struck the "
        "right side of the Activa at about 50 to 58 km/h, and no mechanical defect in either vehicle contributed to the accident. I "
        "prepared detailed inspection reports for both vehicles."
    )

    sunita_supp = (
        "I, Sunita Sharma, wife of Rajesh Kumar Sharma, have been called again by the investigating officer and I state further that "
        "after giving my complaint I remained at St. Stephen's Hospital with my husband throughout his treatment. He was kept in the ICU "
        "for nine days. On the second day the neurosurgeons operated on his head to remove the blood clot, and the orthopaedic doctors "
        "fixed his thigh bone with a metal rod. For several days he could not recognise people properly and could not eat on his own.\n\n"
        "My husband is the only earning member of our family. We have two children studying in Class 8 and Class 5. Since the accident he "
        "has been on leave without pay. We have spent about Rs 4.2 lakh on treatment, medicines, the walker and physiotherapy, part of it "
        "borrowed from relatives. I have handed over copies of the hospital bills, pharmacy receipts and his salary slips to the police.\n\n"
        "On the evening of the accident, when I reached the emergency, the traffic constable Mohammed Asif told me in the presence of other "
        "people how the motorcycle rider had come at high speed against his signal. Later the same night I saw the accused at the police "
        "station; he was the young man in the red delivery T-shirt. Neither he nor anyone from his side came to ask about my husband's "
        "condition. I request that the accused be punished and that we be given compensation under the victim compensation scheme."
    )
    victim_final = (
        "I, Rajesh Kumar Sharma, after my discharge from St. Stephen's Hospital, state further that I remained in hospital for 36 days. "
        "I underwent an operation on my head and an operation on my right thigh. I am now at home and can walk only with a walker. I "
        "attend physiotherapy three times a week and must go for review in the orthopaedic and neurosurgery OPDs.\n\n"
        "The doctors have told me that my right leg has become about one and a half centimetres shorter and that the final disability "
        "will be assessed after six months. I still have headaches and some difficulty in remembering things, for which I am taking "
        "medicines. I cannot ride a scooter or sit at my desk for long, and my department has granted me medical leave without pay.\n\n"
        "So far the treatment has cost about Rs 4.2 lakh, and I have lost three months' salary. I have given copies of my medical bills, "
        "discharge summary and salary slips to the investigating officer for the victim compensation application. I again state that I "
        "was riding slowly, wearing my helmet and turning lawfully with my indicator on. I want the accused to be punished according to "
        "law and I request compensation for my losses."
    )
    dr_mehta = (
        "I, Dr. Anjali Mehta, MBBS, MS (Orthopaedics), Senior Resident, Emergency Department, St. Stephen's Hospital, registration number "
        "DMC/R/2010/45678, state that on 15 October 2024 at about 6:45 pm the patient Rajesh Kumar Sharma, aged 42 years, was brought to "
        "the emergency by the staff of PCR Van Z-45 with a history of a road traffic accident at the Shankar Road T-Point. I examined him "
        "and prepared the MLC number MLC/SSH/2024/5642.\n\n"
        "He was conscious but disoriented, with a Glasgow Coma Scale of 13 out of 15, low blood pressure, a fast pulse and active bleeding "
        "from a scalp wound. Investigations showed an acute subdural haematoma with a midline shift, a comminuted fracture of the right "
        "femur, a displaced fracture of the right clavicle, fractures of three right ribs and a Grade II laceration of the liver. He was "
        "resuscitated, splinted and admitted to the surgical ICU, and the neurosurgery, orthopaedics and general surgery teams were "
        "called.\n\n"
        "In my opinion the injuries are grievous; the head injury was dangerous to life at the time of admission and the femur fracture "
        "alone kept him in hospital and unable to follow his ordinary pursuits for well over twenty days. The pattern of injuries on the "
        "right side of his head, shoulder, chest and thigh is consistent with a high-speed impact from a motorcycle on the right side of a "
        "scooter followed by a fall on the road. His helmet was cracked on the right side, which shows it took the force of the blow to his "
        "head. His blood alcohol was nil. I also issued the discharge summary on 20 November 2024. I can identify the MLC and the "
        "discharge summary, which bear my signature."
    )
    ramesh_kumar = (
        "I, HC Ramesh Kumar, am posted in the photography section and technical cell of PS Rajinder Nagar. On 15 October 2024 I joined the "
        "spot inspection with Inspector Suresh Chandra at the Shankar Road T-Point and took 25 digital photographs of the scene with the "
        "police station camera, a Canon EOS 1300D. The photographs show the general view of the junction from all four sides, the impact "
        "point and debris, the skid mark with a measuring scale, the resting positions of both vehicles, the blood stain, the "
        "non-functional signal, the speed limit board, the stop line and the zebra crossing. I handed over the SD card to the "
        "investigating officer, who sealed it.\n\n"
        "On 16 and 17 October 2024 I examined the recordings of the hospital gate camera, the bank ATM camera and the PCR dash camera "
        "on a forensic workstation, working only on verified copies with hash values recorded. Using the road markings measured during "
        "the spot inspection as reference distances and counting frames, I calculated the speed of the motorcycle as about 60 km/h while "
        "passing the ATM and about 52 km/h between the stop line and the point of impact. The scooter was moving at about 10 km/h.\n\n"
        "The hospital camera clearly shows the traffic constable raising his hand to stop the Shankar Road traffic one second before the "
        "motorcycle crossed the stop line. The timestamps of all three recordings agree with one another within two seconds. I found no "
        "sign of editing or tampering. I prepared the CCTV analysis report and issued a certificate for the copies I made."
    )
    mohan_singh = (
        "I, Constable Mohan Singh, am posted at PS Rajinder Nagar and I am also a trained mechanic. On 16 October 2024 I assisted ASI "
        "Rajender Prasad during the mechanical inspection of the red Pulsar and the white Activa in the police station yard and I signed "
        "the inspection reports as a witness.\n\n"
        "On 17 October 2024 the investigating officer handed over to me the sealed exhibits of this case, namely the two helmets, the "
        "broken vehicle parts, the blood samples of the accused and the victim, the SD card of photographs and the DVR hard disk, along "
        "with the forwarding letter and road certificate number 234/2024. The seals bearing the impression SC were intact. The two "
        "vehicles were taken to the laboratory yard in a police recovery van under my escort.\n\n"
        "I deposited all the exhibits at the Forensic Science Laboratory, Rohini, on the same day and obtained the receipt, which I "
        "handed to the investigating officer. While the exhibits were in my possession nobody tampered with them. After the "
        "examination the exhibits were returned to the malkhana under seal."
    )
    zomato = (
        "I, Kavita Arora, am the nodal officer for law enforcement requests of Zomato Limited for the Delhi region. In reply to a notice "
        "under Section 94 BNSS from PS Rajinder Nagar I furnished the records of delivery partner ID ZOM/DL/478923, who is registered in "
        "the name of Amit Verma, son of Ramesh Verma, with a red Bajaj Pulsar motorcycle declared as his delivery vehicle.\n\n"
        "Our records show that on 15 October 2024 the delivery partner logged in at 9:40 am and completed 18 deliveries during the day. "
        "At 6:10 pm he accepted an order from Haldiram's, Karol Bagh, for delivery near Bada Bazaar, Old Rajinder Nagar, and the app shows "
        "the order picked up at 6:15 pm with a promised delivery time of 6:35 pm. The location pings from his app place him on Shankar Road "
        "moving towards Rajinder Nagar at speeds between 55 and 65 km/h in the minutes before 6:20 pm, after which the pings stop moving at "
        "the T-Point near St. Stephen's Hospital. The order was later marked as delayed and was delivered by another partner.\n\n"
        "These records are generated automatically in the ordinary course of business and are stored on the company's servers. I have "
        "issued a certificate under Section 63 of the Bharatiya Sakshya Adhiniyam for the printouts supplied. Our partner guidelines "
        "require delivery partners to follow all traffic rules and not to use the phone while riding."
    )
    traffic_circle = (
        "I, SI Naresh Kumar, am posted as the Zonal Officer, Karol Bagh Traffic Circle. On the request of the investigating officer I have "
        "produced the record of the circle relating to the traffic signal at the Shankar Road T-Point near St. Stephen's Hospital Gate "
        "No. 2.\n\n"
        "As per our record, a written report was received from Traffic Constable Mohammed Asif on 13 October 2024 that the signal at "
        "this junction had stopped working, and it was forwarded the same day to the signal maintenance agency. The signal was repaired "
        "on 18 October 2024. Until then a constable was deployed to regulate the junction manually.\n\n"
        "As per the duty roster of the circle, Constable Mohammed Asif, badge TPC/DL/3342, was deployed at this junction on 15 October "
        "2024 from 4 pm to 8 pm for manual traffic regulation. The speed limit on this stretch of Shankar Road is 40 km/h and a speed limit "
        "board is installed about 100 metres before the junction. I have handed over attested copies of the complaint register entry and "
        "the duty roster to the investigating officer."
    )

    def witness(filename: str, ref: str, name: str, date: str, age: str, occupation: str, address: str, father: str, contact: str, text: str) -> DemoDocument:
        return DemoDocument(
            filename, "WitnessStatement", ref, "STATEMENT OF WITNESS UNDER SECTION 180 BNSS",
            {"statement_reference": ref, "statement_date": date, "witness_name": name, "father_name": father, "age": age, "occupation": occupation,
             "witness_address": address, "contact": contact, "recorded_by": IO_NAME, "statement_text": text},
        )

    return [
        DemoDocument(
            "fir.pdf", "FIR", "0452/2024", "FIRST INFORMATION REPORT (Section 173 BNSS)",
            {"fir_number": "0452/2024", "crime_number": "0452/2024", "registration_date": "2024-10-15", "police_station": "Rajinder Nagar",
             "complainant_name": "Sunita Sharma", "accused_names": ["Amit Verma"], "victim_names": ["Rajesh Kumar Sharma"],
             "vehicle_registrations": [PULSAR, ACTIVA], "occurrence_datetime": "2024-10-15T18:20:00+05:30", "occurrence_location": PLACE,
             "jurisdiction": "Central Delhi", "court": COURT,
             "reported_sections": ["Section 281 BNS", "Section 125(b) BNS", "Section 184 Motor Vehicles Act", "Section 134 Motor Vehicles Act"],
             "narrative_text": NARRATIVE},
            [("Time of FIR", "7:30 pm"), ("General Diary reference", "DD No. 24-A"), ("Beat", "Beat No. 12, Rajinder Nagar"),
             ("Distance from police station", "1.5 km north-east"), ("Investigating officer", IO_NAME), ("Duty officer", "SI Vikram Singh")],
        ),
        DemoDocument(
            "complaint.pdf", "Complaint", "C/RJN/0452/2024", "WRITTEN COMPLAINT",
            {"complaint_reference": "C/RJN/0452/2024", "complaint_date": "2024-10-15", "complainant_name": "Sunita Sharma",
             "complainant_address": "B-143, R.P. Bagh, Pusa Road, New Delhi - 110005", "person_complained_against_names": ["Amit Verma"],
             "victim_names": ["Rajesh Kumar Sharma"], "vehicle_registrations": [PULSAR, ACTIVA], "complaint_text": complaint_text},
            [("To", "The SHO, Police Station Rajinder Nagar"), ("Relation to victim", "Wife"), ("Recorded by", "SI Vikram Singh, Duty Officer")],
        ),
        witness("witness_statement_01.pdf", "WS/RJN/0452/01", "Mohammed Asif", "2024-10-15", "35", "Traffic Police Constable (TPC/DL/3342)",
                "Police Lines, Rajinder Nagar, New Delhi", "Mohammed Jameel", "9891234567", asif),
        witness("witness_statement_02.pdf", "WS/RJN/0452/02", "Prakash Chandra Joshi", "2024-10-15", "55", "Tea stall owner",
                "Shop No. 7, Shankar Road, opposite Gate No. 2, St. Stephen's Hospital, New Delhi", "Late Ganesh Dutt Joshi", "9958321456", joshi),
        witness("witness_statement_03.pdf", "WS/RJN/0452/03", "HC Ramesh", "2024-10-15", "44", "Head Constable, In-charge PCR Van Z-45",
                "PCR Unit, Central District, Delhi Police", "Shiv Charan", "9810011245", ramesh_pcr),
        witness("witness_statement_04.pdf", "WS/RJN/0452/04", "Ramphal Singh", "2024-10-16", "51", "Assistant Sub-Inspector, PS Rajinder Nagar",
                "PS Rajinder Nagar, New Delhi", "Late Hukam Singh", "9810076543", ramphal),
        witness("witness_statement_05.pdf", "WS/RJN/0452/05", "Thomas George", "2024-10-16", "47", "Security In-charge, St. Stephen's Hospital",
                "Staff Quarters, St. Stephen's Hospital, Tis Hazari, Delhi", "George Mathew", "9811223344", thomas),
        witness("witness_statement_06.pdf", "WS/RJN/0452/06", "S. Venkatesh", "2024-10-16", "45", "Branch Manager, Canara Bank, Shankar Road",
                "Flat 22, Bank Colony, Patel Nagar, New Delhi", "S. Raghavan", "9818765432", venkatesh),
        witness("witness_statement_07.pdf", "WS/RJN/0452/07", "Rajender Prasad", "2024-10-16", "49", "Assistant Sub-Inspector, Motor Transport Section",
                "PS Rajinder Nagar, New Delhi", "Late Ram Prasad", "9810054321", rajender),
        witness("witness_statement_08.pdf", "WS/RJN/0452/08", "Rajesh Kumar Sharma", "2024-10-25", "42", "Accountant, DTC Inderlok Depot",
                "B-143, R.P. Bagh, Pusa Road, New Delhi - 110005", "Late Om Prakash Sharma", "9810345678", victim),
        witness("witness_statement_09.pdf", "WS/RJN/0452/09", "Sunita Sharma", "2024-10-16", "38", "Teacher, Sarvodaya Vidyalaya, Patel Nagar",
                "B-143, R.P. Bagh, Pusa Road, New Delhi - 110005", "W/o Rajesh Kumar Sharma", "9810345679", sunita_supp),
        witness("witness_statement_10.pdf", "WS/RJN/0452/10", "Dr. Anjali Mehta", "2024-10-16", "39", "Senior Resident, Emergency Department, St. Stephen's Hospital",
                "St. Stephen's Hospital, Tis Hazari, Delhi - 110054", "K. L. Mehta", "9811456789", dr_mehta),
        witness("witness_statement_11.pdf", "WS/RJN/0452/11", "Ramesh Kumar", "2024-10-17", "41", "Head Constable, Photography Section and Technical Cell",
                "PS Rajinder Nagar, New Delhi", "Ram Kishan", "9810067890", ramesh_kumar),
        witness("witness_statement_12.pdf", "WS/RJN/0452/12", "Mohan Singh", "2024-10-17", "33", "Constable (mechanic), PS Rajinder Nagar",
                "PS Rajinder Nagar, New Delhi", "Bhagwan Singh", "9810023456", mohan_singh),
        witness("witness_statement_13.pdf", "WS/RJN/0452/13", "Kavita Arora", "2024-10-19", "36", "Nodal Officer, Zomato Limited (Delhi region)",
                "Zomato Limited, Pillar 3, Aravali Corporate Park, Gurugram", "Suresh Arora", "9899012345", zomato),
        witness("witness_statement_14.pdf", "WS/RJN/0452/14", "Naresh Kumar", "2024-10-20", "48", "Sub-Inspector, Zonal Officer, Karol Bagh Traffic Circle",
                "Traffic Circle Office, Karol Bagh, New Delhi", "Late Jagdish Kumar", "9810034567", traffic_circle),
        witness("witness_statement_16.pdf", "WS/RJN/0452/16", "Dr. R. Srinivasan", "2024-10-16", "52", "Chief Medical Officer, Casualty, Dr. Ram Manohar Lohia Hospital",
                "Dr. Ram Manohar Lohia Hospital, Baba Kharak Singh Marg, New Delhi", "R. Krishnan", "9811098765", (
                    "I, Dr. R. Srinivasan, Chief Medical Officer in the casualty of Dr. Ram Manohar Lohia Hospital, state that on 15 October 2024 at "
                    "about 7:45 pm Amit Verma, aged 28 years, was produced before me by the police of PS Rajinder Nagar for medical examination after "
                    "his arrest. I examined him and prepared MLC number MLC/RML/2024/7892.\n\n"
                    "He was conscious, oriented and cooperative. He had a fresh abrasion of about 2 cm by 2 cm over the left knee and no other external "
                    "injury. His pulse, blood pressure and breathing were normal. There was no smell of alcohol in his breath, his speech was clear and "
                    "his gait was steady, and clinically he was not under the influence of alcohol or any drug.\n\n"
                    "At the request of the police I collected 2 ml of his blood in an EDTA vial, which was sealed with the hospital seal and handed over "
                    "to ASI Ramphal Singh for chemical examination. The abrasion is simple in nature and consistent with a fall from a two-wheeler. I "
                    "can identify the MLC, which bears my signature."
                )),
        witness("witness_statement_15.pdf", "WS/RJN/0452/15", "Rajesh Kumar Sharma", "2024-11-22", "42", "Accountant, DTC Inderlok Depot",
                "B-143, R.P. Bagh, Pusa Road, New Delhi - 110005", "Late Om Prakash Sharma", "9810345678", victim_final),
        DemoDocument(
            "medical_report_mlc.pdf", "MedicalReport", "MLC/SSH/2024/5642", "MEDICO-LEGAL EXAMINATION REPORT (MLC)",
            {"report_number": "MLC/SSH/2024/5642", "report_date": "2024-10-15", "patient_name": "Rajesh Kumar Sharma", "doctor_name": "Dr. Anjali Mehta",
             "hospital_name": "St. Stephen's Hospital, Tis Hazari, Delhi", "age": "42", "gender": "Male",
             "observations": [
                 "Brought by PCR Van Z-45 with alleged history of road traffic accident at Shankar Road T-Point; helmet worn",
                 "Conscious but disoriented on arrival, GCS 13/15, BP 100/70 mmHg, pulse 112/min, SpO2 94 percent on room air",
                 "Lacerated wound 6 cm x 2 cm x 1 cm over the right parietal scalp with active bleeding",
                 "Multiple abrasions over the right cheek and forehead covering 12 cm x 8 cm with embedded road debris",
                 "Closed comminuted fracture of the mid-shaft of the right femur with 2.5 cm shortening on X-ray",
                 "Displaced fracture of the middle third of the right clavicle on X-ray",
                 "Fractures of the right 3rd, 4th and 5th ribs anteriorly, no pneumothorax or haemothorax",
                 "CT head: acute subdural haematoma 8 mm thick over the right fronto-parietal region with 4 mm midline shift",
                 "FAST ultrasound: Grade II laceration of the right lobe of the liver without free fluid",
                 "Deep abrasion 15 cm x 6 cm over the right forearm and elbow; superficial abrasion 5 cm x 4 cm over the left knee",
                 "Blood alcohol nil; toxicology screen negative for common drugs",
                 "Admitted to the surgical ICU under orthopaedics, neurosurgery and general surgery; condition serious but stable",
             ],
             "opinion_text": (
                 "The injuries are grievous in nature and were dangerous to life at the time of admission because of the head injury. They are "
                 "consistent with a high-velocity side impact from a motorcycle followed by a fall on the road. No alcohol intoxication was detected. "
                 "Hospitalisation of at least three to four weeks is expected and a permanent disability of the right lower limb is possible."
             )},
            [("Time of admission", "6:45 pm"), ("MLC prepared at", "8:30 pm")],
        ),
        DemoDocument(
            "medical_report_discharge.pdf", "MedicalReport", "SSH/DIS/2024/11234", "DISCHARGE SUMMARY AND MEDICAL OPINION",
            {"report_number": "SSH/DIS/2024/11234", "report_date": "2024-11-20", "patient_name": "Rajesh Kumar Sharma", "doctor_name": "Dr. Anjali Mehta",
             "hospital_name": "St. Stephen's Hospital, Tis Hazari, Delhi", "age": "42", "gender": "Male",
             "observations": [
                 "Craniotomy and evacuation of the right subdural haematoma performed by neurosurgery; post-operative CT satisfactory",
                 "Intramedullary nailing of the right femur fracture performed; fracture in alignment on check X-ray",
                 "Right clavicle fracture managed conservatively in a sling; rib fractures managed with analgesia and breathing exercises",
                 "Liver laceration managed conservatively with serial ultrasound; healing without surgery",
                 "Shifted from ICU to general ward on 24 October 2024; total hospital stay of 36 days",
                 "At discharge the patient is conscious, oriented and stable, walking with a walker with partial weight bearing",
                 "Advised physiotherapy for three months and review in orthopaedic and neurosurgery OPDs",
                 "Residual shortening of the right lower limb of about 1.5 cm; final disability assessment after six months",
             ],
             "opinion_text": (
                 "The patient sustained grievous injuries including a fracture of the femur and a head injury that endangered his life. He is alive, "
                 "discharged in stable condition and recovering, but will remain unable to follow his ordinary pursuits for more than twenty days."
             )},
        ),
        DemoDocument(
            "spot_panchnama.pdf", "SpotPanchnama", "PN/RJN/0452/2024", "SPOT INSPECTION MEMO (PANCHNAMA)",
            {"memo_number": "PN/RJN/0452/2024", "inspection_datetime": "2024-10-15T21:00:00+05:30", "location": PLACE,
             "observations": [
                 "Shankar Road is a 12.5 metre wide divided bitumen road; the road from Rajinder Nagar is 10 metres wide and meets it at a T-junction",
                 "The overhead three-colour traffic signal at the junction was non-functional; a 40 km/h speed limit board is displayed on Shankar Road",
                 "A white stop line is painted on Shankar Road 5 metres before the junction and a faded zebra crossing is present",
                 f"The red Bajaj Pulsar {PULSAR} was lying on its right side in the middle of the junction, 8.2 metres beyond the stop line",
                 f"The white Honda Activa {ACTIVA} was lying on its right side near the edge of the Rajinder Nagar road, 1.5 metres from the footpath",
                 "The point of impact was fixed at the centre of the junction, 6.5 metres from the Shankar Road stop line, from the debris and gouge marks",
                 "A continuous rear-tyre skid mark 4.2 metres long led from the Shankar Road side to the point of impact",
                 "Gouge and scrape marks 1.8 metres long ran from the point of impact to the resting place of the Activa",
                 "A blood stain about 15 cm x 20 cm was found near the resting place of the Activa",
                 "Red fairing pieces, white body-panel pieces, headlamp glass and the right mirror of the Activa were scattered within 3 metres of the impact point",
                 "An engine oil patch of about 30 cm x 50 cm was present at the point of impact",
                 "Four of the six street lights within 100 metres were working; the nearest working light was 15 metres from the impact point",
                 "The weather was clear and the road surface was dry; visibility was good",
                 "CCTV cameras were noticed at St. Stephen's Hospital Gate No. 2 and at the Canara Bank ATM on Shankar Road",
                 "Twenty-five photographs of the scene were taken by HC Ramesh Kumar of the photography section",
             ],
             "witnesses": ["Mohammed Asif", "Prakash Chandra Joshi"]},
            [("Inspection completed", "10:15 pm"), ("Prepared by", IO_NAME)],
        ),
        DemoDocument(
            "site_plan.pdf", "SitePlan", "SP/RJN/0452/2024", "SITE PLAN OF THE PLACE OF OCCURRENCE (SCALED)",
            {"plan_number": "SP/RJN/0452/2024", "plan_date": "2024-10-16", "location": PLACE, "prepared_by": IO_NAME,
             "annotations": [
                 "Drawn to scale 1:200 with north at the top; based on the spot inspection measurements and a revisit to the spot",
                 "Point A: point of impact at the centre of the junction, 6.5 metres from the Shankar Road stop line",
                 "Point B: resting position of the Pulsar, 2.5 metres from the end of the divider, front wheel facing east",
                 "Point C: resting position of the Activa near the edge of the Rajinder Nagar road, front wheel facing south",
                 "Point D: start of the 4.2 metre skid mark of the Pulsar, 2.8 metres before the point of impact",
                 "Point E: position of Traffic Constable Mohammed Asif regulating traffic in the middle of the junction",
                 "Point F: tea stall of witness Prakash Chandra Joshi, 35 metres south-east of the junction",
                 "Point G: CCTV camera CAM-SSH-G2-03 above St. Stephen's Hospital Gate No. 2, 30 metres north of the junction",
                 "Point H: CCTV camera CAM-CB-ATM-01 at the Canara Bank ATM, 50 metres south on Shankar Road",
                 "Dashed line: path of the Pulsar from the Karol Bagh side along Shankar Road into the junction",
                 "Dashed line: path of the Activa from the Rajinder Nagar side turning right towards Old Rajinder Nagar",
                 "Non-functional traffic signal on an overhead gantry at the centre of the junction",
                 "Electric pole SP/23/RJN with a working LED street light 15 metres from the point of impact",
             ]},
        ),
        DemoDocument(
            "arrest_memo.pdf", "ArrestMemo", "ARR/RJN/0452/2024", "ARREST MEMO",
            {"memo_number": "ARR/RJN/0452/2024", "arrest_datetime": "2024-10-15T19:15:00+05:30", "arrested_person_name": "Amit Verma",
             "father_name": "Ramesh Verma", "age": "28", "address": "C-54, Gali No. 4, Old Rajinder Nagar, New Delhi - 110060",
             "occupation": "Food delivery rider (Zomato delivery partner ID ZOM/DL/478923)", "arrest_location": PLACE, "arresting_officer_name": IO_NAME,
             "grounds_of_arrest": "Rash and negligent riding causing grievous hurt and endangering life; identified at the spot by an eyewitness; vehicle involved recovered from him",
             "rights_explained": "Grounds of arrest, right to bail, right to consult a lawyer and right to have a relative informed were explained in Hindi",
             "personal_search": "Samsung Galaxy M32 mobile phone, wallet with Rs 850, driving licence, Aadhaar photocopy, SBI ATM card, motorcycle keys, red Zomato delivery bag",
             "medical_examination": "Examined at Dr. Ram Manohar Lohia Hospital vide MLC/RML/2024/7892: minor abrasion of the left knee, no smell of alcohol",
             "relative_informed": "Father Ramesh Verma informed by telephone by ASI Ramphal Singh",
             "arrest_witnesses": "Mohammed Asif; Prakash Chandra Joshi"},
        ),
        DemoDocument(
            "seizure_memo_vehicles.pdf", "SeizureMemo", "SZ/RJN/0452/01", "SEIZURE MEMO - VEHICLES AND DOCUMENTS",
            {"memo_number": "SZ/RJN/0452/01", "seizure_datetime": "2024-10-15T21:30:00+05:30", "seizure_location": PLACE, "prepared_by": IO_NAME,
             "seized_items": [
                 {"description": f"Red Bajaj Pulsar 220F motorcycle {PULSAR}, chassis MD2A18FX5LCK12345, engine DHYCJ51678, front fairing broken and right handlebar bent", "exhibit_mark": "EX-1"},
                 {"description": f"White Honda Activa 6G scooter {ACTIVA}, chassis ME4JF614AMT67890, engine JF61E3456789, right body panel dented and right mirror broken", "exhibit_mark": "EX-2"},
                 {"description": "Driving licence of the accused Amit Verma, DL/032021/0789456, issued by RTO Moradabad, class MCWG", "exhibit_mark": "EX-3"},
                 {"description": "Driving licence of the victim Rajesh Kumar Sharma, DL/042018/0456789, issued by RTO Sheikh Sarai, class MCWG and LMV", "exhibit_mark": "EX-4"},
                 {"description": "Registration certificates and insurance papers of both vehicles", "exhibit_mark": "EX-5"},
             ],
             "witnesses": "Mohammed Asif; Prakash Chandra Joshi",
             "sealing": "Documents sealed with the seal SC; vehicles taken to the police station yard under seal"},
        ),
        DemoDocument(
            "seizure_memo_articles.pdf", "SeizureMemo", "SZ/RJN/0452/02", "SEIZURE MEMO - ARTICLES FROM THE SCENE AND THE ACCUSED",
            {"memo_number": "SZ/RJN/0452/02", "seizure_datetime": "2024-10-15T22:00:00+05:30", "seizure_location": PLACE, "prepared_by": IO_NAME,
             "seized_items": [
                 {"description": "Black Steelbird full-face helmet of the accused, visor missing, chin strap torn", "exhibit_mark": "EX-6"},
                 {"description": "White Vega full-face helmet of the victim, cracked on the right side with blood stains inside", "exhibit_mark": "EX-7"},
                 {"description": "Broken vehicle parts from the scene: red fairing pieces, white body-panel pieces, headlamp glass and a right mirror", "exhibit_mark": "EX-8"},
                 {"description": "Red Zomato delivery bag of the accused, torn at one corner", "exhibit_mark": "EX-9"},
                 {"description": "Black Samsung Galaxy M32 mobile phone of the accused, IMEI 358123456789012, with handlebar mount", "exhibit_mark": "EX-10"},
                 {"description": "Blood sample of the accused (BLD-0452-A) collected at Dr. Ram Manohar Lohia Hospital", "exhibit_mark": "EX-11"},
                 {"description": "Blood sample of the victim (BLD-0452-B) collected at St. Stephen's Hospital", "exhibit_mark": "EX-12"},
                 {"description": "SD card with 25 digital photographs of the scene taken by HC Ramesh Kumar", "exhibit_mark": "EX-13"},
             ],
             "witnesses": "Mohammed Asif; Prakash Chandra Joshi",
             "sealing": "Each article packed separately, sealed with the seal SC and labelled; blood samples kept refrigerated"},
        ),
        DemoDocument(
            "seizure_memo_cctv.pdf", "SeizureMemo", "SZ/RJN/0452/03", "SEIZURE MEMO - ELECTRONIC RECORDS",
            {"memo_number": "SZ/RJN/0452/03", "seizure_datetime": "2024-10-16T13:00:00+05:30",
             "seizure_location": "Security control room, St. Stephen's Hospital, and Canara Bank, Shankar Road", "prepared_by": IO_NAME,
             "seized_items": [
                 {"description": "1 TB DVR hard disk from St. Stephen's Hospital containing camera CAM-SSH-G2-03 recording of the junction", "exhibit_mark": "EX-14"},
                 {"description": "32 GB pen drive with a copy of the Canara Bank ATM camera CAM-CB-ATM-01 recording", "exhibit_mark": "EX-15"},
                 {"description": "64 GB SD card from the dash camera of PCR Van Z-45", "exhibit_mark": "EX-16"},
             ],
             "witnesses": "Thomas George; S. Venkatesh",
             "certificates": "Certificates under Section 63 of the Bharatiya Sakshya Adhiniyam obtained from the hospital and the bank"},
        ),
        DemoDocument(
            "seizure_memo_records.pdf", "SeizureMemo", "SZ/RJN/0452/04", "SEIZURE MEMO - DOCUMENTARY AND DIGITAL RECORDS",
            {"memo_number": "SZ/RJN/0452/04", "seizure_datetime": "2024-10-20T16:00:00+05:30",
             "seizure_location": "Police Station Rajinder Nagar, New Delhi", "prepared_by": IO_NAME,
             "seized_items": [
                 {"description": "Forensic image and extraction report of the Samsung Galaxy M32 of the accused, with hash values, prepared by the IT cell", "exhibit_mark": "EX-17"},
                 {"description": "Printouts of the Zomato partner app order history, location pings and delivery partner profile for ID ZOM/DL/478923, with Section 63 BSA certificate", "exhibit_mark": "EX-18"},
                 {"description": "Attested copy of the Karol Bagh Traffic Circle complaint register entry about the non-functional signal", "exhibit_mark": "EX-19"},
                 {"description": "Attested copy of the duty roster showing Constable Mohammed Asif deployed at the junction from 4 pm to 8 pm", "exhibit_mark": "EX-20"},
                 {"description": "E-challan portal record of the accused showing one earlier over-speeding challan from Moradabad", "exhibit_mark": "EX-21"},
                 {"description": "Hospital bills, pharmacy receipts and salary slips of the victim produced by the complainant", "exhibit_mark": "EX-22"},
             ],
             "witnesses": "ASI Ramphal Singh; HC Ramesh Kumar",
             "sealing": "Records placed in a sealed envelope bearing the seal SC; digital extraction kept on write-protected media"},
        ),
        DemoDocument(
            "vehicle_inspection_pulsar.pdf", "VehicleInspection", "VIR/RJN/0452/01", "MECHANICAL INSPECTION REPORT - MOTORCYCLE",
            {"report_number": "VIR/RJN/0452/01", "inspection_date": "2024-10-16", "vehicle_registration": PULSAR,
             "inspected_by": "ASI Rajender Prasad, Motor Transport Section",
             "observations": [
                 "Red Bajaj Pulsar 220F, 2020 model, odometer 48,234 km, registered owner Amit Verma; insurance, fitness and pollution certificates valid",
                 "Front fairing broken and partly detached; headlight assembly smashed with hot-shock deformation of the filament showing the lamp was on",
                 "Right front fork bent backward by about 5 degrees; front rim bent with a burst front tyre",
                 "Right handlebar bent downward by about 25 degrees; right mirror broken; white paint transfer on the right side",
                 "Speedometer needle jammed at the 55 km/h mark and the instrument console cracked",
                 "Front brake lever found in the applied position, consistent with last-moment emergency braking",
                 "Front disc and rear drum brakes functional; pad and shoe thickness within limits; brake fluid adequate",
                 "Pre-accident tread depth adequate on both tyres; no irregular wear",
                 "Steering, clutch, gearbox and rear suspension were functional before the accident",
                 "Opinion: the vehicle was roadworthy before the accident and all damage is fresh and accident-related",
             ]},
        ),
        DemoDocument(
            "vehicle_inspection_activa.pdf", "VehicleInspection", "VIR/RJN/0452/02", "MECHANICAL INSPECTION REPORT - SCOOTER",
            {"report_number": "VIR/RJN/0452/02", "inspection_date": "2024-10-16", "vehicle_registration": ACTIVA,
             "inspected_by": "ASI Rajender Prasad, Motor Transport Section",
             "observations": [
                 "White Honda Activa 6G, 2022 model, odometer 12,456 km, registered owner Rajesh Kumar Sharma; insurance and pollution certificates valid",
                 "Right body panel scraped over 35 cm x 20 cm and dented inward by 2.5 cm, with red paint transfer",
                 "Right side trim broken; right mirror bracket broken; right front indicator lens broken",
                 "Right brake lever bent downward by about 15 degrees but still functional",
                 "Engine, transmission, combined braking system, suspension and lights functional; headlight is of the always-on type",
                 "Both tyres in good condition with adequate tread and no impact damage",
                 "Damage is confined to the right side at the height of a motorcycle front wheel and fairing, showing a lateral impact",
                 "Opinion: the scooter was in excellent condition before the accident and no mechanical defect contributed to it",
             ]},
        ),
        DemoDocument(
            "fsl_report.pdf", "FSLReport", "FSL/DL/2024/PHY/8934", "FORENSIC SCIENCE LABORATORY REPORT (PHYSICS AND BIOLOGY)",
            {"report_number": "FSL/DL/2024/PHY/8934", "report_date": "2024-11-18", "laboratory_name": "Forensic Science Laboratory, Rohini, Delhi",
             "examined_items": [
                 f"EX-1 Bajaj Pulsar {PULSAR}", f"EX-2 Honda Activa {ACTIVA}", "EX-6 helmet of the accused", "EX-7 helmet of the victim",
                 "EX-8 broken vehicle parts", "EX-11 blood sample of the accused", "EX-12 blood sample of the victim", "EX-14 DVR hard disk",
             ],
             "findings": [
                 "White paint on the right front fork of the Pulsar matches the paint of the Activa; red paint on the Activa panel matches the Pulsar",
                 "The broken parts recovered from the scene physically fit the damaged areas of the two vehicles",
                 "Primary impact was between the front-right of the Pulsar and the right-centre of the Activa at an angle of about 75 degrees",
                 "Speed of the Pulsar at impact calculated at 52 to 58 km/h from the 4.2 metre skid, a friction coefficient of 0.7 and the crush damage",
                 "Speed of the Activa at impact estimated at 8 to 12 km/h, a normal turning speed",
                 "At the legal limit of 40 km/h the Pulsar could have stopped within 15.5 metres and the collision was avoidable",
                 "Brake systems of both vehicles were functional before the accident",
                 "Victim's helmet shows impact marks and two cracks on the right side; its chin strap was fastened; it prevented a skull fracture",
                 "Blood inside the victim's helmet is human, group B positive, matching the victim",
                 "The chin strap of the accused's helmet was torn before the accident and the helmet was not secured",
                 "No alcohol or drugs of abuse were detected in the blood of either the accused or the victim",
                 "Frame analysis of the hospital camera footage confirms the Pulsar entered the junction against the constable's stop signal",
             ],
             "opinion_text": (
                 "The accident was caused primarily by the over-speeding of the rider of the Bajaj Pulsar at 52 to 58 km/h in a 40 km/h zone and "
                 "his failure to obey the manual stop signal of the traffic constable. The rider of the Activa was riding at a normal speed, was "
                 "making a lawful turn and was wearing a properly secured helmet; no contributory negligence is found on his part."
             )},
            [("Examining officer", "Dr. Priya Nambiar, Senior Scientific Officer (Physics)"), ("Received", "17 October 2024")],
        ),
        DemoDocument(
            "fsl_report_biology.pdf", "FSLReport", "FSL/DL/2024/BIO/2211", "FORENSIC SCIENCE LABORATORY REPORT (BIOLOGY AND TOXICOLOGY)",
            {"report_number": "FSL/DL/2024/BIO/2211", "report_date": "2024-11-12", "laboratory_name": "Forensic Science Laboratory, Rohini, Delhi",
             "examined_items": [
                 "EX-7 helmet of the victim (blood stains and hair from the inner liner)", "EX-11 blood sample of the accused (BLD-0452-A)",
                 "EX-12 blood sample of the victim (BLD-0452-B)", "EX-8 broken vehicle parts (swabs from the Activa body panel)",
             ],
             "findings": [
                 "Blood stains on the inner liner of the victim's helmet are of human origin and of group B positive",
                 "Hair with roots recovered from the inner liner gave a DNA profile that matches the blood sample of the victim",
                 "Blood sample of the victim is group B positive; ethyl alcohol not detected; screening for opiates, cannabinoids, benzodiazepines and amphetamines negative",
                 "Blood sample of the accused is group O positive; ethyl alcohol not detected; screening for opiates, cannabinoids, benzodiazepines and amphetamines negative",
                 "No blood was detected on the swabs from the Activa body panel; the material on the panel is red paint transferred from the motorcycle",
                 "The seals on all parcels were intact and tallied with the specimen seal SC forwarded with the requisition",
             ],
             "opinion_text": (
                 "Neither rider had consumed alcohol or drugs of abuse. The blood and hair in the victim's helmet belong to the victim, confirming "
                 "that the helmet was worn by him and took the impact to the right side of his head."
             )},
            [("Examining officer", "Dr. Rekha Iyer, Assistant Director (Biology)"), ("Received", "17 October 2024")],
        ),
        DemoDocument(
            "cctv_gate_no2.pdf", "CCTVMetadata", "CAM-SSH-G2-03", "CCTV FOOTAGE ANALYSIS - ST. STEPHEN'S HOSPITAL GATE NO. 2",
            {"camera_identifier": "CAM-SSH-G2-03", "recording_datetime": "2024-10-15T18:20:00+05:30",
             "location": "St. Stephen's Hospital Gate No. 2, facing the Shankar Road T-Point, Rajinder Nagar, New Delhi", "duration_seconds": 2700,
             "metadata_text": (
                 "Hikvision 4 MP IP camera at 25 frames per second, 30 metres from the junction with a full view of the T-Point; clock within two seconds "
                 "of standard time. Relevant frames: at 18:20:03 the white Activa enters from the Rajinder Nagar side at about 10 km/h with its right "
                 "indicator blinking; at 18:20:05 the red Pulsar enters from the Karol Bagh side at about 55 to 60 km/h with its rider in a red T-shirt "
                 "and a delivery bag on the rear seat; at 18:20:06 the traffic constable raises his left hand to stop Shankar Road traffic; at 18:20:07 "
                 "the Pulsar crosses the stop line without slowing; at 18:20:07.8 the front of the Pulsar strikes the right side of the Activa; at "
                 "18:20:08 the Activa rider is thrown about four metres; at 18:20:12 the Pulsar rider gets up and tries to lift the motorcycle; at "
                 "18:20:14 the constable catches him by the arm; at 18:31 PCR Van Z-45 arrives; at 18:35 the hospital ambulance arrives; at 18:42 the "
                 "injured rider is taken to the emergency. Analysed by HC Ramesh Kumar, Technical Cell; no sign of editing or tampering."
             )},
        ),
        DemoDocument(
            "cctv_atm.pdf", "CCTVMetadata", "CAM-CB-ATM-01", "CCTV FOOTAGE ANALYSIS - CANARA BANK ATM, SHANKAR ROAD",
            {"camera_identifier": "CAM-CB-ATM-01", "recording_datetime": "2024-10-15T18:19:35+05:30",
             "location": "Canara Bank ATM, Shankar Road, 50 metres south of St. Stephen's Hospital Gate No. 2, Rajinder Nagar, New Delhi", "duration_seconds": 600,
             "metadata_text": (
                 "CP Plus 2 MP dome camera at 15 frames per second covering the ATM entrance and 30 metres of Shankar Road on the Karol Bagh side. At "
                 "18:19:35 a red Pulsar passes the ATM towards the junction with its rider in a red T-shirt, a black helmet and a delivery bag. Using road "
                 "markings measured during the spot inspection, the motorcycle covers 30 metres in 1.8 seconds, an average speed of about 60 km/h. No brake "
                 "light is seen at any point in this stretch. At 18:20:15 the kiosk microphone records a crash sound and the ATM guard turns towards the "
                 "junction. Copy provided on pen drive by the branch manager with a Section 63 BSA certificate."
             )},
        ),
        DemoDocument(
            "cctv_pcr_dashcam.pdf", "CCTVMetadata", "PCR-DASH-Z45", "CCTV FOOTAGE ANALYSIS - PCR VAN Z-45 DASH CAMERA",
            {"camera_identifier": "PCR-DASH-Z45", "recording_datetime": "2024-10-15T18:24:05+05:30",
             "location": "PCR Van Z-45 at the Shankar Road T-Point, near St. Stephen's Hospital Gate No. 2, Rajinder Nagar, New Delhi", "duration_seconds": 1500,
             "metadata_text": (
                 "1080p vehicle dash camera at 30 frames per second. At 18:24:05 the van receives the dispatch about a two-wheeler crash with injury "
                 "at the Shankar Road T-Point. At 18:31:05 the van reaches the junction; the red motorcycle and the white scooter are seen lying on their "
                 "right sides in the positions later recorded in the spot inspection memo, a crowd has gathered, and the traffic constable is seen holding "
                 "a young man in a red T-shirt. The footage fixes the position of the vehicles before they were moved."
             )},
        ),
        DemoDocument(
            "case_diary.pdf", "CaseDiary", "CD/RJN/0452/2024", "CASE DIARY (Section 192 BNSS)",
            {"diary_number": "CD/RJN/0452/2024", "officer_name": IO_NAME,
             "entries": [
                 {"entry_number": "1", "entry_datetime": "2024-10-15T18:45:00+05:30", "text": "Received DD No. 24-A about a road crash at the Shankar Road T-Point and reached the spot with staff. PCR staff were present and the injured had been removed to St. Stephen's Hospital. The rider of the Pulsar, Amit Verma, was produced by Traffic Constable Mohammed Asif. FIR No. 0452/2024 was registered on the written complaint of Sunita Sharma, wife of the injured, and investigation was taken up."},
                 {"entry_number": "2", "entry_datetime": "2024-10-15T19:15:00+05:30", "text": "Accused Amit Verma was arrested at the spot after being informed of the grounds of arrest and his rights. His personal search was conducted and an arrest memo was prepared in the presence of Constable Mohammed Asif and Prakash Chandra Joshi. His father was informed by telephone."},
                 {"entry_number": "3", "entry_datetime": "2024-10-15T19:45:00+05:30", "text": "The accused was medically examined at Dr. Ram Manohar Lohia Hospital, where a minor abrasion of the left knee was recorded and no smell of alcohol was found. His blood sample was collected and sealed. The MLC of the injured was obtained from St. Stephen's Hospital, recording grievous injuries."},
                 {"entry_number": "4", "entry_datetime": "2024-10-15T20:15:00+05:30", "text": "Statements of Traffic Constable Mohammed Asif and of Prakash Chandra Joshi were recorded under Section 180 BNSS. Statement of HC Ramesh of PCR Van Z-45 was recorded about the arrival of the PCR and the removal of the injured."},
                 {"entry_number": "5", "entry_datetime": "2024-10-15T21:00:00+05:30", "text": "The spot was inspected in the presence of the panch witnesses. Road widths, the resting positions of both vehicles, the 4.2 metre skid mark, the blood stain and the debris field were measured and recorded. HC Ramesh Kumar photographed the scene in 25 frames. The non-functional traffic signal and the 40 km/h speed limit board were noted."},
                 {"entry_number": "6", "entry_datetime": "2024-10-15T21:30:00+05:30", "text": "Both vehicles, the driving licences and the vehicle papers were seized under memo SZ/RJN/0452/01. Helmets, broken parts, the delivery bag, the mobile phone of the accused, the blood samples and the photograph SD card were seized under memo SZ/RJN/0452/02 and sealed with the seal SC."},
                 {"entry_number": "7", "entry_datetime": "2024-10-15T22:30:00+05:30", "text": "The accused was questioned in the lock-up in the presence of a legal aid counsel and ASI Ramphal Singh after being informed of his rights. He stated that he was hurrying to deliver a food order and admitted that he was riding fast. The disclosure is kept on the case file and is not relied upon as a confession."},
                 {"entry_number": "8", "entry_datetime": "2024-10-16T10:00:00+05:30", "text": "ASI Rajender Prasad inspected both vehicles in the police station yard. Both were found roadworthy before the crash; the Pulsar speedometer was found jammed at 55 km/h and its front brake lever in the applied position. Inspection reports were received and the statement of ASI Rajender Prasad was recorded."},
                 {"entry_number": "9", "entry_datetime": "2024-10-16T13:00:00+05:30", "text": "The DVR hard disk of camera CAM-SSH-G2-03 was seized from St. Stephen's Hospital and a pen drive copy of camera CAM-CB-ATM-01 was obtained from Canara Bank, with Section 63 BSA certificates. The dash camera SD card of PCR Van Z-45 was obtained. Statements of Thomas George, S. Venkatesh and ASI Ramphal Singh were recorded."},
                 {"entry_number": "10", "entry_datetime": "2024-10-16T17:00:00+05:30", "text": "Visited St. Stephen's Hospital and met Dr. Anjali Mehta. The injured had undergone a craniotomy for the subdural haematoma and fixation of the femur and was in the ICU in serious but stable condition. The doctor confirmed that the injuries are grievous and were dangerous to life. The site plan was prepared to scale after a revisit to the spot."},
                 {"entry_number": "11", "entry_datetime": "2024-10-17T12:00:00+05:30", "text": "The CCTV analysis report of HC Ramesh Kumar was received; it fixes the speed of the Pulsar at about 60 km/h on the approach and 52 to 58 km/h at impact and shows that the rider ignored the constable's stop signal. The exhibits were sent to FSL Rohini under road certificate 234/2024."},
                 {"entry_number": "12", "entry_datetime": "2024-10-18T11:00:00+05:30", "text": "The accused was produced before the Metropolitan Magistrate, Tis Hazari Courts. Two days of police custody were granted for the examination of his phone and delivery records. An order for preservation of other CCTV recordings on the route was obtained."},
                 {"entry_number": "13", "entry_datetime": "2024-10-19T15:00:00+05:30", "text": "With the help of the IT cell, data of the accused's phone was examined. The Zomato partner app showed an order picked up from Haldiram's, Karol Bagh, with a promised delivery time in Old Rajinder Nagar, and the GPS history showed speeds of 55 to 65 km/h on Shankar Road. Zomato confirmed the delivery partner ID and the delayed delivery in reply to a notice."},
                 {"entry_number": "14", "entry_datetime": "2024-10-20T12:00:00+05:30", "text": "On expiry of police custody the accused was produced in court and remanded to judicial custody. The Traffic Circle record of the written complaint about the faulty signal and the duty roster of Constable Mohammed Asif were obtained."},
                 {"entry_number": "15", "entry_datetime": "2024-10-25T11:00:00+05:30", "text": "The injured Rajesh Kumar Sharma, now shifted to the general ward and fit to make a statement as certified by the doctor, was examined and his statement recorded. He confirmed that he was riding slowly with his helmet on and turning lawfully when the motorcycle struck him."},
                 {"entry_number": "16", "entry_datetime": "2024-11-05T14:00:00+05:30", "text": "Antecedents of the accused were verified at his Delhi address and through UP Police at his native village in Moradabad. No previous criminal record was found. One earlier over-speeding challan from Moradabad was found on the e-challan portal."},
                 {"entry_number": "17", "entry_datetime": "2024-11-12T16:00:00+05:30", "text": "The biology and toxicology report FSL/DL/2024/BIO/2211 was received. It confirms that the blood and hair in the victim's helmet belong to the victim and that neither the accused nor the victim had consumed alcohol or drugs. The report was placed on the case file."},
                 {"entry_number": "18", "entry_datetime": "2024-11-14T11:00:00+05:30", "text": "The statement of Dr. R. Srinivasan of Dr. Ram Manohar Lohia Hospital, who examined the accused after his arrest, was placed on file along with MLC/RML/2024/7892. The statement of Constable Mohan Singh about the safe deposit of the sealed exhibits at FSL Rohini and the receipt obtained was also placed on file."},
                 {"entry_number": "19", "entry_datetime": "2024-11-16T12:00:00+05:30", "text": "A notice was served on the registered owner record of the Pulsar with the transport department; the motorcycle is registered in the name of the accused and its insurance policy with ICICI Lombard was valid. The insurer was informed so that the claim of the victim before the Claims Tribunal can proceed."},
                 {"entry_number": "20", "entry_datetime": "2024-11-18T13:00:00+05:30", "text": "FSL report FSL/DL/2024/PHY/8934 was received. It confirms the paint transfer, the speed of the Pulsar at 52 to 58 km/h, that the crash was avoidable at the legal speed, the effectiveness of the victim's helmet and the absence of alcohol in both riders. The exhibits were returned to the malkhana."},
                 {"entry_number": "21", "entry_datetime": "2024-11-22T12:00:00+05:30", "text": "The discharge summary of the injured was obtained; he was discharged after 36 days in hospital with a residual shortening of the right leg. Medical bills of about Rs 4.2 lakh and salary slips were collected for the victim compensation application."},
                 {"entry_number": "22", "entry_datetime": "2024-11-28T17:00:00+05:30", "text": "Investigation completed. The evidence establishes that the accused rode at 52 to 60 km/h in a 40 km/h zone, ignored the manual stop signal of the traffic constable and struck the victim's scooter, which was making a lawful turn, causing grievous injuries dangerous to life, and that he tried to leave the spot without helping the injured. The charge sheet is prepared under Sections 281 and 125(b) BNS and Sections 184 and 134 of the Motor Vehicles Act and submitted to ACP Patel Nagar for approval."},
             ]},
        ),
    ]


def finish(storage_root, review_service_cls, correction_request_cls, add_note_request_cls, decision_request_cls) -> None:
    review = review_service_cls(storage_root)
    review.apply_corrections(
        CASE_ID,
        correction_request_cls(
            reviewer_id=IO_ID,
            reviewer_name=IO_NAME,
            comments="Final opinion and signature block recorded by the investigating officer before supervisory review.",
            corrections={
                "final_opinion": (
                    "On the evidence collected, a prima facie case is made out against the accused Amit Verma under Sections 281 and 125(b) BNS "
                    "and Sections 184 and 134 of the Motor Vehicles Act. The eyewitness accounts of Constable Mohammed Asif and Prakash Chandra Joshi, "
                    "the hospital and ATM camera recordings, the mechanical inspection reports and the FSL report consistently establish that he "
                    "rode at 52 to 60 km/h in a 40 km/h zone against the constable's stop signal and struck the victim's scooter during a lawful "
                    "turn, causing grievous injuries dangerous to life. He is in judicial custody and is sent for trial."
                ),
                "signature": f"{IO_NAME}, SHO and Investigating Officer, Rajinder Nagar Police Station",
            },
        ),
    )
    review.add_note(
        CASE_ID,
        add_note_request_cls(
            author_id=IO_ID,
            author_name=IO_NAME,
            note_text="Investigation complete. Draft charge sheet submitted to ACP Patel Nagar Sub-Division for supervisory approval before filing.",
        ),
    )


CASE = DemoCase(CASE_ID, TITLE, STATION, documents, finish)
