# -*- coding: utf-8 -*-
"""
Helper to rebalance question options so that correct answers are evenly distributed:
~35 A, ~35 B, ~35 C, ~35 D, no cyclical pattern, max streak <= 2.
"""
import json
import random

def rebalance_keys(questions, seed=42):
    random.seed(seed)
    n = len(questions) # 140
    # Desired keys: 35 each
    targets = ['A'] * 35 + ['B'] * 35 + ['C'] * 35 + ['D'] * 35
    
    # Shuffle targets while enforcing max streak <= 2 and no cyclical 4-tuples
    for _ in range(1000):
        random.shuffle(targets)
        # Check streak
        valid = True
        cur_streak = 1
        for i in range(1, len(targets)):
            if targets[i] == targets[i-1]:
                cur_streak += 1
                if cur_streak > 2:
                    valid = False
                    break
            else:
                cur_streak = 1
        # Check no periodic cycles (e.g. ABCDABCD)
        if valid:
            for i in range(len(targets) - 7):
                if targets[i:i+4] == targets[i+4:i+8]:
                    valid = False
                    break
        if valid:
            break
            
    # Now assign targets to questions by rearranging options
    for i, q in enumerate(questions):
        desired_key = targets[i]
        curr_key = q['correctAnswer']
        if q['type'] == 'structure_error':
            # For structure_error, options are simply Underlined part (A), (B), (C), (D)
            # We must swap the data-opt attributes in prompt!
            # Or if it's easier, we can keep the sentence and remap the letters!
            # Let's inspect how structure_error is formatted.
            pass
        else:
            if curr_key != desired_key:
                # Find current correct option text
                curr_opt_text = None
                for opt in q['options']:
                    if opt['key'] == curr_key:
                        curr_opt_text = opt['text']
                        break
                # Find option currently at desired_key
                target_opt_text = None
                for opt in q['options']:
                    if opt['key'] == desired_key:
                        target_opt_text = opt['text']
                        break
                # Swap them
                for opt in q['options']:
                    if opt['key'] == curr_key:
                        opt['text'] = target_opt_text
                    elif opt['key'] == desired_key:
                        opt['text'] = curr_opt_text
                q['correctAnswer'] = desired_key

    # Check distribution
    counts = {'A': 0, 'B': 0, 'C': 0, 'D': 0}
    for q in questions:
        counts[q['correctAnswer']] += 1
    print("New counts:", counts)
    return questions

print("Rebalance helper loaded.")
