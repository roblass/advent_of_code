import sys
from functools import lru_cache


def expand(x, y):
    if y == len(manifold):
        return []
    if manifold[y][x] == '^':
        return [(x - 1, y + 1), (x + 1, y + 1)]
    return [(x, y + 1)]


@lru_cache(maxsize=None)
def dfs_count(x, y):
    if y == len(manifold):
        return 1

    num_timelines = 0
    for next_x, next_y in expand(x, y):
        num_timelines += dfs_count(next_x, next_y)

    return num_timelines


manifold = []
with open(sys.argv[1], 'r', encoding="utf-8") as data:
    for line in data:
        manifold.append(line[:-1])

start_x, start_y = manifold[0].find('S'), 0
print(dfs_count(start_x, start_y))
