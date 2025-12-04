# -*- coding: utf-8 -*-
import sys


dial = 50
num_zeros = 0
with open(sys.argv[1], 'r', encoding="utf-8") as data:
    combo = []
    for line in data:
        if line[0] == "R":
            dial = (dial + int(line[1:])) % 100
        elif line[0] == "L":
            dial = (dial - int(line[1:])) % 100

        if dial == 0:
            num_zeros += 1

print(num_zeros)
