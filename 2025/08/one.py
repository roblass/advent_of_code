import sys

from functools import reduce
from math import sqrt
from itertools import combinations

from disjoint_set import DisjointSet

def distance(pair):
    p1, p2 = pair
    return sqrt(sum([(p1[i] - p2[i])**2 for i in range(len(p1))]))


points = []
with open(sys.argv[1], 'r', encoding="utf-8") as data:
    for line in data:
        points.append([int(e) for e in line.split(',')])

k = int(sys.argv[2])

all_pairs = combinations(points, 2)
distances = {}
for pair in all_pairs:
    distances[distance(pair)] = [str(p) for p in pair]

connections_made = 0
points = [str(p) for p in points]
ds = DisjointSet.from_iterable(points)
for distance in sorted(distances.keys()):
    p1, p2 = distances[distance]

    ds.union(p1, p2)
    connections_made += 1

    if connections_made == k:
        break

print(reduce(lambda x, y: x * y, sorted([len(l) for l in list(ds.itersets())], reverse=True)[:3]))
