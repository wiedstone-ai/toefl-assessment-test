/**
 * =========================================================================
 * GOOGLE APPS SCRIPT — SISTEM MANAJEMEN ASESMEN TOEFL & REKAP NILAI 2026
 * 
 * SPREADSHEET ID : 13RyeWSQwfngQJOyS6vgAX9MKfPbXaJNkI8JDEKXrGfI
 * SPREADSHEET URL: https://docs.google.com/spreadsheets/d/13RyeWSQwfngQJOyS6vgAX9MKfPbXaJNkI8JDEKXrGfI/edit
 * WEB APP URL    : https://script.google.com/macros/s/AKfycbxUcptl2lfudxJKpHS0jw0_P8aORHrfmqTubTzXRIAWc1ho0SdLNQEPetXUdgi-G4iB/exec
 * 
 * FITUR:
 * 1. Manajemen Password / Token Sesi Dinamis pada Sheet 'pass':
 *    - Setiap password menautkan siswa ke Paket Soal tertentu (Paket 1 atau Paket 2).
 *    - Seluruh siswa pada sesi yang sama mengerjakan paket soal yang seragam.
 * 2. Pencatatan Rekapitulasi Nilai Lengkap pada Sheet 'Rekap_Nilai_TOEFL':
 *    - Mencatat secara eksplisit "Password Sesi" yang digunakan siswa.
 *    - Rekap skor ganda: Skor Prediksi TOEFL ITP (310–677), Nilai Rapor (1–100),
 *      serta capaian CEFR B1 (KKTP Min. 75).
 * 3. Verifikasi Realtime Bebas CORS (Mendukung GET JSONP dan POST).
 * =========================================================================
 */

const SPREADSHEET_ID = "13RyeWSQwfngQJOyS6vgAX9MKfPbXaJNkI8JDEKXrGfI";
const PASS_SHEET_NAME = "pass";
const SCORE_SHEET_NAME = "Rekap_Nilai_TOEFL";

/**
 * Mengambil objek Spreadsheet
 */
function getSpreadsheet() {
  try {
    return SpreadsheetApp.openById(SPREADSHEET_ID);
  } catch (err) {
    return SpreadsheetApp.getActiveSpreadsheet();
  }
}

/**
 * Menginisialisasi Sheet 'pass' jika belum ada
 */
function getPassSheet(ss) {
  let sheet = ss.getSheetByName(PASS_SHEET_NAME);
  if (!sheet) {
    sheet = ss.insertSheet(PASS_SHEET_NAME);
  }

  if (sheet.getLastRow() < 2) {
    sheet.clear();
    const headers = ["Password / Token", "Sesi / Keterangan", "Paket Soal (1 atau 2)", "Terakhir Diperbarui", "Status"];
    sheet.appendRow(headers);
    sheet.getRange(1, 1, 1, headers.length)
      .setBackground("#1E3A8A")
      .setFontColor("#FFFFFF")
      .setFontWeight("bold")
      .setHorizontalAlignment("center");
    sheet.setFrozenRows(1);

    // Nilai Default Sesi Ujian (4 Sesi Baku: 3 Jam per Sesi, Grace Period 1 Jam)
    const defaultSessions = [
      ["MALAM19", "Sesi Malam (19.00 - 22.00 WIB)", "1", new Date(), "AKTIF"],
      ["PAGI09", "Sesi Pagi (09.00 - 12.00 WIB)", "1", new Date(), "AKTIF"],
      ["SIANG13", "Sesi Siang (13.00 - 16.00 WIB)", "2", new Date(), "AKTIF"],
      ["SORE16", "Sesi Sore (16.00 - 19.00 WIB)", "1", new Date(), "AKTIF"]
    ];
    for (let i = 0; i < defaultSessions.length; i++) {
      sheet.appendRow(defaultSessions[i]);
    }
  }
  return sheet;
}

/**
 * Menginisialisasi Sheet 'Rekap_Nilai_TOEFL'
 */
function getScoreSheet(ss) {
  let sheet = ss.getSheetByName(SCORE_SHEET_NAME);
  if (!sheet) {
    sheet = ss.insertSheet(SCORE_SHEET_NAME);
    const headers = [
      "Timestamp",
      "Password Sesi",
      "Asal Sekolah",
      "Tingkat",
      "Kompetensi Keahlian",
      "Rombel",
      "No. Presensi",
      "Nama Lengkap Siswa",
      "Paket Soal",
      "Listening Raw (/50)",
      "Listening Scaled (31-68)",
      "Structure Raw (/40)",
      "Structure Scaled (31-68)",
      "Reading Raw (/50)",
      "Reading Scaled (31-67)",
      "Total Skor TOEFL (310-677)",
      "Nilai Rapor (1-100)",
      "Predikat / Level CEFR",
      "Status KKTP (Min. 75)",
      "Durasi Pengerjaan",
      "Detail Jawaban Siswa"
    ];
    sheet.appendRow(headers);
    sheet.getRange(1, 1, 1, headers.length)
      .setBackground("#0F172A")
      .setFontColor("#FFFFFF")
      .setFontWeight("bold")
      .setHorizontalAlignment("center");
    sheet.setFrozenRows(1);
  }
  return sheet;
}

/**
 * Mengambil semua daftar password sesi
 */
function getAllPasswords() {
  const ss = getSpreadsheet();
  const sheet = getPassSheet(ss);
  const data = sheet.getDataRange().getValues();
  const passwords = [];

  for (let i = 1; i < data.length; i++) {
    const row = data[i];
    if (row[0]) {
      passwords.push({
        token: String(row[0]).trim(),
        keterangan: String(row[1] || "").trim(),
        paket: String(row[2] || "1").trim(),
        updatedAt: row[3] ? Utilities.formatDate(new Date(row[3]), Session.getScriptTimeZone(), "yyyy-MM-dd HH:mm:ss") : "-",
        status: String(row[4] || "AKTIF").toUpperCase()
      });
    }
  }
  return passwords;
}

/**
 * Memverifikasi Password Sesi yang Dimasukkan Siswa
 */
function verifySessionPassword(tokenInput) {
  if (!tokenInput) {
    return { status: "error", message: "Password / token tidak boleh kosong." };
  }

  const tokenClean = String(tokenInput).trim().toUpperCase();
  const passwords = getAllPasswords();

  for (let i = 0; i < passwords.length; i++) {
    const item = passwords[i];
    if (item.token.toUpperCase() === tokenClean) {
      if (item.status !== "AKTIF") {
        return { status: "error", message: "Password sesi ini saat ini sedang NONAKTIF oleh pengawas." };
      }
      return {
        status: "success",
        valid: true,
        sessionToken: item.token,
        sessionName: item.keterangan,
        packageId: item.paket === "2" ? "2" : "1"
      };
    }
  }

  return {
    status: "error",
    valid: false,
    message: "Password sesi tidak ditemukan atau salah. Silakan tanyakan kepada Pengawas Ujian."
  };
}

/**
 * Mengatur atau Mengubah Password Sesi (Khusus Guru / Admin)
 */
function setSessionPassword(token, keterangan, paket, status) {
  if (!token) {
    return { status: "error", message: "Token password tidak boleh kosong." };
  }

  const ss = getSpreadsheet();
  const sheet = getPassSheet(ss);
  const data = sheet.getDataRange().getValues();
  const tokenClean = String(token).trim().toUpperCase();
  let foundRow = -1;

  for (let i = 1; i < data.length; i++) {
    if (String(data[i][0]).trim().toUpperCase() === tokenClean) {
      foundRow = i + 1;
      break;
    }
  }

  const now = new Date();
  const statusClean = String(status || "AKTIF").toUpperCase();
  const paketClean = String(paket || "1").trim();

  if (foundRow > 0) {
    sheet.getRange(foundRow, 2).setValue(keterangan || "");
    sheet.getRange(foundRow, 3).setValue(paketClean);
    sheet.getRange(foundRow, 4).setValue(now);
    sheet.getRange(foundRow, 5).setValue(statusClean);
    return { status: "success", message: "Password sesi '" + tokenClean + "' berhasil diperbarui." };
  } else {
    sheet.appendRow([tokenClean, keterangan || "", paketClean, now, statusClean]);
    return { status: "success", message: "Password sesi baru '" + tokenClean + "' berhasil ditambahkan." };
  }
}

/**
 * Menyimpan Hasil Ujian Siswa ke Sheet 'Rekap_Nilai_TOEFL'
 */
function recordStudentSubmission(data) {
  if (!data) data = {};
  const ss = getSpreadsheet();
  const sheet = getScoreSheet(ss);

  const timestamp = new Date();
  const sessionPassword = String(data.sessionPassword || data.password || "-").trim().toUpperCase();
  const sekolah = String(data.sekolah || data.school || "-").trim();
  const tingkat = String(data.tingkat || "XII").trim();
  const keahlian = String(data.keahlian || data.jurusan || "-").trim();
  const rombel = String(data.rombel || "-").trim();
  const presensi = String(data.presensi || "-").trim();
  const nama = String(data.nama || "-").trim();
  const paketSoal = String(data.paketSoal || data.packageId || "Paket 1").trim();

  const lRaw = Number(data.listeningRaw || 0);
  const lScaled = Number(data.listeningScaled || 31);
  const sRaw = Number(data.structureRaw || 0);
  const sScaled = Number(data.structureScaled || 31);
  const rRaw = Number(data.readingRaw || 0);
  const rScaled = Number(data.readingScaled || 31);

  const totalScore = Number(data.toeflScore || Math.round(((lScaled + sScaled + rScaled) / 3) * 10));
  const grade100 = Number(data.grade100 || Math.round(((lRaw + sRaw + rRaw) / 140) * 100));

  const kktpStatus = grade100 >= 75 ? "TUNTAS" : "BELUM TUNTAS";
  let cefrLevel = "B1 (Independent User)";
  if (totalScore >= 543) {
    cefrLevel = "B2 (Vantage / Upper)";
  } else if (totalScore < 433 && totalScore >= 380) {
    cefrLevel = "High A2 (Pre-Intermediate)";
  } else if (totalScore < 380) {
    cefrLevel = "A1-A2 (Elementary)";
  }

  // Deduplication check: cegah dobel submit dalam 30 detik
  const lastRow = sheet.getLastRow();
  if (lastRow > 1) {
    try {
      const lastData = sheet.getRange(lastRow, 1, 1, 8).getValues()[0];
      const lastTime = lastData[0] ? new Date(lastData[0]) : null;
      const lastRombel = String(lastData[5]);
      const lastPres = String(lastData[6]);
      const lastNama = String(lastData[7]);

      if (lastRombel === rombel && lastPres === presensi && lastNama.toLowerCase() === nama.toLowerCase()) {
        if (lastTime && (timestamp.getTime() - lastTime.getTime() < 30000)) {
          return { status: "success", message: "Data nilai telah tersimpan sebelumnya (duplikasi dicegah)." };
        }
      }
    } catch (dupErr) {
      Logger.log("Deduplication error: " + dupErr);
    }
  }

  const row = [
    timestamp,
    sessionPassword,
    sekolah,
    tingkat,
    keahlian,
    rombel,
    presensi,
    nama,
    paketSoal,
    lRaw,
    lScaled,
    sRaw,
    sScaled,
    rRaw,
    rScaled,
    totalScore,
    grade100,
    cefrLevel,
    kktpStatus,
    data.duration || "-",
    data.answers ? (typeof data.answers === "object" ? JSON.stringify(data.answers) : data.answers) : "-"
  ];

  sheet.appendRow(row);
  return {
    status: "success",
    message: "Nilai berhasil direkap ke spreadsheet.",
    totalScore: totalScore,
    grade100: grade100,
    cefrLevel: cefrLevel
  };
}

/**
 * Menghitung statistik rekapitulasi nilai dari Sheet 'Rekap_Nilai_TOEFL'
 */
function getRekapStats() {
  const ss = getSpreadsheet();
  const sheet = getScoreSheet(ss);
  const data = sheet.getDataRange().getValues();

  if (data.length <= 1) {
    return {
      sessionLabel: "Sesi Sebelumnya",
      totalPeserta: 0,
      highest: { toefl: 0, scale100: 0, cefr: "-" },
      lowest: { toefl: 0, scale100: 0, cefr: "-" },
      average: { toefl: 0, scale100: 0, cefr: "-" }
    };
  }

  const totalStudents = data.length - 1;
  let maxToefl = -1, maxScale = -1, maxCefr = "";
  let minToefl = 9999, minScale = 9999, minCefr = "";
  let sumToefl = 0, sumScale = 0;

  for (let i = 1; i < data.length; i++) {
    const row = data[i];
    const toefl = Number(row[15]) || 310;
    const scale = Number(row[16]) || 0;
    const cefr = String(row[17] || "Level B1 (Independent User)");

    if (toefl > maxToefl) { maxToefl = toefl; maxScale = scale; maxCefr = cefr; }
    if (toefl < minToefl) { minToefl = toefl; minScale = scale; minCefr = cefr; }

    sumToefl += toefl;
    sumScale += scale;
  }

  const avgToefl = Math.round(sumToefl / totalStudents);
  const avgScale = Math.round(sumScale / totalStudents);
  let avgCefr = "Level B1 (Independent User)";
  if (avgToefl >= 543) avgCefr = "Level B2 (Vantage)";
  else if (avgToefl < 433 && avgToefl >= 380) avgCefr = "Level High A2";
  else if (avgToefl < 380) avgCefr = "Level A1-A2";

  return {
    sessionLabel: "Sesi Sebelumnya",
    totalPeserta: totalStudents,
    highest: { toefl: maxToefl, scale100: maxScale, cefr: maxCefr },
    lowest: { toefl: minToefl, scale100: minScale, cefr: minCefr },
    average: { toefl: avgToefl, scale100: avgScale, cefr: avgCefr }
  };
}

/**
 * Handle HTTP POST
 */
function doPost(e) {
  try {
    let data = {};
    if (e.postData && e.postData.contents) {
      try {
        data = JSON.parse(e.postData.contents);
      } catch (err) {
        data = e.parameter || {};
      }
    } else {
      data = e.parameter || {};
    }

    const action = String(data.action || "").toLowerCase();

    if (action === "check_password" || action === "verify_password") {
      const res = verifySessionPassword(data.token || data.password);
      return sendJsonResponse(res);
    }

    if (action === "get_passwords") {
      const res = getAllPasswords();
      return sendJsonResponse({ status: "success", passwords: res });
    }

    if (action === "set_password" || action === "save_password") {
      const res = setSessionPassword(data.token, data.keterangan, data.paket, data.status);
      return sendJsonResponse(res);
    }

    if (action === "get_stats" || action === "stats") {
      const stats = getRekapStats();
      return sendJsonResponse({ status: "success", stats: stats });
    }

    // Default action: submit score
    const res = recordStudentSubmission(data);
    return sendJsonResponse(res);

  } catch (error) {
    return sendJsonResponse({ status: "error", message: error.toString() });
  }
}

/**
 * Handle HTTP GET (Mendukung JSONP dan Fetch)
 */
function doGet(e) {
  try {
    const params = e && e.parameter ? e.parameter : {};
    const action = String(params.action || "").toLowerCase();

    if (action === "check_password" || action === "verify_password") {
      const res = verifySessionPassword(params.token || params.password);
      return sendJsonResponse(res, params.callback);
    }

    if (action === "get_passwords") {
      const res = getAllPasswords();
      return sendJsonResponse({ status: "success", passwords: res }, params.callback);
    }

    if (action === "set_password" || action === "save_password") {
      const res = setSessionPassword(params.token, params.keterangan, params.paket, params.status);
      return sendJsonResponse(res, params.callback);
    }

    if (action === "get_stats" || action === "stats") {
      const stats = getRekapStats();
      return sendJsonResponse({ status: "success", stats: stats }, params.callback);
    }

    if (action === "submit_score" || action === "submit") {
      const res = recordStudentSubmission(params);
      return sendJsonResponse(res, params.callback);
    }

    return sendJsonResponse({
      status: "online",
      system: "TOEFL Assessment Test Management API",
      timestamp: new Date()
    }, params.callback);

  } catch (error) {
    return sendJsonResponse({ status: "error", message: error.toString() }, e && e.parameter ? e.parameter.callback : null);
  }
}

/**
 * Helper JSON / JSONP Response
 */
function sendJsonResponse(obj, callback) {
  const jsonStr = JSON.stringify(obj);
  if (callback) {
    return ContentService.createTextOutput(callback + "(" + jsonStr + ")")
      .setMimeType(ContentService.MimeType.JAVASCRIPT);
  }
  return ContentService.createTextOutput(jsonStr)
    .setMimeType(ContentService.MimeType.JSON);
}
