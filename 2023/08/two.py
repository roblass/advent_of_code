#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

from math import gcd
from functools import reduce


def lcm(numbers):
    def lcm_of_two(a, b):
        return a * b // gcd(a, b)

    return reduce(lcm_of_two, numbers, 1)


def follow_instructions(instructions, instruction_pointer, nodes, start_node):
    current_node = start_node

    next_instruction = instructions[instruction_pointer % len(instructions)]

    if next_instruction == "R":
        current_node = nodes[current_node][1]
    elif next_instruction == "L":
        current_node = nodes[current_node][0]

    return current_node


def main(filename):

    nodes = {}
    with open(filename, "r") as data:
        data = data.read().splitlines()
        # first line is instructions
        instructions = data[0]

        # third line and up is nodes
        for line in data[2:]:
            words = line.split()
            nodes[words[0]] = (words[2][1:-1], words[3][:-1])

    print(instructions)
    print(nodes)

    # for each of the instructions, figure out how many steps to get to Z
    # as pointed out by @esultanik, this won't work if there are multiple Zs in a path,
    # but apparently there are not because it worked
    all_steps = []
    for start_node in [n for n in nodes if n.endswith("A")]:
        i = 0
        node = start_node
        while not node.endswith("Z"):
            node = follow_instructions(instructions, i, nodes, node)
            i += 1
        print(f"{start_node} finished in {i} steps")
        all_steps.append(i)
    print(lcm(all_steps))



if __name__ == '__main__':
    main(sys.argv[1])
