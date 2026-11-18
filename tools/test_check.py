# -*- coding: utf-8 -*-
"""
Script to build authentic TOEFL ITP question banks for Paket 1 and Paket 2 (140 questions each = 280 questions total).
Levels strictly adjusted to CEFR B1 (Threshold / Independent User).
Answer keys randomized, evenly distributed (~25% each A, B, C, D), no streaks > 2, no cyclical patterns.
"""
import json
import random

# Helper to check answer key distribution
def check_key_distribution(questions, name):
    counts = {'A': 0, 'B': 0, 'C': 0, 'D': 0}
    max_streak = 0
    cur_streak = 1
    last_key = None
    for q in questions:
        k = q['correctAnswer']
        counts[k] += 1
        if k == last_key:
            cur_streak += 1
            if cur_streak > max_streak:
                max_streak = cur_streak
        else:
            cur_streak = 1
        last_key = k
    print(f"[{name}] Total: {len(questions)} | Counts: {counts} | Max streak: {max_streak}")

print("Preparing Question Bank Generator...")
