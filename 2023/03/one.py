#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 427405 is too low
# 543466 is too low

import re
import sys

SYMBOLS = ("*", "#", "+", "$", "%", "/", "@", "^", "&", "=", "-")

def main(filename):
    data = list(open(filename, "r").read().split("\n"))

    part_numbers = []
    for line_index, line in enumerate(data): # find all the numbers on this line
        matches = re.finditer(r'\d+', line)
        numbers = [(match.start(), int(match.group())) for match in matches]
        for pos, number in numbers: # see if it is a part number
            # symbol before it?
            if pos > 0 and line[pos-1] in SYMBOLS:
                part_numbers.append(number)
                continue

            # symbol after it?
            try:
                if line[pos + len(str(number))] in SYMBOLS:
                    part_numbers.append(number)
                    continue
            except IndexError:
                pass

            # symbol above it?
            if line_index > 0:
                ceiling = data[line_index-1][max(pos-1, 0):pos+len(str(number))+1]
                if number == 30:
                    print(f"30's ceiling is {ceiling}")
                if [c for c in ceiling if c in SYMBOLS]:
                    part_numbers.append(number)
                    continue

            # symbol below it?
            floor = data[line_index+1][max(pos-1, 0):pos+len(str(number))+1]
            if number == 30:
                print(f"30's floor is {floor}")
            if [c for c in floor if c in SYMBOLS]:
                part_numbers.append(number)
                continue

    print(part_numbers)
    print(sum(part_numbers))

if __name__ == '__main__':
    main(sys.argv[1])
