#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# DOES NOT WORK, turns out you can't brute force this

import sys


# "frontier" isn't really the right term, but i misunderstood the problem when i started
def follow_instructions_multi(instructions, instruction_pointer, nodes, frontier):
    next_instruction = instructions[instruction_pointer % len(instructions)]

    new_frontier = []
    for current_node in frontier:
        if next_instruction == "R":
            new_frontier.append(nodes[current_node][1])
        elif next_instruction == "L":
            new_frontier.append(nodes[current_node][0])

    return new_frontier


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


    frontier = [n for n in nodes if n.endswith("A")]
    i = 0
    while [n for n in frontier if not n.endswith("Z")]:
        frontier = follow_instructions_multi(instructions, i, nodes, frontier)
        i += 1
        if i % 10000 == 0:
            print(f"Step {i}")

    print(f"Finished in {i} steps.")


if __name__ == '__main__':
    main(sys.argv[1])
