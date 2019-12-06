import sys
from collections import defaultdict

orbits = defaultdict(list)
orbitings = {}
with open(sys.argv[1], 'r') as f:
    for line in f:
        orbited, orbiting = [o.strip() for o in line.split(')')]
        orbits[orbited].append(orbiting)
        orbitings[orbiting] = orbited


def get_dist_to_com(orbits, distances, current='COM', dist=0):
    total_dist = dist + 1
    for orbiting in orbits[current]:
        distances[orbiting] = total_dist
        get_dist_to_com(orbits, distances, orbiting, total_dist)


distances = {}
get_dist_to_com(orbits, distances)


def get_ancestors(object):
    if object == 'COM':
        return []
    return [orbitings[object]] + get_ancestors(orbitings[object])


# get all the objects that lie in the path of both SAN and YOU to COM
san_set = set(get_ancestors('SAN'))
you_set = set(get_ancestors('YOU'))
both = san_set.intersection(you_set)

# find the furthest common object from COM
highest_distance = 0
closest_common_object = None
for object in both:
    if object == 'COM':
        continue
    if distances[object] > highest_distance:
        highest_distance = distances[object]
        closest_common_object = object

# subtract one because we want the object we orbit, not ourselves
my_dist_to_common = distances['YOU'] - highest_distance - 1
santa_dist_to_common = distances['SAN'] - highest_distance - 1
print('number of transfers:', my_dist_to_common + santa_dist_to_common)
