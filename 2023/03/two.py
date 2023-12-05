#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 64012079 is too low
# 84233757 is too low

import re
import sys

SYMBOLS = ("*", "#", "+", "$", "%", "/", "@", "^", "&", "=", "-")

def get_all_numbers(line):
    matches = re.finditer(r'\d+', line)
    return [(match.start(), len(match.group()), int(match.group())) for match in matches]

def main(filename):
    data = list(open(filename, "r").read().split("\n"))

    gear_ratio_sums = 0
    for line_index, line in enumerate(data): # find all the numbers on this line
        for char_index, char in enumerate(line): # see if it is a part number
            # is it a star?
            if char != "*":
                continue

            adjacent_numbers = []

            # number before it?
            i = char_index
            adj_num = ""
            while i >= 0 and line[i - 1].isdigit():
                adj_num += line[i - 1]
                i -= 1
            if adj_num:
                adjacent_numbers.append(int(adj_num[::-1]))


            # number after it?
            i = char_index
            adj_num = ""
            while i + 1 < len(line) and line[i + 1].isdigit():
                adj_num += line[i + 1]
                i += 1
            if adj_num:
                adjacent_numbers.append(int(adj_num))

            # number(s) above it?
            if line_index > 0:
                for pos, length, number in get_all_numbers(data[line_index - 1]):
                    if pos - 1 <= char_index <= pos + length:
                        print(f"{number} is above")
                        adjacent_numbers.append(number)

            # number(s) below it?
            if line_index + 1 < len(data):
                for pos, length, number in get_all_numbers(data[line_index + 1]):
                    if pos - 1 <= char_index <= pos + length:
                        print(f"{number} is below")
                        adjacent_numbers.append(number)

            print(adjacent_numbers)

            if len(adjacent_numbers) == 2:
                gear_ratio_sums += adjacent_numbers[0] * adjacent_numbers[1]

    print(gear_ratio_sums)


if __name__ == '__main__':
    main(sys.argv[1])
