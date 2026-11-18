# -*- coding: utf-8 -*-
"""
Generate and strictly enforce valid targets for bank-paket2.js
"""
import json
import random

with open(r"c:\Users\LILI\OneDrive - PDK Jateng\Dokumen\TOEFL-Assessment-Test\bank-paket2.js", "r", encoding="utf-8") as f:
    content = f.read()

json_str = content[content.find("["):content.rfind("]")+1]
questions = json.loads(json_str)

random.seed(999)
targets = ['A'] * 35 + ['B'] * 35 + ['C'] * 35 + ['D'] * 35
found = False

for attempt in range(100000):
    random.shuffle(targets)
    streak_ok = True
    cur_streak = 1
    for i in range(1, len(targets)):
        if targets[i] == targets[i-1]:
            cur_streak += 1
            if cur_streak > 2:
                streak_ok = False
                break
        else:
            cur_streak = 1
    if not streak_ok:
        continue
    cycle_ok = True
    for i in range(len(targets) - 7):
        if targets[i:i+4] == targets[i+4:i+8]:
            cycle_ok = False
            break
    if cycle_ok:
        found = True
        print(f"Found permutation at attempt {attempt}")
        break

if not found:
    raise Exception("Could not find valid target sequence")

for i, q in enumerate(questions):
    desired_key = targets[i]
    curr_key = q['correctAnswer']
    if q['type'] == 'structure_error':
        if curr_key != desired_key:
            p = q['prompt']
            p = p.replace(f"data-opt='{curr_key}'", "data-opt='PLACEHOLDER_X'")
            p = p.replace(f"data-opt='{desired_key}'", f"data-opt='{curr_key}'")
            p = p.replace("data-opt='PLACEHOLDER_X'", f"data-opt='{desired_key}'")
            q['prompt'] = p
            q['correctAnswer'] = desired_key
    else:
        if curr_key != desired_key:
            # Swap options text
            curr_text = None
            for opt in q['options']:
                if opt['key'] == curr_key:
                    curr_text = opt['text']
                    break
            target_text = None
            for opt in q['options']:
                if opt['key'] == desired_key:
                    target_text = opt['text']
                    break
            for opt in q['options']:
                if opt['key'] == curr_key:
                    opt['text'] = target_text
                elif opt['key'] == desired_key:
                    opt['text'] = curr_text
            q['correctAnswer'] = desired_key

# Verify
counts = {'A': 0, 'B': 0, 'C': 0, 'D': 0}
max_streak = 0
cur_streak = 1
last_k = None
for q in questions:
    k = q['correctAnswer']
    counts[k] += 1
    if k == last_k:
        cur_streak += 1
        if cur_streak > max_streak:
            max_streak = cur_streak
    else:
        cur_streak = 1
    last_k = k

print(f"Paket 2 Verified: Counts: {counts} | Max streak: {max_streak}")

js_content = "/**\n * BANK SOAL TOEFL ITP OTENTIK - PAKET 2 (140 SOAL)\n * Target Kompetensi: CEFR Level B1 (Passing Score >= 433, Setara IELTS Band 4.5 - 5.0)\n */\n\n"
js_content += "window.TOEFL_BANK_PAKET_2 = " + json.dumps(questions, indent=2, ensure_ascii=False) + ";\n"

with open(r"c:\Users\LILI\OneDrive - PDK Jateng\Dokumen\TOEFL-Assessment-Test\bank-paket2.js", "w", encoding="utf-8") as f:
    f.write(js_content)
print("Paket 2 successfully updated!")
