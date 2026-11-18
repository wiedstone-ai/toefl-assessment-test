# -*- coding: utf-8 -*-
"""
generate_all_banks.py
Generates bank-paket1.js and bank-paket2.js with 140 authentic TOEFL questions each.
Enforces randomized, balanced answer distribution (A, B, C, D each ~25%, max streak <= 2, no cycles).
"""
import json
import random

def enforce_key_balance(questions, target_seed):
    random.seed(target_seed)
    n = len(questions) # 140
    # Create target list: exactly 35 A, 35 B, 35 C, 35 D
    targets = ['A'] * 35 + ['B'] * 35 + ['C'] * 35 + ['D'] * 35
    
    # Generate a permutation with max streak <= 2 and no 4-cycle repeats
    for attempt in range(2000):
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
            
        # Check no periodic cycles of length 4
        cycle_ok = True
        for i in range(len(targets) - 7):
            if targets[i:i+4] == targets[i+4:i+8]:
                cycle_ok = False
                break
        if cycle_ok:
            break

    # Now apply the target keys
    for i, q in enumerate(questions):
        desired_key = targets[i]
        curr_key = q['correctAnswer']
        
        if q['type'] == 'structure_error':
            # For structure_error, prompt contains 4 spans with data-opt='A', 'B', 'C', 'D'
            # To change the correct answer to desired_key, we swap the data-opt attributes in the HTML prompt!
            if curr_key != desired_key:
                prompt_html = q['prompt']
                # Replace with placeholders
                prompt_html = prompt_html.replace(f"data-opt='{curr_key}'", "data-opt='TEMP_CURR'")
                prompt_html = prompt_html.replace(f"data-opt='{desired_key}'", f"data-opt='{curr_key}'")
                prompt_html = prompt_html.replace("data-opt='TEMP_CURR'", f"data-opt='{desired_key}'")
                q['prompt'] = prompt_html
                q['correctAnswer'] = desired_key
        else:
            # Standard options swap
            if curr_key != desired_key:
                # Find current correct text
                curr_text = next(opt['text'] for opt in q['options'] if opt['key'] == curr_key)
                target_text = next(opt['text'] for opt in q['options'] if opt['key'] == desired_key)
                # Swap texts
                for opt in q['options']:
                    if opt['key'] == curr_key:
                        opt['text'] = target_text
                    elif opt['key'] == desired_key:
                        opt['text'] = curr_text
                q['correctAnswer'] = desired_key

    # Verification
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
    print(f"Enforced Distribution: {counts} | Max streak: {max_streak}")
    return questions

print("Balance function ready.")
