#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys


def get_next_element(sequence):
    diffs = [sequence[i + 1] - sequence[i] for i in range(len(sequence) - 1)]
    if not [i for i in diffs if i != 0]: # termination condition
        return 0
    return get_next_element(diffs) + diffs[-1]


def main(filename):
    running_total = 0
    with open(filename, "r")  as data:
        for line in data:
            sequence = [int(i) for i in line.split()]
            next_element = sequence[-1] + get_next_element(sequence)
            print(next_element)
            running_total += next_element
    print(f"Answer is: {running_total}")


if __name__ == '__main__':
    main(sys.argv[1])
