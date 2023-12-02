#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 55752 is too high

import sys


numbers = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8,
           'nine': 9}

def find_text_numbers(line):
    text_numbers = []
    for s_num, i_num in numbers.items():
        index = line.find(s_num)
        while index >= 0:
            text_numbers.append((index, len(s_num), i_num))
            index = line.find(s_num, index+1)
    return text_numbers


def convert_line(line):
    text_numbers = find_text_numbers(line)

    if not text_numbers: # handle lines with no text numbers
        return line

    # rest of the code assume it's sorted by text number index
    text_numbers.sort(key=lambda x: x[0])

    start_pos = 0
    new_line = ""
    for index, length, value in text_numbers:
        # handle the case where the start position is ahead of the index (eg, twone in str)
        if index < start_pos:
            new_line += str(value)
            start_pos = index + length
        else:
            new_line += line[start_pos:index]
            new_line += str(value)
        start_pos = index + length

    if start_pos < len(line): # we have trailing characters without numbers
        index, length, _ = text_numbers[-1]
        new_line += line[index+length:]
    return new_line


def main(filename):
    with open(filename, 'r') as data:
        new_lines = []
        calibration_values = []

        for line in data: # convert words to numbers
            new_lines.append(convert_line(line))

# validation: none of these new lines should have text numbers in them
    for line in new_lines:
        text_numbers = find_text_numbers(line)
        if text_numbers:
            print(f"Error with this line: {line}")

    line_no = 0
    for line in new_lines:
        line_no += 1
        calibration_value = []
        for c in line:
            if c.isdigit():
                calibration_value.append(c)
        calibration_values.append(int(calibration_value[0] + calibration_value[-1]))

    print(sum(calibration_values))


if __name__ == "__main__":
    main(sys.argv[1])
