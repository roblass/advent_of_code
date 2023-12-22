#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys


def compute_hash(input_str):
    current_value = 0
    for char in input_str:
        current_value += ord(char)
        current_value *= 17
        current_value %= 256
    print(f"hash of {input_str} is {current_value}")
    return current_value


def main(filename):
    with open(filename, 'r') as data:
        init_seq = data.read()
        print(sum([compute_hash(seq) for seq in init_seq.replace("\n", "").split(",")]))


if __name__ == '__main__':
    main(sys.argv[1])
