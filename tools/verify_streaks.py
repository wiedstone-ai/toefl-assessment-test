# -*- coding: utf-8 -*-
"""
Strictly verify streak <= 2 for both bank-paket1.js and bank-paket2.js
"""
import json
import re

def check_file(path):
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
    # Extract JSON part
    json_str = content[content.find("["):content.rfind("]")+1]
    data = json.loads(json_str)
    
    counts = {'A': 0, 'B': 0, 'C': 0, 'D': 0}
    max_streak = 0
    cur_streak = 1
    last_k = None
    streak_locs = []
    
    for i, q in enumerate(data):
        k = q['correctAnswer']
        counts[k] += 1
        if k == last_k:
            cur_streak += 1
            if cur_streak > max_streak:
                max_streak = cur_streak
            if cur_streak > 2:
                streak_locs.append((i+1, k, cur_streak))
        else:
            cur_streak = 1
        last_k = k
        
    print(f"{path} -> Counts: {counts} | Max streak: {max_streak} | Over 2: {streak_locs}")
    return data

d1 = check_file(r"c:\Users\LILI\OneDrive - PDK Jateng\Dokumen\TOEFL-Assessment-Test\bank-paket1.js")
d2 = check_file(r"c:\Users\LILI\OneDrive - PDK Jateng\Dokumen\TOEFL-Assessment-Test\bank-paket2.js")
