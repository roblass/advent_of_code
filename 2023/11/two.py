#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
from collections import defaultdict


def main(filename):

    #parse input
    universe = defaultdict(dict)

    with open(filename, "r") as data:
        y = 0
        for line in data:
            x = 0
            for char in line[:-1]: # strip newlines
                universe[x][y] = char
                x += 1
            y += 1

    # find rows and columns with no galaxies
    rows_to_double = []
    cols_to_double = []
    for x in range(len(universe)):
        has_galaxy = False
        for y in range(len(universe[0])):
            if universe[x][y] == "#":
                has_galaxy = True
        if not has_galaxy:
            cols_to_double.append(x)

    for y in range(len(universe[0])):
        has_galaxy = False
        for x in range(len(universe)):
            if universe[x][y] == "#":
                has_galaxy = True
        if not has_galaxy:
            rows_to_double.append(y)

    expanded_universe = defaultdict(dict)
    col_modifier = 0

    galaxies = []
    for x in range(len(universe)):
        if x in cols_to_double:
            col_modifier += 999999
        row_modifier = 0
        for y in range(len(universe[0])):
            if y in rows_to_double:
                row_modifier += 999999
            expanded_universe[x+col_modifier][y+row_modifier] = universe[x][y]
            if universe[x][y]== "#":
                galaxies.append((x+col_modifier, y+row_modifier))
    print(galaxies)
    total_distance = 0
    for galaxy1 in galaxies:
        for galaxy2 in galaxies:
            if galaxy1==galaxy2:
                break
            total_distance += abs(galaxy1[0] - galaxy2[0]) + abs(galaxy1[1] - galaxy2[1])

    print(total_distance)



if __name__ == '__main__':
    main(sys.argv[1])
