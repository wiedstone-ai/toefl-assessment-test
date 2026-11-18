# -*- coding: utf-8 -*-
"""
Generator for bank-paket2.js (140 Distinct Authentic TOEFL ITP Questions for Paket 2 - CEFR B1)
"""
import json
from balance_tool import enforce_key_balance

def make_paket2_questions():
    questions = []

    # =========================================================================
    # SECTION 1: LISTENING COMPREHENSION (50 Questions)
    # =========================================================================
    
    # --- PART A: Short Conversations (Questions 1 - 30) ---
    part_a_data = [
        (1, "woman", "Do you think we can print our architectural blueprints at the campus media center?",
            "man", "The plotters were out of ink yesterday, but the technician refilled them this morning.",
            "What does the man imply?",
            [("A", "The printers are currently ready to use."),
             ("B", "The media center has closed early."),
             ("C", "They must purchase their own ink cartridges."),
             ("D", "The blueprints cannot be printed on paper.")],
            "A", "Pria menyatakan teknisi sudah mengisi ulang tinta pagi ini, menyiratkan mesin cetak sudah bisa dipakai."),

        (2, "man", "I'm having difficulty adjusting the fuel injection pressure on this test vehicle.",
            "woman", "Let me grab the digital service manual from the tool cabinet.",
            "What will the woman probably do next?",
            [("A", "Drive the test vehicle around the garage."),
             ("B", "Retrieve the instruction guide to help the man."),
             ("C", "Replace the entire fuel engine block."),
             ("D", "Ask the teacher to cancel the practical test.")],
            "B", "Wanita mengambil buku manual servis digital dari lemari perkakas untuk membantu pria tersebut."),

        (3, "woman", "Are you interested in joining the student robotics competition in Jakarta?",
            "man", "I've already submitted our team registration form!",
            "What does the man mean?",
            [("A", "He has already signed up their team."),
             ("B", "He is uncertain about traveling to Jakarta."),
             ("C", "He does not want to build a robot."),
             ("D", "The registration deadline has already passed.")],
            "A", "Pria menegaskan bahwa ia sudah mendaftarkan tim mereka ('already submitted our team registration form')."),

        (4, "man", "Professor Adams spoke so quickly during the chemistry lecture that my hand hurt from taking notes.",
            "woman", "Next time, why not record the audio on your smartphone with his permission?",
            "What does the woman suggest the man do?",
            [("A", "Ask to record the lecture audio next time."),
             ("B", "Stop taking notes during chemistry class."),
             ("C", "Drop the chemistry course immediately."),
             ("D", "Borrow someone else's handwritten notebook.")],
            "A", "Wanita menyarankan merekam audio perkuliahan di ponsel dengan izin dosen."),

        (5, "woman", "Did Alan manage to fix the short circuit in the electrical panel?",
            "man", "He was able to replace the damaged breaker just before fifth period started.",
            "What does the man say about Alan?",
            [("A", "He was unable to locate the short circuit."),
             ("B", "He successfully replaced the damaged circuit breaker."),
             ("C", "He asked the instructor to complete the repair."),
             ("D", "He forgot to bring his screwdriver to class.")],
            "B", "Pria mengonfirmasi Alan berhasil mengganti pemutus arus listrik sebelum jam pelajaran ke-5."),

        (6, "man", "The wind outside is blowing hard enough to knock down tree branches.",
            "woman", "We'd better make sure all the workshop windows and shutters are firmly locked.",
            "What will the speakers probably do?",
            [("A", "Go outside to trim the tree branches."),
             ("B", "Secure the workshop windows against the wind."),
             ("C", "Wait outside the building until it is calm."),
             ("D", "Cancel tomorrow morning's workshop class.")],
            "B", "Wanita mengajak memastikan seluruh jendela dan daun jendela bengkel terkunci rapat."),

        (7, "woman", "I thought the English vocabulary quiz was scheduled for tomorrow.",
            "man", "The teacher moved it up to this morning because of the assembly.",
            "What did the teacher do regarding the quiz?",
            [("A", "Postponed the quiz to next week."),
             ("B", "Administered the quiz earlier than planned."),
             ("C", "Canceled the quiz altogether."),
             ("D", "Reduced the number of vocabulary items.")],
             "B", "Guru memajukan jadwal kuis menjadi pagi ini karena ada upacara pertemuan ('moved it up')."),

        (8, "man", "Can you show me how to calibrate this digital micrometer?",
            "woman", "Sure. First, make sure the measuring faces are clean, then press the zero button.",
            "What is the woman doing?",
            [("A", "Explaining how to calibrate the measuring tool."),
             ("B", "Refusing to assist the man with his work."),
             ("C", "Purchasing a new mechanical micrometer."),
             ("D", "Measuring the thickness of a steel plate.")],
            "A", "Wanita menerangkan langkah-langkah mengkalibrasi mikrometer digital."),

        (9, "woman", "The bus was twenty minutes late because of road repairs on Main Street.",
            "man", "I know. Traffic was moving at a snail's pace all morning.",
            "What does the man mean by 'moving at a snail's pace'?",
            [("A", "Vehicles were driving extremely slowly."),
             ("B", "Snails were crossing the highway."),
             ("C", "The bus was speeding dangerously."),
             ("D", "The road was completely deserted.")],
            "A", "Idiom 'at a snail's pace' bermakna lalu lintas bergerak sangat lambat."),

        (10, "man", "I'm having trouble seeing the board from the back of the auditorium.",
             "woman", "There are a few empty seats in the fourth row near the center aisle.",
             "What does the woman imply?",
             [("A", "The man should sit closer to the front."),
              ("B", "The board is too small for anyone to see."),
              ("C", "The man should leave the auditorium."),
              ("D", "All seats in the auditorium are occupied.")],
             "A", "Wanita menginformasikan ada kursi kosong di baris keempat agar pria bisa duduk lebih depan."),

        (11, "woman", "Have you finished drafting the layout for the school website?",
             "man", "I've completed the navigation menu, but the mobile layout still needs fine-tuning.",
             "What is the status of the man's work?",
             [("A", "The website project has been abandoned."),
              ("B", "He still needs to adjust the mobile layout."),
              ("C", "He has not started working on the menu."),
              ("D", "The entire website is completely finished.")],
             "B", "Pria menyatakan tata letak versi seluler masih membutuhkan penyempurnaan ('needs fine-tuning')."),

        (12, "man", "Did you hear that the library is extending its weekend hours during exams?",
             "woman", "That's wonderful news! Now I won't have to study in the noisy dormitory.",
             "Why is the woman pleased?",
             [("A", "She can study longer in a quiet environment."),
              ("B", "Her exams have been canceled."),
              ("C", "The dormitory has become much quieter."),
              ("D", "The library has lowered its book prices.")],
             "A", "Wanita senang karena bisa belajar lebih lama di perpustakaan yang tenang daripada di asrama yang bising."),

        (13, "woman", "I can't seem to find the spare soldering tips anywhere on this workbench.",
             "man", "Check the top drawer of the green metal cabinet near the door.",
             "Where does the man tell the woman to look?",
             [("A", "On top of the instructor's desk."),
              ("B", "In the top drawer of the green cabinet."),
              ("C", "Underneath the electronic workbench."),
              ("D", "Inside the cardboard box on the floor.")],
             "B", "Pria menyarankan mencari di laci paling atas lemari hijau dekat pintu."),

        (14, "man", "Is it necessary to wear protective face shields while cutting metal with the lathe?",
             "woman", "Absolutely! Flying metal shavings can cause serious eye injuries.",
             "What does the woman emphasize?",
             [("A", "The lathe machine should not be used."),
              ("B", "Eye protection is mandatory during metal cutting."),
              ("C", "Metal shavings are harmless to operators."),
              ("D", "Students should cut metal without any shields.")],
             "B", "Wanita menegaskan pelindung wajah mutlak wajib digunakan untuk menghindari cedera mata."),

        (15, "woman", "The speaker at the industrial automation conference was fascinating.",
             "man", "I couldn't agree more. His demonstration of robotic arms was eye-opening.",
             "What does the man think of the conference speaker?",
             [("A", "He thought the speech was overly complicated."),
              ("B", "He fully agreed that the presentation was very impressive."),
              ("C", "He fell asleep during the demonstration."),
              ("D", "He disagreed with the speaker's ideas on robotics.")],
             "B", "'I couldn't agree more' menyatakan persetujuan mutlak bahwa presentasi pembicara sangat mengagumkan."),

        (16, "man", "How did the mechanical stress test on the aluminum beam turn out?",
             "woman", "It withstood more than twice the required load before showing any cracks.",
             "What did the test reveal about the aluminum beam?",
             [("A", "It cracked under very light pressure."),
              ("B", "It performed significantly better than required."),
              ("C", "It was manufactured from defective metal."),
              ("D", "It failed to meet basic safety standards.")],
             "B", "Balok aluminium terbukti mampu menahan beban dua kali lipat dari syarat minimum."),

        (17, "woman", "Do you know when the scholarship interview results will be posted?",
             "man", "The announcement will be made on the student portal at noon on Friday.",
             "When will the interview results become available?",
             [("A", "Immediately following the interview."),
              ("B", "At midday on Friday on the website."),
              ("C", "Early next Monday morning."),
              ("D", "Through postal mail next month.")],
             "B", "Pengumuman akan diunggah di portal siswa pada hari Jumat pukul 12 siang ('at noon on Friday')."),

        (18, "man", "I accidentally stripped the head of this screw while tightening the motor mount.",
             "woman", "Don't force it with that screwdriver. Use a screw extractor from the mechanic's kit.",
             "What does the woman suggest?",
             [("A", "Hit the motor mount with a heavy hammer."),
              ("B", "Use a specialized extractor tool to remove the damaged screw."),
              ("C", "Leave the broken screw inside the motor forever."),
              ("D", "Replace the entire electric motor.")],
             "B", "Wanita menyarankan menggunakan alat khusus 'screw extractor' untuk melepas baut yang rusak."),

        (19, "woman", "Would you like to review the electrical formulas with our study group tonight?",
             "man", "I'd love to, but I promised my uncle I'd help him repair his car engine.",
             "Why is the man unable to attend the study group?",
             [("A", "He already understands all electrical formulas."),
              ("B", "He has a prior commitment to help his relative."),
              ("C", "He dislikes studying in group settings."),
              ("D", "He does not own an automobile.")],
             "B", "Pria sudah berjanji membantu pamannya memperbaiki mesin mobil ('promised my uncle')."),

        (20, "man", "The battery voltage reading is showing only eleven point two volts.",
             "woman", "That explains why the engine is cranking so sluggishly. It needs a full recharge.",
             "What is the problem with the vehicle?",
             [("A", "The fuel tank is completely dry."),
              ("B", "The battery does not have enough electrical charge."),
              ("C", "The spark plugs are covered in oil."),
              ("D", "The tires have lost air pressure.")],
             "B", "Tegangan 11.2V menunjukkan aki lemah sehingga putaran mesin lambat dan perlu diisi ulang daya."),

        (21, "woman", "Can we submit our technical design drawings electronically instead of on paper?",
             "man", "Mr. Surya prefers printed blueprints, but he accepts PDF files if submitted before five.",
             "How can the students submit their drawings?",
             [("A", "Only by sending physical mail to his home."),
              ("B", "As a PDF file before five o'clock."),
              ("C", "By handing them in next week in class."),
              ("D", "Drawings do not need to be submitted.")],
             "B", "Guru menerima file PDF asalkan dikirimkan sebelum pukul lima sore."),

        (22, "man", "Are there any vegetarian options available at the school cafeteria today?",
             "woman", "They have fresh tofu curry and steamed vegetable dumplings.",
             "What does the woman indicate about the cafeteria menu?",
             [("A", "No vegetarian food is being served today."),
              ("B", "There are vegetable and tofu dishes available."),
              ("C", "The cafeteria only serves beef steaks."),
              ("D", "The cafeteria is closed for renovations.")],
             "B", "Kantin menyediakan kari tahu dan siomay sayur kukus untuk pilihan vegetarian."),

        (23, "woman", "I'm having a hard time balancing this chemical equation for combustion.",
             "man", "Remember that oxygen atoms exist as diatomic molecules in the air.",
             "What helpful reminder does the man provide?",
             [("A", "Oxygen in the air is diatomic, written as O2."),
              ("B", "Chemical equations do not require balancing."),
              ("C", "Combustion releases liquid nitrogen."),
              ("D", "Carbon atoms always disappear during burning.")],
             "A", "Pria mengingatkan bahwa atom oksigen di udara berbentuk molekul diatomik (O2)."),

        (24, "man", "The welding instructor said our bead alignment was remarkably straight.",
             "woman", "That's a relief! All those hours of steady-hand practice finally paid off.",
             "What are the speakers discussing?",
             [("A", "Their positive feedback on a welding exercise."),
              ("B", "The price of steel welding rods."),
              ("C", "An accident that occurred in the workshop."),
              ("D", "Their plans to change vocational majors.")],
             "A", "Keduanya membahas pujian instruktur atas kelurusan sambungan las hasil latihan intensif mereka."),

        (25, "woman", "Did the package of electronic transistors arrive from the supplier yet?",
             "man", "The delivery van just pulled up outside the warehouse loading dock.",
             "What does the man imply?",
             [("A", "The electronic components are arriving right now."),
              ("B", "The order was canceled by the supplier."),
              ("C", "The transistors were lost during shipping."),
              ("D", "The warehouse has no room for more packages.")],
             "A", "Mobil kurir baru saja berhenti di dermaga bongkar muat, menandakan paket sedang tiba."),

        (26, "man", "I'm not sure whether to choose the civil engineering or mechanical drafting track.",
             "woman", "Why not speak with our career counselor, Mrs. Wahyu? She helped me decide last year.",
             "What does the woman advise the man to do?",
             [("A", "Consult with the school career counselor."),
              ("B", "Flip a coin to make his decision."),
              ("C", "Drop out of vocational school."),
              ("D", "Choose both tracks at the same time.")],
             "A", "Wanita menyarankan berkonsultasi dengan guru BK / konselor karier, Bu Wahyu."),

        (27, "woman", "The temperature inside the server room feels unusually warm today.",
             "man", "One of the ventilation cooling fans must have stopped spinning.",
             "What does the man suspect is causing the problem?",
             [("A", "Someone left the heater turned on high."),
              ("B", "A cooling fan in the room is malfunctioning."),
              ("C", "The computers are all turned off."),
              ("D", "Hot water is leaking onto the floor.")],
             "B", "Pria menduga salah satu kipas pendingin ventilasi berhenti berputar sehingga ruangan panas."),

        (28, "man", "Could I borrow your wire strippers for just a few minutes?",
             "woman", "Go right ahead, as long as you return them before the bell rings.",
             "Under what condition may the man borrow the tool?",
             [("A", "He must pay a small rental fee."),
              ("B", "He must return the tool before the bell rings."),
              ("C", "He can keep the tool permanently."),
              ("D", "He must clean the entire workshop first.")],
             "B", "Wanita memperbolehkan asalkan tang pengupas kabel dikembalikan sebelum bel berbunyi."),

        (29, "woman", "I heard our school's solar car team placed second in the national contest.",
             "man", "Second place out of fifty competing vocational schools is an incredible achievement!",
             "What is the man's opinion of the team's placement?",
             [("A", "He is very impressed by their outstanding result."),
              ("B", "He thinks the team should have done much better."),
              ("C", "He believes the judges scored unfairly."),
              ("D", "He did not know the competition took place.")],
             "A", "Pria sangat mengapresiasi pencapaian juara dua dari 50 SMK peserta lomba mobil surya."),

        (30, "man", "We need to replace the hydraulic oil in the excavator before tomorrow's field work.",
             "woman", "I've already drained the old fluid and prepared the new synthetic lubricant drums.",
             "What has the woman already completed?",
             [("A", "She finished preparing the machine for fresh hydraulic oil."),
              ("B", "She drove the excavator to the construction site."),
              ("C", "She canceled tomorrow's field work completely."),
              ("D", "She purchased an entirely new excavator.")],
             "A", "Wanita telah menguras cairan lama dan menyiapkan drum pelumas sintetis yang baru.")
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
    # Conversation 1: Digital Engineering Library (Q31 - Q34)
    c1_dialog = [
        {"role": "narrator", "text": "Questions 31 through 34. Listen to a conversation between a student and a university librarian.", "pauseAfter": 450},
        {"role": "man", "text": "Good afternoon. I'm writing a senior research paper on electric vehicle battery cooling systems, but I can't find recent peer-reviewed articles on the open shelves.", "pauseAfter": 350},
        {"role": "woman", "text": "Most engineering research from the past five years is archived in our digital journal database rather than print magazines. Have you accessed the IEEE Xplore or ScienceDirect portal using your student ID?", "pauseAfter": 400},
        {"role": "man", "text": "I haven't set up my digital library account yet. How do I get remote access from my laptop?", "pauseAfter": 300},
        {"role": "woman", "text": "It's straightforward. Go to the library homepage, click on 'Student Database Authentication', and log in with your institutional email. Once activated, you can search thousands of full-text technical papers and download PDF schematics for free.", "pauseAfter": 450}
    ]
    c1_script = "Student (Man): Good afternoon. I'm writing a senior research paper on electric vehicle battery cooling systems, but I can't find recent peer-reviewed articles on the open shelves.\nLibrarian (Woman): Most engineering research from the past five years is archived in our digital journal database rather than print magazines. Have you accessed the IEEE Xplore or ScienceDirect portal using your student ID?\nStudent: I haven't set up my digital library account yet. How do I get remote access from my laptop?\nLibrarian: It's straightforward. Go to the library homepage, click on 'Student Database Authentication', and log in with your institutional email. Once activated, you can search thousands of full-text technical papers and download PDF schematics for free."

    c1_questions = [
        (31, "Why does the student visit the university library?",
         [("A", "To return overdue mechanical textbooks."),
          ("B", "To seek assistance in finding recent engineering research papers."),
          ("C", "To apply for a part-time job as a book stacker."),
          ("D", "To repair a damaged computer terminal.")],
         "B", "Siswa mencari bantuan pustakawan untuk menemukan artikel penelitian teknik terbaru tentang sistem pendingin baterai EV."),

        (32, "Where is the majority of recent engineering research stored?",
         [("A", "In locked file drawers in the library basement."),
          ("B", "In digital journal databases accessible online."),
          ("C", "On microfilms in the city museum archives."),
          ("D", "In printed textbooks located on open shelves.")],
         "B", "Riset teknik 5 tahun terakhir tersimpan di basis data jurnal digital (IEEE, ScienceDirect)."),

        (33, "What must the student do to access the technical database from his laptop?",
         [("A", "Pay a monthly subscription fee with a credit card."),
          ("B", "Log into the library authentication portal using his student email."),
          ("C", "Obtain written permission from the university dean."),
          ("D", "Visit the library in person every time he needs an article.")],
         "B", "Siswa cukup masuk ke portal autentikasi menggunakan email institusi kampus."),

        (34, "What can students do once their digital account is activated?",
         [("A", "Download full-text technical papers and schematics without cost."),
          ("B", "Borrow up to twenty print journals simultaneously."),
          ("C", "Order physical books from foreign bookstores."),
          ("D", "Grade research papers written by other undergraduates.")],
         "A", "Siswa dapat mencari ribuan makalah teknis teks lengkap dan mengunduh skema PDF gratis.")
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

    # Conversation 2: Automotive EFI Diagnostics (Q35 - Q38)
    c2_dialog = [
        {"role": "narrator", "text": "Questions 35 through 38. Listen to a conversation between an automotive instructor and an apprentice in a diagnostic garage.", "pauseAfter": 450},
        {"role": "man", "text": "Mr. Joko, I plugged the On-Board Diagnostic scanner into this sedan, and it gave me a fault code P0302.", "pauseAfter": 350},
        {"role": "woman", "text": "Code P0302 indicates a cylinder two misfire. What steps should we take to systematically isolate the root cause?", "pauseAfter": 350},
        {"role": "man", "text": "Well, a misfire could be caused by a faulty spark plug, a clogged fuel injector, or a malfunctioning ignition coil on that specific cylinder.", "pauseAfter": 350},
        {"role": "woman", "text": "Spot on. Let's swap the ignition coil from cylinder two to cylinder three. If the diagnostic scanner then reports error code P0303 on cylinder three, we know for certain that the ignition coil itself is defective.", "pauseAfter": 450}
    ]
    c2_script = "Apprentice (Man): Mr. Joko, I plugged the On-Board Diagnostic scanner into this sedan, and it gave me a fault code P0302.\nInstructor (Woman): Code P0302 indicates a cylinder two misfire. What steps should we take to systematically isolate the root cause?\nApprentice: Well, a misfire could be caused by a faulty spark plug, a clogged fuel injector, or a malfunctioning ignition coil on that specific cylinder.\nInstructor: Spot on. Let's swap the ignition coil from cylinder two to cylinder three. If the diagnostic scanner then reports error code P0303 on cylinder three, we know for certain that the ignition coil itself is defective."

    c2_questions = [
        (35, "What diagnostic tool did the apprentice use to inspect the vehicle?",
         [("A", "A mechanical hydraulic jack."),
          ("B", "An On-Board Diagnostic scanner."),
          ("C", "A battery acid tester."),
          ("D", "A laser wheel alignment sensor.")],
         "B", "Siswa magang menggunakan pemindai diagnostik OBD (On-Board Diagnostic scanner)."),

        (36, "What malfunction is indicated by the error code P0302?",
         [("A", "A low engine oil pressure warning."),
          ("B", "A cylinder two engine misfire."),
          ("C", "An anti-lock brake pump failure."),
          ("D", "A flat front passenger tire.")],
         "B", "Kode kesalahan P0302 menandakan kegagalan pengapian silinder nomor 2 (cylinder two misfire)."),

        (37, "Which of the following is NOT listed as a possible cause of the misfire?",
         [("A", "A defective spark plug."),
          ("B", "A clogged fuel injector nozzle."),
          ("C", "A broken air conditioning compressor."),
          ("D", "A malfunctioning ignition coil.")],
         "C", "Kompresor AC tidak berhubungan dengan sistem pengapian silinder mesin."),

        (38, "What clever troubleshooting method does the instructor recommend?",
         [("A", "Swapping the ignition coil to another cylinder to see if the code moves."),
          ("B", "Replacing the entire engine assembly immediately."),
          ("C", "Clearing the code without checking any components."),
          ("D", "Draining all gasoline from the vehicle's fuel tank.")],
         "A", "Instruktur menyarankan menukar koil ke silinder 3 untuk melihat apakah kode kesalahan berpindah.")
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
    # Talk 1: Ocean Thermohaline Circulation (Q39 - Q42)
    t1_dialog = [
        {"role": "narrator", "text": "Questions 39 through 42. Listen to an oceanography professor discussing ocean currents.", "pauseAfter": 450},
        {"role": "woman", "text": "The world's oceans are interconnected by an immense global circulation system known as the thermohaline conveyor belt. Driven by differences in water temperature and salinity rather than surface winds, this deep-water current regulates global climate. In polar regions like the North Atlantic, surface water becomes extremely cold. When sea ice forms, it expels dissolved salt into the surrounding liquid, making the remaining water dense and salty. This cold, dense water sinks thousands of meters to the ocean abyss and creeps southward. Century by century, it travels across global ocean basins before warming and welling up toward the surface in the Indian and Pacific Oceans. Without this conveyor belt, northern Europe would be locked in severe subarctic winter conditions.", "pauseAfter": 450}
    ]
    t1_script = "Professor (Woman): The world's oceans are interconnected by an immense global circulation system known as the thermohaline conveyor belt. Driven by differences in water temperature and salinity rather than surface winds, this deep-water current regulates global climate. In polar regions like the North Atlantic, surface water becomes extremely cold. When sea ice forms, it expels dissolved salt into the surrounding liquid, making the remaining water dense and salty. This cold, dense water sinks thousands of meters to the ocean abyss and creeps southward. Century by century, it travels across global ocean basins before warming and welling up toward the surface in the Indian and Pacific Oceans. Without this conveyor belt, northern Europe would be locked in severe subarctic winter conditions."

    t1_questions = [
        (39, "What is the primary driving mechanism of the thermohaline circulation?",
         [("A", "Surface winds generated by coastal hurricanes."),
          ("B", "Differences in water temperature and salt concentration."),
          ("C", "Gravitational pull from underwater volcanoes."),
          ("D", "Commercial ship traffic across international lanes.")],
         "B", "Sirkulasi termohalin digerakkan oleh perbedaan suhu air dan konsentrasi kadar garam (salinitas)."),

        (40, "Why does polar water become extraordinarily dense in the North Atlantic?",
         [("A", "Because forming sea ice expels salt into cold surface water."),
          ("B", "Because warm tropical rivers empty into the Arctic Sea."),
          ("C", "Because atmospheric oxygen dissolves into the deep trench."),
          ("D", "Because sunlight evaporates all liquid water instantly.")],
         "A", "Saat es laut terbentuk, garam dilepaskan ke air sekitarnya sehingga air menjadi sangat dingin, asin, dan padat."),

        (41, "Where does the sinking cold water eventually rise back toward the surface?",
         [("A", "Exclusively beneath the Arctic ice cap."),
          ("B", "In the Indian and Pacific Oceans."),
          ("C", "In the Mediterranean Sea."),
          ("D", "Along the southern coast of Antarctica.")],
         "B", "Arus air dingin bergerak melintasi cekungan samudra dan mengalami upwelling di Samudra Hindia dan Pasifik."),

        (42, "What would happen to Northern Europe without the thermohaline conveyor belt?",
         [("A", "It would experience tropical temperatures all year."),
          ("B", "It would become locked in harsh subarctic cold climates."),
          ("C", "It would be completely submerged under rising seas."),
          ("D", "Its river networks would evaporate entirely.")],
         "B", "Tanpa arus penghantar ini, Eropa utara akan terkunci dalam kondisi musim dingin subarktik yang sangat beku.")
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

    # Talk 2: The Electric Telegraph (Q43 - Q46)
    t2_dialog = [
        {"role": "narrator", "text": "Questions 43 through 46. Listen to a lecture on the history of telecommunications.", "pauseAfter": 450},
        {"role": "man", "text": "Before the 1840s, the speed of long-distance communication was limited by the speed of a galloping horse or a steam train. That changed dramatically when Samuel Morse developed the commercial electric recording telegraph. In May 1844, Morse transmitted the historic message, 'What hath God wrought,' across a forty-mile copper wire between Washington, D.C., and Baltimore. By translating alphabetic letters into a rhythmic binary code of electrical pulses—dots and dashes—Morse code allowed complex messages to travel instantaneously at near the speed of light. Within two decades, transcontinental and transatlantic telegraph cables spanned oceans, synchronizing global financial markets, news reporting, and railway safety networks.", "pauseAfter": 450}
    ]
    t2_script = "Lecturer (Man): Before the 1840s, the speed of long-distance communication was limited by the speed of a galloping horse or a steam train. That changed dramatically when Samuel Morse developed the commercial electric recording telegraph. In May 1844, Morse transmitted the historic message, 'What hath God wrought,' across a forty-mile copper wire between Washington, D.C., and Baltimore. By translating alphabetic letters into a rhythmic binary code of electrical pulses—dots and dashes—Morse code allowed complex messages to travel instantaneously at near the speed of light. Within two decades, transcontinental and transatlantic telegraph cables spanned oceans, synchronizing global financial markets, news reporting, and railway safety networks."

    t2_questions = [
        (43, "What major historical breakthrough is highlighted in the talk?",
         [("A", "The invention of the diesel locomotive."),
          ("B", "The development of the commercial electric telegraph."),
          ("C", "The establishment of the international postal union."),
          ("D", "The manufacture of handheld satellite telephones.")],
         "B", "Ceramah menyoroti terobosan bersejarah penemuan telegraf listrik komersial oleh Samuel Morse."),

        (44, "Between which two cities was the historic 1844 telegraph line strung?",
         [("A", "New York and Boston."),
          ("B", "Washington, D.C., and Baltimore."),
          ("C", "London and Paris."),
          ("D", "Chicago and San Francisco.")],
         "B", "Kabel telegraf pertama direntangkan sejauh 40 mil antara Washington, D.C. dan Baltimore pada Mei 1844."),

        (45, "How does Morse code encode human language?",
         [("A", "By varying the physical color of paper tape."),
          ("B", "Through rhythmic electrical pulses of dots and dashes."),
          ("C", "By transmitting musical notes over acoustic horns."),
          ("D", "Through chemical dye changes on copper plates.")],
         "B", "Kode Morse menerjemahkan huruf ke dalam denyut listrik berirama titik dan garis (dots and dashes)."),

        (46, "What sector was significantly transformed by the expansion of telegraph cables?",
         [("A", "Horse racing tournaments."),
          ("B", "Financial markets, news reporting, and railway operations."),
          ("C", "Traditional wooden shipbuilding."),
          ("D", "Handmade candle manufacturing.")],
         "B", "Kabel telegraf merevolusi pasar keuangan global, kantor berita, dan pengaturan keselamatan rel kereta api.")
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

    # Talk 3: Desert Mammal Physiological Adaptations (Q47 - Q50)
    t3_dialog = [
        {"role": "narrator", "text": "Questions 47 through 50. Listen to a wildlife biology lecture about desert animal survival.", "pauseAfter": 450},
        {"role": "woman", "text": "Surviving in arid desert ecosystems requires extraordinary physiological adaptations, especially for small mammals that face lethal daytime heat and scarce drinking water. Consider the kangaroo rat, an inhabitant of North American deserts. Remarkably, this rodent can survive its entire life without drinking a single drop of liquid water. It derives all necessary moisture metabolically from the dry seeds it eats. When cellular respiration breaks down carbohydrates and fats, hydrogen atoms combine with oxygen to produce metabolic water. To conserve this precious internal fluid, kangaroo rats have hyper-efficient kidneys that concentrate urine into an almost solid crystal paste, and they avoid the scorching sun entirely by residing in cool, humid underground burrows during daylight hours.", "pauseAfter": 450}
    ]
    t3_script = "Biologist (Woman): Surviving in arid desert ecosystems requires extraordinary physiological adaptations, especially for small mammals that face lethal daytime heat and scarce drinking water. Consider the kangaroo rat, an inhabitant of North American deserts. Remarkably, this rodent can survive its entire life without drinking a single drop of liquid water. It derives all necessary moisture metabolically from the dry seeds it eats. When cellular respiration breaks down carbohydrates and fats, hydrogen atoms combine with oxygen to produce metabolic water. To conserve this precious internal fluid, kangaroo rats have hyper-efficient kidneys that concentrate urine into an almost solid crystal paste, and they avoid the scorching sun entirely by residing in cool, humid underground burrows during daylight hours."

    t3_questions = [
        (47, "What is the primary adaptation discussed regarding the kangaroo rat?",
         [("A", "Its ability to migrate across continents each summer."),
          ("B", "Its ability to survive without drinking liquid water."),
          ("C", "Its specialized venomous bite used against snakes."),
          ("D", "Its capacity to store gallons of water in neck pouches.")],
         "B", "Kemampuan adaptasi luar biasa tikus kangguru adalah bertahan hidup tanpa minum air cair sama sekali."),

        (48, "How does the kangaroo rat obtain moisture to sustain its cells?",
         [("A", "By drinking early morning dew from desert cactus leaves."),
          ("B", "Metabolically through cellular respiration from dry seeds."),
          ("C", "By absorbing atmospheric water vapor through its fur."),
          ("D", "From swimming in underground geothermal springs.")],
         "B", "Tikus kangguru memperoleh cairan secara metabolik dari pemecahan karbohidrat biji kering dalam respirasi sel."),

        (49, "What physiological feature enables the rodent to minimize water loss?",
         [("A", "Hyper-efficient kidneys that concentrate urine into crystal paste."),
          ("B", "The complete absence of blood circulation."),
          ("C", "Sweat glands covering its entire body."),
          ("D", "Large external ears that radiate excess body heat.")],
         "A", "Ginjal yang sangat efisien memekatkan urine menjadi pasta kristal padat sehingga meminimalkan kehilangan cairan."),

        (50, "How do kangaroo rats avoid the scorching daytime desert heat?",
         [("A", "By flying into cool upper cloud layers."),
          ("B", "By resting in humid underground burrows until nightfall."),
          ("C", "By submerging themselves in sand dunes for days."),
          ("D", "By shivering violently to reduce core temperature.")],
         "B", "Mereka bersembunyi di liang bawah tanah yang sejuk dan lembap pada siang hari dan baru aktif saat malam.")
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
        (51, "The Great Barrier Reef, off the northeastern coast of Australia, ________ the largest coral reef system on Earth.",
         [("A", "is"), ("B", "being"), ("C", "are"), ("D", "to be")],
         "A", "Subjek tunggal 'The Great Barrier Reef' membutuhkan to be tunggal 'is'."),

        (52, "________ by ancient glaciers thousands of years ago, the Great Lakes contain one-fifth of the world's surface fresh water.",
         [("A", "Carved"), ("B", "Carving"), ("C", "They were carved"), ("D", "When carved they")],
         "A", "Bentuk past participle pasif ('Carved by ancient glaciers...') menerangkan subjek 'the Great Lakes'."),

        (53, "Rarely ________ a thunderstorm develop without the presence of warm, moist air rising into cooler atmospheric layers.",
         [("A", "does"), ("B", "is"), ("C", "a thunderstorm does"), ("D", "it does")],
         "A", "Adverb negatif 'Rarely' di awal kalimat memicu inversi auxiliary verb + subjek: 'does a thunderstorm develop'."),

        (54, "Marie Curie, ________ conducted pioneering research on radioactivity, won Nobel Prizes in both physics and chemistry.",
         [("A", "who"), ("B", "whom"), ("C", "whose"), ("D", "which")],
         "A", "Relative pronoun 'who' berfungsi sebagai subjek klausa yang menerangkan Marie Curie."),

        (55, "Composite materials are valued in aircraft manufacturing because ________ lightweight yet exceptionally strong.",
         [("A", "they are"), ("B", "are"), ("C", "being"), ("D", "there are")],
         "A", "Konjungsi subordinatif 'because' membutuhkan klausa lengkap (Subject + Verb): 'they are'."),

        (56, "Not until the late nineteenth century ________ widespread adoption of electric lighting in public city streets.",
         [("A", "was there"), ("B", "there was"), ("C", "it was"), ("D", "was it")],
         "A", "Ekspresi negatif 'Not until...' memicu inversi: 'was there widespread adoption'."),

        (57, "________ the temperature of a gas increases, its pressure also rises if the container volume remains constant.",
         [("A", "When"), ("B", "Because of"), ("C", "During"), ("D", "Despite")],
         "A", "Konjungsi waktu/kondisi 'When' menghubungkan kenaikan suhu gas dengan peningkatan tekanan."),

        (58, "The Panama Canal, ________ in 1914, drastically shortened maritime cargo shipping routes between the Atlantic and Pacific oceans.",
         [("A", "opened"), ("B", "it opened"), ("C", "opening"), ("D", "was opened")],
         "A", "Appositive participle pasif 'opened in 1914' menerangkan 'The Panama Canal' tanpa menambahkan subjek berulang."),

        (59, "Neither the lead architect nor the project engineers ________ satisfied with the initial soil bearing capacity test.",
         [("A", "were"), ("B", "was"), ("C", "is"), ("D", "being")],
         "A", "Dalam aturan 'Neither... nor...', kata kerja menyesuaikan subjek terdekat ('the project engineers' = jamak), sehingga menggunakan 'were'."),

        (60, "Solar photovoltaic panels generate electrical power more quietly than ________ diesel engine generators.",
         [("A", "do"), ("B", "are"), ("C", "they"), ("D", "is")],
         "A", "Inversi perbandingan komparatif menggunakan auxiliary 'do' yang menggantikan 'generate'."),

        (61, "Automotive apprentices wear protective steel-toed boots in the workshop ________ prevent foot injuries from heavy parts.",
         [("A", "in order to"), ("B", "so that"), ("C", "because of"), ("D", "such that")],
         "A", "Frasa 'in order to' diikuti bare infinitive 'prevent' untuk menyatakan tujuan perlindungan."),

        (62, "The more aerodynamic the exterior body of an electric vehicle is, ________ the energy required to cruise at highway speeds.",
         [("A", "the lower"), ("B", "lower"), ("C", "lowest"), ("D", "the lowest")],
         "A", "Pola komparatif ganda (double comparative): 'The more aerodynamic..., the lower the energy...'."),

        (63, "Only by following strict calibration procedures ________ ensure that the digital CNC machine cuts parts within tolerance limits.",
         [("A", "can technicians"), ("B", "technicians can"), ("C", "technicians do"), ("D", "are technicians")],
         "A", "Frasa restriktif 'Only by...' di awal memicu inversi modal + subjek: 'can technicians ensure'."),

        (64, "Geothermal power plants utilize deep steam wells, ________ emit virtually zero toxic smoke into the surrounding atmosphere.",
         [("A", "which"), ("B", "what"), ("C", "where"), ("D", "who")],
         "A", "Relative pronoun 'which' menerangkan kata benda jamak 'deep steam wells'."),

        (65, "Before the development of modern refrigeration, farmers ________ salt and smoke to preserve meat for winter consumption.",
         [("A", "used"), ("B", "using"), ("C", "were used"), ("D", "use")],
         "A", "Konteks kalimat lampau ('Before...') membutuhkan past tense aktif: 'used' (menggunakan).")
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
    part_b_struct = [
        (66, "The <span class='toefl-err' data-opt='A'>development</span> of high-speed passenger trains <span class='toefl-err' data-opt='B'>have</span> dramatically reduced <span class='toefl-err' data-opt='C'>intercity</span> travel times across <span class='toefl-err' data-opt='D'>Western Europe</span>.",
         "B", "Subjek inti adalah 'The development' (tunggal), sehingga kata kerja seharusnya 'has dramatically reduced', bukan 'have'."),

        (67, "Wind turbines <span class='toefl-err' data-opt='A'>capture</span> kinetic energy from moving air and <span class='toefl-err' data-opt='B'>efficient</span> convert it into <span class='toefl-err' data-opt='C'>clean</span> alternating <span class='toefl-err' data-opt='D'>current</span>.",
         "B", "Kata yang memodifikasi verb 'convert' harus berupa adverb 'efficiently', bukan adjective 'efficient'."),

        (68, "Every <span class='toefl-err' data-opt='A'>apprentice</span> in the automotive program <span class='toefl-err' data-opt='B'>are required</span> to wear safety glasses <span class='toefl-err' data-opt='C'>during</span> lathe machining <span class='toefl-err' data-opt='D'>sessions</span>.",
         "B", "Frasa 'Every apprentice' adalah subjek tunggal, sehingga to be yang benar adalah 'is required', bukan 'are required'."),

        (69, "The robotic arm operates <span class='toefl-err' data-opt='A'>precise</span>, quickly, and <span class='toefl-err' data-opt='B'>reliably</span> on the manufacturing <span class='toefl-err' data-opt='C'>assembly</span> line <span class='toefl-err' data-opt='D'>without pause</span>.",
         "A", "Paralelisme adverb: 'precise' harus diubah menjadi adverb 'precisely' agar setara dengan 'quickly' dan 'reliably'."),

        (70, "Although <span class='toefl-err' data-opt='A'>the severe</span> power outage in the district, the hospital's emergency <span class='toefl-err' data-opt='B'>generators</span> started automatically and <span class='toefl-err' data-opt='C'>maintained</span> power to all <span class='toefl-err' data-opt='D'>intensive care units</span>.",
         "A", "Frasa 'the severe power outage' adalah noun phrase, sehingga harus menggunakan preposisi 'Despite / In spite of', bukan konjungsi klausa 'Although'."),

        (71, "A large <span class='toefl-err' data-opt='A'>number</span> of vocational apprentices <span class='toefl-err' data-opt='B'>is</span> hired by industrial manufacturers immediately <span class='toefl-err' data-opt='C'>after</span> finishing <span class='toefl-err' data-opt='D'>their graduation</span>.",
         "B", "Ekspresi 'A large number of + plural noun' bermakna jamak, sehingga to be seharusnya 'are hired', bukan 'is'."),

        (72, "Reinforced concrete <span class='toefl-err' data-opt='A'>beams</span> with internal steel rebar <span class='toefl-err' data-opt='B'>resists</span> heavy tensile stress <span class='toefl-err' data-opt='C'>better than</span> unreinforced <span class='toefl-err' data-opt='D'>blocks</span>.",
         "B", "Subjek kalimat adalah 'beams' (jamak), sehingga kata kerjanya adalah 'resist' tanpa akhiran -s."),

        (73, "The civil engineer spent <span class='toefl-err' data-opt='A'>two weeks</span> <span class='toefl-err' data-opt='B'>to survey</span> the unstable hillside <span class='toefl-err' data-opt='C'>before</span> approving the road construction <span class='toefl-err' data-opt='D'>project</span>.",
         "B", "Pola kata kerja 'spend + time' membutuhkan gerund (-ing): 'spent two weeks surveying', bukan infinitive 'to survey'."),

        (74, "Neither the lead surveyor <span class='toefl-err' data-opt='A'>or</span> the soil testing technician <span class='toefl-err' data-opt='B'>noticed</span> the subsurface cavity beneath the <span class='toefl-err' data-opt='C'>proposed</span> building <span class='toefl-err' data-opt='D'>site</span>.",
         "A", "Pasangan korelatif untuk 'Neither' adalah 'nor', bukan 'or'."),

        (75, "Modern automated factories <span class='toefl-err' data-opt='A'>rely</span> on optical laser sensors <span class='toefl-err' data-opt='B'>for detect</span> tiny cracks in ceramic <span class='toefl-err' data-opt='C'>engine</span> components <span class='toefl-err' data-opt='D'>prior to shipping</span>.",
         "B", "Setelah preposisi 'for' harus digunakan gerund (-ing): 'for detecting', atau menggunakan 'to detect'."),

        (76, "Sound waves travel <span class='toefl-err' data-opt='A'>considerable</span> <span class='toefl-err' data-opt='B'>faster</span> through solid steel <span class='toefl-err' data-opt='C'>than</span> through liquid water or <span class='toefl-err' data-opt='D'>atmospheric air</span>.",
         "A", "Kata sifat komparatif 'faster' harus dimodifikasi oleh adverb 'considerably', bukan adjective 'considerable'."),

        (77, "The newly overhauled engine <span class='toefl-err' data-opt='A'>runs</span> quiet and <span class='toefl-err' data-opt='B'>smooth</span>, providing <span class='toefl-err' data-opt='C'>excellent</span> fuel mileage on the <span class='toefl-err' data-opt='D'>highway</span>.",
         "A", "Kata kerja 'runs' dimodifikasi oleh adverb: 'runs quietly and smoothly', bukan adjective 'quiet'."),

        (78, "There <span class='toefl-err' data-opt='A'>are</span> very <span class='toefl-err' data-opt='B'>little</span> moisture in the arid desert air <span class='toefl-err' data-opt='C'>during</span> the hot <span class='toefl-err' data-opt='D'>summer months</span>.",
         "A", "Kata 'moisture' adalah uncountable noun (tunggal), sehingga kata kerja seharusnya 'is', bukan 'are'."),

        (79, "Before operating the hydraulic lift, <span class='toefl-err' data-opt='A'>the mechanic</span> <span class='toefl-err' data-opt='B'>must to ensure</span> that the safety locking pins are <span class='toefl-err' data-opt='C'>fully</span> engaged <span class='toefl-err' data-opt='D'>in place</span>.",
         "B", "Modal auxiliary 'must' harus langsung diikuti bare infinitive tanpa 'to': 'must ensure'."),

        (80, "The toxic sulfur gases <span class='toefl-err' data-opt='A'>discharging</span> by old coal furnaces <span class='toefl-err' data-opt='B'>cause</span> acid rain <span class='toefl-err' data-opt='C'>that damages</span> surrounding pine <span class='toefl-err' data-opt='D'>forests</span>.",
         "A", "Makna pasif: gas sulfur dilepaskan/dikeluarkan, sehingga bentuk participle yang tepat adalah past participle 'discharged', bukan 'discharging'."),

        (81, "During yesterday's gale, several <span class='toefl-err' data-opt='A'>tall</span> pine trees were <span class='toefl-err' data-opt='B'>knock down</span> across the main electric <span class='toefl-err' data-opt='C'>transmission</span> line, cutting power to <span class='toefl-err' data-opt='D'>the village</span>.",
         "B", "Bentuk pasif 'were + V3': kata kerja bentuk ketiga dari 'knock' adalah 'knocked down', bukan 'knock down'."),

        (82, "The engineering department <span class='toefl-err' data-opt='A'>made</span> a formal <span class='toefl-err' data-opt='B'>conclude</span> based on the laboratory test results <span class='toefl-err' data-opt='C'>conducted</span> last <span class='toefl-err' data-opt='D'>Tuesday</span>.",
         "B", "Setelah adjective 'formal', kata yang tepat adalah noun 'conclusion', bukan verb 'conclude'."),

        (83, "Marine biologists have noted that <span class='toefl-err' data-opt='A'>many</span> species of sea turtles <span class='toefl-err' data-opt='B'>returns</span> to the exact sandy beach <span class='toefl-err' data-opt='C'>where</span> they were <span class='toefl-err' data-opt='D'>hatched</span>.",
         "B", "Subjek klausa adalah 'many species of sea turtles' (jamak), sehingga kata kerjanya adalah 'return' tanpa akhiran -s."),

        (84, "The supervisor congratulated the apprentices on <span class='toefl-err' data-opt='A'>theirs</span> outstanding technical competence <span class='toefl-err' data-opt='B'>during</span> the annual safety <span class='toefl-err' data-opt='C'>audit</span> inspection <span class='toefl-err' data-opt='D'>process</span>.",
         "A", "Sebelum noun phrase 'outstanding technical competence', kata ganti yang tepat adalah possessive adjective 'their', bukan 'theirs'."),

        (85, "Titanium alloys are <span class='toefl-err' data-opt='A'>extensively employed</span> in aerospace structures <span class='toefl-err' data-opt='B'>because</span> their exceptional resistance to heat and <span class='toefl-err' data-opt='C'>corrosion</span> at high <span class='toefl-err' data-opt='D'>altitudes</span>.",
         "B", "Frasa setelahnya adalah noun phrase, sehingga harus menggunakan preposisi 'because of', bukan konjungsi 'because'."),

        (86, "The instructor demonstrated <span class='toefl-err' data-opt='A'>how</span> the fuel pump functions and <span class='toefl-err' data-opt='B'>its</span> importance to proper combustion <span class='toefl-err' data-opt='C'>efficiency</span> in diesel <span class='toefl-err' data-opt='D'>engines</span>.",
         "B", "Paralelisme struktur klausa: 'explained how the fuel pump functions and why it is important'."),

        (87, "Almost all living <span class='toefl-err' data-opt='A'>mammals</span> in temperate forests <span class='toefl-err' data-opt='B'>grows</span> a thicker layer of fur <span class='toefl-err' data-opt='C'>to protect</span> themselves against winter <span class='toefl-err' data-opt='D'>frost</span>.",
         "B", "Subjek 'Almost all living mammals' adalah jamak, sehingga predikatnya adalah 'grow' tanpa akhiran -s."),

        (88, "Hydroelectric power plants generate <span class='toefl-err' data-opt='A'>electricity</span> by <span class='toefl-err' data-opt='B'>channel</span> rushing river water <span class='toefl-err' data-opt='C'>through</span> giant hydraulic turbines <span class='toefl-err' data-opt='D'>deep inside dams</span>.",
         "B", "Setelah preposisi 'by' harus digunakan gerund (-ing): 'by channeling', bukan bare verb 'channel'."),

        (89, "The technician was <span class='toefl-err' data-opt='A'>unable</span> to locate the diagnostic cables <span class='toefl-err' data-opt='B'>because</span> an apprentice had left <span class='toefl-err' data-opt='C'>it</span> in the trunk of a test <span class='toefl-err' data-opt='D'>car</span>.",
         "C", "Kata 'cables' adalah jamak (plural noun), sehingga pronoun pengganti yang benar adalah 'them', bukan 'it'."),

        (90, "Solar thermal collectors are <span class='toefl-err' data-opt='A'>mounted</span> on open rooftops <span class='toefl-err' data-opt='B'>where</span> solar rays are <span class='toefl-err' data-opt='C'>intense</span> and <span class='toefl-err' data-opt='D'>rely</span>.",
         "D", "Paralelisme adjective setelah to be 'are intense and...': kata 'rely' harus diubah menjadi adjective 'reliable'.")
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

    # Passage 1: Lightning and Thunderstorms (Q91 - Q100)
    p1_title = "Passage 1: Atmospheric Charge Separation and Lightning"
    p1_source = "Source: Adapted from National Oceanic and Atmospheric Administration (NOAA) Archives"
    p1_text = """<p><span class="line-num">Line 1</span> Lightning is one of nature's most spectacular and energetic atmospheric phenomena. At any given moment across the planet, approximately two thousand thunderstorms are active, collectively producing roughly one hundred lightning flashes every second. A lightning bolt consists of a massive electrical discharge that neutralizes charge differences built up within towering cumulonimbus storm clouds or between a charged cloud base and the Earth's surface.</p>
<p><span class="line-num">Line 7</span> The genesis of lightning lies in violent vertical updrafts and downdrafts within developing thunderclouds. As rising warm, moist air cools rapidly at altitudes exceeding six kilometers, supercooled water droplets freeze into millions of tiny ice crystals. Concurrently, larger, denser hail particles called graupel plummet through the cloud. When buoyant upward-traveling ice crystals collide with falling graupel, kinetic friction transfers subatomic electrons. The lighter ice crystals lose electrons and become positively charged, rising toward the freezing cloud anvil. In contrast, the heavier graupel gains electrons, acquiring a net negative charge that accumulates in the lower regions of the cloud.</p>
<p><span class="line-num">Line 16</span> This profound electrostatic separation creates a tremendous electric field. When the insulating capacity of dry air breaks down under voltage potentials exceeding several million volts, a stepped leader of ionized air snakes downward toward the ground. Simultaneously, positive streamers surge upward from tall buildings, trees, and metallic towers. When the two paths connect, an immense return stroke surges upward at nearly one-third the speed of light, heating the surrounding air channel to thirty thousand degrees Celsius—five times hotter than the surface of the sun. This explosive thermal expansion creates the acoustic shockwave heard as thunder.</p>"""

    p1_questions = [
        (91, "What is the primary focus of the passage?",
         [("A", "How weather forecasters predict tornadoes."),
          ("B", "The physical mechanisms responsible for lightning and thunder."),
          ("C", "The construction of lightning rods on urban skyscrapers."),
          ("D", "Methods for measuring rainfall in tropical climates.")],
         "B", "Teks secara komprehensif menjelaskan mekanisme fisik pemisahan muatan, terjadinya kilat dan guntur."),

        (92, "The word 'neutralizes' in Line 4 is closest in meaning to:",
         [("A", "balances or cancels out"),
          ("B", "multiplies rapidly"),
          ("C", "freezes instantly"),
          ("D", "permanently destroys")],
         "A", "'Neutralizes' bermakna menyeimbangkan atau menetralkan perbedaan muatan ('balances / cancels out')."),

        (93, "According to paragraph 1, how many lightning flashes occur worldwide each second?",
         [("A", "About two thousand"),
          ("B", "Roughly one hundred"),
          ("C", "Only five or six"),
          ("D", "Nearly ten thousand")],
         "B", "Paragraf 1 menyatakan terjadi sekitar 100 kilatan petir setiap detiknya di seluruh dunia."),

        (94, "The word 'buoyant' in Line 10 is closest in meaning to:",
         [("A", "heavy and sinking"),
          ("B", "tending to float or rise"),
          ("C", "toxic and flammable"),
          ("D", "bright and shining")],
         "B", "'Buoyant' berarti berbobot ringan dan cenderung mengapung atau melayang naik ('tending to float/rise')."),

        (95, "According to paragraph 2, what causes the transfer of electrons in a storm cloud?",
         [("A", "Direct solar radiation hitting the cloud top."),
          ("B", "Collisions and friction between ice crystals and falling graupel."),
          ("C", "Chemical reactions between nitrogen and oxygen gas."),
          ("D", "Radio waves transmitted from surface stations.")],
         "B", "Transfer elektron terjadi akibat tabrakan dan gesekan antara kristal es dan butiran graupel yang jatuh."),

        (96, "What charge does the lighter ice crystal acquire after colliding with graupel?",
         [("A", "A neutral charge"),
          ("B", "A positive charge"),
          ("C", "A negative charge"),
          ("D", "A magnetic charge")],
         "B", "Kristal es yang lebih ringan kehilangan elektron sehingga bermuatan positif ('positively charged')."),

        (97, "The word 'streamers' in Line 20 refers to:",
         [("A", "decorative paper ribbons"),
          ("B", "channels of electrical charge reaching upward"),
          ("C", "gusts of cold surface wind"),
          ("D", "drops of condensed rainwater")],
         "B", "'Streamers' dalam konteks listrik petir adalah kanal lonjakan muatan listrik yang bergerak naik dari permukaan tanah."),

        (98, "According to paragraph 3, how hot does the lightning air channel become?",
         [("A", "One hundred degrees Celsius"),
          ("B", "About thirty thousand degrees Celsius"),
          ("C", "Five hundred degrees Celsius"),
          ("D", "The exact temperature of ice water")],
         "B", "Suhu kanal udara petir mencapai 30.000 derajat Celsius (5 kali lebih panas dari permukaan matahari)."),

        (99, "What directly produces the acoustic sound of thunder?",
         [("A", "Hail particles hitting the ground at high speeds."),
          ("B", "The explosive thermal expansion of superheated air."),
          ("C", "Raindrops evaporating inside the cloud."),
          ("D", "Strong wind blowing through telephone cables.")],
         "B", "Guntur dihasilkan oleh pemuaian termal yang sangat cepat dan eksplosif dari udara yang super panas."),

        (100, "Which of the following can be inferred about objects on the ground that attract lightning?",
         [("A", "Tall, elevated structures are more likely to initiate positive streamers."),
          ("B", "Flat, low ground surfaces always receive lightning first."),
          ("C", "Wooden trees never conduct electrical current."),
          ("D", "Rubber roofs completely prevent lightning formation anywhere.")],
         "A", "Dapat disimpulkan bahwa bangunan tinggi dan menara logam lebih mudah memicu streamer positif untuk menyambar petir.")
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

    # Passage 2: Dinosaur Feathers and Origin of Flight (Q101 - Q110)
    p2_title = "Passage 2: Non-Avian Dinosaur Feathers and Avian Evolution"
    p2_source = "Source: Adapted from American Museum of Natural History Paleontology Series"
    p2_text = """<p><span class="line-num">Line 1</span> For more than a century following the discovery of Archaeopteryx in 1861, feathers were considered the exclusive anatomical badge of birds. Paleontologists assumed that feathers had evolved specifically to facilitate aerodynamic flight. However, spectacular fossil discoveries from the Liaoning province of northeastern China during the late 1990s fundamentally dismantled this long-standing dogma. Preserved in fine-grained volcanic ash lakebeds, fossils of numerous non-avian theropod dinosaurs—including Sinosauropteryx and Caudipteryx—revealed clear impressions of primitive feathers.</p>
<p><span class="line-num">Line 8</span> These early integumentary structures, often dubbed proto-feathers, were not broad, asymmetrical aerodynamic flight feathers. Instead, they were simple, hollow, branched filaments resembling soft down. Because these small terrestrial carnivores had short, stubby forelimbs incapable of flight, evolutionary biologists deduced that feathers did not initially originate for aerial locomotion. Instead, proto-feathers evolved as thermal insulation, helping active, warm-blooded dinosaurs maintain homeostatic body temperatures in temperate Cretaceous climates.</p>
<p><span class="line-num">Line 16</span> Furthermore, microscopic analysis of fossilized pigment-bearing structures called melanosomes indicates that many dinosaur feathers possessed striking colors and iridescent banding patterns. These vibrant displays strongly suggest that feathers served vital social functions, including courtship displays and species recognition. Over millions of years, natural selection co-opted these insulating, colorful structures, gradually lengthening and stiffening them into planar surfaces that permitted tree-gliding and, ultimately, powered flapping flight in modern avian lineages.</p>"""

    p2_questions = [
        (101, "What is the primary topic of the passage?",
         [("A", "The catastrophic extinction of Cretaceous dinosaurs."),
          ("B", "The evolutionary origin and original functions of dinosaur feathers."),
          ("C", "Methods for excavating fossils from volcanic rocks."),
          ("D", "The aerodynamic principles of modern commercial airplanes.")],
         "B", "Teks membahas asal-usul evolusi dan fungsi awal bulu dinosaurus non-unggas sebelum digunakan untuk terbang."),

        (102, "Prior to the 1990s discoveries, what was the prevailing scientific belief regarding feathers?",
         [("A", "Feathers were unique to birds and evolved solely for flight."),
          ("B", "All reptiles originally had colorful feathers."),
          ("C", "Birds evolved directly from marine mammals."),
          ("D", "Feathers were invented by human ancestors for clothing.")],
         "A", "Sebelum penemuan fosil di Liaoning, bulu diyakini eksklusif milik burung dan berevolusi khusus untuk terbang."),

        (103, "The word 'dismantled' in Line 5 is closest in meaning to:",
         [("A", "disproved or overturned"),
          ("B", "supported strongly"),
          ("C", "published widely"),
          ("D", "carefully copied")],
         "A", "'Dismantled' berarti mematahkan, meruntuhkan, atau membatalkan teori lama ('disproved / overturned')."),

        (104, "Why were the Liaoning fossils so exceptionally well preserved?",
         [("A", "They were preserved in fine-grained volcanic ash in ancient lakebeds."),
          ("B", "They were frozen in giant Arctic ice sheets."),
          ("C", "They were mummified in hot desert sand dunes."),
          ("D", "They were submerged in salt water barrels.")],
         "A", "Fosil terawetkan sangat sempurna karena terkubur abu vulkanik berbutir halus di dasar danau kuno."),

        (105, "What did the earliest proto-feathers physically resemble?",
         [("A", "Broad, stiff airplane wings"),
          ("B", "Simple, hollow downy filaments"),
          ("C", "Sharp, bony defensive quills"),
          ("D", "Long, scaly reptile tails")],
         "B", "Bulu purba berbentuk filamen sederhana berongga yang menyerupai bulu halus burung muda ('soft down')."),

        (106, "The word 'deduced' in Line 12 is closest in meaning to:",
         [("A", "inferred through reasoning"),
          ("B", "accidentally discovered"),
          ("C", "refused to believe"),
          ("D", "measured in weight")],
         "A", "'Deduced' bermakna menyimpulkan berdasarkan bukti logis ('inferred through reasoning')."),

        (107, "According to paragraph 2, what was the primary initial function of proto-feathers?",
         [("A", "Catching small flying insects"),
          ("B", "Thermal insulation to retain body heat"),
          ("C", "Gliding across wide rivers"),
          ("D", "Digging underground nests")],
         "B", "Bulu halus awal berevolusi untuk isolasi termal (menjaga suhu tubuh dinosaurus berdarah panas)."),

        (108, "What do fossilized melanosomes reveal about dinosaur feathers?",
         [("A", "Their chemical toxicity"),
          ("B", "Their colors and visual patterns"),
          ("C", "Their exact flight speeds"),
          ("D", "Their nutritional value to predators")],
         "B", "Melanosom membuktikan warna dan pola garis berkilau pada bulu dinosaurus."),

        (109, "The word 'co-opted' in Line 19 is closest in meaning to:",
         [("A", "adapted for a new purpose"),
          ("B", "permanently destroyed"),
          ("C", "hidden from view"),
          ("D", "artificially manufactured")],
         "A", "'Co-opted' dalam konteks evolusi berarti mengadaptasi struktur yang sudah ada untuk fungsi baru."),

        (110, "Which of the following can be inferred from the final paragraph?",
         [("A", "Flight evolved instantly in a single generation of dinosaurs."),
          ("B", "Flight evolved gradually from structures originally used for insulation and display."),
          ("C", "Modern birds have lost the ability to grow colorful feathers."),
          ("D", "Dinosaurs used wings primarily to swim underwater.")],
         "B", "Dapat disimpulkan kemampuan terbang berevolusi secara bertahap dari struktur yang mulanya berfungsi sebagai penghangat dan display visual.")
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

    # Passage 3: Peatlands and Global Carbon Storage (Q111 - Q120)
    p3_title = "Passage 3: Tropical and Boreal Peatlands in Global Carbon Regulation"
    p3_source = "Source: Adapted from United Nations Environment Programme (UNEP) Global Peatland Assessment"
    p3_text = """<p><span class="line-num">Line 1</span> Peatlands are unique wetland ecosystems characterized by the accumulation of partially decayed organic vegetable matter known as peat. Although covering merely three percent of the global land surface, peatlands store more than five hundred and fifty gigatons of carbon. This staggering figure is double the total carbon stored in all the world's forests combined. Found in both high-latitude boreal regions and equatorial tropical swamp basins such as Indonesia and the Congo, peatlands represent the most space-efficient terrestrial carbon sink on the planet.</p>
<p><span class="line-num">Line 8</span> The secret behind peat's immense carbon-storing capability is water saturation. Under permanently waterlogged, anaerobic conditions, oxygen cannot penetrate the dense, saturated soil matrix. Deprived of oxygen, decomposer microbes and fungi operate at an exceptionally sluggish pace. Plant biomass, primarily mosses, sedges, and rainforest fallen leaves, accumulates much faster than it can decompose. Over millennia, layer upon layer of compressed organic carbon is preserved in deep subterranean layers up to twenty meters thick.</p>
<p><span class="line-num">Line 16</span> Unfortunately, peatlands worldwide face escalating degradation from canal drainage, agricultural conversion, and wildfires. When peat swamps are drained with drainage canals, oxygen rushes into the dried organic layers, triggering rapid microbial decomposition. The desiccated peat shifts from a long-term carbon sink into a catastrophic greenhouse gas emitter, releasing billions of tons of carbon dioxide and toxic haze into the atmosphere. Restoring these fragile wetland matrices through canal blocking and rewetting is recognized as one of the most cost-effective global nature-based climate solutions.</p>"""

    p3_questions = [
        (111, "What is the primary message of the passage?",
         [("A", "How peat moss is packaged for commercial gardening."),
          ("B", "The extraordinary carbon storage capacity of peatlands and the perils of draining them."),
          ("C", "The migration patterns of tropical birds in swamp forests."),
          ("D", "Methods for building highways across wetland swamps.")],
         "B", "Teks berfokus pada daya simpan karbon luar biasa lahan gambut serta ancaman emisi gas rumah kaca saat lahan tersebut dikeringkan."),

        (112, "What percentage of the world's land surface do peatlands cover?",
         [("A", "Approximately three percent"),
          ("B", "Nearly twenty-five percent"),
          ("C", "Fifty percent"),
          ("D", "Seventy percent")],
         "A", "Lahan gambut hanya menutupi sekitar 3 persen dari total permukaan daratan Bumi ('merely 3 percent')."),

        (113, "How does the carbon stored in peatlands compare to that in all world forests combined?",
         [("A", "Peatlands store half as much carbon as forests."),
          ("B", "Peatlands store twice as much carbon as all forests combined."),
          ("C", "Peatlands store an identical amount of carbon."),
          ("D", "Peatlands store almost no carbon at all.")],
         "B", "Jumlah karbon yang tersimpan di gambut adalah dua kali lipat dari seluruh hutan dunia digabungkan."),

        (114, "The word 'staggering' in Line 4 is closest in meaning to:",
         [("A", "astounding or astonishing"),
          ("B", "insignificant"),
          ("C", "uncertain"),
          ("D", "dangerous")],
         "A", "'Staggering' bermakna sangat mencengangkan / luar biasa besar ('astounding / astonishing')."),

        (115, "Why is organic plant matter preserved without fully decaying in peat bogs?",
         [("A", "Extremely hot temperatures sterilize the soil."),
          ("B", "Waterlogged, oxygen-deprived conditions prevent fast microbial decay."),
          ("C", "Salt water preserves the vegetation like pickles."),
          ("D", "Toxic industrial chemicals kill all bacteria.")],
         "B", "Kondisi jenuh air dan tanpa oksigen (anaerobik) memperlambat aktivitas mikroba pengurai sehingga tanaman tidak membusuk."),

        (116, "The word 'sluggish' in Line 11 is closest in meaning to:",
         [("A", "slow-moving and inactive"),
          ("B", "rapid and energetic"),
          ("C", "highly toxic"),
          ("D", "erratic")],
         "A", "'Sluggish' berarti sangat lambat / lamban ('slow-moving / inactive')."),

        (117, "What happens when drainage canals are dug into peat swamps?",
         [("A", "The peat produces fresh drinking water."),
          ("B", "Oxygen enters the dried soil, causing rapid decomposition and massive CO2 emissions."),
          ("C", "Fish populations increase dramatically."),
          ("D", "The soil becomes permanently fireproof.")],
         "B", "Pengeringan saluran menyebabkan oksigen masuk ke lapisan gambut, memicu pembusukan cepat dan pelepasan gas CO2 besar-besaran."),

        (118, "The word 'desiccated' in Line 19 is closest in meaning to:",
         [("A", "completely dried out"),
          ("B", "freshly planted"),
          ("C", "heavily frozen"),
          ("D", "deeply flooded")],
         "A", "'Desiccated' bermakna kering kerontang / mengering total ('completely dried out')."),

        (119, "According to paragraph 3, what is one of the most cost-effective methods for restoring damaged peatlands?",
         [("A", "Paving the entire swamp with asphalt."),
          ("B", "Rewetting the land by blocking artificial drainage canals."),
          ("C", "Spraying chemical fertilizers across the bog."),
          ("D", "Digging deeper canals to drain the water into the sea.")],
         "B", "Metode pemulihan gambut yang efektif adalah pembasahan kembali (rewetting) dengan menutup/membendung kanal drainase."),

        (120, "It can be inferred from the passage that preserving intact peatlands:",
         [("A", "has little relevance to global climate goals."),
          ("B", "is a crucial natural strategy in mitigating worldwide climate change."),
          ("C", "reduces the agricultural economy of all nations to zero."),
          ("D", "is impossible without converting all swamps into cities.")],
         "B", "Menjaga kelestarian gambut merupakan strategi alami yang sangat krusial dalam mitigasi perubahan iklim global.")
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

    # Passage 4: Steam Tractors and American Agriculture (Q121 - Q130)
    p4_title = "Passage 4: Steam Traction Engines and Farm Mechanization"
    p4_source = "Source: Adapted from Smithsonian National Museum of American History Archives"
    p4_text = """<p><span class="line-num">Line 1</span> During the late nineteenth and early twentieth centuries, the introduction of steam traction engines sparked a profound revolution in agricultural productivity across the American prairie. Before mechanical power, plowing the dense, compacted sod of the Great Plains was a punishing task that required teams of six to eight draft horses or oxen. A farmer with a horse-drawn steel plow could cultivate at most two acres per day, limiting farm size and tying the vast majority of the human population to grueling manual labor.</p>
<p><span class="line-num">Line 8</span> The advent of massive, coal-fired steam tractors altered farming scales overnight. Weighing upwards of twenty tons and featuring immense iron wheels with cleated treads, these rumbling behemoths possessed the tractive pull of thirty horses. A single steam engine could drag gang plows cutting a dozen furrows simultaneously, breaking up to fifty acres of tough prairie soil in a twelve-hour workday. Furthermore, through wide belt pulleys connected to their flywheel shafts, steam tractors powered threshing machines that separated wheat grains from chaff far faster than entire community harvesting crews.</p>
<p><span class="line-num">Line 16</span> Despite their immense power, steam tractors suffered from notable operational shortcomings. They were dangerously cumbersome, frequently sinking into soft mud, and required an enormous logistical support crew to haul hundreds of gallons of water and tons of coal daily to keep their boilers steaming. Sparks from their smokestacks frequently ignited devastating prairie wildfires. Consequently, when lighter, more nimble tractors powered by internal combustion gasoline engines arrived in the 1920s, steam behemoths were rapidly decommissioned, leaving behind a legacy as the iron pioneers of modern mechanized food production.</p>"""

    p4_questions = [
        (121, "What is the author's primary purpose in writing this passage?",
         [("A", "To describe the feeding habits of farm draft horses."),
          ("B", "To examine the impact, capabilities, and limitations of early steam farm tractors."),
          ("C", "To explain how modern gasoline combines are manufactured."),
          ("D", "To critique nineteenth-century grain storage elevators.")],
         "B", "Teks bertujuan mengulas dampak, kemampuan kerja, dan kelemahan traktor uap pertanian awal abad ke-20."),

        (122, "Prior to mechanical tractors, how many acres could a farmer plow in a single day with horses?",
         [("A", "Up to fifty acres"),
          ("B", "At most two acres"),
          ("C", "Ten to fifteen acres"),
          ("D", "Over one hundred acres")],
         "B", "Sebelum mekanisasi, petani dengan bajak kuda maksimal hanya membajak 2 acre per hari ('at most two acres')."),

        (123, "The word 'grueling' in Line 6 is closest in meaning to:",
         [("A", "exhausting and demanding"),
          ("B", "pleasant and relaxing"),
          ("C", "inexpensive"),
          ("D", "modern and clean")],
         "A", "'Grueling' bermakna sangat melelahkan dan menguras tenaga ('exhausting and demanding')."),

        (124, "The word 'behemoths' in Line 10 refers to:",
         [("A", "wild prairie buffalo"),
          ("B", "enormous, powerful machines"),
          ("C", "deep river trenches"),
          ("D", "dangerous storms")],
         "B", "'Behemoths' mengacu pada mesin traktor uap raksasa yang berbobot hingga 20 ton."),

        (125, "How many acres of prairie soil could a steam tractor plow during a twelve-hour workday?",
         [("A", "Two acres"),
          ("B", "Up to fifty acres"),
          ("C", "Exactly ten acres"),
          ("D", "Less than one acre")],
         "B", "Traktor uap dapat membajak tanah prairi hingga lima puluh acre dalam satu hari kerja 12 jam."),

        (126, "How did steam engines power grain threshing machines?",
         [("A", "Through wireless electrical radio transmission."),
          ("B", "Via wide belt pulleys connected to their rotating flywheels."),
          ("C", "By dripping hot boiler steam directly onto the crops."),
          ("D", "Through hydraulic hoses filled with vegetable oil.")],
         "B", "Tenaga disalurkan melalui sabuk katrol (belt pulleys) yang terhubung ke poros flywheel mesin."),

        (127, "The word 'cumbersome' in Line 17 is closest in meaning to:",
         [("A", "heavy, bulky, and difficult to manage"),
          ("B", "tiny and lightweight"),
          ("C", "inexpensive to buy"),
          ("D", "noiseless and smooth")],
         "A", "'Cumbersome' bermakna berat, besar, dan sulit dikendalikan ('heavy, bulky, and awkward to manage')."),

        (128, "According to paragraph 3, which of the following was a serious hazard associated with steam tractors?",
         [("A", "They frequently ignited prairie wildfires with boiler sparks."),
          ("B", "Their iron wheels rusted away in dry dust."),
          ("C", "They frightened wild draft horses off cliffs."),
          ("D", "They poisoned groundwater with radioactive isotopes.")],
         "A", "Percikan api dari cerobong asap traktor sering kali memicu kebakaran padang rumput prairi yang berbahaya."),

        (129, "Why were steam tractors replaced by gasoline tractors in the 1920s?",
         [("A", "Gasoline tractors were lighter, more nimble, and did not require heavy coal and water hauling."),
          ("B", "Coal was legally banned from all American farms."),
          ("C", "Farmers preferred to return to manual horse plowing."),
          ("D", "Steam tractors were too fast for operators to control.")],
         "A", "Traktor bensin lebih ringan, gesit, dan tidak membutuhkan pasokan ratusan galon air serta berton-ton batu bara setiap harinya."),

        (130, "The word 'decommissioned' in Line 23 is closest in meaning to:",
         [("A", "taken out of service"),
          ("B", "celebrated with medals"),
          ("C", "exported overseas"),
          ("D", "rebuilt with stone")],
         "A", "'Decommissioned' bermakna diberhentikan dari operasional / dipensiunkan ('taken out of service').")
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

    # Passage 5: Shape-Memory Alloys (Q131 - Q140)
    p5_title = "Passage 5: Smart Materials and Shape-Memory Alloys"
    p5_source = "Source: Adapted from Scientific American Materials Science & Engineering Review"
    p5_text = """<p><span class="line-num">Line 1</span> In conventional metallurgy, when a metal is bent past its elastic limit, the resulting deformation is permanent. However, a revolutionary class of smart materials known as shape-memory alloys (SMAs) defies this classical behavior. These metallic compounds can be severely contorted at low temperatures, yet upon moderate heating, they instantly remember and revert to their original, undeformed geometry with astonishing precision and mechanical force.</p>
<p><span class="line-num">Line 7</span> The most prominent and commercially viable shape-memory alloy is Nitinol, an intermetallic compound composed of roughly equal atomic proportions of nickel and titanium. Discovered accidentally in 1959 by metallurgist William J. Buehler at the U.S. Naval Ordnance Laboratory, Nitinol's shape memory arises from a reversible solid-state phase transformation. At low temperatures, Nitinol exists in a crystal structure called martensite, which is soft, ductile, and easily deformed by rearranging internal atomic twins. When heated past a specific transformation threshold, the crystal lattice shifts instantaneously into a rigid cubic arrangement known as austenite, returning the material to its preset configuration.</p>
<p><span class="line-num">Line 16</span> This thermal responsiveness has opened up groundbreaking applications across biomedicine and robotics. In vascular surgery, miniature Nitinol mesh tubes called stents are compressed into chilled catheters and threaded through blood vessels. Upon contact with warm body temperature at thirty-seven degrees Celsius, the stent automatically expands against clogged arterial walls, restoring healthy blood flow without mechanical balloons. In aerospace engineering, shape-memory actuators replace heavy hydraulic motors and noisy pneumatic pumps, enabling lightweight spacecraft antennas to unfurl silently in the vacuum of space.</p>"""

    p5_questions = [
        (131, "What is the primary subject of the passage?",
         [("A", "The history of deep-sea naval exploration."),
          ("B", "The unique properties, crystal transformation, and applications of shape-memory alloys."),
          ("C", "Methods for recycling scrap nickel in smelting plants."),
          ("D", "The dangers of titanium corrosion in saltwater.")],
         "B", "Teks membahas sifat unik, transformasi kisi kristal martensit-austenit, serta aplikasi inovatif paduan memori bentuk (SMAs)."),

        (132, "How do shape-memory alloys differ from ordinary metals?",
         [("A", "They melt into liquid at freezing temperatures."),
          ("B", "They recover their original shape when heated after being deformed."),
          ("C", "They are completely transparent like optical glass."),
          ("D", "They are incapable of conducting heat or electricity.")],
         "B", "Paduan memori bentuk dapat kembali ke bentuk aslinya saat dipanaskan setelah dideformasi pada suhu rendah."),

        (133, "The word 'contorted' in Line 4 is closest in meaning to:",
         [("A", "twisted or deformed out of shape"),
          ("B", "painted with bright enamel"),
          ("C", "cleaned with acid"),
          ("D", "cooled until solid")],
         "A", "'Contorted' berarti ditekuk, dibengkokkan, atau diubah bentuknya ('twisted / bent out of shape')."),

        (134, "What two metallic elements compose the alloy Nitinol?",
         [("A", "Copper and zinc"),
          ("B", "Nickel and titanium"),
          ("C", "Iron and carbon"),
          ("D", "Aluminum and gold")],
         "B", "Nitinol merupakan paduan atom nikel dan titanium ('nickel and titanium')."),

        (135, "What crystal phase exists when Nitinol is cool, soft, and easily bendable?",
         [("A", "Austenite"),
          ("B", "Martensite"),
          ("C", "Silica"),
          ("D", "Basalt")],
         "B", "Pada suhu rendah, kisi kristal berada pada fase martensit (martensite) yang lunak dan mudah dibentuk."),

        (136, "The word 'threshold' in Line 13 is closest in meaning to:",
         [("A", "starting point or boundary level"),
          ("B", "measurement error"),
          ("C", "surface flaw"),
          ("D", "expensive cost")],
         "A", "'Threshold' bermakna ambang batas atau titik awal transformasi ('starting point / boundary level')."),

        (137, "According to paragraph 3, how does a Nitinol medical stent expand inside a clogged artery?",
         [("A", "Doctors inject pressurized air through a needle."),
          ("B", "It automatically expands when warmed by natural human body temperature."),
          ("C", "An electrical wire zaps the stent with high voltage."),
          ("D", "Chemical acids dissolve the exterior coating.")],
         "B", "Stent memuai sendiri saat terpapar suhu tubuh manusia (37°C) tanpa membutuhkan balon mekanis."),

        (138, "The word 'unfurl' in Line 21 is closest in meaning to:",
         [("A", "open up and spread out"),
          ("B", "break into pieces"),
          ("C", "corrode quickly"),
          ("D", "freeze solid")],
         "A", "'Unfurl' bermakna membuka atau membentang perlahan ('open up / unfold')."),

        (139, "Why are shape-memory actuators advantageous in spacecraft design?",
         [("A", "They replace heavy hydraulic motors and operate silently without pumps."),
          ("B", "They are made of heavy lead that shields radiation."),
          ("C", "They emit bright colored lights in space."),
          ("D", "They are disposable after only one second of use.")],
         "A", "Aktuator SMA menggantikan motor hidrolik yang berat dan pompa berisik, memungkinkan pembentangan antena tanpa getaran."),

        (140, "Which of the following can be inferred about the future potential of smart alloys?",
         [("A", "Their medical and technological applications will continue expanding into diverse engineering sectors."),
          ("B", "They will soon be banned due to excessive rigidity."),
          ("C", "They are only useful in underwater submarines."),
          ("D", "Their crystal lattices will permanently lock in place.")],
         "A", "Dapat disimpulkan paduan cerdas ini akan terus berkembang pesat dalam dunia biomedis, robotika, dan rekayasa antariksa.")
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

p2 = make_paket2_questions()
print(f"Generated Paket 2 raw: {len(p2)} questions.")
p2_balanced = enforce_key_balance(p2, target_seed=202)

js_content = "/**\n * BANK SOAL TOEFL ITP OTENTIK - PAKET 2 (140 SOAL)\n * Target Kompetensi: CEFR Level B1 (Passing Score >= 433, Setara IELTS Band 4.5 - 5.0)\n */\n\n"
js_content += "window.TOEFL_BANK_PAKET_2 = " + json.dumps(p2_balanced, indent=2, ensure_ascii=False) + ";\n"

out_path = r"c:\Users\LILI\OneDrive - PDK Jateng\Dokumen\TOEFL-Assessment-Test\bank-paket2.js"
with open(out_path, "w", encoding="utf-8") as f:
    f.write(js_content)
print(f"SUCCESS: Balanced bank-paket2.js written to {out_path}")
