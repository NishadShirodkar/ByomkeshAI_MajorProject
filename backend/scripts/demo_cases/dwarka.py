"""Case B: hit-and-run causing grievous hurt on Sector 10 Road, Dwarka (FIR 0412/2025) - incomplete draft.

Deliberately carries problems for the review workflow to surface:
  * the complaint names the car owner Vikas Malhotra, while the FIR names the driver Vikram Sethi;
  * witness Sanjay Kumar's statement is dated before the incident and puts it at 8:00 am;
  * the spot inspection memo records a different place (Najafgarh Road, Uttam Nagar East);
  * one vehicle inspection report is for a different car (UP16BK3305);
  * the accused is not yet arrested, the car is not recovered and the FSL report is awaited.
"""

from __future__ import annotations

from .common import DemoCase, DemoDocument

CASE_ID = "DEMO_DRAFT_Dwarka_HitAndRun"
TITLE = "Rash driving causing grievous hurt, Dwarka"
STATION = "Dwarka Sector 23 Police Station, South West District, New Delhi"
IO_ID, IO_NAME = "IO-ASI-RAMESH-CHAND", "ASI Ramesh Chand"
PLACE = "Sector 10 Road, near Dwarka Mor Metro Station, New Delhi"
CAR, BIKE = "DL8CAF7712", "DL9SBK2231"

NARRATIVE = (
    "On 3 September 2025 at about 11:10 pm, the complainant's brother Rohit Mehta was riding his motorcycle on Sector 10 Road near Dwarka Mor "
    f"Metro Station when a speeding Maruti Swift car {CAR}, driven in a rash and negligent manner by the accused Vikram Sethi, hit his "
    "motorcycle from behind. In the accident Rohit Mehta fell on the road and sustained a fracture of the right leg and head injuries. The accused did not stop "
    "the car and drove away towards Najafgarh. "
    f"The victim was riding his red Hero Glamour motorcycle {BIKE} in the left lane at moderate speed, wearing a helmet, while returning home "
    "from his shop. The white car came from behind at high speed, swerved into the left lane while overtaking a bus near the metro station and "
    "struck the rear of the motorcycle, throwing the victim onto the road near the bus stop. Passers-by called the police and an ambulance, and "
    "a cab driver who followed the car for some distance noted its registration number. The accused neither stopped to help the injured nor "
    "informed the police. The car is registered in the name of Vikas Malhotra, a caterer of Najafgarh, whose driver Vikram Sethi had taken it "
    "alone that evening to deliver crockery to a banquet hall in Sector 10. The next morning the accused took the damaged car, with its left "
    "front bumper broken and its left headlight smashed, to a workshop on Najafgarh Road for a quick cash repair, but left in a hurry before "
    "the repair began. He has since absconded with the car, his mobile phone has been switched off and he has not returned to his rented room "
    "in Kakrola. The bus driver, the bus conductor, the cab driver and a nurse waiting at the bus stop saw the car strike the motorcycle."
)


def documents() -> list[DemoDocument]:
    complaint_text = (
        f"My brother Rohit Mehta was hit by a speeding Maruti Swift car {CAR} on Sector 10 Road in Dwarka on the night of 3 September 2025. "
        f"I request legal action against Vikas Malhotra, the owner of the Maruti Swift {CAR}, for the rash and negligent driving.\n\n"
        "My brother runs a mobile accessories shop in Sector 10 market and closes it at about 10:45 pm. He rides home on his red Hero Glamour "
        f"motorcycle {BIKE} and always wears a helmet. That night a passer-by called me from my brother's phone and told me that he was lying "
        "injured near the Dwarka Mor metro station. I reached the spot and found that he had already been taken to Venkateshwar Hospital.\n\n"
        "People at the spot told me that a white Swift car had come at very high speed from behind, hit my brother's motorcycle and fled "
        "towards Najafgarh without stopping. A cab driver gave me the number of the car. When I searched the number on the transport "
        "department website it showed the name of Vikas Malhotra as the owner. My brother has a broken thigh bone and a head wound and is "
        "admitted in the orthopaedic ward. I request that the guilty person be found and punished."
    )
    sanjay = (
        "I run a paan shop near the metro station in Dwarka. The accident happened at about 8:00 am when I was opening my shop. "
        "A white Maruti Swift came speeding and hit a motorcyclist, who fell on the road. The car did not stop.\n\n"
        "The motorcyclist was wearing a helmet and was riding normally in the left side of the road. After the impact the motorcycle slid "
        "along the road and its headlight broke into pieces. The car went away very fast towards Najafgarh. I could not note its number.\n\n"
        "I ran towards the injured man with other people. His right leg was badly hurt and he could not stand. Someone called the police "
        "and an ambulance. I can identify the car if I see it again because its front bumper was damaged on the left side."
    )
    anil_supp = (
        "I, Anil Mehta, state further that after giving my complaint I came to know from the police that the car "
        f"{CAR} is registered in the name of Vikas Malhotra but that on the night of the accident it was being driven by his driver Vikram "
        "Sethi. I had named Vikas Malhotra in my complaint only because his name appeared as the owner on the website; I did not see who was "
        "driving the car.\n\n"
        "My brother remained in the orthopaedic ward of Venkateshwar Hospital and was operated upon for the fracture of his thigh bone. The "
        "doctors have said he will not be able to walk properly for at least three months. Our family runs on the income of his shop, which "
        "has remained closed since then. I have handed over copies of the hospital bills to the police. I request that the driver be arrested "
        "and the car recovered."
    )
    rohit = (
        "I, Rohit Mehta, aged 34 years, son of Late Suresh Mehta, resident of Sector 12, Dwarka, state that I run a mobile accessories shop in "
        f"Sector 10 market. On 3 September 2025 I closed my shop at about 10:45 pm and set off for home on my red Hero Glamour motorcycle {BIKE}. "
        "I was wearing my helmet and riding in the left lane at about 35 to 40 km/h.\n\n"
        "At about 11:10 pm, when I was near the bus stop by Dwarka Mor Metro Station, I heard the loud sound of an engine behind me and before I "
        "could look back something hit the rear of my motorcycle with great force. I was thrown onto the road and my right leg was trapped "
        "under the motorcycle. I saw a white car going away fast without stopping. I could not see its number or the driver.\n\n"
        "People gathered and an ambulance took me to Venkateshwar Hospital. My thigh bone was broken and I had a cut on my head. I was operated "
        "upon and a rod was put in my leg. I cannot walk without support and my shop has remained closed since the accident. I want the driver "
        "who hit me and ran away to be punished."
    )
    gurpreet = (
        "I, Gurpreet Singh, drive a cab with a ride-hailing company. On 3 September 2025 at about 11:10 pm I was driving behind a DTC bus on "
        "Sector 10 Road towards Dwarka Mor when a white Maruti Swift overtook me at very high speed, cut into the left lane to pass the bus, and "
        "hit a red motorcycle in front of the bus. The motorcyclist fell on the road.\n\n"
        f"The car did not stop. I followed it for about 300 metres towards Najafgarh and read its number, {CAR}, in my headlights before it "
        "turned off and went out of sight. The left side of its front bumper was damaged and the left headlight was not working after the "
        "impact. I could see only one man in the car, in the driver's seat, who wore a light-coloured shirt.\n\n"
        "I came back to the spot and gave the number to the injured man's brother and to the PCR staff. I can identify the car. I made a voice "
        "note of the number on my phone at that time and have shown it to the police.\n\n"
        "My cab has a dashboard camera, but its memory card records over itself every few hours and the relevant part had already been "
        "erased by the time the police asked for it. The ride-hailing app record of my trip shows my cab on Sector 10 Road towards Dwarka Mor "
        "at that time, and I have given a screenshot of it to the police. I had no passenger in the cab then. I do not know the driver of "
        "the car or the injured man and I have no interest in this matter except to tell the truth about what I saw."
    )
    priya = (
        "I, Priya Nair, work as a nurse in a private hospital in Dwarka and was waiting for a bus at the stop near Dwarka Mor Metro Station on "
        "3 September 2025 after my evening shift. At about 11:10 pm I heard a loud bang and saw a motorcyclist being thrown onto the road right "
        "in front of the bus stop. A white car was speeding away towards Najafgarh.\n\n"
        "Because I am a nurse I went to the injured man at once. He was conscious but in severe pain. His right thigh was swollen and deformed "
        "and he had a bleeding cut on the right side of his head where the helmet had been pushed up. I kept his neck still, stopped the "
        "bleeding with my scarf and asked people not to move him until the ambulance came. The ambulance reached in about fifteen minutes and "
        "I helped the staff put him on the stretcher. I could not see the number of the car.\n\n"
        "From where I was standing I could see that the motorcycle was going slowly in the leftmost lane with its tail light on, and that the "
        "car came from the right side of the bus very fast and turned sharply into the left lane. There was no time for the motorcyclist to "
        "move out of the way. The car's brake lights did not come on before or after the impact. The injured man told me his name and asked me "
        "to call his brother, which I did from his phone. I gave my name and number to the police when they arrived."
    )
    pcr = (
        "I, HC Ajay Kumar, am the in-charge of PCR Van D-21, South West District. On 3 September 2025 at about 11:14 pm we received a call about "
        "a road accident near the Dwarka Mor metro station bus stop. We reached the spot at about 11:22 pm.\n\n"
        f"A red Hero Glamour motorcycle {BIKE} was lying on its left side in the left lane, with pieces of its rear mudguard, tail light and "
        "number plate scattered around it. The injured man was lying near the bus stop with a woman giving him first aid. The ambulance came "
        f"and took him to Venkateshwar Hospital. A cab driver, Gurpreet Singh, told us that a white Maruti Swift {CAR} had hit the motorcycle "
        "and fled towards Najafgarh. I flashed the number on the wireless and guarded the spot until ASI Ramesh Chand arrived.\n\n"
        "While we waited, the DTC bus driver and conductor told us that the car had overtaken their bus at high speed and cut into the left "
        "lane just before striking the motorcycle. I noted their names and the bus number and gave them to the investigating officer. I also "
        "diverted the traffic around the fallen motorcycle and the broken pieces so that the scene would not be disturbed before the inspection. "
        "Nobody touched the motorcycle until the crime team photographed it."
    )
    dr_iyer = (
        "I, Dr. Meera Iyer, Consultant Orthopaedics, Venkateshwar Hospital, Dwarka, state that on 3 September 2025 at about 11:45 pm Rohit Mehta, "
        "aged 34 years, was brought to the emergency by ambulance with an alleged history of a road traffic accident on Sector 10 Road. I "
        "examined him and prepared MLC number MLC/VH/2025/5127.\n\n"
        "He was conscious and oriented. He had a closed fracture of the shaft of the right femur and a 5 cm scalp laceration over the right "
        "parietal region, with abrasions on the right elbow and knee. CT scan of the head showed no bleeding inside the skull. He underwent "
        "intramedullary nailing of the femur on 4 September 2025.\n\n"
        "In my opinion the injuries are grievous because of the fracture and are consistent with a rear impact on a motorcycle followed by a "
        "fall. His blood alcohol level was nil. He will be unable to follow his ordinary pursuits for well over twenty days."
    )
    vikas = (
        f"I, Vikas Malhotra, am the registered owner of the white Maruti Swift car {CAR}. I run a catering business in Najafgarh and Vikram "
        "Sethi has been working as my driver for about a year. He keeps the car with him at night because he lives near the godown.\n\n"
        "On the night of 3 September 2025 I was at home in Sector 19, Dwarka, and the car was with Vikram Sethi, who had taken it to drop "
        "supplies at a function in Sector 10. He did not return the car the next morning and his phone was switched off. When the police "
        "contacted me I came to know about the accident. I did not drive the car that night.\n\n"
        "I have produced the registration certificate, insurance policy and the address and phone number of Vikram Sethi before the police. I "
        "do not know where Vikram Sethi or the car is at present. I will produce the car if it comes to my notice.\n\n"
        "I have tried to call Vikram Sethi many times since then but his phone is switched off. His salary for August was paid to him in cash "
        "at the start of September. He had driven my car for about a year without any accident that I know of, but I had warned him more than "
        "once about driving fast after receiving e-challans for over-speeding on my registered mobile number. I have given copies of those "
        "e-challans to the police."
    )
    mukesh = (
        "I, Mukesh Yadav, run a denting and painting workshop on Najafgarh Road. On the morning of 4 September 2025 a man who said his name was "
        f"Vicky came to my workshop in a Maruti Swift {CAR}. The car was of white colour, with its front bumper broken on the left side, the left "
        "headlight smashed and red paint marks on the bumper. He asked me to repair it quickly and pay in cash.\n\n"
        "While we were preparing an estimate he received a phone call and left in a hurry in the same car, saying he would come back. He did "
        "not return. He was about 30 years old, of medium build, and wore a light blue shirt. When the police showed me a photograph of Vikram "
        "Sethi I said that he resembles the man. My workshop camera recorded the car arriving and leaving and I gave the recording to the police."
    )
    landlord = (
        "I, Harbans Lal, own a house in Kakrola village where Vikram Sethi has been living as a tenant on the first floor for about two years. "
        "He works as a driver for a caterer.\n\n"
        "He came home very late on the night of 3 September 2025 and left early the next morning with a bag. He told my wife he was going to "
        "his village in Haryana for a few days. He has not come back since and his room is locked. The police came looking for him and I gave "
        "them a copy of his rent agreement and identity card. I have not seen the white car since that night.\n\n"
        "He usually parked the car in the lane outside my house at night. That night I heard the car stop outside very late and saw from my "
        "window that he spent some time looking at its front with the torch of his phone before coming upstairs. In the morning the car was "
        "gone before I woke up. He had paid his rent for September in advance, which he had never done before."
    )
    rakesh = (
        "I, Constable Rakesh, am posted in the crime team of South West District. On 4 September 2025 I photographed the spot on Sector 10 "
        "Road on the direction of ASI Ramesh Chand. The photographs show the damaged motorcycle, the broken pieces of its tail light and rear mudguard, a "
        "broken piece of white plastic and fragments of headlamp glass from the car, and the skid marks.\n\n"
        "I handed over 16 photographs and the memory card with a certificate. I also lifted small chips of white paint from the rear mudguard of "
        "the motorcycle and from the road, which were sealed separately by the investigating officer for chemical comparison."
    )
    dmrc = (
        "I, Rajiv Saxena, am the Station Controller of Dwarka Mor metro station. The DMRC camera DMRC-DM-EXT-04 on the station building covers "
        "Sector 10 Road and the bus stop below. On the request of the police I retrieved and copied the recording of the night of 3 September "
        "2025 between 10:55 pm and 11:25 pm on a pen drive and issued a certificate under Section 63 of the Bharatiya Sakshya Adhiniyam.\n\n"
        "The recording shows a white car overtaking a bus at high speed, swerving into the left lane, striking a motorcycle from behind and "
        "driving away without stopping. The registration number of the car is not readable in the recording because of the headlight glare."
    )
    nodal = (
        "I, Seema Rathi, am the Nodal Officer of Reliance Jio for the Delhi circle. On a notice from Dwarka Sector 23 Police Station I furnished "
        "the customer application form and call detail records of the mobile number used by Vikram Sethi.\n\n"
        "The records show that on the night of 3 September 2025 the number was connected to the tower serving Dwarka Mor and Sector 10 between "
        "10:50 pm and 11:15 pm, and to a tower in Najafgarh shortly afterwards. The number was last connected on the morning of 4 September 2025 "
        "near Najafgarh and has been switched off since. I have issued a certificate under Section 63 of the Bharatiya Sakshya Adhiniyam.\n\n"
        "The customer application form shows that the number was issued in the name of Vikram Sethi on the basis of his Aadhaar card with the "
        "Kakrola address. The records are generated automatically by the company's systems and stored on its servers in the ordinary course "
        "of business."
    )
    malkhana = (
        "I, HC Dinesh Kumar, am the MHC(M) of Dwarka Sector 23 Police Station. I received the sealed parcels of this case from ASI Ramesh Chand, "
        "namely the broken pieces of the motorcycle and the car, the paint chips from the motorcycle and the road, the helmet of the injured and "
        "the CCTV pen drives, as entered in register number 19.\n\n"
        "The parcels of the paint chips and the plastic and glass pieces were sent to FSL Rohini on 9 September 2025 through Constable Sunil, "
        "and the receipt has been placed on the file. The report of the laboratory has not yet been received. The red motorcycle of the injured "
        "is kept in the police station yard.\n\n"
        "The helmet of the injured and the three pen drives of the camera recordings are kept in the malkhana under seal. No part of the case "
        "property has been released so far. The entries in register number 19 and the road certificate bear my signature, and while the case "
        "property has been in my charge nobody has tampered with it."
    )

    bus_driver = (
        "I, Ramkaran, am a driver with the Delhi Transport Corporation, posted at the Dwarka Sector 8 depot. On 3 September 2025 I was driving "
        "DTC bus route 764 from Najafgarh towards Dwarka Mor. At about 11:10 pm I was slowing down in the second lane to pull into the bus stop "
        "near Dwarka Mor Metro Station. A red motorcycle was going ahead of me in the left lane at a normal speed.\n\n"
        "Suddenly a car came from behind on my right side at a very high speed, overtook my bus and cut sharply into the left lane in front of "
        "me. It hit the motorcycle from behind with great force. The motorcyclist was thrown onto the road towards the bus stop and his "
        "motorcycle slid along the road. I braked hard and stopped my bus so that it would not run over him.\n\n"
        "The car did not stop or even slow down; it went on towards Najafgarh. It was a small hatchback of white colour. I could not read its "
        "number because it went past me so fast. I switched on the hazard lights of my bus to protect the injured man and my conductor called "
        "the police. The bus has a camera inside, but it does not cover the road. I can say with certainty that the driver of the car was at "
        "fault and that the motorcyclist was riding properly in his lane."
    )
    conductor = (
        "I, Satpal, am the conductor of DTC bus route 764. On 3 September 2025 at about 11:10 pm I was standing near the front door of the bus as "
        "the driver Ramkaran slowed down for the Dwarka Mor bus stop. I heard a loud noise of an engine and then a crash, and the driver braked "
        "hard. Through the windscreen I saw a motorcyclist lying on the road and a car going away fast towards Najafgarh.\n\n"
        "I immediately called 112 from my mobile phone and told them about the accident and that the car had run away. I got down with some "
        "passengers and stood on the road with a torch to stop other vehicles from coming close to the injured man. A lady at the bus stop was "
        "already giving him first aid. When the PCR came I told them what I had seen. The call record on my phone shows my call to 112 at 11:12 "
        "pm."
    )
    paramedic = (
        "I, Deepak Rana, am an emergency medical technician on CATS ambulance DL1-CATS-118. On 3 September 2025 at about 11:15 pm we were sent "
        "to the Dwarka Mor bus stop for a road accident case. We reached at about 11:27 pm. The patient, a man of about 34 years, was lying near "
        "the bus stop with a lady keeping his neck steady.\n\n"
        "He was conscious and told us his name was Rohit Mehta. He had a deformed and swollen right thigh and a bleeding wound on the right side "
        "of his scalp. We applied a cervical collar and a traction splint to the right leg, dressed the scalp wound and shifted him on a "
        "spine board to the ambulance. On the way he said that a car had come from behind and gone away without stopping. We handed him over "
        "to the emergency of Venkateshwar Hospital at about 11:45 pm. The patient care record of the ambulance bears my signature."
    )
    pump = (
        "I, Naveen Kumar, am the manager of the Indian Oil petrol pump on Sector 10 Road, about 400 metres before Dwarka Mor Metro Station on "
        "the way from Sector 10. The pump has eight cameras, one of which, IOCL-S10-02, covers the forecourt and the main road. The recordings "
        "are stored on a recorder in my office for fifteen days and the time on the recorder is set correctly.\n\n"
        "On the request of ASI Ramesh Chand I played back the recording of the night of 3 September 2025 in his presence. At about 11:08 pm a "
        f"white Maruti Swift is seen passing the pump at very high speed towards Dwarka Mor. Its number, {CAR}, can be read in one frame when "
        "the image is paused. I copied the relevant part onto a pen drive and handed it over to the police with a certificate under Section 63 "
        "of the Bharatiya Sakshya Adhiniyam."
    )
    supervisor = (
        "I, Pawan Kumar, am the supervisor at the catering godown of Vikas Malhotra at Najafgarh. Vikram Sethi works as the driver of the white "
        f"Maruti Swift {CAR} and also helps in loading the material. He keeps the car at night and brings it in the morning.\n\n"
        "On 3 September 2025 at about 9:30 pm Vikram Sethi loaded two boxes of crockery into the car to deliver to a function at a banquet hall "
        "in Sector 10, Dwarka, and left alone in the car. He was wearing a light blue shirt. He did not come to the godown the next morning and "
        "his phone was switched off. He has not returned since.\n\n"
        "The banquet hall manager told me that he delivered the boxes at about 10:45 pm and left. I do not know where he is now. I gave the "
        "police his photograph from our staff records and his mobile number."
    )
    sunil = (
        "I, Constable Sunil, am posted at Dwarka Sector 23 Police Station. On 9 September 2025 the MHC(M) handed over to me the sealed parcels "
        "of this case containing the paint chips, the broken plastic bumper piece and the headlamp glass, with the forwarding letter "
        "and road certificate. The seals were intact.\n\n"
        "I deposited the parcels at FSL Rohini on the same day and obtained the receipt, which I handed over to the MHC(M) on my return. While "
        "the parcels were in my possession nobody tampered with them. The laboratory staff told me that the comparison would need a control "
        "sample of the paint of the car itself once the car is recovered."
    )
    haryana = (
        "I, SI Balwan Singh, am posted at Police Station Beri, District Jhajjar, Haryana. On 10 September 2025 ASI Ramesh Chand of Dwarka Sector "
        "23 Police Station came to our police station with a request for help in tracing Vikram Sethi, son of Om Parkash, resident of village "
        "Dubaldhan in our area.\n\n"
        "I accompanied the Delhi Police team to the house of his family in the village. His father and brother stated that Vikram had come home "
        "for one night in the first week of September and had then left, saying that he was going to look for work in Punjab. The white car was "
        "not found at the house or in the village. I have been asked to inform the Delhi Police if he returns, and a watch has been kept through "
        "the village chowkidar."
    )

    banquet = (
        "I, Arun Khanna, am the manager of Shagun Banquets in Sector 10, Dwarka. On 3 September 2025 we had a wedding reception at the hall, "
        "for which the crockery was supplied by the caterer Vikas Malhotra of Najafgarh.\n\n"
        "At about 10:40 pm his driver, whom I know as Vikram, came alone in a Maruti Swift of white colour and unloaded two boxes of crockery "
        "at our back gate. I signed his delivery challan at 10:45 pm, which carries my signature and the time. He was wearing a light blue "
        "shirt. He was in a hurry and left in the car within a few minutes towards the main Sector 10 Road. The car was undamaged at that "
        "time; I saw its front clearly under the lights of the gate.\n\n"
        "I have given the police a copy of the delivery challan and the recording of our gate camera, which shows the car arriving and "
        "leaving. I can identify Vikram if I see him."
    )
    neighbour = (
        "I, Manpreet Kaur, run a garment shop next to the mobile accessories shop of Rohit Mehta in Sector 10 market. We usually close our "
        "shops at about the same time.\n\n"
        "On 3 September 2025 Rohit closed his shop at about 10:45 pm, as usual, and left on his red motorcycle wearing his helmet. He was "
        "perfectly normal and had not taken any alcohol; he does not drink. He always rides slowly because he carries stock in a bag on the "
        "motorcycle. Later that night I came to know from his brother that he had been injured on Sector 10 Road near Dwarka Mor. His shop "
        "has remained closed since then and his family is facing great difficulty."
    )
    rto = (
        "I, Sudesh Kumari, am the Dealing Assistant in the Motor Licensing Office, Dwarka. On the request of the police I have produced the "
        f"registration record of the Maruti Swift {CAR}. The car, a 2021 model of white colour, is registered in the name of Vikas Malhotra of "
        "Sector 19, Dwarka, and its insurance with a private insurer is valid. No transfer of ownership has been applied for.\n\n"
        f"I have also produced the record of the red Hero Glamour motorcycle {BIKE}, which is registered in the name of Rohit Mehta of Sector 12, "
        "Dwarka. The driving licence record of Vikram Sethi shows a licence for light motor vehicles issued in Jhajjar, Haryana, and valid till "
        "2031. Attested copies of these records have been handed over to the investigating officer."
    )

    wife = (
        "I, Sunaina Mehta, wife of Rohit Mehta, state that my husband runs a mobile accessories shop in Sector 10 market and is the only earning "
        "member of our family of four, including our two young daughters and his mother. On the night of the accident my brother-in-law Anil "
        "Mehta called me and I reached Venkateshwar Hospital, where my husband was in the emergency with his right leg in a splint and a "
        "bandage on his head.\n\n"
        "He was operated upon the next day and a rod was put in his thigh bone. He remained in hospital for eight days. Since his discharge he "
        "has been confined to bed and moves only with a walker. He needs help for every daily activity and goes for physiotherapy three times "
        "a week. The doctors have said that he will not be able to ride a motorcycle or run the shop for at least three months.\n\n"
        "We have spent about Rs 2.6 lakh on the hospital, medicines and physiotherapy, partly by borrowing from relatives, and the shop has "
        "remained closed, so we have no income. I have given copies of the bills to the police. My husband told me that the car came from "
        "behind at great speed and that the driver ran away without helping him. I request that the driver be arrested quickly and that we "
        "be given compensation."
    )
    surveyor = (
        "I, Alok Srivastava, am an insurance surveyor and loss assessor licensed by the IRDAI. On the request of the insurer of the motorcycle of "
        f"Rohit Mehta, I inspected the red Hero Glamour {BIKE} in the yard of Dwarka Sector 23 Police Station in the presence of the police.\n\n"
        "The rear mudguard, tail light assembly, number plate, grab rail and rear indicators were broken, the rear wheel rim was bent and the "
        "rear shock absorber was damaged. The left side of the fuel tank, the left handlebar end and the left foot-rest were scraped. There was "
        "transfer of white paint on the rear mudguard and the grab rail at a height of about 70 to 80 cm from the ground, which corresponds to "
        "the height of the front bumper of a hatchback car.\n\n"
        "In my opinion the damage was caused by a forceful impact from directly behind, followed by the motorcycle falling on its left side. "
        "The pattern does not indicate any sudden braking or turning by the motorcyclist. I have assessed the loss at about Rs 38,000 and have "
        "given a copy of my report to the investigating officer."
    )

    physio = (
        "I, Dr. Kavya Menon, am a physiotherapist at Venkateshwar Hospital, Dwarka. Rohit Mehta has been attending physiotherapy under my care "
        "three times a week since his discharge after the nailing of his right femur.\n\n"
        "At the start he could not lift his right leg against gravity and could walk only a few steps with a walker without putting weight on "
        "the operated leg. The knee on the operated side had become stiff, with bending limited to about 40 degrees. He also complained of "
        "headaches and pain at the scalp wound.\n\n"
        "With exercises his knee bending has improved, but he still cannot bear full weight and will need a walker and then a stick for several "
        "more weeks. In my assessment he will not be fit to ride a two-wheeler or to stand for long hours in his shop for at least three months "
        "from the date of the injury. I have given copies of the treatment record to the police."
    )
    antecedents = (
        "I, SI Mahesh Sharma, am posted at Dwarka Sector 23 Police Station. On the direction of the SHO I verified the antecedents of the "
        "accused Vikram Sethi, son of Om Parkash, resident of village Dubaldhan, District Jhajjar, Haryana, and presently a tenant at Kakrola, "
        "New Delhi.\n\n"
        "As per the records of the crime records office and the Haryana Police, he has one earlier case of rash driving registered at Police "
        "Station Bahadurgarh in 2023, in which he was released on bail, and three e-challans for over-speeding in Delhi in the last year, two of "
        "them recorded on the Najafgarh Road. His driving licence for light motor vehicles was issued by the licensing authority at Jhajjar.\n\n"
        "His employer and landlord describe him as a driver who used to drive fast. Copies of the e-challan records and the earlier FIR have been "
        "placed on the case file."
    )

    fastag = (
        "I, Jaswant Singh, am the nodal officer for law enforcement requests at the regional office of the National Highways Authority of India "
        f"in Delhi. On a notice from Dwarka Sector 23 Police Station I searched the FASTag transaction records of the Maruti Swift {CAR} for the "
        "period from 1 September to 15 September 2025.\n\n"
        "The FASTag linked to the car shows regular transactions at the Mundka and Bahadurgarh toll plazas in August, when the car was being "
        "used for catering deliveries. In September there is only one transaction, at the Bahadurgarh plaza on the morning after the "
        "accident, in the direction of Haryana. There is no transaction after that, which suggests that the car has either been kept off "
        "the highways or the tag has been removed.\n\n"
        "The records are maintained electronically by the toll management system in the ordinary course of business. I have supplied a "
        "printout with a certificate under Section 63 of the Bharatiya Sakshya Adhiniyam and have asked the toll operators to alert the "
        "police if the tag is read again."
    )

    father = (
        "I, Om Parkash, resident of village Dubaldhan, District Jhajjar, Haryana, am the father of Vikram Sethi. My son has been working as a "
        "driver in Delhi for some years and lives in a rented room in Kakrola. He usually comes home once a month.\n\n"
        "In the first week of September he came home late one night without informing us, in a white car which he parked behind our cattle "
        "shed. He looked worried and said that he had left his job and was going to Punjab to look for work. He left before dawn the next day "
        "in the same car. I noticed that the front of the car on the left side was broken, but when I asked him about it he did not answer.\n\n"
        "He has not called us since and his phone is switched off. I do not know where he is. When the police came to our village with the "
        "local police I told them all this. If he contacts us I will ask him to present himself before the police."
    )

    def witness(filename: str, ref: str, name: str, date: str, age: str, occupation: str, address: str, text: str, father: str, contact: str, recorded_by: str = IO_NAME) -> DemoDocument:
        return DemoDocument(
            filename, "WitnessStatement", ref, "STATEMENT OF WITNESS UNDER SECTION 180 BNSS",
            {"statement_reference": ref, "statement_date": date, "witness_name": name, "father_name": father, "age": age, "occupation": occupation,
             "witness_address": address, "contact": contact, "recorded_by": recorded_by, "statement_text": text},
        )

    return [
        DemoDocument(
            "fir.pdf", "FIR", "0412/2025", "FIRST INFORMATION REPORT (Section 173 BNSS)",
            {"fir_number": "0412/2025", "crime_number": "0412/2025", "registration_date": "2025-09-04", "police_station": "Dwarka Sector 23",
             "complainant_name": "Anil Mehta", "accused_names": ["Vikram Sethi"], "victim_names": ["Rohit Mehta"], "vehicle_registrations": [CAR, BIKE],
             "occurrence_datetime": "2025-09-03T23:10:00+05:30", "occurrence_location": PLACE, "jurisdiction": "South West Delhi",
             "reported_sections": ["Section 281 BNS", "Section 125 BNS", "Section 184 Motor Vehicles Act", "Section 134 Motor Vehicles Act"],
             "narrative_text": NARRATIVE},
            [("District", "South West Delhi"), ("General Diary reference", "DD No. 7-A"), ("Investigating officer", IO_NAME)],
        ),
        DemoDocument(
            "complaint.pdf", "Complaint", "C/DW/0412/2025", "WRITTEN COMPLAINT",
            {"complaint_reference": "C/DW/0412/2025", "complaint_date": "2025-09-04", "complainant_name": "Anil Mehta",
             "complainant_address": "Sector 12, Dwarka, New Delhi", "person_complained_against_names": ["Vikas Malhotra"],
             "victim_names": ["Rohit Mehta"], "vehicle_registrations": [CAR], "complaint_text": complaint_text},
            [("To", "The SHO, Dwarka Sector 23 Police Station")],
        ),
        witness("witness_statement_01.pdf", "WS/DW/0412/01", "Sanjay Kumar", "2025-09-01", "41", "Shopkeeper", "Paan shop near Dwarka Mor Metro Station, New Delhi", sanjay, "Late Ram Kishore", "9873321100", "ASI Ramesh Chand"),
        witness("witness_statement_02.pdf", "WS/DW/0412/02", "Gurpreet Singh", "2025-09-04", "37", "Cab driver", "RZ-44, Mahavir Enclave, Palam, New Delhi", gurpreet, "Harjeet Singh", "9811776654"),
        witness("witness_statement_03.pdf", "WS/DW/0412/03", "Priya Nair", "2025-09-04", "29", "Staff nurse", "Flat 204, Sector 7, Dwarka, New Delhi", priya, "K. Nair", "9899123401"),
        witness("witness_statement_04.pdf", "WS/DW/0412/04", "Ajay Kumar", "2025-09-04", "43", "Head Constable, In-charge PCR Van D-21", "PCR Unit, South West District, Delhi Police", pcr, "Om Prakash", "9810556677"),
        witness("witness_statement_05.pdf", "WS/DW/0412/05", "Rakesh", "2025-09-04", "32", "Constable, Crime Team, South West District", "Crime Team Office, South West District, Delhi Police", rakesh, "Mahender Singh", "9810114477"),
        witness("witness_statement_06.pdf", "WS/DW/0412/06", "Vikas Malhotra", "2025-09-05", "45", "Caterer, registered owner of the car", "House 31, Sector 19, Dwarka, New Delhi", vikas, "K. L. Malhotra", "9811890012"),
        witness("witness_statement_07.pdf", "WS/DW/0412/07", "Mukesh Yadav", "2025-09-06", "39", "Workshop owner", "Yadav Motor Works, Najafgarh Road, New Delhi", mukesh, "Shiv Charan Yadav", "9958001122"),
        witness("witness_statement_08.pdf", "WS/DW/0412/08", "Harbans Lal", "2025-09-06", "63", "Landlord of the accused", "Kakrola Village, New Delhi", landlord, "Late Mangat Ram", "9213456780"),
        witness("witness_statement_09.pdf", "WS/DW/0412/09", "Rajiv Saxena", "2025-09-07", "46", "Station Controller, Dwarka Mor Metro Station, DMRC", "Dwarka Mor Metro Station, New Delhi", dmrc, "B. L. Saxena", "9810667788"),
        witness("witness_statement_10.pdf", "WS/DW/0412/10", "Anil Mehta", "2025-09-08", "38", "Businessman", "Sector 12, Dwarka, New Delhi", anil_supp, "Late Suresh Mehta", "9811234500"),
        witness("witness_statement_11.pdf", "WS/DW/0412/11", "Dr. Meera Iyer", "2025-09-10", "44", "Consultant Orthopaedics, Venkateshwar Hospital", "Venkateshwar Hospital, Sector 18A, Dwarka, New Delhi", dr_iyer, "S. Iyer", "9811667700"),
        witness("witness_statement_12.pdf", "WS/DW/0412/12", "Seema Rathi", "2025-09-11", "39", "Nodal Officer, Reliance Jio (Delhi circle)", "Reliance Jio, Saket, New Delhi", nodal, "R. K. Rathi", "9810998800"),
        witness("witness_statement_13.pdf", "WS/DW/0412/13", "Rohit Mehta", "2025-09-12", "34", "Shop owner, mobile accessories", "Sector 12, Dwarka, New Delhi", rohit, "Late Suresh Mehta", "9811234511"),
        witness("witness_statement_15.pdf", "WS/DW/0412/15", "Ramkaran", "2025-09-04", "48", "Driver, Delhi Transport Corporation (route 764)", "DTC Depot, Sector 8, Dwarka, New Delhi", bus_driver, "Late Mangal Singh", "9810775500"),
        witness("witness_statement_16.pdf", "WS/DW/0412/16", "Satpal", "2025-09-04", "36", "Conductor, Delhi Transport Corporation (route 764)", "DTC Depot, Sector 8, Dwarka, New Delhi", conductor, "Raghubir Singh", "9810775511"),
        witness("witness_statement_17.pdf", "WS/DW/0412/17", "Deepak Rana", "2025-09-05", "31", "Emergency medical technician, CATS ambulance", "CATS Centre, Dwarka Sector 9, New Delhi", paramedic, "Jagat Rana", "9810775522"),
        witness("witness_statement_18.pdf", "WS/DW/0412/18", "Pawan Kumar", "2025-09-05", "42", "Supervisor, catering godown of Vikas Malhotra", "Catering godown, Najafgarh, New Delhi", supervisor, "Ram Phal", "9810775533"),
        witness("witness_statement_19.pdf", "WS/DW/0412/19", "Naveen Kumar", "2025-09-07", "40", "Manager, Indian Oil petrol pump, Sector 10 Road", "Indian Oil petrol pump, Sector 10 Road, Dwarka", pump, "Late Sat Narain", "9810775544"),
        witness("witness_statement_20.pdf", "WS/DW/0412/20", "Sunil", "2025-09-09", "27", "Constable, Dwarka Sector 23 Police Station", "Dwarka Sector 23 Police Station, New Delhi", sunil, "Karan Singh", "9810775555"),
        witness("witness_statement_21.pdf", "WS/DW/0412/21", "Balwan Singh", "2025-09-10", "50", "Sub-Inspector, Police Station Beri, District Jhajjar, Haryana", "Police Station Beri, District Jhajjar, Haryana", haryana, "Late Hari Singh", "9416775566"),
        witness("witness_statement_22.pdf", "WS/DW/0412/22", "Arun Khanna", "2025-09-06", "47", "Manager, Shagun Banquets, Sector 10", "Shagun Banquets, Sector 10, Dwarka, New Delhi", banquet, "R. L. Khanna", "9810775577"),
        witness("witness_statement_23.pdf", "WS/DW/0412/23", "Manpreet Kaur", "2025-09-06", "39", "Garment shop owner, Sector 10 market", "Sector 10 market, Dwarka, New Delhi", neighbour, "W/o Jasbir Singh", "9810775588"),
        witness("witness_statement_24.pdf", "WS/DW/0412/24", "Sudesh Kumari", "2025-09-08", "52", "Dealing Assistant, Motor Licensing Office, Dwarka", "Motor Licensing Office, Sector 13, Dwarka, New Delhi", rto, "Late Mohan Lal", "9810775599"),
        witness("witness_statement_25.pdf", "WS/DW/0412/25", "Sunaina Mehta", "2025-09-13", "31", "Homemaker", "Sector 12, Dwarka, New Delhi", wife, "W/o Rohit Mehta", "9811234522"),
        witness("witness_statement_26.pdf", "WS/DW/0412/26", "Alok Srivastava", "2025-09-14", "44", "Insurance surveyor and loss assessor", "Office 14, Sector 6 market, Dwarka, New Delhi", surveyor, "R. N. Srivastava", "9810775600"),
        witness("witness_statement_27.pdf", "WS/DW/0412/27", "Dr. Kavya Menon", "2025-09-15", "33", "Physiotherapist, Venkateshwar Hospital", "Venkateshwar Hospital, Sector 18A, Dwarka, New Delhi", physio, "P. Menon", "9810775611"),
        witness("witness_statement_28.pdf", "WS/DW/0412/28", "Mahesh Sharma", "2025-09-15", "41", "Sub-Inspector, Dwarka Sector 23 Police Station", "Dwarka Sector 23 Police Station, New Delhi", antecedents, "Late Ram Swaroop", "9810775622"),
        witness("witness_statement_29.pdf", "WS/DW/0412/29", "Jaswant Singh", "2025-09-16", "49", "Nodal Officer, NHAI regional office, Delhi", "NHAI Regional Office, Dwarka Sector 10, New Delhi", fastag, "Late Kartar Singh", "9810775633"),
        witness("witness_statement_30.pdf", "WS/DW/0412/30", "Om Parkash", "2025-09-10", "61", "Farmer", "Village Dubaldhan, District Jhajjar, Haryana", father, "Late Chandgi Ram", "9416775644"),
        witness("witness_statement_14.pdf", "WS/DW/0412/14", "Dinesh Kumar", "2025-09-12", "49", "Head Constable, MHC(M), Dwarka Sector 23 Police Station", "Dwarka Sector 23 Police Station, New Delhi", malkhana, "Late Sukhbir Singh", "9810443300"),
        DemoDocument(
            "medical_report.pdf", "MedicalReport", "MLC/VH/2025/5127", "MEDICO-LEGAL EXAMINATION REPORT (MLC)",
            {"report_number": "MLC/VH/2025/5127", "report_date": "2025-09-03", "patient_name": "Rohit Mehta", "doctor_name": "Dr. Meera Iyer",
             "hospital_name": "Venkateshwar Hospital, Dwarka, New Delhi", "age": "34", "gender": "Male",
             "observations": [
                 "Fracture of the shaft of the right femur",
                 "Scalp laceration 5 cm over the right parietal region",
                 "Patient conscious and oriented, admitted to the orthopaedic ward, condition stable",
                 "Abrasions 6 cm x 3 cm over the right elbow and 4 cm x 3 cm over the right knee",
                 "CT head: no intracranial bleed; no skull fracture",
                 "Blood alcohol nil",
             ],
             "opinion_text": "The injuries are grievous in nature (fracture). The patient is alive and under treatment."},
            [("Time of arrival", "11:45 pm"), ("Brought by", "CATS ambulance")],
        ),
        DemoDocument(
            "medical_report_discharge.pdf", "MedicalReport", "VH/DS/2025/3381", "DISCHARGE SUMMARY",
            {"report_number": "VH/DS/2025/3381", "report_date": "2025-09-11", "patient_name": "Rohit Mehta", "doctor_name": "Dr. Meera Iyer",
             "hospital_name": "Venkateshwar Hospital, Dwarka, New Delhi", "age": "34", "gender": "Male",
             "observations": [
                 "Closed intramedullary nailing of the right femur performed; post-operative X-ray satisfactory",
                 "Scalp wound sutured and healing well",
                 "Mobilised with a walker, non-weight bearing on the right leg",
                 "Discharged in stable condition; review after two weeks; physiotherapy for three months",
             ],
             "opinion_text": "Grievous injury (fracture of the femur). The patient is alive, stable and recovering; unable to follow ordinary pursuits for more than twenty days."},
        ),
        DemoDocument(
            "spot_panchnama.pdf", "SpotPanchnama", "SP/DW/0143/2025", "SPOT INSPECTION MEMO (PANCHNAMA)",
            {"memo_number": "SP/DW/0143/2025", "inspection_datetime": "2025-09-04T00:30:00+05:30", "location": "Najafgarh Road, near Uttam Nagar East Metro Station, New Delhi",
             "observations": [
                 "Skid marks about 12 metres long were found on the road surface",
                 "Broken pieces of a motorcycle headlight were found near the divider",
                 "A broken piece of white plastic bumper and headlamp glass of a car were found in the left lane",
                 "Scrape marks about 4 metres long ran along the left lane towards the bus stop",
                 "The road is a six-lane divided road with working street lights and a bus stop on the left side",
             ],
             "witnesses": []},
        ),
        DemoDocument(
            "site_plan.pdf", "SitePlan", "SPL/DW/0412/2025", "SITE PLAN OF THE PLACE OF OCCURRENCE",
            {"plan_number": "SPL/DW/0412/2025", "plan_date": "2025-09-05", "location": PLACE, "prepared_by": IO_NAME,
             "annotations": [
                 "Point A: point of impact in the left lane, 20 metres before the bus stop near Dwarka Mor Metro Station",
                 "Point B: resting position of the red motorcycle, 9 metres beyond Point A",
                 "Point C: place where the injured was found, near the bus stop",
                 "Point D: position of the DTC bus being overtaken by the car",
                 "Point E: paan shop of the witness Sanjay Kumar",
                 "Point F: DMRC camera DMRC-DM-EXT-04 on the station building",
                 "Arrow: direction of escape of the car towards Najafgarh",
             ]},
        ),
        DemoDocument(
            "seizure_memo_spot.pdf", "SeizureMemo", "SM/DW/0201/2025", "SEIZURE MEMO - EXHIBITS FROM THE SPOT",
            {"memo_number": "SM/DW/0201/2025", "seizure_datetime": "2025-09-04T01:10:00+05:30", "seizure_location": PLACE, "prepared_by": IO_NAME,
             "seized_items": [
                 {"description": "Broken piece of white plastic bumper of a car", "exhibit_mark": "EX-1"},
                 {"description": "Fragments of car headlamp glass", "exhibit_mark": "EX-2"},
                 {"description": "Broken pieces of the tail light and rear mudguard of the motorcycle", "exhibit_mark": "EX-3"},
                 {"description": "White paint chips lifted from the rear mudguard of the motorcycle and from the road", "exhibit_mark": "EX-4"},
             ],
             "witnesses": "HC Ajay Kumar; Gurpreet Singh"},
        ),
        DemoDocument(
            "seizure_memo_motorcycle.pdf", "SeizureMemo", "SM/DW/0202/2025", "SEIZURE MEMO - MOTORCYCLE AND HELMET OF THE INJURED",
            {"memo_number": "SM/DW/0202/2025", "seizure_datetime": "2025-09-04T02:00:00+05:30", "seizure_location": PLACE, "prepared_by": IO_NAME,
             "seized_items": [
                 {"description": f"Red Hero Glamour motorcycle {BIKE} of the injured, rear portion damaged", "exhibit_mark": "EX-5"},
                 {"description": "Helmet of the injured, scraped on the right side", "exhibit_mark": "EX-6"},
             ],
             "witnesses": "HC Ajay Kumar; Gurpreet Singh"},
        ),
        DemoDocument(
            "seizure_memo_cctv.pdf", "SeizureMemo", "SM/DW/0205/2025", "SEIZURE MEMO - ELECTRONIC RECORDS",
            {"memo_number": "SM/DW/0205/2025", "seizure_datetime": "2025-09-07T15:00:00+05:30", "seizure_location": "Dwarka Sector 23 Police Station, New Delhi", "prepared_by": IO_NAME,
             "seized_items": [
                 {"description": "Pen drive with the DMRC camera DMRC-DM-EXT-04 recording", "exhibit_mark": "EX-7"},
                 {"description": "Pen drive with the petrol pump camera recording from Sector 10 Road", "exhibit_mark": "EX-8"},
                 {"description": "Pen drive with the Yadav Motor Works workshop camera recording", "exhibit_mark": "EX-9"},
             ],
             "witnesses": "Rajiv Saxena; Mukesh Yadav"},
        ),
        DemoDocument(
            "vehicle_inspection.pdf", "VehicleInspection", "VI/DW/0211/2025", "MOTOR VEHICLE INSPECTION REPORT",
            {"report_number": "VI/DW/0211/2025", "inspection_date": "2025-09-05", "vehicle_registration": "UP16BK3305", "inspected_by": "Motor Vehicle Inspector, Dwarka",
             "observations": ["Front bumper and bonnet are damaged", "Paint transfer consistent with a red motorcycle was found on the bumper"]},
        ),
        DemoDocument(
            "vehicle_inspection_motorcycle.pdf", "VehicleInspection", "VI/DW/0212/2025", "MOTOR VEHICLE INSPECTION REPORT - MOTORCYCLE OF THE INJURED",
            {"report_number": "VI/DW/0212/2025", "inspection_date": "2025-09-05", "vehicle_registration": BIKE, "inspected_by": "Motor Vehicle Inspector, Dwarka",
             "observations": [
                 "Red Hero Glamour motorcycle, registered owner Rohit Mehta",
                 "Rear mudguard, tail light, number plate and grab rail broken; rear wheel rim bent",
                 "White paint transfer on the rear mudguard and the left side of the grab rail",
                 "Left side of the fuel tank, handlebar and foot-rest scraped from the fall",
                 "Brakes, lights and steering were in working order before the accident; damage is fresh and caused by an impact from behind",
             ]},
        ),
        DemoDocument(
            "cctv_metro.pdf", "CCTVMetadata", "DMRC-DM-EXT-04", "CCTV FOOTAGE ANALYSIS - DMRC CAMERA, DWARKA MOR",
            {"camera_identifier": "DMRC-DM-EXT-04", "recording_datetime": "2025-09-03T23:10:00+05:30",
             "location": "Dwarka Mor Metro Station, facing Sector 10 Road, New Delhi", "duration_seconds": 1800,
             "metadata_text": (
                 "External camera on the station building covering Sector 10 Road and the bus stop. A DTC bus slows near the bus stop. A white hatchback "
                 "overtakes the bus at high speed from the right, cuts into the left lane and strikes a red motorcycle from behind. The rider is thrown "
                 "onto the road near the bus stop and the car continues towards Najafgarh without braking. The registration number is not readable "
                 "because of headlight glare."
             )},
        ),
        DemoDocument(
            "cctv_petrol_pump.pdf", "CCTVMetadata", "IOCL-S10-02", "CCTV FOOTAGE ANALYSIS - PETROL PUMP, SECTOR 10 ROAD",
            {"camera_identifier": "IOCL-S10-02", "recording_datetime": "2025-09-03T23:08:00+05:30",
             "location": "Indian Oil petrol pump on Sector 10 Road, 400 metres before Dwarka Mor Metro Station, New Delhi", "duration_seconds": 600,
             "metadata_text": (
                 f"Camera covering the forecourt and the road. A white Maruti Swift passes at high speed towards Dwarka Mor; the registration {CAR} is "
                 "readable in one frame after enhancement and only the driver is seen in the car. Its front bumper is intact at this point."
             )},
        ),
        DemoDocument(
            "cctv_banquet_gate.pdf", "CCTVMetadata", "SB-GATE-02", "CCTV FOOTAGE ANALYSIS - SHAGUN BANQUETS BACK GATE, SECTOR 10",
            {"camera_identifier": "SB-GATE-02", "recording_datetime": "2025-09-03T22:40:00+05:30",
             "location": "Shagun Banquets back gate, Sector 10, near Sector 10 Road, Dwarka, New Delhi", "duration_seconds": 900,
             "metadata_text": (
                 f"Gate camera of the banquet hall. At 22:40 a Maruti Swift {CAR} of white colour arrives with only the driver in it; its front bumper "
                 "and both headlights are intact. A man of about 30 years in a light blue shirt unloads two boxes and gets a paper signed by the manager. "
                 "At 22:52 he drives out alone towards the main Sector 10 Road, in the direction of Dwarka Mor."
             )},
        ),
        DemoDocument(
            "cctv_workshop.pdf", "CCTVMetadata", "YMW-CAM-01", "CCTV FOOTAGE ANALYSIS - YADAV MOTOR WORKS, NAJAFGARH ROAD",
            {"camera_identifier": "YMW-CAM-01", "recording_datetime": "2025-09-04T08:40:00+05:30",
             "location": "Yadav Motor Works, Najafgarh Road, near Sector 10 Road, Dwarka, New Delhi", "duration_seconds": 1500,
             "metadata_text": (
                 f"Workshop camera. A white Maruti Swift {CAR} enters with its left front bumper broken and the left headlight smashed. A man of about "
                 "30 years in a light blue shirt gets out and talks to the workshop owner, takes a phone call and drives away hurriedly about twenty minutes later."
             )},
        ),
        DemoDocument(
            "case_diary.pdf", "CaseDiary", "CD/DW/0412/2025", "CASE DIARY (Section 192 BNSS)",
            {"diary_number": "CD/DW/0412/2025", "officer_name": IO_NAME,
             "entries": [
                 {"entry_number": "1", "entry_datetime": "2025-09-03T23:40:00+05:30", "text": "DD No. 7-A was received from the PCR about a road crash near the Dwarka Mor metro station bus stop in which a car had struck a motorcyclist and fled. I reached the spot with Constable Sunil, where PCR Van D-21 was present. The injured had already been removed to Venkateshwar Hospital by CATS ambulance. The cab driver Gurpreet Singh gave the registration number of the car, which he had followed for some distance, and it was flashed to all pickets and PCR vans of the district and to Najafgarh."},
                 {"entry_number": "2", "entry_datetime": "2025-09-04T00:30:00+05:30", "text": "The spot was inspected under street lights. Skid marks and scrape marks in the left lane, a broken piece of a white plastic bumper and headlamp glass of a car, and pieces of the tail light and rear mudguard of the motorcycle were found. The inspection memo was prepared. Panch witnesses were not available at that hour; the bus crew and the cab driver had left their numbers."},
                 {"entry_number": "3", "entry_datetime": "2025-09-04T01:10:00+05:30", "text": "The exhibits from the spot were lifted and sealed, and the red motorcycle of the injured and his helmet were seized under separate memos in the presence of HC Ajay Kumar and Gurpreet Singh. The mobile forensic team photographed the scene and lifted paint chips from the rear mudguard of the motorcycle and from the road. The motorcycle was taken to the police station yard."},
                 {"entry_number": "4", "entry_datetime": "2025-09-04T02:30:00+05:30", "text": "At Venkateshwar Hospital the MLC of the injured Rohit Mehta was obtained, showing a closed fracture of the right femur and a scalp laceration, with no alcohol in his blood. He was conscious but was being prepared for surgery and was declared unfit for statement. His brother Anil Mehta was present at the hospital."},
                 {"entry_number": "5", "entry_datetime": "2025-09-04T10:00:00+05:30", "text": "FIR No. 0412/2025 was registered under Sections 281 and 125 BNS on the written complaint of Anil Mehta, brother of the injured, who named Vikas Malhotra as the owner of the car. Statements of Gurpreet Singh, Priya Nair, HC Ajay Kumar and Constable Rakesh were recorded. The DTC depot was contacted and the crew of route 764 were called."},
                 {"entry_number": "6", "entry_datetime": "2025-09-04T16:00:00+05:30", "text": "The statements of the DTC bus driver Ramkaran and the conductor Satpal were recorded; both describe the car overtaking the bus at high speed, cutting into the left lane and striking the motorcycle from behind. The transport department record showed the car registered to Vikas Malhotra of Sector 19, Dwarka. His house was visited; he stated that the car was with his driver Vikram Sethi that night."},
                 {"entry_number": "7", "entry_datetime": "2025-09-05T12:00:00+05:30", "text": "The statements of Vikas Malhotra and of his godown supervisor Pawan Kumar were recorded and the papers of the car were taken on record. The supervisor stated that Vikram Sethi left alone in the car to deliver crockery in Sector 10 and has not returned. The statement of the CATS ambulance technician was recorded. The site plan was prepared."},
                 {"entry_number": "8", "entry_datetime": "2025-09-05T17:00:00+05:30", "text": "The vehicle inspection reports were received. The report on the motorcycle of the injured shows fresh rear damage with white paint transfer. The other report, VI/DW/0211/2025, has been prepared for a different vehicle and must be re-done once the Swift is recovered."},
                 {"entry_number": "9", "entry_datetime": "2025-09-06T12:00:00+05:30", "text": "On information, Yadav Motor Works on Najafgarh Road was visited. The owner Mukesh Yadav stated that a man calling himself Vicky had brought the damaged Swift for repair in the morning and left in a hurry after a phone call. The rented room of Vikram Sethi in Kakrola was found locked; the statement of the landlord Harbans Lal was recorded and a copy of the rent agreement was taken."},
                 {"entry_number": "10", "entry_datetime": "2025-09-06T17:00:00+05:30", "text": "Shagun Banquets in Sector 10 was visited. The manager Arun Khanna produced the delivery challan signed by him for the crockery delivered by Vikram Sethi and the gate camera recording, which shows the Swift arriving undamaged and leaving alone with the driver shortly before the crash. The statement of the neighbouring shopkeeper Manpreet Kaur was recorded about the victim closing his shop and leaving normally on his motorcycle."},
                 {"entry_number": "11", "entry_datetime": "2025-09-07T15:00:00+05:30", "text": "Recordings of the DMRC camera at Dwarka Mor, the petrol pump camera on Sector 10 Road and the workshop camera were collected with Section 63 certificates and seized. The petrol pump recording shows the registration of the Swift and only the driver in it. Statements of the DMRC Station Controller and the petrol pump manager were recorded."},
                 {"entry_number": "12", "entry_datetime": "2025-09-08T12:00:00+05:30", "text": "The supplementary statement of the complainant Anil Mehta was recorded; he clarified that he named the owner only because of the website record and did not see who was driving. The photograph of Vikram Sethi obtained from the godown was shown to Mukesh Yadav, who said that the man resembles him."},
                 {"entry_number": "13", "entry_datetime": "2025-09-08T16:00:00+05:30", "text": "The registration records of the Swift and of the motorcycle of the injured, and the driving licence record of Vikram Sethi, were obtained from the Motor Licensing Office, Dwarka, and the statement of the dealing assistant Sudesh Kumari was recorded. The insurer of the Swift was informed so that the claim of the injured before the Claims Tribunal can proceed."},
                 {"entry_number": "14", "entry_datetime": "2025-09-09T12:00:00+05:30", "text": "The paint chips and the plastic and glass pieces were sent to FSL Rohini through Constable Sunil for comparison with the paint of the car. The laboratory has asked for a control sample from the car itself, which can be taken only after the car is recovered. The report is awaited."},
                 {"entry_number": "15", "entry_datetime": "2025-09-10T12:00:00+05:30", "text": "With the help of SI Balwan Singh of PS Beri, a raid was conducted at the native village of Vikram Sethi in District Jhajjar, Haryana. His family stated that he had left for Punjab. The car was not found. A watch has been kept through the local police."},
                 {"entry_number": "16", "entry_datetime": "2025-09-10T18:00:00+05:30", "text": "The statement of Dr. Meera Iyer was recorded about the grievous nature of the injuries and the surgery performed. She confirmed that the injuries are consistent with an impact from behind on a motorcycle followed by a fall."},
                 {"entry_number": "17", "entry_datetime": "2025-09-11T12:00:00+05:30", "text": "The call detail records of Vikram Sethi's number were obtained from Reliance Jio; they place him in the Dwarka Mor area at the relevant time and near Najafgarh afterwards. His number has been switched off since the next morning. The discharge summary of the injured was obtained."},
                 {"entry_number": "18", "entry_datetime": "2025-09-12T12:00:00+05:30", "text": "The injured Rohit Mehta was examined at his home after discharge and his statement was recorded; he could not see the number of the car or the driver. The statement of the MHC(M) was recorded about the custody of the exhibits."},
                 {"entry_number": "19", "entry_datetime": "2025-09-12T16:00:00+05:30", "text": "On scrutiny of the file it was found that the statement of Sanjay Kumar bears a date earlier than the crash and gives a morning time, which conflicts with all other evidence. He has been called to have his statement re-recorded and the discrepancy explained."},
                 {"entry_number": "20", "entry_datetime": "2025-09-13T12:00:00+05:30", "text": "It was also found that the spot inspection memo records a place on Najafgarh Road near Uttam Nagar East instead of Sector 10 Road near Dwarka Mor. The memo is to be corrected after re-inspecting the spot with independent witnesses."},
                 {"entry_number": "21", "entry_datetime": "2025-09-14T12:00:00+05:30", "text": "An application for issue of non-bailable warrants against Vikram Sethi was moved in the court. A lookout notice for the Swift was sent to all districts and to the neighbouring states through the criminal records office."},
                 {"entry_number": "22", "entry_datetime": "2025-09-13T17:00:00+05:30", "text": "The statement of Sunaina Mehta, wife of the injured, was recorded about his condition, the expenses incurred and the loss of income of the family. Copies of the hospital and pharmacy bills were taken on record for the compensation application."},
                 {"entry_number": "23", "entry_datetime": "2025-09-14T12:00:00+05:30", "text": "The motorcycle of the injured was examined by the insurance surveyor Alok Srivastava in the police station yard. He found white paint transfer at the height of a hatchback bumper and damage caused by a forceful impact from directly behind. His statement and a copy of his report were taken on record."},
                 {"entry_number": "24", "entry_datetime": "2025-09-14T17:00:00+05:30", "text": "The detailed road-crash report was prepared and sent to the Claims Tribunal and to the insurer as required under the Motor Vehicles Act, with copies of the FIR, the MLC, the site plan and the registration records. A copy was given to the injured. Information about the case was also given to the District Legal Services Authority for interim compensation to the injured."},
                 {"entry_number": "25", "entry_datetime": "2025-09-15T09:00:00+05:30", "text": "The workshops, parking lots and used-car dealers of Najafgarh, Uttam Nagar and Bahadurgarh were checked for the Swift without result. The FASTag and toll records of the car were requested from the National Highways Authority to trace its movement after the crash."},
                 {"entry_number": "26", "entry_datetime": "2025-09-15T10:30:00+05:30", "text": "The antecedents of Vikram Sethi were verified by SI Mahesh Sharma: one earlier rash-driving case at PS Bahadurgarh and three over-speeding e-challans in Delhi were found. The records were placed on file. The statement of the physiotherapist Dr. Kavya Menon was recorded about the continuing disability of the injured."},
                 {"entry_number": "27", "entry_datetime": "2025-09-15T11:00:00+05:30", "text": "The court issued non-bailable warrants against Vikram Sethi, which were sent for execution at his addresses in Kakrola and in District Jhajjar. If he is not found, proceedings for his proclamation under Section 84 BNSS will be moved."},
                 {"entry_number": "28", "entry_datetime": "2025-09-15T12:00:00+05:30", "text": "Pending: arrest of Vikram Sethi, recovery and mechanical inspection of the Swift, FSL comparison report, re-recording of the statement of Sanjay Kumar, and correction of the inspection memo. The draft charge sheet cannot be finalized until these are completed."},
             ]},
        ),
    ]


def finish(storage_root, review_service_cls, correction_request_cls, add_note_request_cls, decision_request_cls) -> None:
    review_service_cls(storage_root).add_note(
        CASE_ID,
        add_note_request_cls(
            author_id=IO_ID,
            author_name=IO_NAME,
            note_text=(
                "Accused Vikram Sethi is not yet arrested, the Swift is not recovered and the FSL report is awaited. Statement date, "
                "vehicle number and spot location need to be reconciled before this can go forward."
            ),
        ),
    )


CASE = DemoCase(CASE_ID, TITLE, STATION, documents, finish)
