import math
import sys
from collections import defaultdict

lines = [e.strip() for e in open(sys.argv[1], 'r').read().split('\n')[:-1]]

grid = defaultdict(dict)
for i, line in enumerate(lines):
    grid[i] = {j: int(l) for j, l in enumerate(line)}

low_point = []
for i in range(len(lines)):
    for j in range(len(grid[0])):
        point = grid[i][j]
        if point < grid.get(i-1, {}).get(j, math.inf) \
                and point < grid.get(i+1, {}).get(j, math.inf) \
                and point < grid.get(i, {}).get(j+1, math.inf) \
                and point < grid.get(i, {}).get(j-1, math.inf):
            low_point.append([i, j])
print(low_point)
print(sum([grid[p[0]][p[1]]+1 for p in low_point]))
