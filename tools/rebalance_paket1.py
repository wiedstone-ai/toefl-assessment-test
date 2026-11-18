# -*- coding: utf-8 -*-
import json
from generate_paket1 import make_js_file
from balance_tool import enforce_key_balance

p1 = make_js_file()
p1_balanced = enforce_key_balance(p1, target_seed=101)

js_content = "/**\n * BANK SOAL TOEFL ITP OTENTIK - PAKET 1 (140 SOAL)\n * Target Kompetensi: CEFR Level B1 (Passing Score >= 433, Setara IELTS Band 4.5 - 5.0)\n */\n\n"
js_content += "window.TOEFL_BANK_PAKET_1 = " + json.dumps(p1_balanced, indent=2, ensure_ascii=False) + ";\n"

out_path = r"c:\Users\LILI\OneDrive - PDK Jateng\Dokumen\TOEFL-Assessment-Test\bank-paket1.js"
with open(out_path, "w", encoding="utf-8") as f:
    f.write(js_content)
print(f"SUCCESS: Balanced bank-paket1.js written to {out_path}")
