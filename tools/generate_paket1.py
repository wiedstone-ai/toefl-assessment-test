# -*- coding: utf-8 -*-
"""
Generator for bank-paket1.js (140 Authentic TOEFL ITP Questions for Paket 1 - CEFR B1)
"""
import json

def make_js_file():
    questions = []

    # =========================================================================
    # SECTION 1: LISTENING COMPREHENSION (50 Questions)
    # =========================================================================
    
    # --- PART A: Short Conversations (Questions 1 - 30) ---
    part_a_data = [
        (1, "man", "Did you manage to submit the physics lab report before noon?",
            "woman", "I barely made it to the professor's office on time.",
            "What does the woman mean?",
            [("A", "She was unable to hand in the report."),
             ("B", "She submitted the report just in time."),
             ("C", "The professor was absent from his office."),
             ("D", "She decided to delay submitting the report.")],
            "B",
            "Ekspresi 'barely made it on time' bermakna nyaris terlambat namun akhirnya berhasil menyerahkan tepat pada waktunya."),
            
        (2, "woman", "The air conditioner in the computer room is making a strange rattling sound.",
            "man", "I'll call the maintenance technician right away.",
            "What will the man probably do next?",
            [("A", "Turn off all the computers in the room."),
             ("B", "Ignore the sound until tomorrow."),
             ("C", "Contact someone to repair the equipment."),
             ("D", "Buy a new air conditioning unit.")],
            "C",
            "Pria menyatakan akan segera menghubungi teknisi pemeliharaan ('call the maintenance technician right away')."),
            
        (3, "man", "Are you going to the campus career seminar this afternoon?",
            "woman", "I wouldn't miss it for the world! Several major engineering companies will be there.",
            "What does the woman imply?",
            [("A", "She is definitely planning to attend the seminar."),
             ("B", "She is too busy to travel to the campus."),
             ("C", "She is uninterested in engineering careers."),
             ("D", "She thinks the seminar has been canceled.")],
            "A",
            "Idiom 'I wouldn't miss it for the world' menyatakan tekad kuat bahwa ia pasti akan hadir."),

        (4, "woman", "I heard that the final exam for English literature was postponed.",
            "man", "You can say that again! Everyone in our class was relieved.",
            "What does the man mean?",
            [("A", "He wants the woman to repeat what she said."),
             ("B", "He completely agrees with the woman's statement."),
             ("C", "He is disappointed about the postponement."),
             ("D", "He did not hear about the schedule change.")],
            "B",
            "Ungkapan 'You can say that again' merupakan ekspresi persetujuan penuh (agreement)."),

        (5, "man", "Could you lend me your dictionary for the vocabulary test?",
            "woman", "If I had it with me, I certainly would, but I left it in my locker.",
            "What does the woman imply?",
            [("A", "She does not want to lend her dictionary."),
             ("B", "She does not own an English dictionary."),
             ("C", "She cannot lend it because she doesn't have it right now."),
             ("D", "She will buy a new dictionary after class.")],
            "C",
            "Kalimat pengandaian tipe 2 ('If I had it... I certainly would, but I left it in my locker') menunjukkan ia tidak membawanya."),

        (6, "woman", "Professor Miller spoke so softly during the lecture that I missed half of his notes.",
            "man", "Next time, let's sit in the front row instead of the back.",
            "What does the man suggest?",
            [("A", "Asking the professor to speak more loudly."),
             ("B", "Changing their seating position in the classroom."),
             ("C", "Borrowing notes from another classmate."),
             ("D", "Skipping the professor's next lecture.")],
            "B",
            "Pria menyarankan: 'let's sit in the front row instead of the back' (duduk di baris depan)."),

        (7, "man", "Do you know where I can purchase replacement fuses for this electric circuit?",
            "woman", "There is a hardware store just across the street from the bus terminal.",
            "What does the woman tell the man?",
            [("A", "The terminal does not sell electrical parts."),
             ("B", "A store selling hardware is located nearby."),
             ("C", "He should take a bus to another town."),
             ("D", "The circuit cannot be repaired with new fuses.")],
            "B",
            "Wanita menginformasikan adanya toko perkakas di seberang terminal bus."),

        (8, "woman", "Mark looks exhausted today. Did he stay up late finishing his project?",
            "man", "He was working in the machine shop until two in the morning.",
            "What does the man say about Mark?",
            [("A", "He went to bed very early last night."),
             ("B", "He spent most of the night working."),
             ("C", "He forgot to complete his shop assignment."),
             ("D", "He decided to quit his machine project.")],
            "B",
            "Pria menjelaskan Mark bekerja di bengkel mesin hingga pukul dua pagi ('until two in the morning')."),

        (9, "man", "Should we take the highway to the national library or take the city bypass?",
            "woman", "Traffic is bumper to bumper on the highway at this hour.",
            "What does the woman imply?",
            [("A", "The highway is currently clear and fast."),
             ("B", "They should take the city bypass to avoid traffic."),
             ("C", "The national library is already closed."),
             ("D", "They should walk to the library together.")],
            "B",
            "Ungkapan 'bumper to bumper' berarti macet parah di jalan tol, menyiratkan sebaiknya lewat jalur lingkar."),

        (10, "woman", "I didn't expect the renewable energy presentation to be so interesting.",
             "man", "Neither did I! The speaker explained solar cells very clearly.",
             "What does the man mean?",
             [("A", "He found the presentation boring."),
              ("B", "He also found the presentation surprisingly engaging."),
              ("C", "He was unable to attend the speaker's presentation."),
              ("D", "He disagrees with the speaker's ideas on solar cells.")],
             "B",
             "'Neither did I' menunjukkan pria tersebut juga sebelumnya tidak mengira presentasi akan semenarik itu."),

        (11, "man", "Excuse me, does this train stop at the industrial technology park?",
             "woman", "No, this is an express train. You'll need to transfer at Central Station.",
             "What must the man do to reach his destination?",
             [("A", "Stay on the train until the final stop."),
              ("B", "Change trains at Central Station."),
              ("C", "Purchase a different ticket immediately."),
              ("D", "Take a taxi from the current station.")],
             "B",
             "Wanita menyatakan: 'You'll need to transfer at Central Station' (pindah kereta di Stasiun Pusat)."),

        (12, "woman", "Can you believe that the registration deadline is already tomorrow?",
             "man", "I know. It completely slipped my mind until you reminded me.",
             "What does the man mean?",
             [("A", "He had completely forgotten about the deadline."),
              ("B", "He already registered two days ago."),
              ("C", "He does not intend to register for the course."),
              ("D", "He remembered the deadline on his own.")],
             "A",
             "Idiom 'It completely slipped my mind' berarti ia benar-benar lupa sampai diingatkan."),

        (13, "man", "Is Sarah still thinking about applying for the automotive apprenticeship in Germany?",
             "woman", "Her application has already been accepted!",
             "What does the woman say about Sarah?",
             [("A", "She decided not to go to Germany."),
              ("B", "She was successfully admitted to the program."),
              ("C", "She is still preparing her application documents."),
              ("D", "Her application was turned down by the company.")],
             "B",
             "Wanita menegaskan bahwa lamaran Sarah sudah diterima ('has already been accepted')."),

        (14, "woman", "I'm having a hard time understanding how this hydraulic valve functions.",
             "man", "Why not check the instructional video posted on the school portal?",
             "What suggestion does the man give to the woman?",
             [("A", "Ask the teacher to replace the valve."),
              ("B", "Watch an online video tutorial about the device."),
              ("C", "Read the entire textbook from the beginning."),
              ("D", "Attempt to disassemble the valve herself.")],
             "B",
             "Pria menyarankan: 'Why not check the instructional video posted on the school portal?'"),

        (15, "man", "Did you get a chance to read the article about artificial intelligence in manufacturing?",
             "woman", "I only glanced at the headline, but I plan to read it tonight.",
             "What does the woman mean?",
             [("A", "She read the entire article thoroughly."),
              ("B", "She has not yet read the full content of the article."),
              ("C", "She lost the magazine containing the article."),
              ("D", "She thinks the article is poorly written.")],
             "B",
             "Wanita baru melihat sekilas judulnya ('only glanced at the headline') dan baru berencana membaca nanti malam."),

        (16, "woman", "How did your group presentation on environmental protection go?",
             "man", "It couldn't have gone better. The judges praised our research data.",
             "What does the man imply about the presentation?",
             [("A", "It was extremely successful."),
              ("B", "The judges criticized their research methods."),
              ("C", "The group was unprepared for the questions."),
              ("D", "It went worse than expected.")],
             "A",
             "Ungkapan 'It couldn't have gone better' adalah ungkapan bahwa hasilnya sangat memuaskan/sukses."),

        (17, "man", "I'm looking for the department chair's office. Is it on this floor?",
             "woman", "Go down the hallway and take the stairs to the third floor. It's the first door on your left.",
             "Where is the department chair's office located?",
             [("A", "On the ground floor near the entrance."),
              ("B", "On the third floor down the hallway."),
              ("C", "Directly opposite the current classroom."),
              ("D", "In the basement adjacent to the laboratory.")],
             "B",
             "Wanita mengarahkan: 'take the stairs to the third floor. It's the first door on your left'."),

        (18, "woman", "The weather forecast said it would rain heavily all afternoon.",
             "man", "Well, the sky looks completely clear to me.",
             "What does the man imply?",
             [("A", "He thinks the weather forecast may be inaccurate."),
              ("B", "He wants to bring an umbrella just in case."),
              ("C", "He is waiting for the rain to begin."),
              ("D", "He forgot to check the morning forecast.")],
             "A",
             "Pria melihat langit cerah, menyiratkan bahwa ramalan cuaca kemungkinan meleset."),

        (19, "man", "Are you ready to begin the welding test, or do you need a few more minutes?",
             "woman", "I've inspected my protective helmet and gloves. I'm all set.",
             "What does the woman mean?",
             [("A", "She needs to borrow safety equipment."),
              ("B", "She is fully prepared to start the test."),
              ("C", "She feels nervous about using the welding machine."),
              ("D", "She would prefer to postpone the test until later.")],
             "B",
             "Ungkapan 'I'm all set' berarti sudah siap sepenuhnya setelah memeriksa peralatan pelindung."),

        (20, "woman", "I thought Dave was going to help us clean up the chemistry laboratory.",
             "man", "He had an urgent family emergency to take care of.",
             "Why was Dave unable to help?",
             [("A", "He refused to participate in cleaning the lab."),
              ("B", "He had an unexpected personal matter to attend to."),
              ("C", "He fell ill during the chemistry experiment."),
              ("D", "He forgot which day the cleanup was scheduled.")],
             "B",
             "Pria menjelaskan Dave memiliki urusan keluarga darurat yang harus diselesaikan ('urgent family emergency')."),

        (21, "man", "The cafeteria is serving vegetable soup and grilled chicken today.",
             "woman", "Sounds good, but I packed my own sandwich this morning.",
             "What will the woman probably do for lunch?",
             [("A", "Buy lunch at the school cafeteria."),
              ("B", "Eat the sandwich she brought from home."),
              ("C", "Skip lunch to study in the library."),
              ("D", "Share the cafeteria meal with the man.")],
             "B",
             "Wanita membawa bekal sandwich sendiri dari rumah ('packed my own sandwich this morning')."),

        (22, "woman", "Do you mind if I borrow your scientific calculator until fifth period?",
             "man", "Not at all. I don't have math class until tomorrow morning.",
             "What does the man mean?",
             [("A", "He needs his calculator right now."),
              ("B", "He is willing to let the woman use his calculator."),
              ("C", "He lost his calculator earlier today."),
              ("D", "He will help the woman solve math problems.")],
             "B",
             "'Not at all' bermakna ia sama sekali tidak keberatan meminjamkannya."),

        (23, "man", "Has the teacher assigned the topics for our history research paper?",
             "woman", "Not yet. She said she would hand out the list during the next session.",
             "What does the woman say about the research topics?",
             [("A", "Students have already selected their topics."),
              ("B", "The teacher will distribute the topics in the next class."),
              ("C", "The research assignment has been canceled."),
              ("D", "Students must choose topics without teacher guidance.")],
             "B",
             "Wanita menyatakan guru akan membagikan daftar topik pada pertemuan berikutnya."),

        (24, "woman", "I didn't realize that the bus fare had increased by fifty cents.",
             "man", "Neither did I until the driver pointed at the new rate sign.",
             "What did both speakers learn?",
             [("A", "The bus schedule has been altered."),
              ("B", "The price of bus transportation has gone up."),
              ("C", "The bus driver was unfamiliar with the route."),
              ("D", "The bus stops have been relocated.")],
             "B",
             "Kedua pembicara baru menyadari bahwa tarif bus telah naik ('bus fare had increased')."),

        (25, "man", "I'm really struggling to finish this technical drawing project by Friday.",
             "woman", "If you break it down into smaller steps, it won't seem so overwhelming.",
             "What advice does the woman give to the man?",
             [("A", "Ask for an extension on the project deadline."),
              ("B", "Divide the work into manageable portions."),
              ("C", "Hire a professional to complete the drawing."),
              ("D", "Work through the night without taking breaks.")],
             "B",
             "Wanita menyarankan membagi tugas menjadi langkah-langkah kecil ('break it down into smaller steps')."),

        (26, "woman", "Did you know that the campus bookstore is offering a twenty percent discount on engineering tools?",
             "man", "Really? I'd better hurry over there before supplies run out.",
             "What does the man plan to do?",
             [("A", "Wait until next week to buy tools."),
              ("B", "Go quickly to the bookstore to make a purchase."),
              ("C", "Sell his old engineering tools to classmates."),
              ("D", "Ask for a larger discount on books.")],
             "B",
             "Pria menyatakan harus bergegas ke toko buku ('hurry over there before supplies run out')."),

        (27, "man", "I can't seem to open this compressed archive file on my laptop.",
             "woman", "You might need to download a special decompression utility program first.",
             "What does the woman suggest the man do?",
             [("A", "Delete the file from his hard drive."),
              ("B", "Install software designed to extract the archive."),
              ("C", "Purchase a brand new laptop computer."),
              ("D", "Send the file to another recipient.")],
             "B",
             "Wanita menyarankan mengunduh program utilitas dekompresi file."),

        (28, "woman", "Is it true that Mr. Henderson has been teaching at this vocational school for twenty-five years?",
             "man", "Yes, he's the most senior instructor in our mechanical division.",
             "What does the man confirm about Mr. Henderson?",
             [("A", "He recently joined the teaching staff."),
              ("B", "He has extensive teaching experience at the school."),
              ("C", "He teaches in the electrical division."),
              ("D", "He plans to retire at the end of the semester.")],
             "B",
             "Pria mengonfirmasi bahwa Mr. Henderson adalah instruktur paling senior (mengajar selama 25 tahun)."),

        (29, "man", "Should we practice our English presentation one more time before lunch?",
             "woman", "Let's grab a bite to eat first. We can rehearse when our energy is back.",
             "What does the woman want to do first?",
             [("A", "Eat a meal before practicing again."),
              ("B", "Present their project immediately."),
              ("C", "Cancel the presentation entirely."),
              ("D", "Practice without taking any lunch break.")],
             "A",
             "Wanita mengajak makan siang terlebih dahulu ('Let's grab a bite to eat first')."),

        (30, "woman", "I'm afraid I won't be able to finish this wiring schematic before 3 PM.",
             "man", "Don't panic. The instructor said we can continue it during tomorrow's practical session.",
             "What does the man tell the woman?",
             [("A", "She will be penalized for incomplete work."),
              ("B", "She will have additional time in the next class."),
              ("C", "She must finish the schematic at home tonight."),
              ("D", "The instructor will finish the wiring for her.")],
             "B",
             "Pria menenangkan bahwa mereka bisa melanjutkannya pada sesi praktik besok.")
    ]

    for item in part_a_data:
        qid, s1_role, s1_text, s2_role, s2_text, prompt, opts, key, expl = item
        questions.append({
            "id": qid,
            "section": 1,
            "sectionName": "Section 1: Listening Comprehension",
            "part": "Part A: Short Conversations",
            "type": "listening_dialog",
            "audioSegments": [
                {"role": "narrator", "text": f"Number {qid}. Listen to a short conversation between two speakers.", "pauseAfter": 350},
                {"role": s1_role, "text": s1_text, "pauseAfter": 300},
                {"role": s2_role, "text": s2_text, "pauseAfter": 400},
                {"role": "narrator", "text": f"Question: {prompt}", "pauseAfter": 300}
            ],
            "audioScript": f"Speaker 1 ({s1_role}): {s1_text}\nSpeaker 2 ({s2_role}): {s2_text}\nQuestion: {prompt}",
            "prompt": prompt,
            "options": [{"key": k, "text": txt} for k, txt in opts],
            "correctAnswer": key,
            "explanation": expl
        })

    # --- PART B: Longer Conversations (Questions 31 - 38) ---
    # Conversation 1 (Q31 - Q34)
    c1_dialog = [
        {"role": "narrator", "text": "Questions 31 through 34. Listen to a conversation between two students discussing their vocational internship.", "pauseAfter": 450},
        {"role": "man", "text": "Hi Lisa, have you decided where you want to do your four-month industrial internship next term?", "pauseAfter": 300},
        {"role": "woman", "text": "Yes, David. I just received approval from a renewable energy plant near the coastal harbor.", "pauseAfter": 300},
        {"role": "man", "text": "That's fantastic! What specific department will you be working in?", "pauseAfter": 300},
        {"role": "woman", "text": "I'll be assisting electrical technicians in maintaining high-capacity solar inverters and wind turbine generators. It's directly related to our power engineering coursework.", "pauseAfter": 350},
        {"role": "man", "text": "Are they providing safety training before you enter the generator facility?", "pauseAfter": 300},
        {"role": "woman", "text": "Definitely. During the first two weeks, all interns must complete an intensive safety certification course and learn how to use digital circuit diagnostic equipment.", "pauseAfter": 400}
    ]
    c1_script = "David (Man): Hi Lisa, have you decided where you want to do your four-month industrial internship next term?\nLisa (Woman): Yes, David. I just received approval from a renewable energy plant near the coastal harbor.\nDavid: That's fantastic! What specific department will you be working in?\nLisa: I'll be assisting electrical technicians in maintaining high-capacity solar inverters and wind turbine generators. It's directly related to our power engineering coursework.\nDavid: Are they providing safety training before you enter the generator facility?\nLisa: Definitely. During the first two weeks, all interns must complete an intensive safety certification course and learn how to use digital circuit diagnostic equipment."

    c1_questions = [
        (31, "What is the primary topic of the conversation?",
         [("A", "Preparing for a final written examination."),
          ("B", "Arrangements for a vocational industrial internship."),
          ("C", "Purchasing electrical equipment for the school."),
          ("D", "Building a miniature wind turbine model.")],
         "B", "Percakapan berfokus pada rencana dan persetujuan tempat magang industri (vocational industrial internship)."),

        (32, "Where will the woman be doing her internship?",
         [("A", "At a local automotive assembly plant."),
          ("B", "At a renewable energy power station."),
          ("C", "In a university chemistry research lab."),
          ("D", "At a municipal water filtration facility.")],
         "B", "Wanita menyatakan ia diterima di 'renewable energy plant near the coastal harbor'."),

        (33, "What will be one of the woman's main responsibilities?",
         [("A", "Designing commercial marketing brochures."),
          ("B", "Assisting technicians with generator maintenance."),
          ("C", "Supervising newly hired office clerks."),
          ("D", "Teaching physics classes to junior students.")],
         "B", "Tugas utamanya adalah membantu teknisi dalam pemeliharaan inverter surya dan generator turbin angin."),

        (34, "What must the interns do during their first two weeks?",
         [("A", "Travel to another province for field study."),
          ("B", "Complete a safety certification course."),
          ("C", "Take a final theoretical examination."),
          ("D", "Purchase their own personal tools.")],
         "B", "Siswa magang wajib menyelesaikan kursus sertifikasi keselamatan ('intensive safety certification course').")
    ]

    for qid, prompt, opts, key, expl in c1_questions:
        q_audio = list(c1_dialog)
        q_audio.append({"role": "narrator", "text": f"Question {qid}: {prompt}", "pauseAfter": 300})
        questions.append({
            "id": qid,
            "section": 1,
            "sectionName": "Section 1: Listening Comprehension",
            "part": "Part B: Longer Conversations",
            "type": "listening_long_dialog",
            "audioSegments": q_audio,
            "audioScript": c1_script + f"\n\nQuestion {qid}: {prompt}",
            "prompt": prompt,
            "options": [{"key": k, "text": txt} for k, txt in opts],
            "correctAnswer": key,
            "explanation": expl
        })

    # Conversation 2 (Q35 - Q38)
    c2_dialog = [
        {"role": "narrator", "text": "Questions 35 through 38. Listen to a conversation between two vocational students in an architectural studio.", "pauseAfter": 450},
        {"role": "woman", "text": "Tom, did you finish rendering the 3D model of the school auditorium on the computer?", "pauseAfter": 300},
        {"role": "man", "text": "Almost. I just need to adjust the natural lighting angles coming through the eastern glass windows.", "pauseAfter": 300},
        {"role": "woman", "text": "Good idea. Mr. Hendra emphasized that passive solar lighting can significantly reduce electricity consumption during daytime events.", "pauseAfter": 350},
        {"role": "man", "text": "Exactly. I'm also adding rooftop ventilation louvers to improve airflow without relying entirely on mechanical air conditioning.", "pauseAfter": 350},
        {"role": "woman", "text": "When we present our blueprints on Friday, let's make sure to highlight those eco-friendly architectural features.", "pauseAfter": 400}
    ]
    c2_script = "Woman: Tom, did you finish rendering the 3D model of the school auditorium on the computer?\nTom (Man): Almost. I just need to adjust the natural lighting angles coming through the eastern glass windows.\nWoman: Good idea. Mr. Hendra emphasized that passive solar lighting can significantly reduce electricity consumption during daytime events.\nTom: Exactly. I'm also adding rooftop ventilation louvers to improve airflow without relying entirely on mechanical air conditioning.\nWoman: When we present our blueprints on Friday, let's make sure to highlight those eco-friendly architectural features."

    c2_questions = [
        (35, "What project are the students collaborating on?",
         [("A", "Building an actual brick wall outside."),
          ("B", "Creating a 3D architectural model of an auditorium."),
          ("C", "Repairing broken lighting fixtures in the hallway."),
          ("D", "Drafting an electrical wiring diagram for a house.")],
         "B", "Keduanya sedang mengerjakan pemodelan 3D arsitektural gedung auditorium sekolah."),

        (36, "What adjustment is the man making to the model?",
         [("A", "Changing the color of the stage curtains."),
          ("B", "Modifying natural lighting angles through windows."),
          ("C", "Removing the eastern entrance door."),
          ("D", "Increasing the total seating capacity.")],
         "B", "Pria menyatakan sedang mengatur sudut pencahayaan alami melalui jendela kaca timur."),

        (37, "Why did the instructor emphasize passive solar lighting?",
         [("A", "To make the building look more modern."),
          ("B", "To reduce daytime electricity usage."),
          ("C", "To prevent rain from entering the hall."),
          ("D", "To block sunlight completely.")],
         "B", "Pencahayaan surya pasif dapat mengurangi konsumsi listrik di siang hari ('reduce electricity consumption')."),

        (38, "When will the students present their architectural blueprints?",
         [("A", "Later this afternoon."),
          ("B", "Tomorrow morning at eight."),
          ("C", "On Friday."),
          ("D", "Next month.")],
         "C", "Wanita menyebutkan presentasi cetak biru akan dilakukan pada hari Jumat ('present our blueprints on Friday').")
    ]

    for qid, prompt, opts, key, expl in c2_questions:
        q_audio = list(c2_dialog)
        q_audio.append({"role": "narrator", "text": f"Question {qid}: {prompt}", "pauseAfter": 300})
        questions.append({
            "id": qid,
            "section": 1,
            "sectionName": "Section 1: Listening Comprehension",
            "part": "Part B: Longer Conversations",
            "type": "listening_long_dialog",
            "audioSegments": q_audio,
            "audioScript": c2_script + f"\n\nQuestion {qid}: {prompt}",
            "prompt": prompt,
            "options": [{"key": k, "text": txt} for k, txt in opts],
            "correctAnswer": key,
            "explanation": expl
        })

    # --- PART C: Talks / Mini Lectures (Questions 39 - 50) ---
    # Talk 1: Geothermal Energy (Q39 - Q42)
    t1_dialog = [
        {"role": "narrator", "text": "Questions 39 through 42. Listen to an instructor giving a talk on renewable energy.", "pauseAfter": 450},
        {"role": "man", "text": "Good morning, class. Today we will explore geothermal energy, which harnesses the intense heat stored deep within the Earth's crust. In active volcanic regions such as the Pacific Ring of Fire, underground water comes into contact with superheated magma rocks. This water turns into high-pressure steam. Power engineers drill deep production wells to bring this steam to the surface, where it drives massive turbine generators to produce clean electricity. Because geothermal plants emit almost zero greenhouse gases and operate continuously regardless of rain or calm winds, they offer reliable baseload power for national electrical grids.", "pauseAfter": 450}
    ]
    t1_script = "Instructor (Man): Good morning, class. Today we will explore geothermal energy, which harnesses the intense heat stored deep within the Earth's crust. In active volcanic regions such as the Pacific Ring of Fire, underground water comes into contact with superheated magma rocks. This water turns into high-pressure steam. Power engineers drill deep production wells to bring this steam to the surface, where it drives massive turbine generators to produce clean electricity. Because geothermal plants emit almost zero greenhouse gases and operate continuously regardless of rain or calm winds, they offer reliable baseload power for national electrical grids."

    t1_questions = [
        (39, "What is the main topic of the instructor's talk?",
         [("A", "The history of coal mining."),
          ("B", "Harnessing geothermal energy for electricity."),
          ("C", "Predicting volcanic eruptions accurately."),
          ("D", "Methods for cleaning contaminated river water.")],
         "B", "Topik utama kuliah singkat adalah pemanfaatan energi panas bumi (geothermal energy) untuk pembangkit listrik."),

        (40, "Where does natural geothermal steam originate?",
         [("A", "From boiling ocean water on coastal beaches."),
          ("B", "From underground water heated by magma rocks."),
          ("C", "From artificial furnaces installed in deep caves."),
          ("D", "From chemical reactions in surface soil layers.")],
         "B", "Uap panas bumi terbentuk saat air bawah tanah bersentuhan dengan batuan magma yang sangat panas."),

        (41, "What mechanical device converts steam energy into electricity?",
         [("A", "Hydraulic water valves."),
          ("B", "Turbine generators."),
          ("C", "Solar inverter panels."),
          ("D", "Centrifugal cooling fans.")],
         "B", "Uap bertekanan tinggi menggerakkan generator turbin ('turbine generators') untuk menghasilkan listrik."),

        (42, "Why is geothermal power considered a reliable baseload energy source?",
         [("A", "It operates continuously regardless of weather conditions."),
          ("B", "It is cheaper than all other fuels to construct initially."),
          ("C", "It requires no maintenance or human supervision."),
          ("D", "It can be installed anywhere without geological surveys.")],
         "A", "Pembangkit panas bumi beroperasi terus-menerus tanpa bergantung pada cuaca hujan atau angin tenang.")
    ]

    for qid, prompt, opts, key, expl in t1_questions:
        q_audio = list(t1_dialog)
        q_audio.append({"role": "narrator", "text": f"Question {qid}: {prompt}", "pauseAfter": 300})
        questions.append({
            "id": qid,
            "section": 1,
            "sectionName": "Section 1: Listening Comprehension",
            "part": "Part C: Talks",
            "type": "listening_talk",
            "audioSegments": q_audio,
            "audioScript": t1_script + f"\n\nQuestion {qid}: {prompt}",
            "prompt": prompt,
            "options": [{"key": k, "text": txt} for k, txt in opts],
            "correctAnswer": key,
            "explanation": expl
        })

    # Talk 2: The Evolution of Bridges (Q43 - Q46)
    t2_dialog = [
        {"role": "narrator", "text": "Questions 43 through 46. Listen to a lecture in a civil engineering course.", "pauseAfter": 450},
        {"role": "woman", "text": "Throughout human history, bridge engineering has evolved alongside advancements in building materials. Ancient Roman builders relied on the stone arch, which distributes compressive weight downward onto sturdy abutments. However, stone was too heavy and brittle for very long spans. During the Industrial Era of the nineteenth century, the development of inexpensive wrought iron and structural steel allowed engineers to build suspension bridges. By suspending the roadway from flexible steel cables anchored into bedrock, modern bridges can span broad rivers and ocean straits over two kilometers wide while flexing safely against strong wind gusts.", "pauseAfter": 450}
    ]
    t2_script = "Lecturer (Woman): Throughout human history, bridge engineering has evolved alongside advancements in building materials. Ancient Roman builders relied on the stone arch, which distributes compressive weight downward onto sturdy abutments. However, stone was too heavy and brittle for very long spans. During the Industrial Era of the nineteenth century, the development of inexpensive wrought iron and structural steel allowed engineers to build suspension bridges. By suspending the roadway from flexible steel cables anchored into bedrock, modern bridges can span broad rivers and ocean straits over two kilometers wide while flexing safely against strong wind gusts."

    t2_questions = [
        (43, "What is the primary focus of the lecture?",
         [("A", "The architectural design of Roman amphitheaters."),
          ("B", "The historical evolution of bridge engineering materials."),
          ("C", "Environmental damage caused by river dredging."),
          ("D", "Manufacturing techniques for concrete road barriers.")],
         "B", "Fokus utama kuliah adalah evolusi historis teknik jembatan dan material bangunannya."),

        (44, "What structural feature characterized ancient Roman bridges?",
         [("A", "Flexible steel wire cables."),
          ("B", "The stone arch distributing compressive weight."),
          ("C", "Pneumatic air cushions beneath piers."),
          ("D", "Lightweight aluminum trusses.")],
         "B", "Jembatan Romawi kuno mengandalkan lengkungan batu (stone arch) yang mendistribusikan beban tekan ke bawah."),

        (45, "What material innovation enabled the construction of suspension bridges?",
         [("A", "Reinforced clay bricks."),
          ("B", "Inexpensive structural steel and iron cables."),
          ("C", "Treated waterproof timber logs."),
          ("D", "Hardened volcanic basalt blocks.")],
         "B", "Pengembangan baja struktural dan kabel besi memungkinkan pembangunan jembatan gantung bentang panjang."),

        (46, "How do modern suspension bridges withstand heavy wind gusts?",
         [("A", "By remaining completely rigid without any movement."),
          ("B", "By flexing safely through engineered cable tension."),
          ("C", "By closing wind shutters during stormy days."),
          ("D", "By sinking their roadways closer to the water level.")],
         "B", "Kabel baja yang fleksibel memungkinkan jembatan melengkung/bergerak secara aman terhadap terpaan angin kencang.")
    ]

    for qid, prompt, opts, key, expl in t2_questions:
        q_audio = list(t2_dialog)
        q_audio.append({"role": "narrator", "text": f"Question {qid}: {prompt}", "pauseAfter": 300})
        questions.append({
            "id": qid,
            "section": 1,
            "sectionName": "Section 1: Listening Comprehension",
            "part": "Part C: Talks",
            "type": "listening_talk",
            "audioSegments": q_audio,
            "audioScript": t2_script + f"\n\nQuestion {qid}: {prompt}",
            "prompt": prompt,
            "options": [{"key": k, "text": txt} for k, txt in opts],
            "correctAnswer": key,
            "explanation": expl
        })

    # Talk 3: Honeybee Communication (Q47 - Q50)
    t3_dialog = [
        {"role": "narrator", "text": "Questions 47 through 50. Listen to a biology talk about animal behavior.", "pauseAfter": 450},
        {"role": "man", "text": "In the 1940s, Austrian zoologist Karl von Frisch decoded one of nature's most sophisticated communication systems: the honeybee waggle dance. When a foraging bee discovers a rich patch of nectar flowers, she returns to the hive and performs a figure-eight dance on the vertical honeycomb. The angle at which she dances relative to gravity indicates the exact direction of the flowers relative to the sun. Furthermore, the duration of the central waggle run signals the distance to the food source. One second of waggling corresponds to approximately one kilometer of flight distance. Through this symbolic dance, hundreds of sister bees locate flowers with remarkable precision.", "pauseAfter": 450}
    ]
    t3_script = "Speaker (Man): In the 1940s, Austrian zoologist Karl von Frisch decoded one of nature's most sophisticated communication systems: the honeybee waggle dance. When a foraging bee discovers a rich patch of nectar flowers, she returns to the hive and performs a figure-eight dance on the vertical honeycomb. The angle at which she dances relative to gravity indicates the exact direction of the flowers relative to the sun. Furthermore, the duration of the central waggle run signals the distance to the food source. One second of waggling corresponds to approximately one kilometer of flight distance. Through this symbolic dance, hundreds of sister bees locate flowers with remarkable precision."

    t3_questions = [
        (47, "What remarkable animal behavior is described in the talk?",
         [("A", "How honeybees construct hexagonal comb cells."),
          ("B", "The honeybee waggle dance communication system."),
          ("C", "How queen bees maintain order in the colony."),
          ("D", "The chemical synthesis of flower nectar into honey.")],
         "B", "Ceramah mendeskripsikan tarian komunikasi lebah madu ('waggle dance')."),

        (48, "What does the angle of the bee's dance indicate?",
         [("A", "The quality and sweetness of the nectar."),
          ("B", "The direction of the food source relative to the sun."),
          ("C", "The presence of dangerous predators nearby."),
          ("D", "The temperature inside the wooden hive.")],
         "B", "Sudut tarian lebah terhadap gravitasi menunjukkan arah sumber makanan relatif terhadap matahari."),

        (49, "How do bees convey the distance to the flowers?",
         [("A", "By vibrating their wings at varying frequencies."),
          ("B", "Through the duration of the central waggle run."),
          ("C", "By touching antennae with other worker bees."),
          ("D", "By releasing specific floral pheromone scents.")],
         "B", "Durasi getaran (waggle run) menandakan jarak ke sumber bunga (1 detik melambangkan sekitar 1 km)."),

        (50, "Approximately what distance does one second of waggling represent?",
         [("A", "One hundred meters."),
          ("B", "One kilometer."),
          ("C", "Five kilometers."),
          ("D", "Ten kilometers.")],
         "B", "Disebutkan dalam teks: 'One second of waggling corresponds to approximately one kilometer'.")
    ]

    for qid, prompt, opts, key, expl in t3_questions:
        q_audio = list(t3_dialog)
        q_audio.append({"role": "narrator", "text": f"Question {qid}: {prompt}", "pauseAfter": 300})
        questions.append({
            "id": qid,
            "section": 1,
            "sectionName": "Section 1: Listening Comprehension",
            "part": "Part C: Talks",
            "type": "listening_talk",
            "audioSegments": q_audio,
            "audioScript": t3_script + f"\n\nQuestion {qid}: {prompt}",
            "prompt": prompt,
            "options": [{"key": k, "text": txt} for k, txt in opts],
            "correctAnswer": key,
            "explanation": expl
        })

    # =========================================================================
    # SECTION 2: STRUCTURE & WRITTEN EXPRESSION (40 Questions)
    # =========================================================================
    
    # --- PART A: Sentence Completion (Questions 51 - 65) ---
    part_a_struct = [
        (51, "The giant panda, native to the bamboo forests of central China, ________ largely on bamboo shoots for its daily nutrition.",
         [("A", "depend"), ("B", "depends"), ("C", "is depended"), ("D", "depending")],
         "B", "Subjek tunggal 'The giant panda' memerlukan kata kerja tunggal (singular verb) 'depends' dalam present tense."),

        (52, "________ by strong magnetic fields, plasma can be safely contained inside experimental nuclear fusion reactors.",
         [("A", "It is guided"), ("B", "Guided"), ("C", "Guiding"), ("D", "When it is")],
         "B", "Bentuk reduced passive participle ('Guided by strong magnetic fields...') menerangkan subjek 'plasma'."),

        (53, "Not only ________ renewable energy, but modern wind farms also create high-skilled maintenance jobs.",
         [("A", "wind turbines produce"), ("B", "do wind turbines produce"), ("C", "producing wind turbines"), ("D", "wind turbines are produced")],
         "B", "Klausa diawali ekspresi negatif 'Not only', sehingga memerlukan pola inversi (Auxiliary + Subject + Verb): 'do wind turbines produce'."),

        (54, "Thomas Edison, ________ invented the phonograph, established one of the world's first industrial research laboratories.",
         [("A", "who"), ("B", "whom"), ("C", "whose"), ("D", "which")],
         "A", "Relative pronoun 'who' digunakan sebagai subjek dalam adjective clause yang menerangkan orang ('Thomas Edison')."),

        (55, "A laser beam differs from ordinary light in that ________ coherent and consists of waves of a single wavelength.",
         [("A", "is"), ("B", "it is"), ("C", "being"), ("D", "it has")],
         "B", "Frasa 'in that' berfungsi sebagai konjungsi subordinatif yang membutuhkan klausa lengkap (Subject + Verb): 'it is'."),

        (56, "Seldom ________ a solar eclipse visible from the same geographic location twice within a single decade.",
         [("A", "is"), ("B", "it is"), ("C", "does"), ("D", "being")],
         "A", "Adverb negatif 'Seldom' di awal kalimat memicu inversi to be + subjek: 'is a solar eclipse visible'."),

        (57, "________ the atmospheric pressure drops rapidly, meteorologists usually predict a severe incoming storm.",
         [("A", "Because"), ("B", "When"), ("C", "During"), ("D", "Despite")],
         "B", "Konjungsi 'When' menyatakan hubungan waktu logis ketika tekanan atmosfer turun drastis."),

        (58, "The Brooklyn Bridge, ________ in 1883, was the longest suspension bridge in the world at the time of its completion.",
         [("A", "completed"), ("B", "it was completed"), ("C", "completing"), ("D", "was completed")],
         "A", "Appositive phrase memerlukan bentuk past participle pasif 'completed in 1883' tanpa menambahkan subjek berulang."),

        (59, "Neither the laboratory supervisor nor the apprentice technicians ________ aware of the short circuit in the fuse box.",
         [("A", "was"), ("B", "were"), ("C", "is"), ("D", "being")],
         "B", "Dalam aturan 'Neither... nor...', kata kerja disesuaikan dengan subjek terdekat ('the apprentice technicians' = jamak), sehingga memakai 'were'."),

        (60, "Fiber optic cables transmit digital communication signals much faster than ________ copper telephone wires.",
         [("A", "do"), ("B", "they"), ("C", "is"), ("D", "are")],
         "A", "Inversi perbandingan (comparative clause inversion) menggunakan auxiliary verb 'do' yang menggantikan kata kerja 'transmit'."),

        (61, "Automotive engineers test new vehicle engines thoroughly ________ ensure optimal fuel economy and low emissions.",
         [("A", "so that"), ("B", "in order to"), ("C", "because of"), ("D", "such as")],
         "B", "Frasa 'in order to' diikuti bare infinitive ('ensure') untuk menyatakan tujuan (purpose)."),

        (62, "The deeper an ocean trench is, ________ the hydrostatic pressure exerted on deep-sea exploratory submersibles.",
         [("A", "greatest"), ("B", "greater"), ("C", "the greater"), ("D", "the greatest")],
         "C", "Pola paralel komparatif ganda (double comparative): 'The deeper..., the greater...'."),

        (63, "Only after completing rigorous safety training ________ permitted to operate the Computer Numerical Control milling machine.",
         [("A", "students are"), ("B", "are students"), ("C", "do students"), ("D", "students have")],
         "B", "Ekspresi restriktif 'Only after...' di awal kalimat memerlukan inversi to be + subjek pasif: 'are students permitted'."),

        (64, "Geothermal energy is a sustainable power resource, ________ emits virtually no sulfur dioxide during electricity production.",
         [("A", "which"), ("B", "what"), ("C", "who"), ("D", "where")],
         "A", "Non-defining relative clause menerangkan benda ('geothermal energy') menggunakan relative pronoun 'which'."),

        (65, "Before the widespread adoption of electronic microchips, computers ________ immense rooms and consumed excessive power.",
         [("A", "occupied"), ("B", "occupying"), ("C", "were occupied"), ("D", "occupy")],
         "A", "Konteks kalimat lampau ('Before...') membutuhkan kata kerja past tense aktif: 'occupied' (menempati).")
    ]

    for qid, prompt, opts, key, expl in part_a_struct:
        questions.append({
            "id": qid,
            "section": 2,
            "sectionName": "Section 2: Structure and Written Expression",
            "part": "Part A: Incomplete Sentences",
            "type": "structure_sentence",
            "prompt": prompt,
            "options": [{"key": k, "text": txt} for k, txt in opts],
            "correctAnswer": key,
            "explanation": expl
        })

    # --- PART B: Written Expression / Error Identification (Questions 66 - 90) ---
    # Represented with clear HTML spans for underlined A, B, C, D
    part_b_struct = [
        (66, "The <span class='toefl-err' data-opt='A'>collection</span> of ancient technical manuscripts <span class='toefl-err' data-opt='B'>were</span> carefully <span class='toefl-err' data-opt='C'>preserved</span> by the museum <span class='toefl-err' data-opt='D'>curator</span>.",
         "B", "Subjek inti adalah 'The collection' (tunggal), sehingga kata kerja to be seharusnya adalah 'was', bukan 'were'."),

        (67, "Solar panels <span class='toefl-err' data-opt='A'>absorb</span> sunlight and <span class='toefl-err' data-opt='B'>direct</span> convert <span class='toefl-err' data-opt='C'>it</span> into clean electrical <span class='toefl-err' data-opt='D'>power</span>.",
         "B", "Kata yang memodifikasi kata kerja 'convert' harus berupa kata keterangan (adverb) 'directly', bukan adjective 'direct'."),

        (68, "Each <span class='toefl-err' data-opt='A'>of the</span> hydraulic <span class='toefl-err' data-opt='B'>machines</span> in the workshop <span class='toefl-err' data-opt='C'>require</span> regular lubrication <span class='toefl-err' data-opt='D'>to prevent</span> friction.",
         "C", "Frasa 'Each of the...' memiliki subjek tunggal 'Each', sehingga predikat kata kerjanya harus berakhiran -s: 'requires'."),

        (69, "The industrial robot can <span class='toefl-err' data-opt='A'>assemble</span> engine parts <span class='toefl-err' data-opt='B'>quick</span>, accurately, and <span class='toefl-err' data-opt='C'>without</span> making <span class='toefl-err' data-opt='D'>errors</span>.",
         "B", "Paralelisme adverb: 'quick' harus diubah menjadi bentuk adverb 'quickly' agar setara dengan 'accurately'."),

        (70, "Despite <span class='toefl-err' data-opt='A'>it was</span> raining heavily, the civil engineering team <span class='toefl-err' data-opt='B'>continued</span> laying the concrete <span class='toefl-err' data-opt='C'>foundation</span> for the <span class='toefl-err' data-opt='D'>bridge</span>.",
         "A", "Preposisi 'Despite' diikuti noun phrase, bukan klausa subjek-predikat. Seharusnya menggunakan 'Although it was' atau 'Despite the heavy rain'."),

        (71, "A <span class='toefl-err' data-opt='A'>number</span> of international <span class='toefl-err' data-opt='B'>scholarships</span> is <span class='toefl-err' data-opt='C'>available</span> for talented vocational school <span class='toefl-err' data-opt='D'>graduates</span>.",
         "C", "Ekspresi 'A number of + plural noun' dianggap jamak, sehingga to be yang benar adalah 'are available', bukan 'is'."),

        (72, "Electrical wires <span class='toefl-err' data-opt='A'>made of</span> copper <span class='toefl-err' data-opt='B'>conducts</span> electricity much <span class='toefl-err' data-opt='C'>better</span> than wires made <span class='toefl-err' data-opt='D'>of aluminum</span>.",
         "B", "Subjek kalimat adalah 'Electrical wires' (jamak), sehingga kata kerjanya adalah 'conduct' tanpa akhiran -s."),

        (73, "The apprentice <span class='toefl-err' data-opt='A'>spent</span> three hours <span class='toefl-err' data-opt='B'>to repair</span> the damaged transmission gears <span class='toefl-err' data-opt='C'>in the</span> automotive <span class='toefl-err' data-opt='D'>garage</span>.",
         "B", "Pola kata kerja 'spend + time' diikuti gerund (-ing): 'spent three hours repairing', bukan infinitive 'to repair'."),

        (74, "Neither the architect <span class='toefl-err' data-opt='A'>or</span> the structural engineer <span class='toefl-err' data-opt='B'>expected</span> the bedrock <span class='toefl-err' data-opt='C'>to be</span> so close to the ground <span class='toefl-err' data-opt='D'>surface</span>.",
         "A", "Pasangan konjungsi korelatif untuk 'Neither' adalah 'nor', bukan 'or'."),

        (75, "Modern automated factories <span class='toefl-err' data-opt='A'>utilize</span> artificial intelligence <span class='toefl-err' data-opt='B'>for inspect</span> finished products <span class='toefl-err' data-opt='C'>for</span> microscopic <span class='toefl-err' data-opt='D'>defects</span>.",
         "B", "Setelah preposisi 'for' harus digunakan gerund (-ing): 'for inspecting', atau 'to inspect'."),

        (76, "Light travels <span class='toefl-err' data-opt='A'>significant</span> <span class='toefl-err' data-opt='B'>faster</span> in a vacuum <span class='toefl-err' data-opt='C'>than</span> it does through glass <span class='toefl-err' data-opt='D'>or water</span>.",
         "A", "Kata sifat komparatif 'faster' harus dimodifikasi oleh adverb 'significantly', bukan adjective 'significant'."),

        (77, "The <span class='toefl-err' data-opt='A'>newly</span> installed cooling system <span class='toefl-err' data-opt='B'>functions</span> smooth, maintaining an <span class='toefl-err' data-opt='C'>even</span> temperature <span class='toefl-err' data-opt='D'>throughout</span> the building.",
         "B", "Kata kerja 'functions' harus dimodifikasi oleh adverb: 'smoothly', bukan adjective 'smooth'."),

        (78, "There <span class='toefl-err' data-opt='A'>are</span> very <span class='toefl-err' data-opt='B'>little</span> information available <span class='toefl-err' data-opt='C'>regarding</span> the prehistoric <span class='toefl-err' data-opt='D'>settlement</span>.",
         "A", "Kata 'information' adalah uncountable noun (tunggal), sehingga kata kerja seharusnya 'is' (dan memakai 'little information')."),

        (79, "Before submitting <span class='toefl-err' data-opt='A'>the blueprint</span>, the student <span class='toefl-err' data-opt='B'>must to double-check</span> all dimensional <span class='toefl-err' data-opt='C'>calculations</span> for <span class='toefl-err' data-opt='D'>accuracy</span>.",
         "B", "Modal auxiliary 'must' harus langsung diikuti bare infinitive: 'must double-check' tanpa 'to'."),

        (80, "The greenhouse gases <span class='toefl-err' data-opt='A'>emitting</span> by gasoline vehicles <span class='toefl-err' data-opt='B'>contribute</span> directly <span class='toefl-err' data-opt='C'>to air pollution</span> in dense <span class='toefl-err' data-opt='D'>urban areas</span>.",
         "A", "Gas rumah kaca dipancarkan/dilepaskan (makna pasif), sehingga bentuk participle yang benar adalah past participle 'emitted', bukan 'emitting'."),

        (81, "During the storm, <span class='toefl-err' data-opt='A'>several</span> telephone poles were <span class='toefl-err' data-opt='B'>blow down</span> by the <span class='toefl-err' data-opt='C'>intense</span> ocean <span class='toefl-err' data-opt='D'>winds</span>.",
         "B", "Bentuk pasif 'were + V3': kata kerja bentuk ketiga dari 'blow' adalah 'blown down', bukan 'blow down'."),

        (82, "The committee <span class='toefl-err' data-opt='A'>has decided</span> to postpone the <span class='toefl-err' data-opt='B'>decide</span> until further geological data <span class='toefl-err' data-opt='C'>can be</span> properly <span class='toefl-err' data-opt='D'>collected</span>.",
         "B", "Setelah artikel 'the', kata yang dibutuhkan adalah noun 'decision', bukan verb 'decide'."),

        (83, "Biologists have discovered that <span class='toefl-err' data-opt='A'>some</span> species of bats <span class='toefl-err' data-opt='B'>navigates</span> through total darkness <span class='toefl-err' data-opt='C'>using</span> high-frequency sound <span class='toefl-err' data-opt='D'>echoes</span>.",
         "B", "Subjek klausa adalah 'some species of bats' (jamak), sehingga kata kerjanya adalah 'navigate' tanpa akhiran -s."),

        (84, "The supervisor praised the interns for <span class='toefl-err' data-opt='A'>theirs</span> exceptional dedication and <span class='toefl-err' data-opt='B'>punctual</span> attendance <span class='toefl-err' data-opt='C'>during</span> the training <span class='toefl-err' data-opt='D'>period</span>.",
         "A", "Sebelum noun phrase 'exceptional dedication', kata ganti kepemilikan yang tepat adalah possessive adjective 'their', bukan possessive pronoun 'theirs'."),

        (85, "Titanium is <span class='toefl-err' data-opt='A'>widely used</span> in aerospace manufacturing <span class='toefl-err' data-opt='B'>because</span> its light weight, <span class='toefl-err' data-opt='C'>high strength</span>, and resistance to <span class='toefl-err' data-opt='D'>corrosion</span>.",
         "B", "Frasa setelahnya adalah noun phrase ('its light weight...'), sehingga harus menggunakan preposisi 'because of', bukan konjungsi 'because'."),

        (86, "The instructor explained <span class='toefl-err' data-opt='A'>how</span> the internal combustion engine <span class='toefl-err' data-opt='B'>operates</span> and <span class='toefl-err' data-opt='C'>its</span> importance to modern <span class='toefl-err' data-opt='D'>transport</span>.",
         "C", "Paralelisme klausa: 'explained how the engine operates and why it is important', atau jika menggunakan noun phrase harus setara."),

        (87, "Almost <span class='toefl-err' data-opt='A'>all</span> living organisms <span class='toefl-err' data-opt='B'>depends</span> on liquid water <span class='toefl-err' data-opt='C'>to sustain</span> their biological <span class='toefl-err' data-opt='D'>processes</span>.",
         "B", "Subjek 'Almost all living organisms' adalah jamak, sehingga kata kerjanya adalah 'depend' tanpa akhiran -s."),

        (88, "Geothermal power plants produce <span class='toefl-err' data-opt='A'>electricity</span> by <span class='toefl-err' data-opt='B'>convert</span> underground steam <span class='toefl-err' data-opt='C'>into</span> mechanical energy <span class='toefl-err' data-opt='D'>via turbines</span>.",
         "B", "Setelah preposisi 'by' harus digunakan gerund (-ing): 'by converting', bukan bare verb 'convert'."),

        (89, "The student was <span class='toefl-err' data-opt='A'>unable</span> to locate his safety goggles <span class='toefl-err' data-opt='B'>because</span> someone had moved <span class='toefl-err' data-opt='C'>it</span> to another <span class='toefl-err' data-opt='D'>workbench</span>.",
         "C", "Kata 'goggles' berbentuk jamak (plural noun), sehingga pronoun penggantinya harus 'them', bukan 'it'."),

        (90, "Wind turbines are <span class='toefl-err' data-opt='A'>erected</span> in open fields <span class='toefl-err' data-opt='B'>where</span> wind velocities are <span class='toefl-err' data-opt='C'>consistently</span> strong and <span class='toefl-err' data-opt='D'>predict</span>.",
         "D", "Paralelisme adjective setelah to be 'are consistently strong and...': kata 'predict' harus diubah menjadi adjective 'predictable'.")
    ]

    for qid, prompt, key, expl in part_b_struct:
        questions.append({
            "id": qid,
            "section": 2,
            "sectionName": "Section 2: Structure and Written Expression",
            "part": "Part B: Written Expression",
            "type": "structure_error",
            "prompt": prompt,
            "options": [
                {"key": "A", "text": "Underlined part (A)"},
                {"key": "B", "text": "Underlined part (B)"},
                {"key": "C", "text": "Underlined part (C)"},
                {"key": "D", "text": "Underlined part (D)"}
            ],
            "correctAnswer": key,
            "explanation": expl
        })

    # =========================================================================
    # SECTION 3: READING COMPREHENSION (50 Questions - 5 Passages @ 10 Questions)
    # =========================================================================

    # Passage 1: Geothermal Energy and Volcanic Rocks (Q91 - Q100)
    p1_title = "Passage 1: Volcanic Rocks and Geothermal Energy"
    p1_source = "Source: Adapted from Smithsonian Institution & U.S. Geological Survey"
    p1_text = """<p><span class="line-num">Line 1</span> Geothermal energy originates from the immense reservoir of heat stored within the Earth's core and mantle. In regions of active volcanism, such as tectonic plate boundaries, magma chambers rise relatively close to the surface crust. When rainwater percolates deep into permeable geological strata, it encounters these superheated rocks. Heated to temperatures exceeding two hundred degrees Celsius, the trapped water becomes pressurized steam.</p>
<p><span class="line-num">Line 7</span> To harness this underground power, geological engineers drill production wells reaching depths of two to three kilometers. The high-pressure steam rushes upward through insulated steel conduits to drive heavy turbine blades at electrical generating stations. After spinning the turbines, the residual steam passes through condenser cooling towers, where it transforms back into liquid water. Crucially, modern geothermal facilities reinject this condensed fluid back into the deep subterranean reservoir. This closed-loop circulation prevents local groundwater depletion and sustains reservoir pressure over decades of operation.</p>
<p><span class="line-num">Line 15</span> Unlike solar arrays and wind farms, which fluctuate with weather conditions and daylight hours, geothermal facilities provide continuous baseload electricity around the clock. Moreover, their physical surface footprint is remarkably compact compared to hydroelectric reservoirs or strip mines. Consequently, volcanic nations worldwide increasingly prioritize geothermal exploration as a clean, sustainable cornerstone of their national energy transition.</p>"""

    p1_questions = [
        (91, "What is the primary topic of the passage?",
         [("A", "The history of volcanic eruptions across the globe."),
          ("B", "How geothermal heat is utilized to produce sustainable electricity."),
          ("C", "The chemical composition of deep tectonic magma."),
          ("D", "Methods for drilling oil wells through bedrock.")],
         "B", "Teks secara menyeluruh membahas pemanfaatan panas bumi (geothermal heat) untuk membangkitkan listrik bersih."),

        (92, "The word 'percolates' in Line 4 is closest in meaning to:",
         [("A", "freezes rapidly"),
          ("B", "filters through slowly"),
          ("C", "evaporates upward"),
          ("D", "expands suddenly")],
         "B", "Kata 'percolates' bermakna meresap perlahan menembus lapisan batuan permeable ('filters through slowly')."),

        (93, "According to paragraph 1, high-pressure steam is formed when:",
         [("A", "magma is exposed directly to ocean air."),
          ("B", "percolating water touches superheated underground rocks."),
          ("C", "geologists pump chemical fluids into dry wells."),
          ("D", "cold winds cool the Earth's upper crust.")],
         "B", "Uap bertekanan tinggi terbentuk saat air resapan bersentuhan dengan batuan magma yang super panas."),

        (94, "The word 'harness' in Line 7 is closest in meaning to:",
         [("A", "prevent"),
          ("B", "utilize"),
          ("C", "discover"),
          ("D", "measure")],
         "B", "'Harness' bermakna memanfaatkan sumber daya ('utilize / make use of')."),

        (95, "According to paragraph 2, what happens to steam after it drives the turbines?",
         [("A", "It is released directly into the atmosphere as smog."),
          ("B", "It is condensed into water and reinjected into the ground."),
          ("C", "It is bottled and sold as mineral drinking water."),
          ("D", "It is stored in open surface reservoirs.")],
         "B", "Uap sisa diembunkan kembali menjadi air dan diinjeksikan kembali ke dalam reservoir tanah (closed-loop)."),

        (96, "The word 'it' in Line 10 refers to:",
         [("A", "production well"),
          ("B", "the residual steam"),
          ("C", "cooling tower"),
          ("D", "turbine blade")],
         "B", "Kata ganti 'it' merujuk pada 'the residual steam' yang mengembun kembali menjadi air."),

        (97, "Why do geothermal plants reinject condensed fluid back into deep reservoirs?",
         [("A", "To clean the turbine blades from soot."),
          ("B", "To maintain reservoir pressure and prevent water depletion."),
          ("C", "To extinguish active volcanic magma chambers."),
          ("D", "To cool the surrounding residential towns.")],
         "B", "Injeksi ulang bertujuan mempertahankan tekanan reservoir dan mencegah berkurangnya air tanah."),

        (98, "Which of the following is NOT mentioned as an advantage of geothermal energy?",
         [("A", "It provides constant baseload electricity day and night."),
          ("B", "It requires a comparatively small land surface footprint."),
          ("C", "It is completely immune to earthquakes and volcanic tremors."),
          ("D", "It operates independently of daily weather conditions.")],
         "C", "Teks tidak menyebutkan bahwa fasilitas panas bumi kebal terhadap gempa bumi atau getaran vulkanik."),

        (99, "The word 'compact' in Line 18 is closest in meaning to:",
         [("A", "small in area"),
          ("B", "fragile in construction"),
          ("C", "difficult to locate"),
          ("D", "expensive to maintain")],
         "A", "'Compact' berarti berukuran ringkas / tidak memakan banyak lahan ('small in area')."),

        (100, "It can be inferred from the final paragraph that volcanic nations:",
         [("A", "are phasing out geothermal plants due to high costs."),
          ("B", "possess natural geographical advantages for geothermal energy."),
          ("C", "rely exclusively on wind and solar power."),
          ("D", "face frequent fuel shortages in their cities.")],
         "B", "Dapat disimpulkan bahwa negara-negara vulkanik memiliki keuntungan geografis alami untuk memproduksi energi geotermal.")
    ]

    for qid, prompt, opts, key, expl in p1_questions:
        questions.append({
            "id": qid,
            "section": 3,
            "sectionName": "Section 3: Reading Comprehension",
            "part": "Reading: Passage 1",
            "type": "reading_passage",
            "stimulusTitle": p1_title,
            "stimulusSource": p1_source,
            "stimulusBody": p1_text,
            "prompt": prompt,
            "options": [{"key": k, "text": txt} for k, txt in opts],
            "correctAnswer": key,
            "explanation": expl
        })

    # Passage 2: Water Ice on Mars (Q101 - Q110)
    p2_title = "Passage 2: Water Ice and the Atmosphere of Mars"
    p2_source = "Source: Adapted from NASA Jet Propulsion Laboratory (JPL) Science Archives"
    p2_text = """<p><span class="line-num">Line 1</span> For decades, Mars was widely viewed as a barren, hyper-arid desert frozen in time. However, orbital radar sounding instruments and robotic rovers have fundamentally transformed our understanding of the Red Planet. Data transmitted by robotic explorers demonstrate that vast reservoirs of water ice are sequestered beneath the Martian surface and within its polar ice caps.</p>
<p><span class="line-num">Line 6</span> The atmospheric pressure on modern Mars is extraordinarily thin, averaging less than one percent of Earth's sea-level pressure. Because this tenuous carbon dioxide atmosphere cannot retain substantial solar heat, surface temperatures fluctuate wildly between minus one hundred and twenty degrees Celsius during winter nights and twenty degrees Celsius near the equator at midday. Under such low pressure, pure liquid water cannot remain stable on the surface; it boils away into vapor or freezes solid almost immediately. Nevertheless, ground-penetrating radar from the Mars Reconnaissance Orbiter has revealed extensive subsurface glaciers shielded beneath blankets of rocky debris and dust.</p>
<p><span class="line-num">Line 15</span> These buried ice deposits represent an invaluable asset for future human space exploration. If astronauts can extract this subsurface ice, it can be purified for drinking water, split into hydrogen and oxygen to manufacture rocket propellants, and utilized to sustain hydroponic greenhouses. Understanding the distribution of Martian water is therefore both a window into the planet's ancient warmer past and a stepping stone toward human colonization.</p>"""

    p2_questions = [
        (101, "What is the author's primary purpose in writing the passage?",
         [("A", "To compare the orbits of Mars and Jupiter."),
          ("B", "To discuss the discovery and significance of water ice on Mars."),
          ("C", "To prove that intelligent life exists on the Martian surface."),
          ("D", "To describe the mechanical design of NASA rocket engines.")],
         "B", "Tujuan utama teks adalah menjelaskan penemuan dan kegunaan penting lapisan es air di planet Mars."),

        (102, "The word 'barren' in Line 1 is closest in meaning to:",
         [("A", "densely populated"),
          ("B", "lifeless and unproductive"),
          ("C", "covered in oceans"),
          ("D", "tropical and humid")],
         "B", "'Barren' berarti gersang, tandus, tanpa tanda kehidupan ('lifeless and unproductive')."),

        (103, "According to paragraph 1, how did scientists confirm the existence of Martian water ice?",
         [("A", "Through orbital radar sounding and robotic rover expeditions."),
          ("B", "By observing Mars with ordinary handheld binoculars."),
          ("C", "From meteorites that fell into the Pacific Ocean."),
          ("D", "Through samples collected by human astronauts.")],
         "A", "Penemuan es air dikonfirmasi melalui instrumen radar pengorbit dan penjelajah robotik (robotic rovers)."),

        (104, "The word 'tenuous' in Line 7 is closest in meaning to:",
         [("A", "thin and weak"),
          ("B", "heavy and moist"),
          ("C", "toxic and acidic"),
          ("D", "warm and comforting")],
         "A", "'Tenuous' bermakna sangat tipis / renggang ('thin and weak')."),

        (105, "Why is liquid water unable to exist stably on the surface of Mars today?",
         [("A", "Solar radiation destroys all hydrogen molecules."),
          ("B", "The atmospheric pressure is far too low."),
          ("C", "The soil contains toxic levels of sulfuric acid."),
          ("D", "Strong winds blow the water directly into space.")],
         "B", "Tekanan atmosfer Mars yang sangat rendah menyebabkan air mendidih atau langsung membeku solid."),

        (106, "The word 'it' in Line 11 refers to:",
         [("A", "atmospheric pressure"),
          ("B", "pure liquid water"),
          ("C", "carbon dioxide"),
          ("D", "the equator")],
         "B", "Kata 'it' merujuk pada 'pure liquid water' yang tidak stabil di permukaan Mars."),

        (107, "What protects the subsurface glaciers from evaporating into the thin atmosphere?",
         [("A", "Artificial plastic shields erected by rovers."),
          ("B", "Protective blankets of rocky debris and dust."),
          ("C", "Dense clouds of carbon dioxide ice."),
          ("D", "Volcanic steam erupting from craters.")],
         "B", "Lapisan debu dan bebatuan (rocky debris and dust) melindungi gletser bawah tanah dari evaporasi."),

        (108, "The word 'asset' in Line 15 is closest in meaning to:",
         [("A", "danger"),
          ("B", "valuable resource"),
          ("C", "unknown mystery"),
          ("D", "minor problem")],
         "B", "'Asset' bermakna sumber daya yang sangat berharga / bernilai ('valuable resource')."),

        (109, "According to the passage, all of the following are potential uses of Martian ice EXCEPT:",
         [("A", "producing drinking water for astronaut crews."),
          ("B", "splitting into hydrogen and oxygen for rocket fuel."),
          ("C", "hydrating vegetables grown in hydroponic greenhouses."),
          ("D", "melting glaciers to create open commercial shipping canals.")],
         "D", "Teks tidak pernah menyebutkan pencairan gletser untuk kanal perkapalan komersial terbuka."),

        (110, "Which of the following can be inferred about Mars' past climate?",
         [("A", "It was likely warmer and had a denser atmosphere in ancient times."),
          ("B", "It has always possessed the exact atmospheric thickness it has now."),
          ("C", "It was once completely covered by boiling lava oceans."),
          ("D", "It had no water anywhere in its geological history.")],
         "A", "Keberadaan cadangan es membuktikan bahwa iklim Mars pada masa purba jauh lebih hangat dan beratmosfer tebal.")
    ]

    for qid, prompt, opts, key, expl in p2_questions:
        questions.append({
            "id": qid,
            "section": 3,
            "sectionName": "Section 3: Reading Comprehension",
            "part": "Reading: Passage 2",
            "type": "reading_passage",
            "stimulusTitle": p2_title,
            "stimulusSource": p2_source,
            "stimulusBody": p2_text,
            "prompt": prompt,
            "options": [{"key": k, "text": txt} for k, txt in opts],
            "correctAnswer": key,
            "explanation": expl
        })

    # Passage 3: Coral Reef Ecosystems (Q111 - Q120)
    p3_title = "Passage 3: Coral Reef Biodiversity and Environmental Resilience"
    p3_source = "Source: Adapted from National Geographic Society — Marine Biology Studies"
    p3_text = """<p><span class="line-num">Line 1</span> Although coral reefs occupy less than one percent of the global ocean floor, they support more than twenty-five percent of all known marine species. Often celebrated as the underwater rainforests of the planet, coral reefs are complex biological structures constructed over centuries by tiny colonial organisms called coral polyps. These soft-bodied animals secrete hard calcium carbonate exoskeletons that gradually cement together to form immense underwater ridges.</p>
<p><span class="line-num">Line 7</span> The biological engine sustaining tropical corals is a mutualistic symbiotic relationship with photosynthetic microscopic algae known as zooxanthellae. Residing within the transparent tissues of the polyps, these algae convert sunlight into vital nutrients and oxygen through photosynthesis, which nourishes the host coral. In return, the coral polyp provides the algae with a protected environment and essential chemical compounds, including carbon dioxide and phosphorus. This efficient partnership also produces the vibrant green, purple, and orange hues that characterize healthy reefs.</p>
<p><span class="line-num">Line 15</span> However, coral ecosystems are exceptionally sensitive to thermal stress. When ocean temperatures rise just one or two degrees Celsius above normal seasonal thresholds for extended durations, corals become stressed and expel their symbiotic algae. Deprived of their primary food source, the coral polyps become translucent, exposing the stark white calcium carbonate skeletons underneath in a phenomenon termed coral bleaching. If cooler water temperatures return promptly, corals can reacquire algae and recover. However, prolonged heatwaves cause mass mortality, collapsing the complex food webs that sustain coastal fisheries and shorelines.</p>"""

    p3_questions = [
        (111, "What is the central focus of the passage?",
         [("A", "The commercial harvesting of ocean fish species."),
          ("B", "The biological structure, symbiosis, and vulnerability of coral reefs."),
          ("C", "How volcanic islands form in tropical archipelagos."),
          ("D", "Methods for cultivating ornamental aquarium corals.")],
         "B", "Teks berfokus pada struktur biologis karang, hubungan simbiosisnya, dan kerentanannya terhadap pemanasan laut."),

        (112, "Why are coral reefs compared to underwater rainforests in paragraph 1?",
         [("A", "They receive heavy rainfall throughout the year."),
          ("B", "They harbor extraordinary biodiversity despite covering a small area."),
          ("C", "They are primarily composed of tall green seaweed forests."),
          ("D", "They grow exclusively along muddy freshwater river mouths.")],
         "B", "Karang diibaratkan hutan hujan karena menampung keanekaragaman hayati yang luar biasa di area yang relatif kecil."),

        (113, "What material do coral polyps secrete to construct reef ridges?",
         [("A", "Silica crystals"),
          ("B", "Calcium carbonate"),
          ("C", "Volcanic basalt"),
          ("D", "Iron oxide")],
         "B", "Polip karang mensekresikan kalsium karbonat ('calcium carbonate') untuk membentuk kerangka luar yang keras."),

        (114, "The word 'mutualistic' in Line 8 is closest in meaning to:",
         [("A", "harmful to both"),
          ("B", "mutually beneficial"),
          ("C", "one-sided and parasitic"),
          ("D", "temporary and accidental")],
         "B", "'Mutualistic' bermakna saling menguntungkan kedua belah pihak ('mutually beneficial')."),

        (115, "According to paragraph 2, what vital service do zooxanthellae algae provide to corals?",
         [("A", "They dig deep burrows into the rocky seabed."),
          ("B", "They produce nutrients and oxygen via photosynthesis."),
          ("C", "They protect the reef against heavy storm waves."),
          ("D", "They filter toxic salt particles out of seawater.")],
         "B", "Ganggang zooxanthellae menghasilkan nutrisi dan oksigen melalui fotosintesis untuk memberi makan polip karang."),

        (116, "The word 'vibrant' in Line 13 is closest in meaning to:",
         [("A", "pale and dull"),
          ("B", "bright and vivid"),
          ("C", "dangerous to touch"),
          ("D", "artificial and painted")],
         "B", "'Vibrant' berarti cerah, tajam, dan hidup ('bright and vivid')."),

        (117, "What primary trigger causes the phenomenon known as coral bleaching?",
         [("A", "Excessive deep-sea fishing trawlers."),
          ("B", "Abnormally warm ocean water temperatures."),
          ("C", "A severe decline in atmospheric oxygen levels."),
          ("D", "Rapid shifts in lunar tidal heights.")],
         "B", "Pemutihan karang dipicu oleh suhu air laut yang meningkat di atas ambang normal musiman."),

        (118, "The word 'expel' in Line 17 is closest in meaning to:",
         [("A", "eject or cast out"),
          ("B", "attract quickly"),
          ("C", "consume entirely"),
          ("D", "protect safely")],
         "A", "'Expel' bermakna mengeluarkan atau mengusir ('eject / cast out')."),

        (119, "According to the passage, why do bleached corals appear white?",
         [("A", "Their tissues become covered in thick sea salt."),
          ("B", "The white calcium carbonate skeleton becomes visible through translucent polyps."),
          ("C", "The polyps paint themselves to reflect bright solar radiation."),
          ("D", "White microscopic bacteria colonize the exterior surface.")],
         "B", "Polip menjadi transparan sehingga kerangka kalsium karbonat putih di bawahnya terlihat jelas."),

        (120, "What can be inferred about a coral reef's ability to survive a bleaching event?",
         [("A", "Corals can recover if sea temperatures return to normal quickly."),
          ("B", "Bleached corals die immediately within twenty-four hours."),
          ("C", "Bleached corals permanently lose the ability to capture food."),
          ("D", "Corals can survive only if moved to freshwater rivers.")],
         "A", "Karang dapat pulih kembali jika suhu air laut segera kembali normal dalam waktu singkat.")
    ]

    for qid, prompt, opts, key, expl in p3_questions:
        questions.append({
            "id": qid,
            "section": 3,
            "sectionName": "Section 3: Reading Comprehension",
            "part": "Reading: Passage 3",
            "type": "reading_passage",
            "stimulusTitle": p3_title,
            "stimulusSource": p3_source,
            "stimulusBody": p3_text,
            "prompt": prompt,
            "options": [{"key": k, "text": txt} for k, txt in opts],
            "correctAnswer": key,
            "explanation": expl
        })

    # Passage 4: Transcontinental Railroad (Q121 - Q130)
    p4_title = "Passage 4: The Transcontinental Railroad and Industrial Expansion"
    p4_source = "Source: Adapted from Library of Congress Historical Archives & Britannica"
    p4_text = """<p><span class="line-num">Line 1</span> Completed in May 1869 at Promontory Summit, Utah, the first Transcontinental Railroad revolutionized the economic geography of North America. Prior to the joining of the Union Pacific and Central Pacific railway lines, traveling between the East Coast and the Pacific West required a grueling six-month overland journey by horse-drawn covered wagon, or a hazardous voyage by sailing ship around Cape Horn at the stormy tip of South America.</p>
<p><span class="line-num">Line 7</span> The construction of the railroad represented a triumph of nineteenth-century civil engineering. Thousands of laborers, predominantly Chinese and Irish immigrants, endured brutal weather, sheer granite cliffs, and track-laying through mountain ranges. Workers blasted solid rock tunnels through the Sierra Nevada mountains using volatile nitroglycerin explosives, erected towering wooden trestle bridges, and laid iron rails at a breakneck pace of up to ten miles in a single day.</p>
<p><span class="line-num">Line 14</span> The socio-economic impacts of the railroad were immediate and profound. A cross-country trip that previously consumed half a year was slashed to less than a single week. Freight transportation costs plunged by ninety percent, creating an integrated national marketplace. Agricultural harvests, manufactured machinery, and cattle could be shipped swiftly between rural frontier settlements and booming industrial cities. The railroad accelerated urban development, established standardized time zones across the continent, and transformed the United States into a manufacturing powerhouse.</p>"""

    p4_questions = [
        (121, "What is the passage mainly about?",
         [("A", "The architectural design of nineteenth-century steam locomotives."),
          ("B", "The construction and economic impact of the Transcontinental Railroad."),
          ("C", "Trade routes between North America and South America."),
          ("D", "The lives of famous American railway magnates.")],
         "B", "Teks membahas proses pembangunan jembatan/rel dan dampak ekonomi jalur kereta api lintas benua."),

        (122, "Prior to 1869, how long did an overland wagon trip between the East Coast and California take?",
         [("A", "About one week"),
          ("B", "About one month"),
          ("C", "Approximately six months"),
          ("D", "Nearly two full years")],
         "C", "Sebelum adanya kereta api, perjalanan darat memakan waktu sekitar enam bulan ('grueling six-month overland journey')."),

        (123, "The word 'hazardous' in Line 4 is closest in meaning to:",
         [("A", "rapid"),
          ("B", "dangerous"),
          ("C", "inexpensive"),
          ("D", "relaxing")],
         "B", "'Hazardous' bermakna berbahaya dan penuh risiko ('dangerous / risky')."),

        (124, "According to paragraph 2, who constituted a large portion of the construction workforce?",
         [("A", "British naval officers"),
          ("B", "Chinese and Irish immigrant laborers"),
          ("C", "French architectural scholars"),
          ("D", "Russian mining engineers")],
         "B", "Mayoritas pekerja adalah imigran Tiongkok dan Irlandia ('predominantly Chinese and Irish immigrants')."),

        (125, "The word 'volatile' in Line 10 is closest in meaning to:",
         [("A", "easily explosive or unstable"),
          ("B", "completely safe and non-toxic"),
          ("C", "slow to ignite"),
          ("D", "water-soluble")],
         "A", "'Volatile' bermakna mudah meledak dan tidak stabil ('easily explosive or unstable')."),

        (126, "How fast were workers able to lay track during peak construction?",
         [("A", "One mile every three months"),
          ("B", "Up to ten miles in a single day"),
          ("C", "Fifty miles per week"),
          ("D", "One hundred miles per month")],
         "B", "Pekerja mampu memasang rel hingga sepuluh mil dalam satu hari ('up to ten miles in a single day')."),

        (127, "The word 'plunged' in Line 16 is closest in meaning to:",
         [("A", "dropped sharply"),
          ("B", "increased gradually"),
          ("C", "remained constant"),
          ("D", "fluctuated wildly")],
         "A", "'Plunged' berarti anjlok tajam / turun drastis ('dropped sharply')."),

        (128, "According to paragraph 3, by what percentage were freight shipping costs reduced?",
         [("A", "Ten percent"),
          ("B", "Fifty percent"),
          ("C", "Seventy-five percent"),
          ("D", "Ninety percent")],
         "D", "Biaya pengiriman kargo turun sebesar sembilan puluh persen ('plunged by ninety percent')."),

        (129, "Which of the following was NOT an outcome of the Transcontinental Railroad?",
         [("A", "The introduction of standardized time zones."),
          ("B", "A dramatic reduction in cross-country travel time."),
          ("C", "A complete decline in American urban industrial cities."),
          ("D", "The creation of an integrated national commercial marketplace.")],
         "C", "Rel justru mempercepat pertumbuhan kota industri, bukan menyebabkannya menurun."),

        (130, "The word 'profound' in Line 14 is closest in meaning to:",
         [("A", "deep and far-reaching"),
          ("B", "temporary and negligible"),
          ("C", "unintended and harmful"),
          ("D", "unnoticed by citizens")],
         "A", "'Profound' berarti sangat mendalam dan berdampak luas ('deep and far-reaching').")
    ]

    for qid, prompt, opts, key, expl in p4_questions:
        questions.append({
            "id": qid,
            "section": 3,
            "sectionName": "Section 3: Reading Comprehension",
            "part": "Reading: Passage 4",
            "type": "reading_passage",
            "stimulusTitle": p4_title,
            "stimulusSource": p4_source,
            "stimulusBody": p4_text,
            "prompt": prompt,
            "options": [{"key": k, "text": txt} for k, txt in opts],
            "correctAnswer": key,
            "explanation": expl
        })

    # Passage 5: Photovoltaic Solar Power Innovations (Q131 - Q140)
    p5_title = "Passage 5: Photovoltaic Solar Cells and Modern Energy Transition"
    p5_source = "Source: Adapted from Scientific American Technology Archives"
    p5_text = """<p><span class="line-num">Line 1</span> Photovoltaic technology converts radiant solar energy directly into electricity at the atomic scale. First demonstrated by French physicist Edmond Becquerel in 1839, the photovoltaic effect occurs when photons of light strike specific semiconducting materials, most commonly crystalline silicon. The energy delivered by the incoming photons dislodges electrons from their atomic bonds within the silicon lattice, creating free charge carriers. An engineered internal electric field directs these liberated electrons to flow in a single direction, producing a continuous direct current.</p>
<p><span class="line-num">Line 8</span> For decades, the widespread commercial adoption of solar arrays was hindered by exorbitant manufacturing costs and modest conversion efficiency. Early satellite solar panels in the 1960s converted less than ten percent of available solar irradiance into usable power. Over the past twenty years, however, automated wafer slicing, anti-reflective coating chemistries, and economies of scale have driven production costs down by more than eighty percent. Modern commercial silicon panels routinely achieve efficiencies exceeding twenty-two percent.</p>
<p><span class="line-num">Line 15</span> Recent scientific breakthroughs are pushing solar capabilities even further through multi-junction tandem cells. By layering revolutionary mineral compounds called perovskites on top of conventional silicon, researchers can absorb complementary wavelengths across the broader solar spectrum. Silicon efficiently captures infrared light, while perovskites absorb higher-energy blue and green light. Laboratory prototypes of these hybrid tandem cells have surpassed thirty-three percent efficiency, heralding an era where solar power is not only environmentally clean, but also the most economically competitive electricity on Earth.</p>"""

    p5_questions = [
        (131, "What is the primary subject of the passage?",
         [("A", "The history of nuclear fusion experiments."),
          ("B", "The operating principles and technological advancements of photovoltaic solar cells."),
          ("C", "Methods for storing electric vehicle batteries."),
          ("D", "The dangers of working with industrial silicon dust.")],
         "B", "Teks membahas prinsip kerja dan inovasi kemajuan teknologi sel surya fotovoltaik."),

        (132, "What occurs when photons of light strike a semiconducting silicon cell?",
         [("A", "The silicon melts into a conductive liquid."),
          ("B", "Electrons are dislodged from their atomic bonds to flow as electricity."),
          ("C", "The panel reflects all sunlight into mirrors."),
          ("D", "Chemical gases are released into the surrounding air.")],
         "B", "Foton cahaya melepaskan elektron dari ikatan atomnya sehingga mengalir menjadi arus listrik."),

        (133, "The word 'liberated' in Line 6 is closest in meaning to:",
         [("A", "trapped"),
          ("B", "freed"),
          ("C", "heated"),
          ("D", "destroyed")],
         "B", "'Liberated' bermakna dibebaskan atau dilepaskan ('freed')."),

        (134, "The word 'hindered' in Line 9 is closest in meaning to:",
         [("A", "assisted"),
          ("B", "impeded or delayed"),
          ("C", "celebrated"),
          ("D", "expanded")],
         "B", "'Hindered' bermakna terhalang / terhambat ('impeded / obstructed')."),

        (135, "What was a major limitation of early solar panels in the 1960s?",
         [("A", "They could only operate under moonlight."),
          ("B", "They had conversion efficiencies under ten percent."),
          ("C", "They were too light to be mounted on rooftops."),
          ("D", "They required fossil fuels to generate electricity.")],
         "B", "Panel surya awal 1960-an memiliki efisiensi konversi yang rendah (di bawah 10 persen)."),

        (136, "According to paragraph 2, what factor contributed to the dramatic reduction in solar panel costs?",
         [("A", "A shortage of global silicon supplies."),
          ("B", "Automated manufacturing and economies of scale."),
          ("C", "The prohibition of wind turbines worldwide."),
          ("D", "Higher taxes placed on fossil fuels.")],
         "B", "Otomatisasi manufaktur dan skala ekonomi menurunkan biaya produksi hingga lebih dari 80%."),

        (137, "The word 'exorbitant' in Line 9 is closest in meaning to:",
         [("A", "unreasonably high"),
          ("B", "extremely affordable"),
          ("C", "steadily declining"),
          ("D", "government subsidized")],
         "A", "'Exorbitant' bermakna sangat mahal / terlampau tinggi ('unreasonably high / excessive')."),

        (138, "Why are perovskites layered on top of silicon in tandem cells?",
         [("A", "To protect the silicon from heavy rainfall and hail."),
          ("B", "To capture complementary high-energy light wavelengths."),
          ("C", "To make the solar panels flexible like fabric."),
          ("D", "To cool the panel during midday heatwaves.")],
         "B", "Perovskit menyerap panjang gelombang cahaya biru/hijau berenergi tinggi yang melengkapi silicon (penyerap inframerah)."),

        (139, "What efficiency level have laboratory hybrid tandem cells surpassed?",
         [("A", "Ten percent"),
          ("B", "Twenty-two percent"),
          ("C", "Thirty-three percent"),
          ("D", "Fifty percent")],
         "C", "Prototipe sel tandem hibrida di laboratorium telah melampaui efisiensi tiga puluh tiga persen ('surpassed 33%')."),

        (140, "What can be inferred about the future of solar energy based on the passage?",
         [("A", "Solar panels will soon be abandoned for coal power."),
          ("B", "Continuous technological breakthroughs will make solar increasingly cost-effective."),
          ("C", "Solar power will only be useful in desert environments."),
          ("D", "Silicon will be completely banned from electrical engineering.")],
         "B", "Inovasi berkelanjutan akan membuat tenaga surya semakin bersih dan paling kompetitif secara ekonomi di dunia.")
    ]

    for qid, prompt, opts, key, expl in p5_questions:
        questions.append({
            "id": qid,
            "section": 3,
            "sectionName": "Section 3: Reading Comprehension",
            "part": "Reading: Passage 5",
            "type": "reading_passage",
            "stimulusTitle": p5_title,
            "stimulusSource": p5_source,
            "stimulusBody": p5_text,
            "prompt": prompt,
            "options": [{"key": k, "text": txt} for k, txt in opts],
            "correctAnswer": key,
            "explanation": expl
        })

    return questions

paket1_questions = make_js_file()
print(f"Generated Paket 1: {len(paket1_questions)} questions.")

# Check answer distribution
counts = {'A': 0, 'B': 0, 'C': 0, 'D': 0}
for q in paket1_questions:
    counts[q['correctAnswer']] += 1
print("Paket 1 Answer distribution:", counts)

# Write to bank-paket1.js
js_content = "/**\n * BANK SOAL TOEFL ITP OTENTIK - PAKET 1 (140 SOAL)\n * Target Kompetensi: CEFR Level B1 (Passing Score >= 433, Setara IELTS Band 4.5 - 5.0)\n */\n\n"
js_content += "window.TOEFL_BANK_PAKET_1 = " + json.dumps(paket1_questions, indent=2, ensure_ascii=False) + ";\n"

out_path = r"c:\Users\LILI\OneDrive - PDK Jateng\Dokumen\TOEFL-Assessment-Test\bank-paket1.js"
with open(out_path, "w", encoding="utf-8") as f:
    f.write(js_content)
print(f"SUCCESS: Written to {out_path}")
