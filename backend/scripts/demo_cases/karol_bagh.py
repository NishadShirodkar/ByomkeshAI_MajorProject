"""Case A: armed robbery with grievous hurt at Ajmal Khan Road, Karol Bagh (FIR 0287/2025).

Fully investigated against the arrested accused Rakesh Yadav; co-accused Sunil Chauhan absconding. The seeding
finalizes, signs and QR-seals the charge sheet.
"""

from __future__ import annotations

from .common import DemoCase, DemoDocument

CASE_ID = "DEMO_COMPLETED_KarolBagh_Robbery"
TITLE = "Armed robbery with grievous hurt, Karol Bagh"
STATION = "Karol Bagh Police Station, Central District, New Delhi"
IO_ID, IO_NAME = "IO-SI-DEEPAK-RAWAT", "SI Deepak Rawat"
PLACE = "Ajmal Khan Road, near Metro Pillar 112, Karol Bagh, New Delhi"
COURT = "Metropolitan Magistrate, Tis Hazari Courts, Delhi"
BIKE = "DL3SCX4821"

NARRATIVE = (
    "On 14 August 2025 at about 10:30 pm, the complainant Neha Arora was walking home along Ajmal Khan Road, Karol Bagh, "
    f"when two men on a motorcycle {BIKE} stopped near Metro Pillar 112. The accused Rakesh Yadav threatened her with a knife "
    "and demanded her gold chain and mobile phone. When she resisted, the accused deliberately attacked her and slashed her on the "
    "left forearm with the knife, causing grievous hurt. The accused then robbed her of a gold chain and an iPhone 14 and fled towards "
    "Rani Jhansi Road with the second accused Sunil Chauhan, who kept the engine of the motorcycle running throughout. Passers-by, "
    "including the tea stall owner Mohan Lal, raised an alarm and the complainant was taken to Dr. Ram Manohar Lohia Hospital, where "
    "a deep stab wound of the left forearm with a fracture of the left ulna was found. The robbery and the escape of the two men were "
    "recorded by a CCTV camera of a shop opposite the spot. The motorcycle used in the offence is registered in the name of Deepak "
    "Chauhan of Anand Parbat, a cousin of Sunil Chauhan, who had taken it from him in the first week of August. The accused Rakesh "
    "Yadav was arrested at Anand Parbat on the information of secret sources and, pursuant to his disclosure, the knife, the robbed "
    "gold chain, the iPhone 14 and the motorcycle were recovered from his room and from outside his house. He was identified by the "
    "complainant and by the eyewitness Mohan Lal in a test identification parade, his fingerprints were found on the handle of the "
    "knife and the blood on the knife was found to be the complainant's. The second accused Sunil Chauhan has absconded."
)


def documents() -> list[DemoDocument]:
    complaint_text = (
        "To the SHO, Karol Bagh Police Station. I, Neha Arora, aged 29 years, resident of 21 Idgah Road, Karol Bagh, work as a "
        "customer service executive at a bank call centre in Jhandewalan. My shift ends at 10 pm and I usually walk home along Ajmal "
        "Khan Road.\n\n"
        "On the night of 14 August 2025 at about 10:30 pm I was walking home along Ajmal Khan Road near Metro Pillar 112 when two men "
        f"on a black motorcycle {BIKE} stopped in front of me. The man on the pillion seat got down, held a knife to my face and "
        "demanded my gold chain and phone. I was in great fear. When I tried to step back and shouted for help, he slashed my left arm "
        "with the knife. Blood started flowing and I could not hold my phone.\n\n"
        "He pulled the gold chain from my neck, which broke, and snatched my iPhone 14 from my hand. The rider, who never switched off "
        "the motorcycle, shouted at him to hurry, and they rode away towards Rani Jhansi Road. I saw the face of the man with the knife "
        "clearly under the street light; he was about 25 to 28 years old, thin, with short hair and wore a grey T-shirt. The rider wore a "
        "black jacket and a cap.\n\n"
        "The tea stall owner nearby and other people came to help me and took me to Dr. Ram Manohar Lohia Hospital. My gold chain weighed "
        "about 18 grams and the iPhone 14 was bought in March 2025. I request that strict legal action be taken against the two men and "
        "that my property be recovered."
    )
    mohan_lal = (
        "I run a tea stall near Metro Pillar 112 on Ajmal Khan Road for the last eleven years and I keep it open until about 11 pm. On 14 "
        f"August 2025 at about 10:30 pm I saw two men on a black motorcycle number {BIKE} stop in front of a young woman who was walking "
        "past my stall. The man sitting behind got down and pointed a knife at her. I saw the knife clearly; it had a black handle and a "
        "long blade.\n\n"
        "She shouted for help and he slashed her arm. The two men took her gold chain and phone without her consent and fled towards Rani "
        "Jhansi Road. The rider kept the engine running the whole time. I ran towards them with my customers, but they had already gone. "
        "I noted the number of the motorcycle on my hand with a pen and gave it to the police when they arrived.\n\n"
        "The woman was bleeding heavily from her left forearm. I tied a cloth on her arm and, with the help of a passer-by, put her in an "
        "auto-rickshaw to Dr. Ram Manohar Lohia Hospital. I called the police on 112 from my phone. The man with the knife was thin, about "
        "25 years old and wore a grey T-shirt. On 18 August 2025 I correctly identified him as Rakesh Yadav in the test identification "
        "parade held at Tihar Jail. I acted as a witness to the spot inspection and I can identify him again."
    )
    pooja = (
        "I live on the first floor above the shops on Ajmal Khan Road, opposite Metro Pillar 112. On 14 August 2025 at about 10:30 pm I "
        "was on my balcony when I heard a woman screaming from the street and looked down. Under the street light I saw a man with a knife "
        "standing in front of a young woman and the woman bleeding from her left arm.\n\n"
        f"A second man was sitting on a black motorcycle {BIKE} and kept the engine running. The man with the knife pulled something from "
        "the woman's neck and took a phone from her hand, then jumped on the motorcycle behind the rider. The attackers rode away towards "
        "Rani Jhansi Road at high speed.\n\n"
        "I came down with my husband. The tea stall owner Mohan Lal was helping the woman. I gave her my dupatta to press on the wound. I "
        "saw a broken piece of a gold chain lying on the footpath and asked people not to touch it until the police came. I showed it to "
        "the police officers when they inspected the spot and I signed the inspection memo as a witness. I could not see the face of the "
        "rider clearly because he wore a cap."
    )
    neha_supp = (
        "I, Neha Arora, state further that I was operated upon at Dr. Ram Manohar Lohia Hospital on 15 August 2025. The doctors repaired "
        "the tendons of my left forearm and fixed the broken bone with a plate. I remained in hospital until 21 August 2025 and my arm "
        "was in a cast for six weeks. I am right-handed but I still cannot lift weight or type properly with my left hand and I have been "
        "on medical leave from work.\n\n"
        "On 18 August 2025 I attended the test identification parade at Tihar Jail conducted by the Metropolitan Magistrate. Among the "
        "persons lined up I identified Rakesh Yadav as the man who threatened me with the knife, cut my arm and took my chain and phone.\n\n"
        "On 23 August 2025 the police showed me a gold chain and an iPhone 14 at the police station in the presence of the investigating "
        "officer. I identified the chain as mine from its design and the hook that I had got repaired, and the phone as mine from its "
        "IMEI number, which matches the purchase invoice and the box that I produced. I also identified the knife with the black handle "
        "as the one used to cut me. The clothes I was wearing that night, a blood-stained blue kurta, were handed over to the police at "
        "the hospital. I request that the chain and phone be returned to me on superdari."
    )
    vikas = (
        "I, Vikas Arora, am the brother of Neha Arora. On 14 August 2025 at about 10:50 pm I received a phone call from a stranger who "
        "said that my sister had been attacked on Ajmal Khan Road and was being taken to Dr. Ram Manohar Lohia Hospital. I reached the "
        "emergency and found her with a deep cut on her left forearm, bleeding through a bandage.\n\n"
        "She told me in the emergency itself that two men on a motorcycle had threatened her with a knife, cut her arm and taken her gold "
        "chain and her phone. She described the man with the knife as thin, about 25 years old, in a grey T-shirt. The police reached the "
        "hospital soon after, and her statement was recorded the next morning when the doctors declared her fit.\n\n"
        "I produced the purchase invoice and the box of the iPhone 14 bearing its IMEI number, and the bill of the gold chain from Soni "
        "Jewellers, Karol Bagh, before the investigating officer. I also arranged for my sister's treatment and kept the hospital bills."
    )
    pcr = (
        "I, HC Satbir Singh, am the in-charge of PCR Van K-17, Central District. On 14 August 2025 at about 10:34 pm my van received a call "
        "about a robbery with a knife near Metro Pillar 112, Ajmal Khan Road. We reached the spot at about 10:41 pm. The injured woman had "
        "already been sent to the hospital by the public.\n\n"
        f"The tea stall owner Mohan Lal told us that two men on a black motorcycle {BIKE} had cut the woman with a knife and taken her chain "
        "and phone and had fled towards Rani Jhansi Road. I flashed the description and the number of the motorcycle on the wireless to all "
        "PCR vans and pickets. I guarded the spot, kept the public away from the blood stains and the broken chain link, and handed over "
        "the spot to SI Deepak Rawat when he arrived."
    )
    dr_kapoor = (
        "I, Dr. Anil Kapoor, Senior Resident, Department of Orthopaedics, Dr. Ram Manohar Lohia Hospital, state that on 14 August 2025 at "
        "about 11:05 pm Neha Arora, aged 29 years, was brought to the emergency with an alleged history of assault with a knife. I examined "
        "her and prepared MLC number MLC/RML/2025/08841.\n\n"
        "She had a deep incised stab wound 6 cm long on the back of the left forearm, cutting the extensor tendons, and an X-ray showed a "
        "fracture of the shaft of the left ulna. She was conscious and stable. She underwent tendon repair and plating of the ulna on 15 "
        "August 2025 and was discharged on 21 August 2025.\n\n"
        "In my opinion the injury was caused by a sharp-edged weapon such as a knife and is grievous because of the fracture. The knife with "
        "a black handle and a 22 cm blade shown to me by the police could cause such an injury. Her blood-stained blue kurta was sealed and "
        "handed to the police. I can identify the MLC and the discharge summary, which bear my signature."
    )
    ritesh = (
        "I, Ritesh Gupta, own Gupta Mobile Store on Ajmal Khan Road, directly opposite Metro Pillar 112. A CCTV camera fixed above my "
        "shutter covers the footpath and the road in front of the pillar. Its recorder is kept inside my shop and runs all the time.\n\n"
        "When the police asked me for the recording I played it back in the presence of SI Deepak Rawat. It shows a black motorcycle "
        "stopping near the pillar, a man getting down with a knife, the attack on the woman and the two men riding away towards Rani "
        "Jhansi Road. The time on my recorder is correct; I check it every month.\n\n"
        "I gave the police a copy of the recording on a pen drive and the hard disk of the recorder, which were sealed in my presence. I "
        "signed the seizure memo and gave a certificate under Section 63 of the Bharatiya Sakshya Adhiniyam."
    )
    sandeep = (
        "I, HC Sandeep Kumar, am posted at Karol Bagh Police Station. After the incident I was assigned to trace the motorcycle and the "
        f"accused. A search of the vehicle registration records showed that motorcycle {BIKE} was registered in the name of Deepak Chauhan "
        "of Anand Parbat.\n\n"
        "On 16 August 2025 at about 8:30 am I received secret information that a man matching the description given by the eyewitnesses was "
        "living in Anand Parbat and was using the motorcycle. I informed SI Deepak Rawat, and we reached House No. 14, Anand Parbat, with staff. The "
        "man there was identified by Mohan Lal, who had accompanied us, and gave his name as Rakesh Yadav. He was arrested by SI Deepak Rawat "
        "at about 9:30 am after being told the grounds of arrest.\n\n"
        "During questioning he disclosed that he had hidden the knife, the chain and the phone in his room and that the motorcycle was "
        "parked outside. He led us to his room and took out the knife from under a mattress and the chain and phone from a bag. These were "
        "seized by SI Deepak Rawat in my presence and in the presence of a local resident, Satish Kumar."
    )
    satish = (
        "I, Satish Kumar, live in Anand Parbat and run a grocery shop near House No. 14. On 16 August 2025 in the morning the police came "
        "to House No. 14 with a young man in custody whom they called Rakesh Yadav. They asked me to come along as a public witness and I "
        "agreed.\n\n"
        "Rakesh Yadav took us to a room on the ground floor where he lived. In my presence he lifted the mattress of the bed and took out a "
        "knife with a black plastic handle and a long blade. From a black bag on the shelf he took out a gold chain and an iPhone. A black "
        f"Hero Splendor motorcycle {BIKE} was parked outside the house and he said he had been using it.\n\n"
        "The police measured the knife, wrapped all the articles in cloth, sealed them and prepared a memo, which was read over to me and "
        "which I signed. I can identify the articles and Rakesh Yadav."
    )
    deepak_chauhan = (
        f"I, Deepak Chauhan, live in Anand Parbat and I am the registered owner of the black Hero Splendor motorcycle {BIKE}. Sunil Chauhan "
        "is my cousin. In the first week of August 2025 he took my motorcycle saying he needed it for a few days to look for work.\n\n"
        "He did not return it. I later came to know that he and his friend Rakesh Yadav, who also lives in Anand Parbat, were using it. I "
        "have not seen Sunil Chauhan since the police came to our area, and his phone is switched off. I do not know where he is. I have "
        "produced the registration certificate and insurance papers of the motorcycle before the police."
    )
    kailash = (
        "I, Kailash Soni, run Soni Jewellers in Karol Bagh. The bill produced by the police, number SJ/2024/1187, was issued by my shop "
        "to Neha Arora in November 2024 for a 22 carat gold chain of about 18 grams with a lobster hook and a design of small leaves.\n\n"
        "The gold chain shown to me at the police station is the same chain that we sold; it carries our hallmark stamp and our shop's "
        "identification mark. One link near the hook is broken and missing. Its present weight is 17.6 grams and its value is about Rs "
        "1,65,000. I also repaired the hook of this chain for Neha Arora in June 2025 and the repair is visible."
    )
    malkhana = (
        "I, HC Jagdish Prasad, am the MHC(M) of Karol Bagh Police Station in charge of the malkhana. I received the sealed parcels of this "
        "case from SI Deepak Rawat as entered in register number 19 at serial numbers 4471 to 4479, including the knife, the chain, the "
        "phone, the motorcycle, the blood-stained kurta, the blood swab and the chain link from the spot, and the CCTV hard disk.\n\n"
        "On 18 August 2025 I handed over the parcels of the knife, the kurta and the swab, with the seals intact, to Constable Arvind for "
        "deposit at FSL Rohini under road certificate number 112/2025, and he returned the receipt the same day. While the parcels were in "
        "my custody nobody tampered with them. The chain and phone were later released to the complainant on superdari by court order."
    )

    raju = (
        "I, Raju Paswan, drive an auto-rickshaw and usually wait for passengers near Metro Pillar 110 on Ajmal Khan Road. On 14 August 2025 "
        "at about 10:30 pm I heard a woman screaming and saw people running towards Metro Pillar 112. When I went there with my auto-rickshaw "
        "I saw a young woman sitting near the tea stall with her left arm wrapped in cloth soaked with blood.\n\n"
        "The tea stall owner Mohan Lal asked me to take her to the hospital at once. A lady from the building opposite and Mohan Lal helped "
        "her into my auto-rickshaw, and I drove her to the emergency of Dr. Ram Manohar Lohia Hospital, reaching at about 11 pm. On the way "
        "she was crying and kept saying that two men on a motorcycle had cut her with a knife and taken her chain and phone.\n\n"
        "At the hospital I helped her to the emergency counter and waited until her brother arrived. I did not take any fare. I gave my name "
        "and number to the police at the hospital. I did not see the men on the motorcycle myself."
    )
    rahul = (
        "I, Constable Rahul, am posted in the crime team of Central District. On 15 August 2025 I reached the spot near Metro Pillar 112, "
        "Ajmal Khan Road, with the crime team on the call of SI Deepak Rawat and inspected the place of occurrence.\n\n"
        "I photographed the spot from different angles, including the blood stains on the footpath, the trail of blood drops towards the tea "
        "stall, the broken chain link, the tyre marks near the kerb and the street light on the metro pillar. I took 18 photographs with the "
        "district camera and later handed over the printed photographs and the memory card to the investigating officer with a certificate.\n\n"
        "In the morning I also accompanied the investigating officer to Dr. Ram Manohar Lohia Hospital, where the sealed parcel containing "
        "the blood-stained kurta of the injured was handed over by the hospital, and I signed the seizure memo as a witness."
    )
    arvind = (
        "I, Constable Arvind, am posted at Karol Bagh Police Station. On 18 August 2025 the MHC(M) handed over to me three sealed parcels of "
        "this case, namely the knife, the blood-stained kurta and the blood gauze from the spot, together with the sealed FTA card of the "
        "complainant, the forwarding letter and road certificate number 112/2025. The seals bore the impression DR and were intact.\n\n"
        "I took the parcels directly to the Forensic Science Laboratory, Rohini, by the official vehicle and deposited them there on the same "
        "day. I obtained the receipt and handed it to the MHC(M) on my return. On 19 August 2025 I also carried the specimen fingerprint slip "
        "of the accused, sealed by the court, to the fingerprint division of the laboratory. While the parcels were with me nobody tampered "
        "with them."
    )
    sunita = (
        "I, W/Constable Sunita, am posted at Karol Bagh Police Station. On 15 August 2025 I accompanied SI Deepak Rawat to Dr. Ram Manohar "
        "Lohia Hospital. After the doctor declared the injured Neha Arora fit to make a statement, I sat with her and wrote down her complaint "
        "in her own words as she narrated it, in the presence of her brother Vikas Arora.\n\n"
        "The complaint was read over to her and she signed it with her right hand because her left arm was bandaged. The complaint was handed "
        "over to SI Deepak Rawat, who sent it to the police station for registration of the FIR. During the conversation she clearly described "
        "the man with the knife as thin, about 25 years old, in a grey T-shirt, and said that she would be able to identify him."
    )
    dmrc = (
        "I, Manoj Tiwari, am the Station Controller of the Karol Bagh metro station of the Delhi Metro Rail Corporation. The DMRC has cameras "
        "on the viaduct that cover the road below, including camera DMRC-KB-P112 on Metro Pillar 112, Ajmal Khan Road. Its recordings are "
        "stored at the station control room for thirty days.\n\n"
        "On a written request from the investigating officer dated 15 August 2025 I retrieved the recording of camera DMRC-KB-P112 for the "
        "night of 14 August 2025 between 10:15 pm and 10:45 pm and copied it onto a pen drive. The copy was handed over to the police and I "
        "issued a certificate under Section 63 of the Bharatiya Sakshya Adhiniyam stating that the camera was working properly and that the "
        "copy is a true copy of the original. The original recording has been preserved at the station on the request of the police."
    )
    fingerprint = (
        "I, Dr. Mamta Joshi, Assistant Director, Fingerprint Division, Forensic Science Laboratory, Rohini, state that I received the knife "
        "(EX-1) of this case in a sealed parcel bearing the seal DR and, later, the specimen fingerprint slip of the accused Rakesh Yadav, "
        "sealed by the court.\n\n"
        "I developed the latent prints on the black plastic handle of the knife with powder and cyanoacrylate fuming. Two chance prints, "
        "marked Q1 and Q2, were found suitable for comparison. On comparison with the specimen slip, Q1 was found identical with the right "
        "thumb impression and Q2 with the right index finger impression of Rakesh Yadav, with 14 and 12 ridge characteristics in their "
        "relative positions respectively and no unexplained difference.\n\n"
        "My report number FSL/DEL/2025/FP/0941 dated 2 September 2025 bears my signature. In my opinion the knife was held in the right hand "
        "of Rakesh Yadav."
    )
    nodal = (
        "I, Anand Bhushan, am the Nodal Officer of Bharti Airtel Limited for the Delhi circle. On a notice under Section 94 BNSS from Karol "
        "Bagh Police Station I supplied the customer application forms and call detail records of mobile numbers 98XXXX4471, issued to "
        "Rakesh Yadav, and 87XXXX2290, issued to Sunil Chauhan, for the period 10 August to 20 August 2025.\n\n"
        "The records show that on the night of 14 August 2025 both numbers were connected to the same tower serving Ajmal Khan Road and "
        "Pusa Road, Karol Bagh, between 10:10 pm and 10:35 pm, and then to the tower serving Anand Parbat from 10:50 pm. Between 8 pm and "
        "midnight the two numbers called each other six times. The number of Sunil Chauhan has not connected to the network since the "
        "morning of 16 August 2025.\n\n"
        "These records are maintained by the company's systems in the ordinary course of business. I have issued a certificate under "
        "Section 63 of the Bharatiya Sakshya Adhiniyam with the records."
    )
    employer = (
        "I, Ankita Bose, am the Human Resources Manager of the call centre at Jhandewalan where Neha Arora works as a customer service "
        "executive. As per our attendance records she worked her normal shift on 14 August 2025 and logged out at 10:07 pm. Her usual route "
        "home is on foot along Ajmal Khan Road.\n\n"
        "She informed us the next day that she had been injured and admitted to Dr. Ram Manohar Lohia Hospital. She has been on medical "
        "leave since then, supported by medical certificates from the hospital, and has not yet been able to resume work at the computer "
        "because of the injury to her left forearm. I have given attested copies of the attendance and leave records to the police."
    )

    dr_pankaj = (
        "I, Dr. Pankaj Malhotra, Casualty Medical Officer, Dr. Ram Manohar Lohia Hospital, state that on 16 August 2025 at about 1:15 pm "
        "Rakesh Yadav, aged 27 years, was produced before me by the police of Karol Bagh Police Station for medical examination after his "
        "arrest. I examined him and prepared MLC number MLC/RML/2025/09012.\n\n"
        "He was conscious, oriented and cooperative and did not complain of any injury or ill-treatment. There was no fresh external "
        "injury on his body. There was an old healed scar on the back of his right hand. His pulse, blood pressure and breathing were "
        "normal. He was not under the influence of alcohol.\n\n"
        "At the request of the police and with the permission of the court, his specimen fingerprints were later taken in my presence "
        "on the standard slip, which was sealed and handed over to the investigating officer. I can identify the MLC and the slip, which "
        "bear my signature."
    )
    traffic_cam = (
        "I, HC Vinod Kumar, am posted at the Integrated Traffic Management control room of the Delhi Traffic Police. Camera TRF-RJR-07 is "
        "installed at the Rani Jhansi Road crossing near Ajmal Khan Road and records continuously to the central server, where recordings "
        "are retained for thirty days. The clock of the system is synchronised with standard time automatically.\n\n"
        "On a written request of SI Deepak Rawat I retrieved the recording of camera TRF-RJR-07 for the night of 14 August 2025 between "
        "10:20 pm and 10:45 pm and copied it onto a pen drive. In the recording a black motorcycle with two riders is seen crossing the "
        "junction at high speed towards Anand Parbat; the pillion rider wears a grey T-shirt. I handed over the pen drive and issued a "
        "certificate under Section 63 of the Bharatiya Sakshya Adhiniyam that the system was working properly and that the copy is true."
    )
    manish = (
        "I, Constable Manish, am posted at Karol Bagh Police Station. Since 16 August 2025 I have been assigned, along with HC Sandeep Kumar, "
        "to trace the co-accused Sunil Chauhan, son of Mahavir Chauhan, resident of Gali No. 3, Anand Parbat.\n\n"
        "We have repeatedly visited his house, which has remained locked, and the houses of his relatives in Anand Parbat and Sultanpuri, "
        "his known associates and the places where he used to work. His mobile phone has remained switched off. On 5 September 2025 the "
        "court issued non-bailable warrants against him, which I tried to execute at all known addresses, but he could not be found. The "
        "warrants were returned unexecuted with my report.\n\n"
        "After the court ordered proceedings for his proclamation, I published the proclamation by beat of drum at his house and in the "
        "locality and affixed copies at his house and on the notice board of the court. Efforts to arrest him are continuing."
    )

    def witness(filename: str, ref: str, name: str, date: str, age: str, occupation: str, address: str, text: str, father: str = "", contact: str = "") -> DemoDocument:
        return DemoDocument(
            filename, "WitnessStatement", ref, "STATEMENT OF WITNESS UNDER SECTION 180 BNSS",
            {"statement_reference": ref, "statement_date": date, "witness_name": name, "father_name": father or None, "age": age,
             "occupation": occupation, "witness_address": address, "contact": contact or None, "recorded_by": IO_NAME, "statement_text": text},
        )

    return [
        DemoDocument(
            "fir.pdf", "FIR", "0287/2025", "FIRST INFORMATION REPORT (Section 173 BNSS)",
            {"fir_number": "0287/2025", "crime_number": "0287/2025", "registration_date": "2025-08-15", "police_station": "Karol Bagh",
             "complainant_name": "Neha Arora", "accused_names": ["Rakesh Yadav", "Sunil Chauhan"], "victim_names": ["Neha Arora"],
             "vehicle_registrations": [BIKE], "occurrence_datetime": "2025-08-14T22:30:00+05:30", "occurrence_location": PLACE,
             "jurisdiction": "Central Delhi", "court": COURT, "reported_sections": ["Section 309(4) BNS", "Section 118(2) BNS"],
             "narrative_text": NARRATIVE},
            [("District", "Central Delhi"), ("General Diary reference", "DD No. 61-A"), ("Investigating officer", IO_NAME)],
        ),
        DemoDocument(
            "complaint.pdf", "Complaint", "C/KB/0287/2025", "WRITTEN COMPLAINT",
            {"complaint_reference": "C/KB/0287/2025", "complaint_date": "2025-08-15", "complainant_name": "Neha Arora",
             "complainant_address": "21 Idgah Road, Karol Bagh, New Delhi", "person_complained_against_names": [],
             "victim_names": ["Neha Arora"], "vehicle_registrations": [BIKE], "complaint_text": complaint_text},
            [("To", "The SHO, Karol Bagh Police Station")],
        ),
        witness("witness_statement_01.pdf", "WS/KB/0287/01", "Mohan Lal", "2025-08-15", "46", "Tea stall owner", "Tea stall near Metro Pillar 112, Ajmal Khan Road, Karol Bagh", mohan_lal, "Late Hari Ram", "9811402236"),
        witness("witness_statement_02.pdf", "WS/KB/0287/02", "Pooja Sharma", "2025-08-15", "38", "Homemaker", "First floor, 7/4 Ajmal Khan Road, Karol Bagh", pooja, "W/o Rajiv Sharma", "9871203345"),
        witness("witness_statement_03.pdf", "WS/KB/0287/03", "Satbir Singh", "2025-08-15", "45", "Head Constable, In-charge PCR Van K-17", "PCR Unit, Central District, Delhi Police", pcr, "Dharam Singh", "9810112233"),
        witness("witness_statement_04.pdf", "WS/KB/0287/04", "Vikas Arora", "2025-08-15", "33", "Sales manager", "21 Idgah Road, Karol Bagh, New Delhi", vikas, "Suresh Arora", "9899456123"),
        witness("witness_statement_05.pdf", "WS/KB/0287/05", "Raju Paswan", "2025-08-15", "34", "Auto-rickshaw driver", "Jhuggi No. 112, Bapa Nagar, Karol Bagh", raju, "Ramesh Paswan", "9958774410"),
        witness("witness_statement_06.pdf", "WS/KB/0287/06", "Sunita", "2025-08-15", "29", "Woman Constable, Karol Bagh Police Station", "Karol Bagh Police Station, New Delhi", sunita, "Om Prakash", "9810554433"),
        witness("witness_statement_07.pdf", "WS/KB/0287/07", "Rahul", "2025-08-15", "31", "Constable, Crime Team, Central District", "Crime Team Office, Central District, Delhi Police", rahul, "Jai Bhagwan", "9810661122"),
        witness("witness_statement_08.pdf", "WS/KB/0287/08", "Ritesh Gupta", "2025-08-15", "41", "Shop owner, Gupta Mobile Store", "Gupta Mobile Store, Ajmal Khan Road, Karol Bagh", ritesh, "Mahesh Gupta", "9811900876"),
        witness("witness_statement_09.pdf", "WS/KB/0287/09", "Sandeep Kumar", "2025-08-16", "39", "Head Constable, Karol Bagh Police Station", "Karol Bagh Police Station, New Delhi", sandeep, "Ram Niwas", "9810223344"),
        witness("witness_statement_10.pdf", "WS/KB/0287/10", "Satish Kumar", "2025-08-16", "52", "Grocery shop owner", "Near House No. 14, Anand Parbat, New Delhi", satish, "Late Bhola Ram", "9213345566"),
        witness("witness_statement_11.pdf", "WS/KB/0287/11", "Deepak Chauhan", "2025-08-17", "31", "Driver", "Gali No. 3, Anand Parbat, New Delhi", deepak_chauhan, "Mahavir Chauhan", "9654412378"),
        witness("witness_statement_12.pdf", "WS/KB/0287/12", "Manoj Tiwari", "2025-08-18", "44", "Station Controller, Karol Bagh Metro Station, DMRC", "Karol Bagh Metro Station, New Delhi", dmrc, "Shyam Tiwari", "9810887766"),
        witness("witness_statement_13.pdf", "WS/KB/0287/13", "Arvind", "2025-08-19", "28", "Constable, Karol Bagh Police Station", "Karol Bagh Police Station, New Delhi", arvind, "Rajbir Singh", "9810998877"),
        witness("witness_statement_14.pdf", "WS/KB/0287/14", "Dr. Anil Kapoor", "2025-08-22", "36", "Senior Resident, Orthopaedics, Dr. Ram Manohar Lohia Hospital", "Dr. Ram Manohar Lohia Hospital, New Delhi", dr_kapoor, "R. K. Kapoor", "9811665544"),
        witness("witness_statement_15.pdf", "WS/KB/0287/15", "Neha Arora", "2025-08-23", "29", "Customer service executive", "21 Idgah Road, Karol Bagh, New Delhi", neha_supp, "Suresh Arora", "9899456120"),
        witness("witness_statement_16.pdf", "WS/KB/0287/16", "Kailash Soni", "2025-08-23", "58", "Jeweller, Soni Jewellers", "Soni Jewellers, Bank Street, Karol Bagh", kailash, "Late Ganga Ram Soni", "9811233211"),
        witness("witness_statement_17.pdf", "WS/KB/0287/17", "Ankita Bose", "2025-08-25", "35", "HR Manager, call centre, Jhandewalan", "Call centre office, Jhandewalan Extension, New Delhi", employer, "Pranab Bose", "9830012345"),
        witness("witness_statement_18.pdf", "WS/KB/0287/18", "Anand Bhushan", "2025-08-26", "47", "Nodal Officer, Bharti Airtel Limited (Delhi circle)", "Bharti Airtel Limited, Okhla Phase III, New Delhi", nodal, "Vishnu Bhushan", "9810776655"),
        witness("witness_statement_19.pdf", "WS/KB/0287/19", "Jagdish Prasad", "2025-08-29", "50", "Head Constable, MHC(M), Karol Bagh Police Station", "Karol Bagh Police Station, New Delhi", malkhana, "Late Mool Chand", "9810443322"),
        witness("witness_statement_21.pdf", "WS/KB/0287/21", "Dr. Pankaj Malhotra", "2025-08-16", "40", "Casualty Medical Officer, Dr. Ram Manohar Lohia Hospital", "Dr. Ram Manohar Lohia Hospital, New Delhi", dr_pankaj, "S. P. Malhotra", "9811773344"),
        witness("witness_statement_22.pdf", "WS/KB/0287/22", "Vinod Kumar", "2025-08-19", "42", "Head Constable, Traffic Management Control Room", "Delhi Traffic Police Headquarters, Todapur, New Delhi", traffic_cam, "Ram Kumar", "9810445566"),
        witness("witness_statement_23.pdf", "WS/KB/0287/23", "Manish", "2025-09-08", "30", "Constable, Karol Bagh Police Station", "Karol Bagh Police Station, New Delhi", manish, "Satpal", "9810332211"),
        witness("witness_statement_20.pdf", "WS/KB/0287/20", "Dr. Mamta Joshi", "2025-09-03", "45", "Assistant Director, Fingerprint Division, FSL Rohini", "Forensic Science Laboratory, Rohini, Delhi", fingerprint, "D. C. Joshi", "9811556677"),
        DemoDocument(
            "medical_report.pdf", "MedicalReport", "MLC/RML/2025/08841", "MEDICO-LEGAL EXAMINATION REPORT (MLC)",
            {"report_number": "MLC/RML/2025/08841", "report_date": "2025-08-14", "patient_name": "Neha Arora", "doctor_name": "Dr. Anil Kapoor",
             "hospital_name": "Dr. Ram Manohar Lohia Hospital, New Delhi", "age": "29", "gender": "Female",
             "observations": [
                 "Deep stab wound 6 cm long on the left forearm with injury to the extensor tendons",
                 "Fracture of the shaft of the left ulna",
                 "Patient conscious and stable, admitted for surgery",
                 "Wound margins clean-cut with tailing towards the wrist, suggesting a sharp-edged weapon drawn across the forearm",
                 "Abrasion 3 cm long on the back of the neck consistent with forcible pulling of a chain",
                 "Pulse 104 per minute, blood pressure 110/70 mmHg; blood loss estimated at about 400 ml",
                 "Blood-stained blue kurta of the patient sealed and handed over to the police",
             ],
             "opinion_text": "The injury is grievous hurt caused by a sharp-edged weapon such as a knife. The patient is alive and under treatment."},
            [("Time of arrival", "11:05 pm"), ("Brought by", "Members of the public; PCR informed")],
        ),
        DemoDocument(
            "medical_report_discharge.pdf", "MedicalReport", "RML/DS/2025/14420", "DISCHARGE SUMMARY AND FINAL MEDICAL OPINION",
            {"report_number": "RML/DS/2025/14420", "report_date": "2025-08-21", "patient_name": "Neha Arora", "doctor_name": "Dr. Anil Kapoor",
             "hospital_name": "Dr. Ram Manohar Lohia Hospital, New Delhi", "age": "29", "gender": "Female",
             "observations": [
                 "Repair of the extensor tendons of the left forearm and open reduction with plate fixation of the left ulna performed",
                 "Post-operative X-ray shows the fracture in good alignment",
                 "Wound healing well; sutures to be removed after two weeks",
                 "Above-elbow cast for six weeks followed by physiotherapy",
                 "Discharged in stable condition; she is unable to use the left hand for ordinary pursuits for more than twenty days",
             ],
             "opinion_text": "The injuries are grievous in nature (fracture with tendon injury) caused by a sharp-edged weapon. The patient is alive and recovering."},
        ),
        DemoDocument(
            "spot_panchnama.pdf", "SpotPanchnama", "SP/KB/0087/2025", "SPOT INSPECTION MEMO (PANCHNAMA)",
            {"memo_number": "SP/KB/0087/2025", "inspection_datetime": "2025-08-15T00:40:00+05:30", "location": PLACE,
             "observations": [
                 "Blood stains were found on the footpath about three metres from Metro Pillar 112",
                 "One broken gold-coloured chain link was recovered from the footpath",
                 "A CCTV camera on the opposite shop covers the spot",
                 "The footpath is 2.5 metres wide and paved; the road is a two-lane road under the metro viaduct",
                 "A working street light on the metro pillar lights the spot; the place is clearly visible from the tea stall and the balconies opposite",
                 "Drops of blood lead about 6 metres from the spot towards the tea stall where the injured was given first aid",
                 "Tyre marks of a two-wheeler turning sharply were seen in the dust near the kerb, leading towards Rani Jhansi Road",
                 "Blood was lifted from the footpath on sterile gauze and the chain link was sealed in a separate envelope",
                 "Photographs of the spot were taken by Constable Rahul of the crime team",
             ],
             "witnesses": ["Mohan Lal", "Pooja Sharma"]},
            [("Prepared by", IO_NAME)],
        ),
        DemoDocument(
            "site_plan.pdf", "SitePlan", "SPL/KB/0287/2025", "SITE PLAN OF THE PLACE OF OCCURRENCE",
            {"plan_number": "SPL/KB/0287/2025", "plan_date": "2025-08-15", "location": PLACE, "prepared_by": IO_NAME,
             "annotations": [
                 "Point A: place where the motorcycle stopped, beside Metro Pillar 112",
                 "Point B: place where the complainant was attacked with the knife and blood stains were found",
                 "Point C: broken chain link found on the footpath, 1 metre from Point B",
                 "Point D: tea stall of witness Mohan Lal, 9 metres from Point B",
                 "Point E: balcony of witness Pooja Sharma, first floor opposite Point B",
                 "Point F: CCTV camera of Gupta Mobile Store, 14 metres across the road facing Point B",
                 "Arrow: direction of escape of the motorcycle towards Rani Jhansi Road",
                 "Street light on Metro Pillar 112 lighting Points A to C",
             ]},
        ),
        DemoDocument(
            "arrest_memo.pdf", "ArrestMemo", "AM/KB/0059/2025", "ARREST MEMO",
            {"memo_number": "AM/KB/0059/2025", "arrest_datetime": "2025-08-16T09:30:00+05:30", "arrested_person_name": "Rakesh Yadav",
             "father_name": "Ramesh Yadav", "age": "27", "address": "H.No. 14, Anand Parbat, New Delhi", "occupation": "Delivery rider",
             "arrest_location": "Anand Parbat, New Delhi", "arresting_officer_name": IO_NAME,
             "grounds_of_arrest": "Robbery with a knife causing grievous hurt; identified by an eyewitness; motorcycle used in the offence found with him",
             "rights_explained": "Grounds of arrest, right to bail and right to a lawyer explained; his mother informed",
             "arrest_witnesses": "HC Sandeep Kumar; Satish Kumar"},
            [("Note", "The arrested person was informed of the grounds of arrest and of his right to inform a relative.")],
        ),
        DemoDocument(
            "seizure_memo.pdf", "SeizureMemo", "SM/KB/0112/2025", "SEIZURE MEMO - RECOVERY AT THE INSTANCE OF THE ACCUSED",
            {"memo_number": "SM/KB/0112/2025", "seizure_datetime": "2025-08-16T11:45:00+05:30", "seizure_location": "Anand Parbat, New Delhi", "prepared_by": IO_NAME,
             "seized_items": [
                 {"description": "Knife with a black plastic handle and a 22 cm blade", "exhibit_mark": "EX-1"},
                 {"description": "Gold chain (22 carat, about 18 grams), stolen property recovered from the accused", "exhibit_mark": "EX-2"},
                 {"description": "iPhone 14, stolen property knowingly retained by the accused", "exhibit_mark": "EX-3"},
                 {"description": f"Motorcycle {BIKE} (Hero Splendor)", "exhibit_mark": "EX-4"},
             ],
             "witnesses": "HC Sandeep Kumar; Satish Kumar",
             "sealing": "Articles wrapped in cloth and sealed with the seal DR; sketch of the knife prepared"},
        ),
        DemoDocument(
            "seizure_memo_spot.pdf", "SeizureMemo", "SM/KB/0108/2025", "SEIZURE MEMO - EXHIBITS FROM THE SPOT",
            {"memo_number": "SM/KB/0108/2025", "seizure_datetime": "2025-08-15T01:20:00+05:30", "seizure_location": PLACE, "prepared_by": IO_NAME,
             "seized_items": [
                 {"description": "Blood lifted from the footpath on sterile gauze", "exhibit_mark": "EX-5"},
                 {"description": "Control sample of the footpath surface", "exhibit_mark": "EX-6"},
                 {"description": "Broken gold-coloured chain link found on the footpath", "exhibit_mark": "EX-7"},
             ],
             "witnesses": "Mohan Lal; Pooja Sharma"},
        ),
        DemoDocument(
            "seizure_memo_clothes.pdf", "SeizureMemo", "SM/KB/0109/2025", "SEIZURE MEMO - CLOTHES OF THE INJURED",
            {"memo_number": "SM/KB/0109/2025", "seizure_datetime": "2025-08-15T03:10:00+05:30", "seizure_location": "Dr. Ram Manohar Lohia Hospital, New Delhi", "prepared_by": IO_NAME,
             "seized_items": [
                 {"description": "Blood-stained blue kurta of the complainant, handed over sealed by the hospital", "exhibit_mark": "EX-8"},
                 {"description": "Blood sample of the complainant on FTA card for DNA comparison", "exhibit_mark": "EX-9"},
             ],
             "witnesses": "Vikas Arora; Constable Rahul"},
        ),
        DemoDocument(
            "seizure_memo_cctv.pdf", "SeizureMemo", "SM/KB/0110/2025", "SEIZURE MEMO - ELECTRONIC RECORDS",
            {"memo_number": "SM/KB/0110/2025", "seizure_datetime": "2025-08-15T13:00:00+05:30", "seizure_location": "Gupta Mobile Store, Ajmal Khan Road, Karol Bagh", "prepared_by": IO_NAME,
             "seized_items": [
                 {"description": "500 GB hard disk of the CCTV recorder of Gupta Mobile Store", "exhibit_mark": "EX-10"},
                 {"description": "Pen drive with a copy of the relevant recording", "exhibit_mark": "EX-11"},
                 {"description": "Pen drive with a copy of the DMRC camera recording near Metro Pillar 112 and the traffic camera recording at Rani Jhansi Road", "exhibit_mark": "EX-12"},
             ],
             "witnesses": "Ritesh Gupta; HC Sandeep Kumar",
             "certificates": "Section 63 BSA certificates obtained from the shop owner, DMRC and the traffic police"},
        ),
        DemoDocument(
            "vehicle_inspection.pdf", "VehicleInspection", "MVI/KB/0287/2025", "MECHANICAL INSPECTION REPORT - MOTORCYCLE",
            {"report_number": "MVI/KB/0287/2025", "inspection_date": "2025-08-17", "vehicle_registration": BIKE, "inspected_by": "Motor Vehicle Inspector, Central District",
             "observations": [
                 "Black Hero Splendor motorcycle, registered owner Deepak Chauhan of Anand Parbat",
                 "Engine, brakes, lights and steering in working order; the vehicle can be ridden at speed",
                 "Front number plate bent and partly covered with black tape; rear plate clean",
                 "Pillion foot-rests in the open position; fresh scuff marks on the left foot-rest",
                 "No accident damage; vehicle fit to be released on superdari after trial evidence",
             ]},
        ),
        DemoDocument(
            "fsl_report.pdf", "FSLReport", "FSL/DEL/2025/BIO/3318", "FORENSIC SCIENCE LABORATORY REPORT (BIOLOGY AND DNA)",
            {"report_number": "FSL/DEL/2025/BIO/3318", "report_date": "2025-08-28", "laboratory_name": "Forensic Science Laboratory, Rohini, Delhi",
             "examined_items": ["Knife (EX-1)", "Blood-stained clothing of the complainant", "Blood gauze from the spot (EX-5)", "Blood sample of the complainant on FTA card (EX-9)"],
             "findings": [
                 "Human blood was detected on the knife blade (EX-1)",
                 "The DNA profile from the knife matches the blood of the complainant Neha Arora",
                 "Blood on the kurta (EX-8) and on the gauze from the spot (EX-5) is human and gives the same DNA profile as the complainant",
                 "A cut 7 cm long in the left sleeve of the kurta corresponds with the forearm wound and could be caused by the knife EX-1",
             ],
             "opinion_text": "The blood on EX-1 is of human origin and matches the complainant."},
        ),
        DemoDocument(
            "fsl_report_fingerprint.pdf", "FSLReport", "FSL/DEL/2025/FP/0941", "FORENSIC SCIENCE LABORATORY REPORT (FINGERPRINTS)",
            {"report_number": "FSL/DEL/2025/FP/0941", "report_date": "2025-09-02", "laboratory_name": "Forensic Science Laboratory, Rohini, Delhi",
             "examined_items": ["Knife (EX-1), handle", "Specimen fingerprint slip of the accused Rakesh Yadav"],
             "findings": [
                 "Two chance prints suitable for comparison were developed on the black plastic handle of the knife",
                 "Chance print Q1 is identical with the right thumb impression of Rakesh Yadav, with 14 matching ridge characteristics",
                 "Chance print Q2 is identical with the right index finger impression of Rakesh Yadav",
             ],
             "opinion_text": "The knife EX-1 was handled by the accused Rakesh Yadav."},
        ),
        DemoDocument(
            "cctv_shop.pdf", "CCTVMetadata", "CAM-GMS-01", "CCTV FOOTAGE ANALYSIS - GUPTA MOBILE STORE",
            {"camera_identifier": "CAM-GMS-01", "recording_datetime": "2025-08-14T22:29:40+05:30",
             "location": "Gupta Mobile Store, opposite Metro Pillar 112, Ajmal Khan Road, Karol Bagh, New Delhi", "duration_seconds": 300,
             "metadata_text": (
                 "2 MP bullet camera covering the footpath at Metro Pillar 112. At 22:29:40 a black motorcycle with two riders stops beside the pillar. At "
                 "22:29:52 the pillion rider in a grey T-shirt gets down holding a knife and confronts a woman walking on the footpath. At 22:30:05 he swings "
                 "the knife at her left arm. At 22:30:11 he pulls the chain from her neck and takes a phone from her hand. At 22:30:16 he mounts the motorcycle "
                 "and it leaves towards Rani Jhansi Road. The face of the pillion rider is visible in four frames and compares with the arrested accused."
             )},
        ),
        DemoDocument(
            "cctv_metro.pdf", "CCTVMetadata", "DMRC-KB-P112", "CCTV FOOTAGE ANALYSIS - DMRC CAMERA, METRO PILLAR 112",
            {"camera_identifier": "DMRC-KB-P112", "recording_datetime": "2025-08-14T22:29:30+05:30",
             "location": "DMRC viaduct camera at Metro Pillar 112, Ajmal Khan Road, Karol Bagh, New Delhi", "duration_seconds": 240,
             "metadata_text": (
                 "Overhead camera on the metro viaduct. The black motorcycle approaches from the Pusa Road side at 22:29:30 and stops at the pillar. The "
                 f"registration {BIKE} is readable in two frames after enhancement. The rider keeps both feet on the ground and the engine running while "
                 "the pillion rider attacks the woman, then accelerates away at 22:30:17."
             )},
        ),
        DemoDocument(
            "cctv_traffic.pdf", "CCTVMetadata", "TRF-RJR-07", "CCTV FOOTAGE ANALYSIS - TRAFFIC CAMERA, RANI JHANSI ROAD",
            {"camera_identifier": "TRF-RJR-07", "recording_datetime": "2025-08-14T22:31:10+05:30",
             "location": "Traffic camera at Rani Jhansi Road crossing, near Ajmal Khan Road, Karol Bagh, New Delhi", "duration_seconds": 120,
             "metadata_text": (
                 "Traffic surveillance camera at the Rani Jhansi Road crossing, about 600 metres from the spot. At 22:31:10 a black Hero Splendor with two "
                 "riders passes at high speed towards Anand Parbat; the pillion rider wears a grey T-shirt and holds a phone. The time and route match the "
                 "escape seen on the shop and DMRC cameras."
             )},
        ),
        DemoDocument(
            "case_diary.pdf", "CaseDiary", "CD/KB/0287/2025", "CASE DIARY (Section 192 BNSS)",
            {"diary_number": "CD/KB/0287/2025", "officer_name": IO_NAME,
             "entries": [
                 {"entry_number": "1", "entry_datetime": "2025-08-14T22:45:00+05:30", "text": "DD No. 61-A was received from the PCR about a robbery with a knife near Metro Pillar 112, Ajmal Khan Road. I reached the spot with HC Sandeep Kumar and Constable Rahul, where the staff of PCR Van K-17 were guarding the place. The injured woman had already been taken to Dr. Ram Manohar Lohia Hospital by an auto-rickshaw driver. The tea stall owner Mohan Lal gave the registration number of the motorcycle, which he had noted on his hand, and it was flashed on the wireless to all PCR vans and pickets of the district."},
                 {"entry_number": "2", "entry_datetime": "2025-08-15T00:40:00+05:30", "text": "The spot was inspected in the presence of Mohan Lal and Pooja Sharma. Blood stains were found on the footpath about three metres from the pillar, with a trail of drops leading to the tea stall, and a broken chain link was found on the footpath. The blood was lifted on gauze with a control sample and the chain link was sealed, under seizure memo SM/KB/0108/2025. The district photography team photographed the spot and the street lighting was noted. The CCTV camera of Gupta Mobile Store opposite was found to cover the spot."},
                 {"entry_number": "3", "entry_datetime": "2025-08-15T03:10:00+05:30", "text": "At the hospital the MLC of the injured Neha Arora was obtained. It records a deep stab wound 6 cm long on the left forearm with injury to the extensor tendons and a fracture of the ulna, caused by a sharp weapon. Her blood-stained blue kurta and a blood sample on an FTA card were handed over sealed by the hospital and seized under memo SM/KB/0109/2025. The doctor declared her unfit to make a statement until the morning because of sedation. Her brother Vikas Arora was present."},
                 {"entry_number": "4", "entry_datetime": "2025-08-15T10:00:00+05:30", "text": "After the doctor declared the injured fit, her written complaint was recorded at the hospital by W/Constable Sunita in her own words and signed by her. On the basis of the complaint FIR No. 0287/2025 was registered at the police station under Sections 309(4) and 118(2) BNS and the investigation was entrusted to me. A copy of the FIR was sent to the court and to senior officers. The site plan of the spot was prepared on the basis of the spot inspection."},
                 {"entry_number": "5", "entry_datetime": "2025-08-15T13:00:00+05:30", "text": "The CCTV recording of Gupta Mobile Store was played in the presence of its owner Ritesh Gupta. It clearly shows the motorcycle stopping, the pillion rider confronting the complainant with a knife and the two men leaving. The hard disk and a pen drive copy were seized under memo SM/KB/0110/2025 with a Section 63 certificate. Written requests were sent to DMRC and to the traffic police for their camera recordings. Statements of Ritesh Gupta, Mohan Lal, Pooja Sharma, HC Satbir Singh, Raju Paswan, W/Constable Sunita, Constable Rahul and Vikas Arora were recorded."},
                 {"entry_number": "6", "entry_datetime": "2025-08-15T18:00:00+05:30", "text": "The vehicle registration record showed that the motorcycle used by the two men is registered in the name of Deepak Chauhan of Gali No. 3, Anand Parbat. Inquiry showed that his cousin Sunil Chauhan, who has a record of snatching cases, and a friend of Sunil named Rakesh Yadav were seen using the motorcycle in Anand Parbat. Secret informers were deployed in Anand Parbat to locate both men."},
                 {"entry_number": "7", "entry_datetime": "2025-08-16T09:30:00+05:30", "text": "On secret information received by HC Sandeep Kumar, a raid was conducted at House No. 14, Anand Parbat, with Mohan Lal accompanying the police party. The man found there was identified by Mohan Lal as the man with the knife and gave his name as Rakesh Yadav. He was arrested after being informed of the grounds of arrest and his rights, and his mother was informed. His face was kept muffled because a test identification parade was to be held."},
                 {"entry_number": "8", "entry_datetime": "2025-08-16T11:45:00+05:30", "text": "During interrogation the accused disclosed that he had hidden the knife, the chain and the phone in his room. Pursuant to his disclosure he took the police party into his room and took out a knife with a black handle from under the mattress and a gold chain and an iPhone 14 from a black bag on the shelf. The motorcycle parked outside was also seized. All articles were sealed with the seal DR and seized under memo SM/KB/0112/2025 in the presence of HC Sandeep Kumar and the local resident Satish Kumar, whose statements were recorded."},
                 {"entry_number": "9", "entry_datetime": "2025-08-16T14:00:00+05:30", "text": "The accused was medically examined and produced in muffled face before the court. He was remanded to judicial custody and an application for a test identification parade was moved, which was fixed at Tihar Jail. A raid at the house of Sunil Chauhan in Anand Parbat found it locked; neighbours stated that he had left the area in the morning. The case property was deposited in the malkhana."},
                 {"entry_number": "10", "entry_datetime": "2025-08-17T12:00:00+05:30", "text": "The statement of Deepak Chauhan, the registered owner of the motorcycle, was recorded. He stated that his cousin Sunil Chauhan had taken the motorcycle in the first week of August and had not returned it, and that Sunil and Rakesh Yadav were using it together. The registration certificate and insurance papers were taken on record. The motorcycle was inspected by the Motor Vehicle Inspector, who found its front number plate partly covered with black tape."},
                 {"entry_number": "11", "entry_datetime": "2025-08-18T12:00:00+05:30", "text": "The test identification parade was conducted at Tihar Jail by the Metropolitan Magistrate. The complainant Neha Arora and the eyewitness Mohan Lal separately and correctly identified Rakesh Yadav among the persons in the parade. The accused raised no objection to the proceedings. The knife, the kurta, the blood gauze and the FTA card were sent to FSL Rohini through Constable Arvind. The DMRC recording was received from the Station Controller Manoj Tiwari with a certificate and his statement was recorded."},
                 {"entry_number": "12", "entry_datetime": "2025-08-19T15:00:00+05:30", "text": "The specimen fingerprints of the accused were taken with the permission of the court and sent to the fingerprint division of FSL Rohini to be compared with the prints on the knife handle. The traffic camera recording from the Rani Jhansi Road crossing was received; it shows the motorcycle with two riders heading towards Anand Parbat a minute after the robbery. The statement of Constable Arvind about the deposit of the exhibits was recorded."},
                 {"entry_number": "13", "entry_datetime": "2025-08-22T12:00:00+05:30", "text": "The discharge summary of the injured was obtained from Dr. Ram Manohar Lohia Hospital. It records repair of the extensor tendons and plating of the ulna and states that she is unable to follow her ordinary pursuits for more than twenty days. The statement of Dr. Anil Kapoor was recorded about the nature of the injuries and the weapon; on being shown the knife he stated that it could cause the injury."},
                 {"entry_number": "14", "entry_datetime": "2025-08-23T12:00:00+05:30", "text": "The complainant identified the gold chain, the iPhone 14 and the knife at the police station. The jeweller Kailash Soni verified the chain against his bill and hallmark and confirmed the broken link. The IMEI of the iPhone was matched with the purchase invoice and box produced by Vikas Arora. Supplementary statements of the complainant and the jeweller were recorded."},
                 {"entry_number": "15", "entry_datetime": "2025-08-25T12:00:00+05:30", "text": "Attendance and leave records of the complainant were obtained from her employer, showing that she left office shortly before she was robbed and has been on medical leave since. The statement of the HR Manager Ankita Bose was recorded."},
                 {"entry_number": "16", "entry_datetime": "2025-08-26T12:00:00+05:30", "text": "The call detail records and customer application forms of the mobile numbers of both accused were obtained from Bharti Airtel. They place both phones together on the tower serving Ajmal Khan Road at the relevant time and on the tower serving Anand Parbat afterwards, with repeated calls between them that evening. Sunil Chauhan's number has been switched off since the arrest of Rakesh Yadav. The statement of the nodal officer was recorded."},
                 {"entry_number": "17", "entry_datetime": "2025-08-28T17:00:00+05:30", "text": "FSL report FSL/DEL/2025/BIO/3318 was received confirming that the blood on the knife is human and gives the DNA profile of the complainant, and that the blood on the kurta and on the gauze from the spot is also hers. The cut in the left sleeve of the kurta corresponds with the wound. Efforts continue to trace the second accused Sunil Chauhan."},
                 {"entry_number": "18", "entry_datetime": "2025-08-29T12:00:00+05:30", "text": "The chain and the phone were released to the complainant on superdari by order of the court after being photographed and their descriptions recorded. The statement of the malkhana in-charge HC Jagdish Prasad was recorded about the safe custody of the case property and the deposit of the exhibits at FSL."},
                 {"entry_number": "19", "entry_datetime": "2025-09-02T16:00:00+05:30", "text": "The fingerprint report FSL/DEL/2025/FP/0941 was received. The two chance prints developed on the black plastic handle of the knife are identical with the right thumb and right index finger impressions of Rakesh Yadav. The statement of the fingerprint expert Dr. Mamta Joshi was recorded."},
                 {"entry_number": "20", "entry_datetime": "2025-09-05T12:00:00+05:30", "text": "Non-bailable warrants against Sunil Chauhan were obtained from the court and raids were conducted at his relatives' houses in Anand Parbat and Sultanpuri without success. Proceedings for his proclamation under Section 84 BNSS were initiated. His previous involvement in two snatching cases of PS Patel Nagar was verified from the criminal records."},
                 {"entry_number": "21", "entry_datetime": "2025-09-08T12:00:00+05:30", "text": "The previous record of Rakesh Yadav was checked through the criminal records office; no previous conviction was found. His employer confirmed that he had stopped reporting for delivery work from the first week of August. Copies of all documents were arranged for supply to the accused under Section 230 BNSS."},
                 {"entry_number": "22", "entry_datetime": "2025-09-10T17:00:00+05:30", "text": "Investigation against Rakesh Yadav completed. The evidence of the complainant and the eyewitnesses, the identification in the test identification parade, the CCTV recordings, the recovery of the knife, chain, phone and motorcycle at his instance, the DNA report and the fingerprint report together establish the charges. The charge sheet is prepared against him under Sections 309(4) and 118(2) read with 3(5) BNS. Investigation against the absconding Sunil Chauhan continues under Section 193(9) BNSS."},
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
            comments="Final opinion and signature block recorded by the investigating officer.",
            corrections={
                "final_opinion": (
                    "On the evidence collected, a prima facie case is made out against accused Rakesh Yadav under Sections 309(4) and 118(2) BNS "
                    "for armed robbery causing grievous hurt. He was identified by the complainant and an eyewitness in the test identification "
                    "parade, the knife, chain, phone and motorcycle were recovered at his instance, the FSL report links the knife to the "
                    "complainant's blood and his fingerprints were found on its handle. He is forwarded for trial. The second accused, Sunil "
                    "Chauhan, is absconding and investigation against him is continuing under Section 193(9) BNSS."
                ),
                "signature": f"{IO_NAME}, Investigating Officer, Karol Bagh Police Station",
            },
        ),
    )
    review.record_decision(CASE_ID, decision_request_cls(decision="approve", reviewer_id=IO_ID, reviewer_name=IO_NAME, comments="Reviewed against source documents; approved."))
    review.record_decision(CASE_ID, decision_request_cls(decision="finalize", reviewer_id=IO_ID, reviewer_name=IO_NAME))


CASE = DemoCase(CASE_ID, TITLE, STATION, documents, finish)
