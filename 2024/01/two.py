# -*- coding: utf-8 -*-
import sys

from collections import Counter

with open(sys.argv[1], 'r', encoding="utf-8") as data:
    col1 = []
    col2 = []

    for line in data:
        pair = line.split()
        col1.append(int(pair[0]))
        col2.append(int(pair[1]))

    col1_count = Counter(col1)

    total_score = 0
    for val in col2:
        total_score += int(val * col1_count[val])

    print(total_score)
