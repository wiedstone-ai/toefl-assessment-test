/**
 * =========================================================================
 * TOEFL ASSESSMENT TEST — CORE CBT ENGINE (140 SOAL - 115 MENIT)
 * Standar: ETS TOEFL ITP Level 1 (Aligned to CEFR B1 - Passing Score >= 433)
 * Dual Scoring: TOEFL ITP (310–677) & Nilai Rapor Sekolah (1–100)
 * =========================================================================
 */

// Google Apps Script Default Web App URL
const DEFAULT_GS_URL = "https://script.google.com/macros/s/AKfycbxUcptl2lfudxJKpHS0jw0_P8aORHrfmqTubTzXRIAWc1ho0SdLNQEPetXUdgi-G4iB/exec";

// Official ETS TOEFL ITP Scaled Score Conversion Tables (Level 1)
const ETS_LISTENING_CONVERSION = [
  31, 31, 32, 32, 33, 34, 35, 36, 37, 38, // 0-9
  39, 40, 41, 41, 42, 43, 44, 45, 45, 46, // 10-19
  47, 47, 48, 48, 49, 49, 50, 51, 51, 52, // 20-29
  52, 53, 54, 54, 55, 56, 57, 57, 58, 59, // 30-39
  60, 61, 62, 63, 64, 65, 66, 67, 68, 68, 68 // 40-50
];

const ETS_STRUCTURE_CONVERSION = [
  31, 31, 32, 33, 34, 35, 36, 37, 38, 40, // 0-9
  41, 42, 43, 44, 45, 46, 47, 48, 49, 50, // 10-19
  51, 52, 53, 54, 55, 56, 57, 58, 59, 60, // 20-29
  61, 62, 63, 64, 65, 66, 67, 68, 68, 68, 68 // 30-40
];

const ETS_READING_CONVERSION = [
  31, 31, 32, 32, 33, 34, 35, 36, 37, 38, // 0-9
  39, 40, 41, 42, 43, 44, 45, 46, 47, 47, // 10-19
  48, 48, 49, 50, 50, 51, 52, 52, 53, 54, // 20-29
  54, 55, 56, 56, 57, 58, 59, 60, 60, 61, // 30-39
  62, 63, 63, 64, 65, 65, 66, 66, 67, 67, 67 // 40-50
];

// App State
let questions = [];
let currentIndex = 0; // 0 to 139
let userAnswers = {}; // { qid: 'A' | 'B' | 'C' | 'D' }
let flaggedQuestions = {}; // { qid: true }
let studentInfo = {};
let sessionPassword = "";
let packageId = "1";
let totalExamSeconds = 180 * 60; // 180 minutes (3 jam: 2 jam waktu reguler + 1 jam grace period)
let timerInterval = null;
let examFinished = false;
let audioSpeed = 1.0;
let isAudioPlaying = false;
let currentUtterance = null;

// Initialization
window.addEventListener('DOMContentLoaded', () => {
  // 1. Load Student Info & Session
  const rawInfo = sessionStorage.getItem('toefl_student_info') || localStorage.getItem('toefl_student_info');
  if (!rawInfo) {
    alert("Data identitas peserta tidak ditemukan. Mengalihkan ke halaman awal.");
    window.location.href = 'index.html';
    return;
  }
  studentInfo = JSON.parse(rawInfo);

  sessionPassword = sessionStorage.getItem('toefl_session_password') || localStorage.getItem('toefl_session_password') || "SESI-TOEFL";
  packageId = "1"; // Sementara seluruh peserta dipatok menggunakan Paket 1

  // 2. Gunakan Bank Soal Paket 1
  if (window.TOEFL_BANK_PAKET_1 && window.TOEFL_BANK_PAKET_1.length === 140) {
    questions = window.TOEFL_BANK_PAKET_1;
  } else {
    alert("Bank soal sedang dimuat atau tidak lengkap. Silakan refresh halaman.");
    return;
  }

  // 3. Load Saved Progress if any & Inisialisasi Opsi Acak
  initShuffledOptions();
  loadSavedProgress();

  // 4. Initialize UI
  buildQuestionGrid();
  renderCurrentQuestion();
  updateSectionTabCounts();

  // 5. Start Countdown Timer
  startCountdownTimer();
});

// Map Pengacakan Posisi Opsi Soal (Disimpan di localStorage agar tetap konsisten untuk tiap peserta)
let shuffledOptionsMap = {};

function initShuffledOptions() {
  const saved = localStorage.getItem('toefl_shuffled_options_' + packageId);
  if (saved) {
    try {
      shuffledOptionsMap = JSON.parse(saved);
    } catch (e) {}
  }
}

/**
 * Mengambil opsi soal yang telah diacak posisinya (Tanpa label huruf A, B, C, D)
 * Menjamin opsi tiap peserta berbeda urutan dan tetap konsisten saat refresh/HP mati.
 */
function getShuffledOptionsForQuestion(q) {
  const qid = q.id;

  // Bersihkan teks opsi: Jika Section 2 Part B bertuliskan "Underlined part (X)", ambil langsung kata yang digarisbawahi dari prompt
  const cleanOptions = q.options.map(opt => {
    let displayText = opt.text;
    if (displayText.indexOf("Underlined part") >= 0) {
      const regex = new RegExp(`<span[^>]*data-opt=['"]${opt.key}['"][^>]*>([^<]+)<\\/span>`, 'i');
      const match = q.prompt.match(regex);
      if (match && match[1]) {
        displayText = match[1].trim();
      }
    }
    return {
      key: opt.key,
      text: displayText
    };
  });

  // Jika peserta ini sudah memiliki urutan acak tersimpan untuk nomor ini, gunakan urutan tersebut
  if (shuffledOptionsMap[qid] && Array.isArray(shuffledOptionsMap[qid])) {
    const keyOrder = shuffledOptionsMap[qid];
    const ordered = [];
    keyOrder.forEach(k => {
      const found = cleanOptions.find(o => o.key === k);
      if (found) ordered.push(found);
    });
    if (ordered.length === cleanOptions.length) {
      return ordered;
    }
  }

  // Jika belum ada, acak urutan opsi untuk peserta ini (Fisher-Yates Shuffle)
  const shuffled = [...cleanOptions];
  for (let i = shuffled.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1));
    const temp = shuffled[i];
    shuffled[i] = shuffled[j];
    shuffled[j] = temp;
  }

  // Simpan urutan acak peserta ini
  shuffledOptionsMap[qid] = shuffled.map(o => o.key);
  try {
    localStorage.setItem('toefl_shuffled_options_' + packageId, JSON.stringify(shuffledOptionsMap));
  } catch (e) {}

  return shuffled;
}

// Load progress from localStorage
function loadSavedProgress() {
  const savedAnswers = localStorage.getItem('toefl_answers_' + packageId);
  if (savedAnswers) {
    try {
      userAnswers = JSON.parse(savedAnswers);
    } catch (e) {}
  }

  const savedFlags = localStorage.getItem('toefl_flags_' + packageId);
  if (savedFlags) {
    try {
      flaggedQuestions = JSON.parse(savedFlags);
    } catch (e) {}
  }

  const savedTime = localStorage.getItem('toefl_time_' + packageId);
  if (savedTime) {
    const t = parseInt(savedTime, 10);
    if (!isNaN(t) && t > 0) {
      totalExamSeconds = t;
    }
  }

  const savedIndex = localStorage.getItem('toefl_curr_idx_' + packageId);
  if (savedIndex) {
    const idx = parseInt(savedIndex, 10);
    if (!isNaN(idx) && idx >= 0 && idx < questions.length) {
      currentIndex = idx;
    }
  }
}

// Auto-save function
function autoSaveProgress() {
  localStorage.setItem('toefl_answers_' + packageId, JSON.stringify(userAnswers));
  localStorage.setItem('toefl_flags_' + packageId, JSON.stringify(flaggedQuestions));
  localStorage.setItem('toefl_time_' + packageId, totalExamSeconds.toString());
  localStorage.setItem('toefl_curr_idx_' + packageId, currentIndex.toString());

  const indicator = document.getElementById('autosave-indicator');
  if (indicator) {
    indicator.style.opacity = '1';
    indicator.innerHTML = '<span>💾</span> Tersimpan Otomatis';
    setTimeout(() => {
      indicator.style.opacity = '0.7';
    }, 1200);
  }
}

// Countdown Timer (115 Menit)
function startCountdownTimer() {
  updateTimerDisplay();
  timerInterval = setInterval(() => {
    if (examFinished) {
      clearInterval(timerInterval);
      return;
    }

    totalExamSeconds--;
    if (totalExamSeconds % 10 === 0) {
      autoSaveProgress();
    }

    if (totalExamSeconds <= 0) {
      clearInterval(timerInterval);
      alert("⏰ Waktu ujian (3 jam termasuk grace period) telah habis! Sistem akan mengumpulkan lembar jawaban Anda.");
      executeFinalSubmission();
    } else {
      updateTimerDisplay();
    }
  }, 1000);
}

function updateTimerDisplay() {
  const timerBox = document.getElementById('timer-box');
  const timerDisplay = document.getElementById('timer-display');
  if (!timerDisplay) return;

  const m = Math.floor(totalExamSeconds / 60);
  const s = totalExamSeconds % 60;
  const formatted = `${m.toString().padStart(2, '0')}:${s.toString().padStart(2, '0')}`;
  timerDisplay.textContent = formatted;

  if (totalExamSeconds <= 600) { // < 10 mins
    timerBox.classList.add('timer-warning');
  } else {
    timerBox.classList.remove('timer-warning');
  }
}

// Build 140 Questions Grid in Sidebar
function buildQuestionGrid() {
  const container = document.getElementById('questions-grid-container');
  if (!container) return;
  container.innerHTML = '';

  for (let i = 0; i < questions.length; i++) {
    const q = questions[i];
    const btn = document.createElement('button');
    btn.className = 'q-grid-btn';
    btn.id = `grid-btn-${i}`;
    btn.textContent = (i + 1).toString();
    btn.onclick = () => jumpToQuestion(i);
    container.appendChild(btn);
  }
  updateGridButtonsUI();
}

function updateGridButtonsUI() {
  for (let i = 0; i < questions.length; i++) {
    const qid = questions[i].id;
    const btn = document.getElementById(`grid-btn-${i}`);
    if (!btn) continue;

    let cls = 'q-grid-btn';
    if (i === currentIndex) {
      cls += ' current';
    } else if (flaggedQuestions[qid]) {
      cls += ' flagged';
    } else if (userAnswers[qid]) {
      cls += ' answered';
    }
    btn.className = cls;
  }

  // Update answered counter
  const answeredCount = Object.keys(userAnswers).length;
  const counterEl = document.getElementById('answered-counter');
  if (counterEl) {
    counterEl.textContent = `${answeredCount} / 140 Terjawab`;
  }
}

// Filter Navigation Grid by Section
function filterNavGrid(sec) {
  for (let i = 0; i < questions.length; i++) {
    const btn = document.getElementById(`grid-btn-${i}`);
    if (!btn) continue;
    if (sec === 'all') {
      btn.style.display = 'flex';
    } else if (sec === 'sec1') {
      btn.style.display = (i < 50) ? 'flex' : 'none';
    } else if (sec === 'sec2') {
      btn.style.display = (i >= 50 && i < 90) ? 'flex' : 'none';
    } else if (sec === 'sec3') {
      btn.style.display = (i >= 90) ? 'flex' : 'none';
    }
  }
}

// Section Tab Switcher
function switchSectionTab(secNum) {
  stopAudioPlayback();
  if (secNum === 1) {
    currentIndex = 0;
  } else if (secNum === 2) {
    currentIndex = 50;
  } else if (secNum === 3) {
    currentIndex = 90;
  }
  renderCurrentQuestion();
}

function updateSectionTabCounts() {
  let s1Count = 0;
  let s2Count = 0;
  let s3Count = 0;

  for (let i = 0; i < questions.length; i++) {
    const qid = questions[i].id;
    if (userAnswers[qid]) {
      if (i < 50) s1Count++;
      else if (i < 90) s2Count++;
      else s3Count++;
    }
  }

  const c1 = document.getElementById('count-sec-1');
  const c2 = document.getElementById('count-sec-2');
  const c3 = document.getElementById('count-sec-3');
  if (c1) c1.textContent = `${s1Count} / 50`;
  if (c2) c2.textContent = `${s2Count} / 40`;
  if (c3) c3.textContent = `${s3Count} / 50`;

  // Highlight active tab
  const tab1 = document.getElementById('tab-sec-1');
  const tab2 = document.getElementById('tab-sec-2');
  const tab3 = document.getElementById('tab-sec-3');
  if (tab1 && tab2 && tab3) {
    tab1.classList.toggle('active', currentIndex < 50);
    tab2.classList.toggle('active', currentIndex >= 50 && currentIndex < 90);
    tab3.classList.toggle('active', currentIndex >= 90);
  }
}

// Render Current Question
function renderCurrentQuestion() {
  if (currentIndex < 0) currentIndex = 0;
  if (currentIndex >= questions.length) currentIndex = questions.length - 1;

  stopAudioPlayback();

  const q = questions[currentIndex];
  const qid = q.id;

  // Header badges
  document.getElementById('q-number-badge').textContent = `Soal No. ${currentIndex + 1} dari 140`;
  document.getElementById('q-section-badge').textContent = q.sectionName || "Section Test";

  // Flag Button State
  const flagBtn = document.getElementById('btn-flag-q');
  if (flaggedQuestions[qid]) {
    flagBtn.textContent = '🟡 Ditandai Ragu';
    flagBtn.style.background = '#fef3c7';
    flagBtn.style.borderColor = '#f59e0b';
    flagBtn.style.color = '#92400e';
  } else {
    flagBtn.textContent = '⚪ Ragu-ragu';
    flagBtn.style.background = 'transparent';
    flagBtn.style.borderColor = '#cbd5e1';
    flagBtn.style.color = '#334155';
  }

  // Listening Audio Box (Section 1 only)
  const listeningBox = document.getElementById('listening-box');
  if (q.section === 1 && q.audioSegments && q.audioSegments.length > 0) {
    listeningBox.style.display = 'block';
    document.getElementById('play-btn-text').textContent = 'Putar Audio Listening';
    document.getElementById('audio-status-msg').textContent = 'Klik tombol untuk mendengarkan percakapan.';
  } else {
    listeningBox.style.display = 'none';
  }

  // Reading Passage Box (Section 3 only)
  const readingWrapper = document.getElementById('reading-passage-wrapper');
  if (q.section === 3 && q.stimulusBody) {
    readingWrapper.style.display = 'block';
    document.getElementById('stimulus-title').textContent = q.stimulusTitle || "Reading Passage";
    document.getElementById('stimulus-source').textContent = q.stimulusSource || "Source: Authentic Academic Literature";
    document.getElementById('stimulus-body').innerHTML = q.stimulusBody;
  } else {
    readingWrapper.style.display = 'none';
  }

  // Question Prompt
  const promptEl = document.getElementById('question-prompt-text');
  promptEl.innerHTML = q.prompt;

  // Render Options (Posisi diacak & Huruf A, B, C, D dihapuskan)
  const optionsContainer = document.getElementById('options-container');
  optionsContainer.innerHTML = '';

  const chosenKey = userAnswers[qid] || null;
  const displayOptions = getShuffledOptionsForQuestion(q);

  displayOptions.forEach(opt => {
    const isSelected = (chosenKey === opt.key);
    const card = document.createElement('div');
    card.className = 'option-card' + (isSelected ? ' selected' : '');
    card.onclick = () => selectOption(qid, opt.key);

    // Indikator visual radio / centang, TANPA huruf A, B, C, D
    const badge = document.createElement('div');
    badge.className = 'opt-badge';
    badge.innerHTML = isSelected 
      ? '<span style="font-size:0.95rem; font-weight:900; line-height:1; color:#ffffff;">✓</span>' 
      : '<span style="font-size:0.5rem; color:#94a3b8; line-height:1;">●</span>';

    const txt = document.createElement('div');
    txt.className = 'opt-text';
    txt.textContent = opt.text;

    card.appendChild(badge);
    card.appendChild(txt);
    optionsContainer.appendChild(card);
  });

  // Previous button state
  document.getElementById('btn-prev-q').disabled = (currentIndex === 0);

  // Update Grid UI
  updateGridButtonsUI();
  updateSectionTabCounts();
  autoSaveProgress();

  // Scroll to active grid button
  const activeBtn = document.getElementById(`grid-btn-${currentIndex}`);
  if (activeBtn) {
    activeBtn.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
  }
}

// Option Selection
function selectOption(qid, key) {
  userAnswers[qid] = key;
  autoSaveProgress(); // Simpan instan setiap kali opsi diklik agar tidak hilang jika HP mati
  renderCurrentQuestion();
}

// Toggle Flag / Ragu-ragu
function toggleFlagCurrentQuestion() {
  const qid = questions[currentIndex].id;
  if (flaggedQuestions[qid]) {
    delete flaggedQuestions[qid];
  } else {
    flaggedQuestions[qid] = true;
  }
  autoSaveProgress(); // Simpan instan
  renderCurrentQuestion();
}

// Navigation Previous / Next
function navigateQuestion(delta) {
  currentIndex += delta;
  if (currentIndex < 0) currentIndex = 0;
  if (currentIndex >= questions.length) currentIndex = questions.length - 1;
  renderCurrentQuestion();
}

function jumpToQuestion(idx) {
  currentIndex = idx;
  renderCurrentQuestion();
}

// Audio Playback Engine (Web Speech Synthesis API with en-US Native Accents)
function playCurrentAudio() {
  const q = questions[currentIndex];
  if (!q.audioSegments || q.audioSegments.length === 0) return;

  if (isAudioPlaying) {
    stopAudioPlayback();
    return;
  }

  if (!('speechSynthesis' in window)) {
    alert("Peramban Anda tidak mendukung Web Speech Synthesis. Silakan gunakan Google Chrome atau Edge.");
    return;
  }

  window.speechSynthesis.cancel();
  isAudioPlaying = true;

  const playBtn = document.getElementById('btn-play-audio');
  const playText = document.getElementById('play-btn-text');
  const statusMsg = document.getElementById('audio-status-msg');

  playBtn.classList.add('playing');
  playText.textContent = 'Hentikan Audio';
  statusMsg.textContent = 'Sedang memutar percakapan listening...';

  const voices = window.speechSynthesis.getVoices();
  const enVoices = voices.filter(v => v.lang.startsWith('en'));

  let maleVoice = enVoices.find(v => v.name.includes('David') || v.name.includes('Guy') || v.name.includes('Male')) || enVoices[0] || null;
  let femaleVoice = enVoices.find(v => v.name.includes('Zira') || v.name.includes('Jenny') || v.name.includes('Female')) || enVoices[1] || enVoices[0] || null;
  let narratorVoice = enVoices.find(v => v.name.includes('Google US English') || v.name.includes('Aria') || v.name.includes('Natural')) || enVoices[0] || null;

  let segIdx = 0;

  function speakNextSegment() {
    if (!isAudioPlaying || segIdx >= q.audioSegments.length) {
      stopAudioPlayback();
      return;
    }

    const seg = q.audioSegments[segIdx];
    const u = new SpeechSynthesisUtterance(seg.text);
    u.lang = 'en-US';
    u.rate = audioSpeed;

    if (seg.role === 'man') {
      u.pitch = 0.95;
      if (maleVoice) u.voice = maleVoice;
    } else if (seg.role === 'woman') {
      u.pitch = 1.05;
      if (femaleVoice) u.voice = femaleVoice;
    } else {
      u.pitch = 1.0;
      if (narratorVoice) u.voice = narratorVoice;
    }

    u.onend = () => {
      segIdx++;
      const pause = seg.pauseAfter || 350;
      setTimeout(speakNextSegment, pause);
    };

    u.onerror = () => {
      stopAudioPlayback();
    };

    currentUtterance = u;
    window.speechSynthesis.speak(u);
  }

  speakNextSegment();
}

function stopAudioPlayback() {
  if ('speechSynthesis' in window) {
    window.speechSynthesis.cancel();
  }
  isAudioPlaying = false;
  currentUtterance = null;

  const playBtn = document.getElementById('btn-play-audio');
  const playText = document.getElementById('play-btn-text');
  const statusMsg = document.getElementById('audio-status-msg');

  if (playBtn) playBtn.classList.remove('playing');
  if (playText) playText.textContent = 'Putar Audio Listening';
  if (statusMsg) statusMsg.textContent = 'Audio selesai diputar.';
}

function toggleAudioSpeed() {
  if (audioSpeed === 1.0) audioSpeed = 1.2;
  else if (audioSpeed === 1.2) audioSpeed = 0.8;
  else audioSpeed = 1.0;

  const lbl = document.getElementById('speed-label');
  if (lbl) lbl.textContent = audioSpeed.toFixed(1) + 'x';
}

// Confirmation Submit Modal
function openConfirmSubmitModal() {
  const answered = Object.keys(userAnswers).length;
  const unanswered = 140 - answered;
  const flagged = Object.keys(flaggedQuestions).length;

  let msg = `Anda telah menjawab <strong>${answered} dari 140</strong> butir soal.<br>`;
  if (unanswered > 0) {
    msg += `⚠️ Masih ada <strong>${unanswered} soal belum dijawab</strong>!<br>`;
  }
  if (flagged > 0) {
    msg += `🟡 Terdapat <strong>${flagged} soal yang masih ditandai ragu-ragu</strong>.<br>`;
  }
  msg += `<br>Apakah Anda yakin ingin mengakhiri asesmen dan mengirimkan jawaban sekarang?`;

  document.getElementById('confirm-summary-text').innerHTML = msg;
  document.getElementById('confirm-modal').style.display = 'flex';
}

function closeConfirmModal() {
  document.getElementById('confirm-modal').style.display = 'none';
}

// Final Submission & Dual Scoring Calculation
async function executeFinalSubmission() {
  closeConfirmModal();
  examFinished = true;
  clearInterval(timerInterval);
  stopAudioPlayback();

  // 1. Calculate Raw Scores per Section
  let lRaw = 0; // Section 1 (50 questions)
  let sRaw = 0; // Section 2 (40 questions)
  let rRaw = 0; // Section 3 (50 questions)

  for (let i = 0; i < questions.length; i++) {
    const q = questions[i];
    const userChoice = userAnswers[q.id];
    if (userChoice && userChoice === q.correctAnswer) {
      if (q.section === 1) lRaw++;
      else if (q.section === 2) sRaw++;
      else if (q.section === 3) rRaw++;
    }
  }

  // 2. Scaled Scores via Official ETS Conversion Tables
  const lScaled = ETS_LISTENING_CONVERSION[Math.min(lRaw, 50)];
  const sScaled = ETS_STRUCTURE_CONVERSION[Math.min(sRaw, 40)];
  const rScaled = ETS_READING_CONVERSION[Math.min(rRaw, 50)];

  // Total Predicted TOEFL ITP Score: ((L + S + R) / 3) * 10
  const totalToefl = Math.round(((lScaled + sScaled + rScaled) / 3) * 10);

  // School Grade (1 - 100): (Total Raw / 140) * 100
  const totalRaw = lRaw + sRaw + rRaw;
  const grade100 = Math.max(1, Math.round((totalRaw / 140) * 100));

  // Determine CEFR Achievement Status
  let cefrText = "Memenuhi Target B1 (Independent User)";
  let cefrClass = "cefr-pill cefr-b1";
  let kktpStatus = grade100 >= 75 ? "TUNTAS" : "BELUM TUNTAS";

  if (totalToefl >= 543) {
    cefrText = "Melampaui Target (Level B2 / Vantage, Setara IELTS 5.5 - 6.5)";
    cefrClass = "cefr-pill cefr-b2";
  } else if (totalToefl >= 433) {
    cefrText = "Memenuhi Target B1 (Independent User, Setara IELTS 4.5 - 5.0 - Lulus KKTP)";
    cefrClass = "cefr-pill cefr-b1";
  } else if (totalToefl >= 380) {
    cefrText = "Menuju B1 (High A2 / Pre-Intermediate, Setara IELTS 3.5 - 4.0)";
    cefrClass = "cefr-pill cefr-a2";
  } else {
    cefrText = "Tingkat Dasar (A1 - A2 / Elementary)";
    cefrClass = "cefr-pill cefr-a2";
  }

  // 3. Display Score Certificate Modal
  document.getElementById('cert-total-toefl').textContent = totalToefl;
  document.getElementById('cert-grade-100').textContent = grade100;
  document.getElementById('cert-kktp-status').textContent = kktpStatus;
  document.getElementById('cert-kktp-status').style.background = (kktpStatus === "TUNTAS" ? "#ecfdf5" : "#fef2f2");
  document.getElementById('cert-kktp-status').style.color = (kktpStatus === "TUNTAS" ? "#047857" : "#b91c1c");

  const badgeEl = document.getElementById('cert-cefr-badge');
  badgeEl.className = cefrClass;
  badgeEl.textContent = cefrText;

  document.getElementById('cert-sec1-score').textContent = lScaled;
  document.getElementById('cert-sec1-raw').textContent = `${lRaw}/50 Benar`;

  document.getElementById('cert-sec2-score').textContent = sScaled;
  document.getElementById('cert-sec2-raw').textContent = `${sRaw}/40 Benar`;

  document.getElementById('cert-sec3-score').textContent = rScaled;
  document.getElementById('cert-sec3-raw').textContent = `${rRaw}/50 Benar`;

  document.getElementById('cert-student-name').textContent = studentInfo.nama || "-";
  document.getElementById('cert-student-school').textContent = studentInfo.sekolah || "-";
  document.getElementById('cert-student-class').textContent = 
    `Kelas ${studentInfo.tingkat || 'XII'} | Keahlian ${studentInfo.keahlian || '-'} | Rombel ${studentInfo.rombel || '-'}`;
  document.getElementById('cert-session-token').textContent = sessionPassword;

  document.getElementById('score-modal').style.display = 'flex';

  // 4. Send to Google Sheets (records session password!)
  const elapsedSeconds = (180 * 60) - totalExamSeconds;
  const elapsedMinutes = Math.floor(elapsedSeconds / 60);

  const payload = {
    action: "submit_score",
    sessionPassword: sessionPassword, // Password sesi yang dimasukkan siswa!
    sekolah: studentInfo.sekolah || "-",
    tingkat: studentInfo.tingkat || "XII",
    keahlian: studentInfo.keahlian || "-",
    rombel: studentInfo.rombel || "-",
    presensi: studentInfo.presensi || "-",
    nama: studentInfo.nama || "-",
    paketSoal: `Paket ${packageId}`,
    listeningRaw: lRaw,
    listeningScaled: lScaled,
    structureRaw: sRaw,
    structureScaled: sScaled,
    readingRaw: rRaw,
    readingScaled: rScaled,
    toeflScore: totalToefl,
    grade100: grade100,
    cefrLevel: cefrText,
    duration: `${elapsedMinutes} menit`,
    answers: userAnswers
  };

  try {
    const gsUrl = localStorage.getItem('toefl_gs_url') || DEFAULT_GS_URL;
    if (navigator.sendBeacon) {
      navigator.sendBeacon(gsUrl, new Blob([JSON.stringify(payload)], { type: "text/plain;charset=utf-8" }));
    } else {
      fetch(gsUrl, {
        method: "POST",
        mode: "no-cors",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(payload)
      });
    }
  } catch (err) {
    console.warn("Error sending score payload to server:", err);
  }

  // Tandai ujian telah selesai dan bersihkan cache in-progress
  localStorage.setItem('toefl_exam_finished_' + packageId, 'true');
  localStorage.removeItem('toefl_time_' + packageId);
}
