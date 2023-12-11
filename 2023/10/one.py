#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
from collections import defaultdict, deque

def shortest_paths(positions, start): # basically BFS
    shortest_path = {position: None for position in positions}
    shortest_path[start] = 0  # Distance to the start is 0

    queue = deque([start])

    while queue:
        current_position = queue.popleft()

        # Iterate through linked positions
        for next_position in positions[current_position]:
            if shortest_path[next_position] is None:
                queue.append(next_position)
                shortest_path[next_position] = shortest_path[current_position] + 1

    return shortest_path


def find_enclosed_tiles(grid): # flood fill algorithm
    rows, cols = len(grid), len(grid[0])

    # Mark a position as visited
    def mark(x, y):
        if 0 <= x < rows and 0 <= y < cols and grid[x][y] == '.':
            grid[x][y] = 'O'  # Mark as outside
            for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                mark(x + dx, y + dy)

    # Mark the outside tiles
    for i in range(rows):
        mark(i, 0)
        mark(i, cols - 1)
    for j in range(cols):
        mark(0, j)
        mark(rows - 1, j)

    # Collect the enclosed dots
    enclosed_tiles = []
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == '.':
                enclosed_tiles.append((i, j))

    return enclosed_tiles


def main(filename):
    sketch = defaultdict(list) # (x, y) -> adjacent positions
    with open(filename, "r") as data:
        y = 0
        starting_pos = (None, None)
        for line in data:
            x = 0

            for char in line:
                key = f"({x}, {y})"
                if char == "|":
                    sketch[key].append(f"({x}, {y-1})")
                    sketch[key].append(f"({x}, {y+1})")
                elif char == "-":
                    sketch[key].append(f"({x-1}, {y})")
                    sketch[key].append(f"({x+1}, {y})")
                elif char == "L":
                    sketch[key].append(f"({x}, {y-1})")
                    sketch[key].append(f"({x+1}, {y})")
                elif char == "J":
                    sketch[key].append(f"({x}, {y-1})")
                    sketch[key].append(f"({x-1}, {y})")
                elif char == "7":
                    sketch[key].append(f"({x}, {y+1})")
                    sketch[key].append(f"({x-1}, {y})")
                elif char == "F":
                    sketch[key].append(f"({x}, {y+1})")
                    sketch[key].append(f"({x+1}, {y})")
                elif char == ".":
                    pass # ground
                elif char == "S":
                    starting_pos = key
                x += 1
            y += 1

    # now connect the starting position to everything connected to it
    to_add = []
    for key in sketch:
        if starting_pos in sketch[key]:
            to_add.append(key)
    sketch[starting_pos].extend(to_add)

    print(sketch)

    # compute shortest pathes
    path_lengths = shortest_paths(sketch, starting_pos)
    print(max([v for v in path_lengths.values() if v]))

if __name__ == '__main__':
    main(sys.argv[1])
