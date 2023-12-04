#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math
import sys


def compute_matches(card_line):
    pos = card_line.find("|")
    winners = set(card_line[:pos].split()[2:])

    my_numbers = card_line[pos:].split()[1:]

    num_winners = 0
    for number in my_numbers:
        if number in winners:
            num_winners += 1

    return num_winners


def main(filename):

    num_winners = 0
    with open(filename, "r") as cardfile:
        for line in cardfile:
            matches = compute_matches(line)
            if matches > 0:
                num_winners += int(math.pow(2, matches-1))

    print(num_winners)


if __name__ == '__main__':
    main(sys.argv[1])
