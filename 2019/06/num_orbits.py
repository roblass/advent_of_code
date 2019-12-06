import sys
from collections import defaultdict

orbits = defaultdict(list)
with open(sys.argv[1], 'r') as f:
    for line in f:
        orbited, orbiting = [o.strip() for o in line.split(')')]
        orbits[orbited].append(orbiting)



def get_dist_to_com(orbits, distances, current='COM', dist=0):
    total_dist = dist + 1
    for orbiting in orbits[current]:
        distances[orbiting] = total_dist
        get_dist_to_com(orbits, distances, orbiting, total_dist)


distances = {}
get_dist_to_com(orbits, distances)
print(sum(distances.values()))
