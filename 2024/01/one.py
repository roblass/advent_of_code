# -*- coding: utf-8 -*-
import math
import sys

with open(sys.argv[1], 'r', encoding="utf-8") as data:
    col1 = []
    col2 = []

    for line in data:
        pair = line.split()
        col1.append(int(pair[0]))
        col2.append(int(pair[1]))

    col1.sort()
    col2.sort()

    total_diff = 0
    for val1, val2 in zip(col1, col2):
        total_diff += int(math.fabs(val1 - val2))

    print(total_diff)
