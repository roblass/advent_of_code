#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys


def follow_instructions(instructions, instruction_pointer, nodes, start_node):
    current_node = start_node

    next_instruction = instructions[instruction_pointer % len(instructions)]

    if next_instruction == "R":
        current_node = nodes[current_node][1]
    elif next_instruction == "L":
        current_node = nodes[current_node][0]

    # Return the current node
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

    node = "AAA"
    i = 0
    while node != "ZZZ":
        node = follow_instructions(instructions, i, nodes, node)
        print(node)
        i += 1

    print(f"Finished in {i} steps.")


if __name__ == '__main__':
    main(sys.argv[1])
