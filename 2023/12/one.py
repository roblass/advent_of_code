#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys


def generate_replacements(s, num_octothorpes, start=0):
    if num_octothorpes == 0:
        return [s]

    possibilities = []
    for i in range(start, len(s)):
        if s[i] == '?':
            # Replace '?' with '#'
            new_s = s[:i] + '#' + s[i+1:]
            # Recursively generate further replacements
            further_replacements = generate_replacements(new_s, num_octothorpes - 1, i + 1)
            possibilities.extend(further_replacements)

    return possibilities


def filter_invalid_spring_groups(possibilities, springs_desc):
    good_ones = []
    for p in possibilities:
        counts = []
        count = 0

        for char in p:
            if char == '#':
                count += 1
            elif count > 0:
                counts.append(count)
                count = 0

        # Handle case where string ends with '#'
        if count > 0:
            counts.append(count)

        if springs_desc == counts:
            good_ones.append(p)
    return good_ones


def get_num_arrangements(springs, springs_desc):
    # how many total ? do we need to turn into #?
    num_switches = sum(springs_desc) - springs.count("#")

    # get all the combinations of switches that match our total number
    possibilities = generate_replacements(springs, num_switches)

    # for each of the possibilities, filter out the ones that don't meet the spring group desc
    possibilities = filter_invalid_spring_groups(possibilities, springs_desc)
    return len(possibilities)


def main(filename):
    total_arrangements = 0
    with open(filename, "r") as data:
        i = 0
        for line in data:
            springs, springs_desc = line.split()
            springs_desc = [int(i) for i in springs_desc.split(",")]
            total_arrangements += get_num_arrangements(springs, springs_desc)
            i += 1
            print(f"completed {i} / 1000")

    print(total_arrangements)


if __name__ == '__main__':
    main(sys.argv[1])
