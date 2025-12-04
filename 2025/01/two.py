# -*- coding: utf-8 -*-
import sys


dial = 50
num_zeros = 0
with open(sys.argv[1], 'r', encoding="utf-8") as data:
    combo = []
    for line in data:
        rot = int(line[1:])
        if line[0] == "R":
            num_zeros += (dial + rot) // 100
            dial = (dial + rot) % 100
        elif line[0] == "L":
            num_zeros += (((100 - dial) % 100) + rot) // 100
            dial = (dial - rot) % 100

print(num_zeros)
