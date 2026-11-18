# TOEFL Assessment Test — Institutional English Proficiency System (Level 1)

Sistem Asesmen Kemahiran Bahasa Inggris Otentik Berstandar **ETS TOEFL ITP (Institutional Testing Program) Level 1** untuk Tingkat XII (Fase F/F+), diselaraskan dengan target capaian **CEFR Level B1 (Independent User)** setara **IELTS Band 4.5 – 5.0**.

---

## 🌟 Fitur Utama Sistem

1. **Format Asli & Otentik TOEFL ITP (140 Butir Soal — Durasi: 115 Menit)**:
   - **Section 1: Listening Comprehension (50 Soal)**:
     - *Part A (Soal 1–30)*: 30 dialog singkat dua pembicara.
     - *Part B (Soal 31–38)*: 2 percakapan panjang akademik.
     - *Part C (Soal 39–50)*: 3 kuliah/ceramah ilmiah mini (*Earth Science, Civil Engineering, Biology*).
     - Didukung engine suara native American (*SpeechSynthesis* multi-speaker: Narator, Pria, Wanita) dengan jeda hening alami.
   - **Section 2: Structure & Written Expression (40 Soal)**:
     - *Part A (Soal 51–65)*: 15 soal kalimat rumpang (*Inversion, Reduced Clauses, Parallelism*).
     - *Part B (Soal 66–90)*: 25 soal *Error Identification* dengan tampilan visual bergaris bawah $\underline{\text{(A)}}$, $\underline{\text{(B)}}$, $\underline{\text{(C)}}$, $\underline{\text{(D)}}$.
   - **Section 3: Reading Comprehension (50 Soal)**:
     - 5 Teks Akademik Otentik (@ 10 Soal) bersumber resmi dari *Smithsonian Institution, NOAA, NASA JPL, National Geographic, dan Scientific American*.
     - Dilengkapi nomor baris bacaan (*Line 5, Line 10, Line 15*) dan sitasi atribusi ilmiah.

2. **2 Paket Soal & Pemetaan Sesi Tanpa Bocor**:
   - Terdapat **Paket 1 (140 Soal)** dan **Paket 2 (140 Soal Berbeda)**.
   - Siswa pada sesi yang sama otomatis mengerjakan paket soal yang seragam berdasarkan Password Sesi.
   - **Identitas paket dirahasiakan dari siswa** (antarmuka siswa 100% netral tanpa tulisan "Paket 1" atau "Paket 2").

3. **Distribusi Kunci Jawaban Acak & Seimbang**:
   - Masing-masing opsi (A, B, C, D) berjumlah tepat 35 butir (25%).
   - Maksimal kemunculan huruf yang sama berurutan adalah 2 nomor (*Max Streak $\le 2$*).
   - Bebas dari pola siklis berulang.

4. **Sistem Skoring Ganda (*Dual Scoring System*)**:
   - **Skor Prediksi TOEFL ITP (310 – 677)**: Menggunakan tabel konversi resmi ETS Level 1 per section.
   - **Nilai Rapor Sekolah (1 – 100)**: Berdasarkan persentase jawaban benar $\left(\frac{\text{Total Benar}}{140} \times 100\right)$.
   - **Status Ketercapaian Target CEFR B1**:
     - $\ge$ 543: Level B2 (Vantage / Melampaui Target)
     - **433 – 542: Level B1 (Independent User / Target Kelulusan KKTP, Setara IELTS Band 4.5 – 5.0)**
     - 380 – 432: High A2 (Menuju B1)
     - < 380: A1–A2 (Tingkat Dasar)

5. **Pencatatan Database Google Spreadsheet Terpadu**:
   - **ID Spreadsheet**: `13RyeWSQwfngQJOyS6vgAX9MKfPbXaJNkI8JDEKXrGfI`
   - **Password sesi yang dimasukkan siswa dicatat secara otomatis** pada kolom spreadsheet, sehingga guru dapat memverifikasi sesi ujian setiap siswa.

6. **File Excel Kisi-Kisi & Kamus Vocabulary**:
   - `Kisi_Kisi_dan_Vocabulary_TOEFL_B1_Tingkat_XII.xlsx` berisi matriks konversi skor, kisi-kisi per section, dan 120+ kosakata akademik B1 dengan terjemahan dan contoh kalimat.

---

## 📁 Struktur Direktori

```
toefl-assessment-test/
├── index.html                                        <-- Portal Utama Netral & Form Siswa
├── masuk-toefl.html                                  <-- Halaman Verifikasi Password Sesi
├── test-toefl.html                                   <-- Ruang Ujian CBT TOEFL (140 Soal)
├── test-toefl.js                                     <-- Engine Ujian, Timer 115 Menit & Skoring
├── bank-paket1.js                                    <-- 140 Soal Otentik Paket 1
├── bank-paket2.js                                    <-- 140 Soal Otentik Paket 2
├── style.css                                         <-- Tampilan Netral Akademik & Responsif
├── google_apps_script.js                             <-- Backend Script untuk Google Sheet
├── pass.html                                         <-- Panel Manajemen Sesi & Token Guru
├── Kisi_Kisi_dan_Vocabulary_TOEFL_B1_Tingkat_XII.xlsx <-- Dokumen Belajar Siswa
└── README.md                                         <-- Dokumentasi Panduan Ini
```

---

## 🚀 Panduan Pemasangan Google Apps Script

1. Buka spreadsheet Anda:  
   [https://docs.google.com/spreadsheets/d/13RyeWSQwfngQJOyS6vgAX9MKfPbXaJNkI8JDEKXrGfI/edit](https://docs.google.com/spreadsheets/d/13RyeWSQwfngQJOyS6vgAX9MKfPbXaJNkI8JDEKXrGfI/edit)
2. Klik menu **Extensions (Ekstensi)** $\rightarrow$ **Apps Script**.
3. Hapus kode default di editor, lalu salin dan tempel seluruh isi file `google_apps_script.js`.
4. Klik tombol **Save (Simpan / Ikon Disket)**.
5. Klik **Deploy (Terapkan)** $\rightarrow$ **New deployment (Penerapan baru)**:
   - Pilih jenis: **Web app (Aplikasi web)**.
   - *Description*: `TOEFL Assessment API v1`.
   - *Execute as*: **Me (Saya / email pemilik)**.
   - *Who has access*: **Anyone (Siapa saja)**.
6. Klik **Deploy**. Berikan izin otorisasi akses Google Sheet bila diminta.
7. Salin URL Web App yang dihasilkan (berakhiran `/exec`), lalu buka `pass.html` di browser Anda, masukkan PIN `123456`, dan tempel URL tersebut di kolom *Google Apps Script Web App URL*, lalu klik **Simpan URL**.

---

## 🔑 Pengaturan Password Sesi Ujian

Pada `pass.html` (atau langsung pada Sheet `pass` di Google Spreadsheet), Anda dapat mengatur password sesi:

| Token / Password | Keterangan Sesi | Paket Terkait | Status |
| :--- | :--- | :---: | :---: |
| `SESI1-PAGI` | Sesi 1 Pagi (07.30 - 09.30) | **Paket 1** | AKTIF |
| `SESI2-SIANG` | Sesi 2 Siang (10.00 - 12.00) | **Paket 2** | AKTIF |
| `SKADAPATI` | Sesi Khusus SMK Negeri 2 Pati | **Paket 1** | AKTIF |
| `SABAKU` | Sesi Khusus SMA Negeri 1 Bae Kudus | **Paket 2** | AKTIF |
| `TOEFL2026` | Password Cadangan Umum | **Paket 1** | AKTIF |

---

## 💻 Cara Menjalankan Ujian di Sekolah

1. Buka file `index.html` langsung di browser Chrome/Edge siswa, atau jalankan server lokal via PowerShell:
   ```powershell
   cd "c:\Users\LILI\OneDrive - PDK Jateng\Dokumen\toefl-assessment-test"
   python -m http.server 8000
   ```
2. Siswa membuka `http://localhost:8000` (atau IP laptop server guru).
3. Siswa mengisi formulir identitas, mengunduh file kisi-kisi Excel jika perlu, lalu memasukkan Password Sesi dari Pengawas.
4. Siswa mengerjakan 140 soal dalam waktu 115 menit. Saat selesai, nilai otomatis direkap ke Google Sheets dan siswa menerima laporan skor digital.
