# -*- coding: utf-8 -*-
"""
Generate Kisi-Kisi dan Kamus Vocabulary TOEFL B1 Tingkat XII (Excel .xlsx)
"""
import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter

wb = openpyxl.Workbook()

# Setup styles
font_family = "Segoe UI"
header_fill = PatternFill(start_color="1E3A8A", end_color="1E3A8A", fill_type="solid") # Dark Navy
section_fill = PatternFill(start_color="0284C7", end_color="0284C7", fill_type="solid") # Sky Blue
highlight_fill = PatternFill(start_color="FEF3C7", end_color="FEF3C7", fill_type="solid") # Warm Yellow
zebra_fill = PatternFill(start_color="F8FAFC", end_color="F8FAFC", fill_type="solid") # Very light slate

header_font = Font(name=font_family, size=11, bold=True, color="FFFFFF")
title_font = Font(name=font_family, size=14, bold=True, color="1E3A8A")
subtitle_font = Font(name=font_family, size=10, italic=True, color="475569")
bold_font = Font(name=font_family, size=10, bold=True, color="0F172A")
regular_font = Font(name=font_family, size=10, color="1E293B")
italic_font = Font(name=font_family, size=10, italic=True, color="475569")

thin_border = Border(
    left=Side(style='thin', color='CBD5E1'),
    right=Side(style='thin', color='CBD5E1'),
    top=Side(style='thin', color='CBD5E1'),
    bottom=Side(style='thin', color='CBD5E1')
)

align_center = Alignment(horizontal="center", vertical="center", wrap_text=True)
align_left = Alignment(horizontal="left", vertical="center", wrap_text=True)
align_right = Alignment(horizontal="right", vertical="center")

# -------------------------------------------------------------
# SHEET 1: Panduan & Standar B1
# -------------------------------------------------------------
ws1 = wb.active
ws1.title = "Panduan_Standar_B1"
ws1.views.sheetView[0].showGridLines = True

ws1.append(["PANDUAN ASESMEN & STANDAR TARGET KELULUSAN CEFR LEVEL B1"])
ws1.append(["TOEFL Assessment Test — Tingkat XII (Fase F) Tahun Pelajaran 2026/2027"])
ws1.append([])

ws1.cell(1, 1).font = title_font
ws1.cell(2, 1).font = subtitle_font

# Table 1: Konversi Skor
ws1.append(["1. MATRIKS EKUIVALENSI SKOR KELULUSAN (CEFR B1)"])
ws1.cell(4, 1).font = bold_font

headers_t1 = [
    "Tingkat Kemahiran (CEFR)", 
    "Rentang Skor TOEFL ITP", 
    "Ekuivalensi Band IELTS", 
    "Rentang Nilai Sekolah (1-100)", 
    "Status Kelulusan (KKTP Min. 75)", 
    "Karakteristik Kemampuan Bahasa Inggris Siswa"
]
ws1.append(headers_t1)
row_idx = 5
for col_idx in range(1, len(headers_t1) + 1):
    c = ws1.cell(row_idx, col_idx)
    c.fill = header_fill
    c.font = header_font
    c.alignment = align_center

data_t1 = [
    [
        "Level B2+ (Vantage / Upper Intermediate)",
        "543 – 677",
        "Band 5.5 – 6.5+",
        "85 – 100",
        "SANGAT MEMUASKAN",
        "Mampu memahami teks akademik kompleks, percakapan ilmiah mendalam, dan menggunakan struktur tata bahasa tingkat lanjut secara akurat."
    ],
    [
        "Level B1 (Independent User / Threshold)\n*TARGET UTAMA KELULUSAN*",
        "433 – 542",
        "Band 4.5 – 5.0",
        "75 – 84",
        "TUNTAS (LULUS KKTP)",
        "Mampu memahami gagasan utama teks dan audio seputar topik akademis & kehidupan nyata, mengenali kekeliruan tata bahasa umum, dan menangkap ide penting."
    ],
    [
        "Level High A2 (Pre-Intermediate)",
        "380 – 432",
        "Band 3.5 – 4.0",
        "60 – 74",
        "BELUM TUNTAS",
        "Mampu memahami informasi eksplisit sederhana namun masih kesulitan pada kalimat majemuk, idiom, dan inferensi bacaan panjang."
    ],
    [
        "Level A1 – A2 (Basic / Elementary)",
        "310 – 379",
        "Band <= 3.0",
        "1 – 59",
        "PERLU BIMBINGAN",
        "Hanya mampu memahami frasa dasar dan kosakata umum; membutuhkan bimbingan intensif dalam kosakata akademik dan struktur gramatikal."
    ]
]

for row in data_t1:
    ws1.append(row)
    cur_row = ws1.max_row
    is_target = "TARGET UTAMA" in row[0]
    for col_idx in range(1, len(row) + 1):
        c = ws1.cell(cur_row, col_idx)
        c.font = bold_font if (is_target or col_idx in [1, 5]) else regular_font
        c.border = thin_border
        if is_target:
            c.fill = highlight_fill
        elif cur_row % 2 == 0:
            c.fill = zebra_fill
        if col_idx in [2, 3, 4, 5]:
            c.alignment = align_center
        else:
            c.alignment = align_left

ws1.append([])
ws1.append(["2. STRUKTUR RESMI TOEFL ITP (TOTAL: 140 SOAL - 115 MENIT)"])
ws1.cell(ws1.max_row, 1).font = bold_font

headers_t2 = ["Bagian (Section)", "Format Sub-Bagian", "Jumlah Soal", "Alokasi Waktu", "Fokus Kompetensi Yang Diuji"]
ws1.append(headers_t2)
cur_row = ws1.max_row
for col_idx in range(1, len(headers_t2) + 1):
    c = ws1.cell(cur_row, col_idx)
    c.fill = section_fill
    c.font = header_font
    c.alignment = align_center

data_t2 = [
    ["Section 1: Listening Comprehension", "Part A: Short Dialogues (Soal 1–30)\nPart B: Longer Dialogues (Soal 31–38)\nPart C: Short Talks/Lectures (Soal 39–50)", "50 Butir", "~35–40 Menit", "Menangkap arti tersirat pembicara kedua (Part A), topik obrolan kampus (Part B), dan inti ceramah akademis ilmiah (Part C)."],
    ["Section 2: Structure & Written Expression", "Part A: Incomplete Sentences (Soal 51–65)\nPart B: Error Identification (Soal 66–90)", "40 Butir", "25 Menit", "Melengkapi kalimat dengan klausa baku (Part A) dan menemukan kata bergaris bawah A, B, C, D yang secara gramatikal salah (Part B)."],
    ["Section 3: Reading Comprehension", "5 Bacaan Otentik (@ 10 Soal, Soal 91–140)", "50 Butir", "55 Menit", "Menemukan ide pokok (main idea), rincian tersurat, pernyataan pengecualian (EXCEPT/NOT), kosakata konteks B1, dan rujukan kata ganti."],
    ["TOTAL KESELURUHAN", "3 Section Lengkap", "140 Butir Soal", "115 Menit", "Standar Resmi ETS TOEFL ITP Level 1"]
]

for row in data_t2:
    ws1.append(row)
    cur_row = ws1.max_row
    is_total = "TOTAL" in row[0]
    for col_idx in range(1, len(row) + 1):
        c = ws1.cell(cur_row, col_idx)
        c.font = bold_font if (is_total or col_idx in [1, 3, 4]) else regular_font
        c.border = thin_border
        if is_total:
            c.fill = PatternFill(start_color="E2E8F0", end_color="E2E8F0", fill_type="solid")
            c.alignment = align_center
        else:
            if col_idx in [3, 4]:
                c.alignment = align_center
            else:
                c.alignment = align_left

# -------------------------------------------------------------
# SHEET 2: Kisi-Kisi Section 1 Listening
# -------------------------------------------------------------
ws2 = wb.create_sheet("Kisi_Kisi_Listening")
ws2.views.sheetView[0].showGridLines = True
ws2.append(["KISI-KISI SECTION 1: LISTENING COMPREHENSION (50 SOAL)"])
ws2.append(["Sumber: ETS TOEFL ITP Level 1 Standard Specification (Diselaraskan ke Level CEFR B1)"])
ws2.append([])
ws2.cell(1, 1).font = title_font
ws2.cell(2, 1).font = subtitle_font

headers_l = ["No.", "Bagian (Part)", "Nomor Soal", "Bentuk Stimulus", "Indikator Soal & Keterampilan B1", "Strategi & Tips Menjawab"]
ws2.append(headers_l)
cur_row = 4
for col_idx in range(1, len(headers_l) + 1):
    c = ws2.cell(cur_row, col_idx)
    c.fill = header_fill
    c.font = header_font
    c.alignment = align_center

kisi_listening = [
    [1, "Part A", "1 – 5", "Percakapan Pendek Pria & Wanita (Kampus/Keseharian)", "Mengidentifikasi makna tersirat pada ucapan pembicara kedua (Restatement).", "Fokus penuh pada kalimat pembicara kedua; hindari kata-kata yang bunyinya persis sama."],
    [2, "Part A", "6 – 10", "Percakapan Pendek Pria & Wanita", "Memahami ungkapan negatif (Negative statements) dan ekspresi ganda.", "Perhatikan kata 'not', 'rarely', 'hardly' yang mengubah makna menjadi sebaliknya."],
    [3, "Part A", "11 – 15", "Percakapan Pendek Pria & Wanita", "Memahami saran/anjuran (Suggestions: Why not...?, Let's..., You'd better...).", "Pahami tindakan yang disarankan oleh pembicara kedua untuk memecahkan masalah."],
    [4, "Part A", "16 – 20", "Percakapan Pendek Pria & Wanita", "Menyimpulkan profesi pembicara, lokasi obrolan, atau benda yang dibicarakan (Inference: Who, Where, What).", "Cari kata kunci petunjuk tempat (laboratorium, perpustakaan, stasiun) atau alat."],
    [5, "Part A", "21 – 25", "Percakapan Pendek Pria & Wanita", "Memahami ungkapan persetujuan (Agreement: So do I, Me too, I'll say, You can say that again).", "Pahami bahwa pembicara kedua memiliki pendapat yang sama dengan pembicara pertama."],
    [6, "Part A", "26 – 30", "Percakapan Pendek Pria & Wanita", "Memahami makna idiom dan phrasal verbs sederhana tingkat B1 (give up, take off, look forward to).", "Pahami makna kontekstual idiom, bukan terjemahan kata per kata."],
    [7, "Part B", "31 – 34", "Percakapan Panjang 1 (Topik Akademik / Kehidupan Kampus)", "Menentukan gagasan utama obrolan dan informasi spesifik tentang tugas kuliah/praktikum.", "Catat garis besar topik di 2 kalimat pertama; perhatikan siapa yang mengajukan ide."],
    [8, "Part B", "35 – 38", "Percakapan Panjang 2 (Topik Karier / Magang Industri / Sains)", "Menemukan solusi masalah, prosedur kerja, dan rencana tindak lanjut pembicara.", "Dengarkan urutan langkah logis yang disepakati oleh kedua pembicara."],
    [9, "Part C", "39 – 42", "Monolog / Kuliah Singkat 1 (Bidang Ilmu Bumi / Ekologi Lingkungan)", "Mengidentifikasi topik utama kuliah mini dan penyebab fenomena alam (bencana, cuaca, tanah).", "Identifikasi topik pada kalimat pengantar narator/dosen di 15 detik pertama."],
    [10, "Part C", "43 – 46", "Monolog / Kuliah Singkat 2 (Bidang Sejarah Penemuan / Teknologi)", "Menjelaskan urutan kronologis penemuan mesin/teknologi dan dampaknya pada masyarakat.", "Fokus pada hubungan sebab-akibat (cause and effect) dan tahun/era penting."],
    [11, "Part C", "47 – 50", "Monolog / Kuliah Singkat 3 (Bidang Biologi / Kehidupan Satwa Liar)", "Menjelaskan mekanisme adaptasi hewan/tumbuhan terhadap lingkungan ekstrim.", "Perhatikan contoh spesifik yang diberikan oleh pembicara untuk memperjelas konsep."]
]

for row in kisi_listening:
    ws2.append(row)
    cur_row = ws2.max_row
    for col_idx in range(1, len(row) + 1):
        c = ws2.cell(cur_row, col_idx)
        c.font = regular_font
        c.border = thin_border
        if cur_row % 2 == 1:
            c.fill = zebra_fill
        if col_idx in [1, 2, 3]:
            c.alignment = align_center
        else:
            c.alignment = align_left

# -------------------------------------------------------------
# SHEET 3: Kisi-Kisi Section 2 Structure
# -------------------------------------------------------------
ws3 = wb.create_sheet("Kisi_Kisi_Structure")
ws3.views.sheetView[0].showGridLines = True
ws3.append(["KISI-KISI SECTION 2: STRUCTURE & WRITTEN EXPRESSION (40 SOAL)"])
ws3.append(["Standar Resmi ETS TOEFL ITP: Part A (15 Soal) & Part B (25 Soal)"])
ws3.append([])
ws3.cell(1, 1).font = title_font
ws3.cell(2, 1).font = subtitle_font

headers_s = ["No.", "Bagian", "Nomor Soal", "Bentuk Soal", "Fokus Tata Bahasa (Grammar Rule B1)", "Contoh Indikator Pengujian"]
ws3.append(headers_s)
cur_row = 4
for col_idx in range(1, len(headers_s) + 1):
    c = ws3.cell(cur_row, col_idx)
    c.fill = header_fill
    c.font = header_font
    c.alignment = align_center

kisi_structure = [
    [1, "Part A", "51 – 54", "Sentence Completion", "Subject-Verb Agreement & Kalimat Tunggal S-V", "Menentukan Subjek atau Predikat Kata Kerja yang hilang pada kalimat majemuk."],
    [2, "Part A", "55 – 57", "Sentence Completion", "Appositive Phrases (Keterangan Penjelas Noun)", "Memilih appositive yang benar tanpa mengacaukan keberadaan subjek utama."],
    [3, "Part A", "58 – 60", "Sentence Completion", "Adjective Clauses & Relative Pronouns (who, which, that)", "Melengkapi klausa relatif yang menerangkan subjek atau objek kalimat."],
    [4, "Part A", "61 – 62", "Sentence Completion", "Reduced Clauses (Participle -ing / -ed)", "Menentukan bentuk participle aktif (-ing) atau pasif (-ed) sebagai pengganti klausa."],
    [5, "Part A", "63 – 65", "Sentence Completion", "Inversion & Inverted Word Order (Negative Expressions)", "Menyusun pola inversi (Auxiliary + Subject + Verb) setelah kata 'Not only', 'Rarely', 'Seldom'."],
    [6, "Part B", "66 – 70", "Written Expression", "Kesalahan Subject-Verb Agreement (Singular vs Plural)", "Mendeteksi kesalahan kata kerja jamak dengan subjek tunggal (misal: 'The list of items ARE' -> 'IS')."],
    [7, "Part B", "71 – 75", "Written Expression", "Kesalahan Paralelisme Struktur (Parallel Structure)", "Mendeteksi ketidaksesuaian bentuk kata dalam konjungsi 'and', 'but', 'or' (noun, noun, dan VERB)."],
    [8, "Part B", "76 – 80", "Written Expression", "Kesalahan Bentuk Kata (Word Form: Adjective vs Adverb)", "Menemukan penggunaan kata sifat (adjective) di posisi kata keterangan (adverb) yang memodifikasi verb."],
    [9, "Part B", "81 – 85", "Written Expression", "Kesalahan Kata Benda Dapat/Tidak Dapat Dihitung (Countable vs Uncountable)", "Mengidentifikasi kesalahan penggunaan 'many vs much', 'few vs little', 'number vs amount'."],
    [10, "Part B", "86 – 90", "Written Expression", "Kesalahan Preposisi dan Pasangan Kata Kerja (Collocation/Preposition)", "Menemukan preposisi yang keliru setelah kata sifat/kerja tertentu (misal: 'depend ON', 'interested IN')."]
]

for row in kisi_structure:
    ws3.append(row)
    cur_row = ws3.max_row
    for col_idx in range(1, len(row) + 1):
        c = ws3.cell(cur_row, col_idx)
        c.font = regular_font
        c.border = thin_border
        if cur_row % 2 == 1:
            c.fill = zebra_fill
        if col_idx in [1, 2, 3]:
            c.alignment = align_center
        else:
            c.alignment = align_left

# -------------------------------------------------------------
# SHEET 4: Kisi-Kisi Section 3 Reading
# -------------------------------------------------------------
ws4 = wb.create_sheet("Kisi_Kisi_Reading")
ws4.views.sheetView[0].showGridLines = True
ws4.append(["KISI-KISI SECTION 3: READING COMPREHENSION (50 SOAL)"])
ws4.append(["5 Teks Akademik Otentik Otentik Disertai Nomor Baris (Line 5, 10, 15...)"])
ws4.append([])
ws4.cell(1, 1).font = title_font
ws4.cell(2, 1).font = subtitle_font

headers_r = ["No.", "Teks Bacaan", "Nomor Soal", "Bidang Ilmu & Sumber Otentik", "Tipe Pertanyaan TOEFL Otentik", "Indikator Keterampilan Siswa"]
ws4.append(headers_r)
cur_row = 4
for col_idx in range(1, len(headers_r) + 1):
    c = ws4.cell(cur_row, col_idx)
    c.fill = header_fill
    c.font = header_font
    c.alignment = align_center

kisi_reading = [
    [1, "Passage 1", "91 – 100", "Earth Science & Geologi\n(Smithsonian Institution / USGS)", "1. Main Idea / Primary Purpose\n2. Stated Detail Question\n3. Unstated Detail (NOT/EXCEPT)\n4. Vocabulary in Context\n5. Pronoun Reference\n6. Inference Question", "Menentukan gagasan pokok pembentukan batuan vulkanik, rincian proses letusan gunung api, mencari makna kata kontekstual, dan menyimpulkan dampak iklim."],
    [2, "Passage 2", "101 – 110", "Astronomy & Planetary Science\n(NASA JPL / Space Science)", "1. Topic / Main Subject\n2. Factual Detail Questions (2x)\n3. Negative Factual (EXCEPT)\n4. Contextual Vocabulary (2x)\n5. Pronoun Referent (it, they)\n6. Author's Purpose / Tone", "Menganalisis karakteristik atmosfer planet Mars, membandingkan unsur air es dengan Bumi, dan menentukan makna istilah astronomi dalam konteks kalimat."],
    [3, "Passage 3", "111 – 120", "Marine Biology & Ecology\n(National Geographic Society)", "1. Main Idea of the Passage\n2. Direct Factual Details (3x)\n3. Negative Detail (NOT mentioned)\n4. Vocabulary in Context (2x)\n5. Specific Line Reference", "Memahami ekosistem terumbu karang, faktor pemutihan karang (coral bleaching), dan menemukan kata ganti yang merujuk pada spesies laut tertentu."],
    [4, "Passage 4", "121 – 130", "American History & Industry\n(Library of Congress / Britannica)", "1. Primary Topic\n2. Historical Sequence / Cause-Effect\n3. Unstated Detail (EXCEPT)\n4. Contextual Synonym (2x)\n5. Paragraph Purpose", "Menguraikan perkembangan jalur kereta api lintas benua abad ke-19 dan dampak industrialisasi terhadap percepatan distribusi barang dan ekonomi kota."],
    [5, "Passage 5", "131 – 140", "Renewable Energy & Technology\n(Scientific American Archives)", "1. Central Theme of Passage\n2. Factual Advantages (2x)\n3. Negative Detail (Which is NOT true)\n4. Vocabulary in Context (2x)\n5. Logical Inference", "Menjelaskan prinsip kerja panel surya fotovoltaik generasi baru, efisiensi konversi daya, dan memprediksi masa depan transisi energi hijau terbarukan."]
]

for row in kisi_reading:
    ws4.append(row)
    cur_row = ws4.max_row
    for col_idx in range(1, len(row) + 1):
        c = ws4.cell(cur_row, col_idx)
        c.font = regular_font
        c.border = thin_border
        if cur_row % 2 == 1:
            c.fill = zebra_fill
        if col_idx in [1, 2, 3]:
            c.alignment = align_center
        else:
            c.alignment = align_left

# -------------------------------------------------------------
# SHEET 5: Kamus Vocabulary B1 TOEFL (120+ Kata Kunci)
# -------------------------------------------------------------
ws5 = wb.create_sheet("Kamus_Vocabulary_B1")
ws5.views.sheetView[0].showGridLines = True
ws5.append(["KAMUS KOSAKATA AKADEMIK TOEFL — LEVEL CEFR B1 (UNTUK PERSIAPAN SISWA)"])
ws5.append(["Kosakata Kunci yang Sering Muncul Beserta Padanan Sederhana & Contoh Kalimat"])
ws5.append([])
ws5.cell(1, 1).font = title_font
ws5.cell(2, 1).font = subtitle_font

headers_v = [
    "No.", 
    "Vocabulary Word", 
    "Part of Speech", 
    "Pronunciation (Phonetic)", 
    "Definisi Ringkas (English)", 
    "Arti (Bahasa Indonesia)", 
    "Padanan Sederhana (Level B1)", 
    "Contoh Kalimat Kontekstual Ujian"
]
ws5.append(headers_v)
cur_row = 4
for col_idx in range(1, len(headers_v) + 1):
    c = ws5.cell(cur_row, col_idx)
    c.fill = header_fill
    c.font = header_font
    c.alignment = align_center

vocab_list = [
    (1, "Accurate", "Adjective", "/ˈækjərət/", "Correct, exact, and without any mistakes", "Akurat, tepat, benar", "Correct, exact", "Scientists need accurate measurements to calculate the speed of light."),
    (2, "Adapt", "Verb", "/əˈdæpt/", "To adjust to new conditions or environment", "Menyesuaikan diri, beradaptasi", "Adjust, fit", "Desert plants adapt to dry climates by storing water in thick stems."),
    (3, "Adequate", "Adjective", "/ˈædɪkwət/", "Enough in quantity or of good quality", "Memadai, cukup", "Enough, sufficient", "Solar batteries require adequate sunlight to store electrical energy efficiently."),
    (4, "Alternative", "Noun / Adj", "/ɔːlˈtɜːrnətɪv/", "Another possibility or choice", "Alternatif, pilihan lain", "Another choice, option", "Wind energy serves as a clean alternative to coal and petroleum fuels."),
    (5, "Analyze", "Verb", "/ˈænəlaɪz/", "To examine something methodically and in detail", "Menganalisis, memeriksa teliti", "Examine, study", "Researchers analyze ancient fossils to understand climatic changes."),
    (6, "Apparent", "Adjective", "/əˈpærənt/", "Clearly visible or understood; obvious", "Jelas, nyata, tampak", "Clear, obvious", "It became apparent that the machine stopped working due to battery drainage."),
    (7, "Approximate", "Adjective", "/əˈprɒksɪmət/", "Close to the actual, but not completely accurate", "Perkiraan, mendekati", "Rough, close to", "The approximate distance between the two research stations is fifty miles."),
    (8, "Artificial", "Adjective", "/ˌɑːrtɪˈfɪʃl/", "Made or produced by human beings rather than naturally", "Buatan, tiruan", "Man-made, not real", "The greenhouse uses artificial lighting to speed up plant photosynthesis."),
    (9, "Aspect", "Noun", "/ˈæspekt/", "A particular part or feature of something", "Aspek, segi, sudut pandang", "Part, feature", "Safety is the most crucial aspect of operating industrial manufacturing machinery."),
    (10, "Benefit", "Noun / Verb", "/ˈbenɪfɪt/", "An advantage or profit gained from something", "Manfaat, keuntungan", "Advantage, help", "Regular English reading practice brings substantial benefits for test takers."),
    (11, "Capable", "Adjective", "/ˈkeɪpəbl/", "Having the ability, fitness, or quality necessary", "Mampu, cakap", "Able, talented", "Modern robotic sensors are capable of detecting toxic gas leaks instantly."),
    (12, "Circumstance", "Noun", "/ˈsɜːrkəmstæns/", "A condition connected to an event or action", "Keadaan, situasi, kondisi", "Situation, condition", "Under normal circumstances, the engine runs smoothly without overheating."),
    (13, "Complex", "Adjective", "/kəmˈpleks/", "Consisting of many different and connected parts", "Rumit, kompleks", "Complicated, not simple", "The human nervous system has a remarkably complex network of cells."),
    (14, "Component", "Noun", "/kəmˈpoʊnənt/", "A part or element of a larger whole", "Komponen, bagian", "Part, element", "Each electrical component in the circuit must be checked before assembly."),
    (15, "Concept", "Noun", "/ˈkɑːnsept/", "An abstract idea or general notion", "Konsep, gagasan dasar", "Idea, notion", "Students must understand the basic concept of gravity before physics lab."),
    (16, "Conclusion", "Noun", "/kənˈkluːʒn/", "The end or finish of an event or process", "Kesimpulan, akhir", "End, summary", "Based on laboratory data, the professor reached a definitive conclusion."),
    (17, "Conduct", "Verb", "/kənˈdʌkt/", "To organize and carry out a task or research", "Melaksanakan, melakukan", "Carry out, perform", "Engineers will conduct a safety inspection on the bridge tomorrow morning."),
    (18, "Consequence", "Noun", "/ˈkɑːnsəkwens/", "A result or effect of an action or condition", "Konsekuensi, akibat", "Result, outcome", "Soil erosion is a serious consequence of reckless deforestation on hills."),
    (19, "Considerable", "Adjective", "/kənˈsɪdərəbl/", "Notably large in size, amount, or extent", "Cukup besar, signifikan", "Large, significant", "Solar power technology has made considerable progress over the last decade."),
    (20, "Consistent", "Adjective", "/kənˈsɪstənt/", "Acting or done in the same way over time", "Konsisten, selaras", "Steady, unchanging", "Consistent effort in grammar exercises guarantees high achievement in TOEFL."),
    (21, "Construct", "Verb", "/kənˈstrʌkt/", "To build or erect something large", "Membangun, mendirikan", "Build, make", "Architects construct earthquake-resistant buildings using flexible steel frames."),
    (22, "Consumer", "Noun", "/kənˈsuːmər/", "A person who purchases goods and services", "Konsumen, pemakai", "Buyer, customer", "Informed consumers prefer eco-friendly products made of recycled materials."),
    (23, "Crucial", "Adjective", "/ˈkruːʃl/", "Decisive or critical, especially in the success", "Sangat penting, krusial", "Very important, vital", "Time management is a crucial factor during the 115-minute TOEFL exam."),
    (24, "Data", "Noun", "/ˈdeɪtə/", "Facts and statistics collected together for reference", "Data, keterangan fakta", "Facts, information", "The weather station gathers atmospheric data every fifteen minutes."),
    (25, "Demonstrate", "Verb", "/ˈdemənstreɪt/", "To clearly show the existence or truth of something", "Menunjukkan, membuktikan", "Show, prove", "The test results demonstrate that the new battery holds charge longer."),
    (26, "Distinct", "Adjective", "/dɪˈstɪŋkt/", "Recognizably different in nature from something else", "Berbeda, khas, nyata", "Different, clear", "The two bird species have distinct migration patterns during winter months."),
    (27, "Domestic", "Adjective", "/dəˈmestɪk/", "Relating to the running of a home or a country", "Domestik, dalam negeri", "Home, national", "The airport expanded its terminal to accommodate more domestic flights."),
    (28, "Economy", "Noun", "/ɪˈkɑːnəmi/", "The wealth and resources of a country or region", "Perekonomian", "Financial system", "Agricultural exports play an essential role in bolstering the national economy."),
    (29, "Efficient", "Adjective", "/ɪˈfɪʃnt/", "Achieving maximum productivity with minimum wasted effort", "Efisien, hemat daya", "Effective, well-working", "LED light bulbs are significantly more efficient than old incandescent lamps."),
    (30, "Element", "Noun", "/ˈelɪmənt/", "An essential or characteristic part of something", "Unsur, elemen, bagian penting", "Part, component", "Carbon is an essential chemical element present in all living organisms."),
    (31, "Emphasize", "Verb", "/ˈemfəsaɪz/", "Give special importance or prominence to something", "Menekankan, mengutamakan", "Stress, highlight", "The lecturer emphasized the importance of submitting lab reports on time."),
    (32, "Enable", "Verb", "/ɪˈneɪbl/", "Give the authority or means to do something", "Memungkinkan, menyanggupkan", "Allow, permit", "Advanced radar systems enable airplanes to navigate safely through heavy storms."),
    (33, "Environment", "Noun", "/ɪnˈvaɪrənmənt/", "The surroundings or conditions in which an organism operates", "Lingkungan hidup, alam sekitar", "Surroundings, nature", "Plastic waste threatens the marine environment and coral reef ecosystems."),
    (34, "Establish", "Verb", "/ɪˈstæblɪʃ/", "Set up on a firm or permanent basis", "Mendirikan, membentuk, menetapkan", "Set up, found", "The university was established in 1895 as a vocational technical college."),
    (35, "Estimate", "Verb / Noun", "/ˈestɪmeɪt/", "Roughly calculate or judge the value, number, or quantity", "Memperkirakan, taksiran", "Guess, calculate roughly", "Biologists estimate that thousands of unidentified insect species inhabit the rainforest."),
    (36, "Evidence", "Noun", "/ˈevɪdəns/", "Facts or information indicating whether a belief is true", "Bukti, tanda nyata", "Proof, facts", "Fossil footprints provide clear evidence that dinosaurs walked across muddy shores."),
    (37, "Examine", "Verb", "/ɪɡˈzæmɪn/", "Inspect someone or something in detail", "Memeriksa, meneliti", "Check, inspect", "Doctors examine the patient thoroughly before making a medical diagnosis."),
    (38, "Expand", "Verb", "/ɪkˈspænd/", "Become or make larger or more extensive", "Memperluas, berkembang", "Grow, enlarge", "Metals expand when heated and contract when cooled down to room temperature."),
    (39, "Export", "Verb / Noun", "/ˈekspɔːrt/", "Send goods or services to another country for sale", "Mengekspor, barang ekspor", "Send abroad", "Indonesia exports high-grade coffee and palm oil to international markets."),
    (40, "Factor", "Noun", "/ˈfæktər/", "A circumstance or influence that contributes to a result", "Faktor, unsur penentu", "Element, cause", "Adequate sleep and nutritious meals are key factors in maintaining physical stamina."),
    (41, "Feature", "Noun / Verb", "/ˈfiːtʃər/", "A distinctive attribute or aspect of something", "Fitur, ciri khas", "Characteristic, trait", "The main feature of this smartphone is its long-lasting lithium battery."),
    (42, "Function", "Noun / Verb", "/ˈfʌŋkʃn/", "An activity or purpose natural to or intended for a person/thing", "Fungsi, kegunaan, bekerja", "Purpose, role, work", "The primary function of white blood cells is defending the body against pathogens."),
    (43, "Generate", "Verb", "/ˈdʒenəreɪt/", "Produce or create something (e.g. power, heat, idea)", "Menghasilkan, membangkitkan", "Produce, create", "Hydroelectric dams generate clean electricity by utilizing rushing river currents."),
    (44, "Identify", "Verb", "/aɪˈdentɪfaɪ/", "Establish or indicate who or what something is", "Mengidentifikasi, mengenali", "Recognize, find", "Astronomers identify new celestial bodies using high-resolution space telescopes."),
    (45, "Impact", "Noun / Verb", "/ˈɪmpækt/", "The action of one object coming forcibly into contact; marked effect", "Dampak, pengaruh, benturan", "Effect, influence", "The eruption of Mount Tambora had an immediate impact on worldwide weather patterns."),
    (46, "Indicate", "Verb", "/ˈɪndɪkeɪt/", "Point out; show or be a sign of", "Menunjukkan, menandakan", "Show, signal", "Rising mercury levels in the thermometer indicate a rapid increase in room temperature."),
    (47, "Individual", "Noun / Adj", "/ˌɪndɪˈvɪdʒuəl/", "A single human being as distinct from a group", "Individu, perseorangan", "Single person, personal", "Every individual student has unique talents and distinct learning styles."),
    (48, "Initial", "Adjective", "/ɪˈnɪʃl/", "Existing or occurring at the beginning", "Awal, mula-mula", "First, beginning", "The initial phase of the construction project involved surveying the soil foundations."),
    (49, "Interaction", "Noun", "/ˌɪntərˈækʃn/", "Reciprocal action or influence", "Interaksi, hubungan timbal balik", "Communication, contact", "Social interaction among classmates improves confidence and communicative fluency."),
    (50, "Internal", "Adjective", "/ɪnˈtɜːrnl/", "Of or situated on the inside", "Internal, bagian dalam", "Inside, inner", "The internal combustion engine converts fuel combustion into mechanical rotational energy."),
    (51, "Interpret", "Verb", "/ɪnˈtɜːrprɪt/", "Explain the meaning of information, words, or actions", "Menafsirkan, mengartikan", "Explain, understand", "Historians interpret ancient cave paintings to learn about prehistoric rituals."),
    (52, "Involve", "Verb", "/ɪnˈvɑːlv/", "Include or contain as a necessary part", "Melibatkan, mengikutsertakan", "Include, contain", "Vocational training involves hands-on laboratory practice and real factory simulations."),
    (53, "Issue", "Noun / Verb", "/ˈɪʃuː/", "An important topic or problem for debate or discussion", "Isu, masalah penting", "Problem, topic", "Global warming is a critical environmental issue demanding worldwide cooperation."),
    (54, "Major", "Adjective", "/ˈmeɪdʒər/", "Important, serious, or significant", "Utama, besar, penting", "Big, main, important", "Deforestation remains a major cause of biodiversity loss in tropical regions."),
    (55, "Maintain", "Verb", "/meɪnˈteɪn/", "Cause or enable a condition or state of affairs to continue", "Memelihara, mempertahankan", "Keep up, preserve", "Regular vehicle servicing helps maintain engine efficiency and prevents accidents."),
    (56, "Method", "Noun", "/ˈmeθəd/", "A particular procedure for accomplishing or approaching something", "Metode, cara sistematis", "Way, technique", "The scientific method requires formulating hypotheses and testing them through experiments."),
    (57, "Modify", "Verb", "/ˈmɑːdɪfaɪ/", "Make partial or minor changes to something", "Memodifikasi, mengubah sedikit", "Change, adjust", "Automotive students learn how to modify car carburetors for better fuel mileage."),
    (58, "Negative", "Adjective", "/ˈneɡətɪv/", "Consisting in or characterized by the absence rather than presence", "Negatif, buruk", "Bad, harmful", "Prolonged exposure to loud industrial noise can have negative effects on hearing."),
    (59, "Obtain", "Verb", "/əbˈteɪn/", "Get, acquire, or secure something", "Memperoleh, mendapatkan", "Get, acquire", "Students must obtain a score of 75 or higher to fulfill the passing standard."),
    (60, "Occur", "Verb", "/əˈkɜːr/", "Happen; take place", "Terjadi, berlangsung", "Happen, take place", "Major earthquakes occur along tectonic plate boundaries surrounding the Pacific Ocean."),
    (61, "Outcome", "Noun", "/ˈaʊtkʌm/", "The way a thing turns out; a consequence", "Hasil akhir, dampak", "Result, consequence", "The successful launch of the communication satellite was a proud national outcome."),
    (62, "Participate", "Verb", "/pɑːrˈtɪsɪpeɪt/", "Take part in an action or event", "Berpartisipasi, ikut serta", "Join, take part", "All senior students are encouraged to participate in the English speech contest."),
    (63, "Perceive", "Verb", "/pərˈsiːv/", "Become aware or conscious of something; realize", "Melihat, mengamati, menyadari", "Notice, see, realize", "Birds perceive ultraviolet light frequencies that are completely invisible to humans."),
    (64, "Period", "Noun", "/ˈpɪriəd/", "A length or portion of time", "Periode, kurun waktu", "Time, era", "The Industrial Revolution was a period of rapid technological and mechanical innovation."),
    (65, "Policy", "Noun", "/ˈpɑːləsi/", "A course or principle of action adopted by an organization", "Kebijakan, aturan resmi", "Rule, plan of action", "The school enforces a strict policy regarding punctual attendance in lab sessions."),
    (66, "Positive", "Adjective", "/ˈpɑːzətɪv/", "Constructive, optimistic, or confident", "Positif, baik, menguntungkan", "Good, beneficial", "Constructive feedback from teachers produces a positive effect on student motivation."),
    (67, "Potential", "Noun / Adj", "/pəˈtenʃl/", "Having or showing the capacity to develop into something in future", "Potensial, kemungkinan besar", "Possible, promising", "Indonesia has tremendous potential for geothermal and solar renewable energy generation."),
    (68, "Previous", "Adjective", "/ˈpriːviəs/", "Existing or occurring before in time or order", "Sebelumnya, yang lalu", "Earlier, before", "Reviewing previous test questions helps students become familiar with the exam format."),
    (69, "Primary", "Adjective", "/ˈpraɪmeri/", "Of chief importance; principal", "Utama, pokok", "Main, chief", "The primary objective of this TOEFL test is assessing English proficiency at B1 level."),
    (70, "Principle", "Noun", "/ˈprɪnsəpl/", "A fundamental truth or proposition serving as the foundation", "Prinsip, asas dasar", "Rule, basic truth", "Hydraulic elevators operate on the physical principle of fluid pressure transmission."),
    (71, "Procedure", "Noun", "/prəˈsiːdʒər/", "An established or official way of doing something", "Prosedur, tata cara", "Steps, process", "Safety goggles must be worn following standard laboratory procedure during welding."),
    (72, "Process", "Noun / Verb", "/ˈprɑːses/", "A series of actions or steps taken in order to achieve a result", "Proses, mengolah", "Steps, handling", "Water purification is a multi-stage process involving filtration and chemical treatment."),
    (73, "Produce", "Verb", "/prəˈduːs/", "Make or manufacture from components or raw materials", "Memproduksi, menghasilkan", "Make, create", "The automated factory line can produce over five hundred electronic circuits hourly."),
    (74, "Promote", "Verb", "/prəˈmoʊt/", "Further the progress of something; encourage", "Mendorong, memajukan", "Encourage, support", "Schools promote environmental awareness by organizing regular plastic recycling drives."),
    (75, "Proportion", "Noun", "/prəˈpɔːrʃn/", "A part, share, or number considered in comparative relation", "Proporsi, perbandingan", "Part, ratio, share", "A substantial proportion of the school's electricity is supplied by rooftop solar cells."),
    (76, "Publish", "Verb", "/ˈpʌblɪʃ/", "Prepare and issue for public sale, distribution, or reading", "Menerbitkan, mempublikasikan", "Print, issue", "The research institution publishes annual findings on marine ecosystem conservation."),
    (77, "Range", "Noun / Verb", "/reɪndʒ/", "The area of variation between upper and lower limits", "Rentang, jangkauan", "Variety, scope, limit", "The score range for the TOEFL ITP test spans from 310 to a maximum of 677 points."),
    (78, "Region", "Noun", "/ˈriːdʒən/", "An area or division, especially part of a country or the world", "Wilayah, daerah", "Area, zone", "The coastal region of Central Java possesses vast mangrove forests protecting the shore."),
    (79, "Regulate", "Verb", "/ˈreɡjuleɪt/", "Control or maintain the rate or speed of a machine or process", "Mengatur, mengendalikan", "Control, manage", "Thermostats regulate room temperature by turning heating elements on or off."),
    (80, "Reliable", "Adjective", "/rɪˈlaɪəbl/", "Consistently good in quality or performance; trustworthy", "Dapat diandalkan, tepercaya", "Trustworthy, dependable", "Engineers need reliable diagnostic tools to detect electrical faults accurately."),
    (81, "Require", "Verb", "/rɪˈkwaɪər/", "Need for a particular purpose; depend on for success", "Membutuhkan, mewajibkan", "Need, demand", "Operating heavy machinery requires certified vocational training and personal safety gear."),
    (82, "Research", "Noun / Verb", "/ˈriːsɜːrtʃ/", "The systematic investigation into and study of materials", "Penelitian, meneliti", "Study, investigation", "Scientific research shows that regular physical exercise improves cognitive concentration."),
    (83, "Respond", "Verb", "/rɪˈspɑːnd/", "Say something in reply; react quickly", "Merespons, menanggapi", "Answer, react", "Emergency technicians responded promptly when the industrial fire alarm went off."),
    (84, "Restore", "Verb", "/rɪˈstɔːr/", "Bring back to original condition; repair", "Memulihkan, mengembalikan", "Bring back, repair", "Conservationists work tirelessly to restore depleted peatlands and coastal mangrove swamps."),
    (85, "Restricted", "Adjective", "/rɪˈstrɪktɪd/", "Limited in extent, number, or scope; confidential", "Terbatas, terlarang", "Limited, bounded", "Access to the server control room is strictly restricted to authorized network technicians."),
    (86, "Role", "Noun", "/roʊl/", "The function assumed or part played by a person or thing", "Peran, fungsi", "Part, function", "English plays a vital role as an international medium of communication and science."),
    (87, "Section", "Noun", "/ˈsekʃn/", "Any of the more or less distinct parts into which something is divided", "Bagian, seksi", "Part, division", "The TOEFL exam is divided into three distinct sections: Listening, Structure, and Reading."),
    (88, "Sector", "Noun", "/ˈsektər/", "An area or portion that is distinct from others (e.g. economy)", "Sektor, bidang", "Branch, field", "The vocational education sector equips high school graduates with high-demand job skills."),
    (89, "Shift", "Verb / Noun", "/ʃɪft/", "Move or cause to move from one position to another", "Pergeseran, beralih", "Change, move", "Automobile manufacturers are shifting their production lines toward electric vehicles."),
    (90, "Significant", "Adjective", "/sɪɡˈnɪfɪkənt/", "Sufficiently great or important to be worthy of attention", "Signifikan, sangat penting", "Important, notable", "There was a significant improvement in student test scores after intensive practice."),
    (91, "Similar", "Adjective", "/ˈsɪmələr/", "Resembling without being identical", "Mirip, serupa", "Alike, resembling", "Both species of pine trees have similar needle-like leaves and cylindrical cones."),
    (92, "Source", "Noun", "/sɔːrs/", "A place, person, or thing from which something originates", "Sumber, asal", "Origin, start", "The sun is the ultimate source of heat and radiant light energy for planet Earth."),
    (93, "Specific", "Adjective", "/spəˈsɪfɪk/", "Clearly defined or identified; precise", "Khusus, spesifik, jelas", "Exact, particular", "Each question in the Reading section refers to a specific paragraph in the passage."),
    (94, "Structure", "Noun", "/ˈstrʌktʃər/", "The arrangement of and relations between the parts or elements", "Struktur, susunan", "Setup, building", "Engineers analyzed the steel structure of the warehouse before installing solar arrays."),
    (95, "Substitute", "Noun / Verb", "/ˈsʌbstɪtuːt/", "A person or thing acting or serving in place of another", "Pengganti, menggantikan", "Replacement, replace", "Soy milk can serve as a nutritious substitute for cow's milk in many recipes."),
    (96, "Sufficient", "Adjective", "/səˈfɪʃnt/", "Enough; adequate for a purpose", "Cukup, memadai", "Enough, plenty", "Make sure your laptop has sufficient battery power before starting the online exam."),
    (97, "Survive", "Verb", "/sərˈvaɪv/", "Continue to live or exist, especially in spite of danger", "Bertahan hidup", "Live through, endure", "Polar bears possess thick insulating fat layers that enable them to survive freezing Arctic cold."),
    (98, "Technique", "Noun", "/tekˈniːk/", "A way of carrying out a particular task, especially skillful", "Teknik, keterampilan cara", "Method, skill", "Welding students practiced arc-welding techniques on scrap steel plates."),
    (99, "Technology", "Noun", "/tekˈnɑːlədʒi/", "The application of scientific knowledge for practical purposes", "Teknologi", "Applied science", "Advances in battery technology have dramatically improved the range of electric cars."),
    (100, "Theory", "Noun", "/ˈθiːəri/", "A supposition or a system of ideas intended to explain something", "Teori, penjelasan ilmiah", "Explanation, concept", "Albert Einstein proposed the theory of relativity to explain the nature of gravity and light."),
    (101, "Transfer", "Verb / Noun", "/trænsˈfɜːr/", "Move from one place, person, or group to another", "Memindahkan, mentransfer", "Move, shift", "The automated conveyor belt transfers finished goods straight to the storage warehouse."),
    (102, "Transform", "Verb", "/trænsˈfɔːrm/", "Make a marked change in the form, nature, or appearance", "Mengubah wujud, mentransformasi", "Change, convert", "Solar cells transform photon energy from sunlight directly into electrical voltage."),
    (103, "Transport", "Verb / Noun", "/ˈtrænspɔːrt/", "Take or carry people or goods from one place to another", "Mengangkut, transportasi", "Carry, convey", "Tanker ships transport crude oil across international sea shipping routes."),
    (104, "Ultimate", "Adjective", "/ˈʌltɪmət/", "Being or happening at the end of a process; final", "Terakhir, pokok, tertinggi", "Final, greatest", "The ultimate goal of language learning is fluent, respectful, and clear communication."),
    (105, "Undergo", "Verb", "/ˌʌndərˈɡoʊ/", "Experience or be subjected to something (e.g. change, test)", "Mengalami, menjalani", "Go through, experience", "The mechanical prototype must undergo rigorous load tests before mass production."),
    (106, "Uniform", "Adjective", "/ˈjuːnɪfɔːrm/", "Remaining the same in all cases and at all times", "Seragam, serba sama", "Even, identical", "The chemical mixture must be stirred thoroughly to achieve a uniform liquid density."),
    (107, "Unique", "Adjective", "/juˈniːk/", "Being the only one of its kind; unlike anything else", "Unik, khas, tiada duanya", "Special, one-of-a-kind", "Each fingerprint pattern is completely unique to an individual human being."),
    (108, "Utilize", "Verb", "/ˈjuːtəlaɪz/", "Make practical and effective use of", "Memanfaatkan, menggunakan", "Use, employ", "Agricultural engineers utilize drone mapping to monitor crop hydration across vast plantations."),
    (109, "Valid", "Adjective", "/ˈvælɪd/", "Having a sound basis in logic or fact; reasonable", "Sah, valid, beralasan kuat", "Sound, legitimate", "You must present a valid student identification card prior to entering the exam venue."),
    (110, "Variable", "Noun / Adj", "/ˈveriəbl/", "An element, feature, or factor that is liable to vary or change", "Variabel, peubah", "Changing factor", "Temperature is a critical variable influencing the rate of chemical decomposition in liquids."),
    (111, "Vehicle", "Noun", "/ˈviːəkl/", "A thing used for transporting people or goods", "Kendaraan, alat angkut", "Car, transport", "Electric vehicles produce zero tailpipe carbon emissions, preserving urban air quality."),
    (112, "Visible", "Adjective", "/ˈvɪzəbl/", "Able to be seen with the human eye", "Terlihat, tampak jelas", "Noticeable, seen", "The constellation of Orion is clearly visible in the clear night sky during December."),
    (113, "Visual", "Adjective", "/ˈvɪʒuəl/", "Relating to seeing or sight", "Visual, penglihatan", "Optical, seen", "Teachers use colorful visual charts to help students grasp abstract scientific diagrams."),
    (114, "Volume", "Noun", "/ˈvɑːljuːm/", "The amount of space that a substance or object occupies", "Volume, daya tampung", "Capacity, amount", "The storage cylinder has a maximum capacity volume of five thousand liters."),
    (115, "Widespread", "Adjective", "/ˈwaɪdspred/", "Found or distributed over a large area or number of people", "Meluas, tersebar luas", "Common, broad", "Smartphone ownership has become widespread among students of all age groups."),
    (116, "Abandon", "Verb", "/əˈbændən/", "Cease to support or look after; leave behind", "Meninggalkan, menelantarkan", "Leave, desert", "The crew had to abandon the sinking fishing vessel and board emergency lifeboats."),
    (117, "Accomplish", "Verb", "/əˈkɑːmplɪʃ/", "Achieve or complete successfully", "Menyelesaikan, meraih", "Achieve, finish", "Hard-working apprentices accomplished the mechanical overhaul well ahead of schedule."),
    (118, "Acquire", "Verb", "/əˈkwaɪər/", "Buy or obtain an asset or skill for oneself", "Memperoleh, menguasai", "Get, obtain, learn", "Vocational school students acquire specialized technical competencies through studio workshops."),
    (119, "Advocate", "Verb / Noun", "/ˈædvəkeɪt/", "Publicly recommend or support a particular cause or policy", "Menganjurkan, pendukung", "Support, recommend", "Environmental scientists advocate for an urgent global transition to clean wind and solar power."),
    (120, "Broaden", "Verb", "/ˈbrɔːdn/", "Become larger in distance from side to side; expand", "Memperluas, memperlebar", "Widen, expand", "Reading diverse international publications broadens students' global worldview and vocabulary.")
]

for row in vocab_list:
    ws5.append(row)
    cur_row = ws5.max_row
    for col_idx in range(1, len(row) + 1):
        c = ws5.cell(cur_row, col_idx)
        c.font = bold_font if col_idx in [1, 2] else regular_font
        c.border = thin_border
        if cur_row % 2 == 1:
            c.fill = zebra_fill
        if col_idx in [1, 3]:
            c.alignment = align_center
        else:
            c.alignment = align_left

# Auto adjust columns for all sheets
for sheet in wb.worksheets:
    for col in sheet.columns:
        col_letter = get_column_letter(col[0].column)
        max_len = 0
        for cell in col:
            val = str(cell.value or '')
            lines = val.split('\n')
            for l in lines:
                if len(l) > max_len:
                    max_len = len(l)
        sheet.column_dimensions[col_letter].width = min(max(max_len + 3, 10), 55)

excel_path = r"c:\Users\LILI\OneDrive - PDK Jateng\Dokumen\TOEFL-Assessment-Test\Kisi_Kisi_dan_Vocabulary_TOEFL_B1_Tingkat_XII.xlsx"
wb.save(excel_path)
print("SUCCESS: Excel file saved to", excel_path)
