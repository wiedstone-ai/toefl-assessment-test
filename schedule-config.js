/**
 * =========================================================================
 * TOEFL ASSESSMENT TEST — SCHEDULE & SESSION MANAGEMENT CONFIGURATION
 * 
 * Jadwal Resmi Ujian TOEFL (Durasi 3 Jam per Sesi: 2 Jam Reguler + 1 Jam Grace Period):
 * 1. Sesi Malam: 19.00 - 22.00 WIB (Dimulai 19.00 WIB Nanti Malam)
 * 2. Sesi Pagi : 09.00 - 12.00 WIB
 * 3. Sesi Siang: 13.00 - 16.00 WIB
 * 4. Sesi Sore : 16.00 - 19.00 WIB
 * 
 * Aturan Penting:
 * - Password/token seragam untuk semua sekolah (tidak dibedakan per sekolah).
 * - Password otomatis tampil di halaman ID saat sesi sudah masuk.
 * - Grace period 1 jam tambahan waktu selesai (total pengerjaan 3 jam).
 * - Toleransi keterlambatan maksimal 1 jam (60 menit) dari jam mulai sesi.
 *   Jika sudah berjalan >= 1 jam (60 menit), peserta otomatis ditolak dan diarahkan ke sesi berikutnya.
 * =========================================================================
 */

const DEFAULT_GS_URL = "https://script.google.com/macros/s/AKfycbxUcptl2lfudxJKpHS0jw0_P8aORHrfmqTubTzXRIAWc1ho0SdLNQEPetXUdgi-G4iB/exec";

// 4 Jadwal Baku Sesi @ 3 Jam (Termasuk 1 Jam Grace Period, Toleransi Masuk: 60 Menit)
const DEFAULT_SCHEDULES = [
  {
    id: "sesi-malam",
    name: "Sesi Malam",
    start: "19:00",
    end: "22:00",
    token: "MALAM19",
    paket: "1",
    status: "AKTIF",
    toleransiMenit: 60,
    keterangan: "Sesi Malam (19.00 - 22.00 WIB)"
  },
  {
    id: "sesi-pagi",
    name: "Sesi Pagi",
    start: "09:00",
    end: "12:00",
    token: "PAGI09",
    paket: "1",
    status: "AKTIF",
    toleransiMenit: 60,
    keterangan: "Sesi Pagi (09.00 - 12.00 WIB)"
  },
  {
    id: "sesi-siang",
    name: "Sesi Siang",
    start: "13:00",
    end: "16:00",
    token: "SIANG13",
    paket: "2",
    status: "AKTIF",
    toleransiMenit: 60,
    keterangan: "Sesi Siang (13.00 - 16.00 WIB)"
  },
  {
    id: "sesi-sore",
    name: "Sesi Sore",
    start: "16:00",
    end: "19:00",
    token: "SORE16",
    paket: "1",
    status: "AKTIF",
    toleransiMenit: 60,
    keterangan: "Sesi Sore (16.00 - 19.00 WIB)"
  }
];

// Baseline Statistik Sesi Sebelumnya (Digunakan jika belum ada rekap atau sedang offline)
const DEFAULT_PREVIOUS_STATS = {
  sessionLabel: "Sesi Sebelumnya",
  totalPeserta: 68,
  highest: {
    toefl: 577,
    scale100: 89,
    cefr: "Level B2 (Vantage / Melampaui Target)"
  },
  lowest: {
    toefl: 347,
    scale100: 36,
    cefr: "Level A1-A2 (Elementary)"
  },
  average: {
    toefl: 462,
    scale100: 72,
    cefr: "Level B1 (Independent User / Target KKTP)"
  },
  lastUpdated: new Date().toLocaleDateString('id-ID')
};

/**
 * Mengambil daftar jadwal dari localStorage atau default
 */
function getScheduleList() {
  const saved = localStorage.getItem('toefl_schedule_sessions');
  if (saved) {
    try {
      const parsed = JSON.parse(saved);
      if (Array.isArray(parsed) && parsed.length > 0) {
        // Validasi jika jadwal masih format lama 2 jam, upgrade ke 3 jam dengan toleransi 60 menit
        let needUpgrade = false;
        parsed.forEach(s => {
          if (s.toleransiMenit !== 60) {
            s.toleransiMenit = 60;
            needUpgrade = true;
          }
          if (s.id === 'sesi-malam' && s.end === '21:00') { s.end = '22:00'; needUpgrade = true; }
          if (s.id === 'sesi-pagi' && s.end === '11:00') { s.end = '12:00'; needUpgrade = true; }
          if (s.id === 'sesi-siang' && s.end === '15:00') { s.end = '16:00'; needUpgrade = true; }
          if (s.id === 'sesi-sore' && s.end === '18:00') { s.end = '19:00'; needUpgrade = true; }
        });
        if (needUpgrade) {
          saveScheduleList(parsed);
        }
        return parsed;
      }
    } catch (e) {
      console.warn("Gagal parse jadwal tersimpan, gunakan default:", e);
    }
  }
  return JSON.parse(JSON.stringify(DEFAULT_SCHEDULES));
}

/**
 * Menyimpan daftar jadwal ke localStorage
 */
function saveScheduleList(list) {
  localStorage.setItem('toefl_schedule_sessions', JSON.stringify(list));
}

/**
 * Menghitung waktu WIB (UTC+7) secara presisi
 */
function getWIBDate() {
  const now = new Date();
  const utc = now.getTime() + (now.getTimezoneOffset() * 60000);
  return new Date(utc + (7 * 3600000));
}

/**
 * Format waktu ke string HH:mm:ss WIB
 */
function formatWIBTime(date) {
  const d = date || getWIBDate();
  const h = String(d.getHours()).padStart(2, '0');
  const m = String(d.getMinutes()).padStart(2, '0');
  const s = String(d.getSeconds()).padStart(2, '0');
  return `${h}:${m}:${s} WIB`;
}

/**
 * Konversi "HH:mm" ke total menit dari 00:00
 */
function timeToMinutes(timeStr) {
  if (!timeStr) return 0;
  const parts = timeStr.split(':');
  return parseInt(parts[0], 10) * 60 + parseInt(parts[1], 10);
}

/**
 * Format menit ke "X jam Y menit" atau "X menit"
 */
function formatMinutes(mins) {
  if (mins <= 0) return "0 menit";
  const h = Math.floor(mins / 60);
  const m = mins % 60;
  if (h > 0 && m > 0) return `${h} jam ${m} menit`;
  if (h > 0) return `${h} jam`;
  return `${m} menit`;
}

/**
 * Mengevaluasi status seluruh jadwal saat ini
 */
function evaluateCurrentSchedule() {
  const wib = getWIBDate();
  const currentMinutes = wib.getHours() * 60 + wib.getMinutes();
  const schedules = getScheduleList();

  let activeSession = null;
  let isLate = false;
  let elapsedMinutes = 0;
  let remainingLateWindow = 0;
  let remainingSessionTime = 0;

  // Urutkan jadwal berdasarkan jam mulai
  const sorted = [...schedules].sort((a, b) => timeToMinutes(a.start) - timeToMinutes(b.start));

  for (let s of sorted) {
    if (s.status !== 'AKTIF') continue;

    const startM = timeToMinutes(s.start);
    const endM = timeToMinutes(s.end);
    const tol = s.toleransiMenit || 60; // Toleransi keterlambatan 1 jam (60 menit)

    // Sesi aktif jika sekarang berada di antara start dan end
    if (currentMinutes >= startM && currentMinutes < endM) {
      activeSession = s;
      elapsedMinutes = currentMinutes - startM;
      remainingSessionTime = endM - currentMinutes;

      if (elapsedMinutes >= tol) {
        isLate = true; // Terlambat >= 1 jam (60 menit) -> Akses DITOLAK
        remainingLateWindow = 0;
      } else {
        isLate = false; // Masih boleh masuk dalam batas 1 jam
        remainingLateWindow = tol - elapsedMinutes;
      }
      break;
    }
  }

  // Tentukan sesi berikutnya
  let nextSession = null;
  let minutesUntilNext = null;

  for (let s of sorted) {
    if (s.status !== 'AKTIF') continue;
    const startM = timeToMinutes(s.start);
    if (startM > currentMinutes) {
      nextSession = s;
      minutesUntilNext = startM - currentMinutes;
      break;
    }
  }

  // Jika tidak ada lagi sesi hari ini, sesi berikutnya adalah sesi pertama besok
  if (!nextSession && sorted.length > 0) {
    const firstActive = sorted.find(s => s.status === 'AKTIF');
    if (firstActive) {
      nextSession = firstActive;
      const startM = timeToMinutes(firstActive.start);
      minutesUntilNext = (1440 - currentMinutes) + startM;
    }
  }

  // Cari sesi sebelumnya yang baru saja selesai
  let previousSession = null;
  for (let i = sorted.length - 1; i >= 0; i--) {
    const s = sorted[i];
    if (s.status !== 'AKTIF') continue;
    const endM = timeToMinutes(s.end);
    if (currentMinutes >= endM) {
      previousSession = s;
      break;
    }
  }
  if (!previousSession && sorted.length > 0) {
    previousSession = sorted[sorted.length - 1];
  }

  return {
    wibDate: wib,
    wibTimeStr: formatWIBTime(wib),
    activeSession,
    isLate,
    elapsedMinutes,
    remainingLateWindow,
    remainingSessionTime,
    nextSession,
    minutesUntilNext,
    previousSession,
    allSchedules: sorted
  };
}

/**
 * Mengambil statistik sesi sebelumnya (dari cache lokal atau server)
 */
function getPreviousStats() {
  const cached = localStorage.getItem('toefl_previous_stats');
  if (cached) {
    try {
      return JSON.parse(cached);
    } catch (e) {}
  }
  return DEFAULT_PREVIOUS_STATS;
}

/**
 * Menyimpan statistik sesi sebelumnya ke localStorage
 */
function savePreviousStats(stats) {
  localStorage.setItem('toefl_previous_stats', JSON.stringify(stats));
}

/**
 * Sinkronisasi statistik dari Google Apps Script secara asynchronous
 */
async function fetchStatsFromServer(callback) {
  try {
    const gsUrl = localStorage.getItem('toefl_gs_url') || DEFAULT_GS_URL;
    const fetchUrl = `${gsUrl}?action=get_stats&_=${Date.now()}`;
    const controller = new AbortController();
    const timeoutId = setTimeout(() => controller.abort(), 4500);

    const response = await fetch(fetchUrl, { signal: controller.signal });
    clearTimeout(timeoutId);
    const data = await response.json();

    if (data && data.status === 'success' && data.stats) {
      savePreviousStats(data.stats);
      if (typeof callback === 'function') {
        callback(data.stats);
      }
      return data.stats;
    }
  } catch (err) {
    console.warn("Gagal mengambil statistik dari server Google Apps Script:", err.message);
  }
  return null;
}
