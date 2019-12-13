import operator
import sys
from collections import defaultdict
from math import asin, degrees, fabs, sqrt

import numpy as np

asteroid_locations = []
with open(sys.argv[1], 'r') as f:
    y = 0
    for line in f:
        x = 0
        for c in line:
            if c == '#':
                asteroid_locations.append((x, y))
            x += 1
        y += 1


def compute_slope(a, b):
    run = a[0] - b[0]
    rise = a[1] - b[1]
    try:
        slope = float(rise) / run
    except:
        slope = np.inf
    return slope


def distance(a, b):
    return sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)


def get_quadrant(a, b):
    run = b[0] - a[0]
    rise = a[1] - b[1]

    if run > 0 and rise > 0:
        return 1
    if run < 0 and rise > 0:
        return 2
    if run < 0 and rise < 0:
        return 3
    if run > 0 and rise < 0:
        return 4
    if run > 0 and rise == 0:
        return 5
    if run < 0 and rise == 0:
        return 6
    if run == 0 and rise < 0:
        return 7
    return 8


def get_relative_angle(a, b):
    run = b[0] - a[0]
    rise = a[1] - b[1]
    opposite = fabs(run)
    hypotenus = distance(a, b)

    if run > 0 and rise > 0:
        return degrees(asin(opposite / hypotenus))
    elif run < 0 and rise > 0:
        return 270 + degrees(asin(opposite / hypotenus))
    elif run < 0 and rise < 0:
        return 180 + degrees(asin(opposite / hypotenus))
    elif run > 0 and rise < 0:
        return 90 + degrees(asin(opposite / hypotenus))
    elif run > 0 and rise == 0:
        return 90
    elif run < 0 and rise == 0:
        return 270
    elif run == 0 and rise < 0:
        return 0
    else:
        return 0


# compute pair-wise slopes
checked = []
slopes = {}
for asteroid1 in asteroid_locations:
    for asteroid2 in asteroid_locations:
        if asteroid2 in checked or asteroid1 == asteroid2:
            continue
        # a bit sloppy, but makes lookups easier
        slopes[(asteroid1, asteroid2)] = compute_slope(asteroid1, asteroid2)
        slopes[(asteroid2, asteroid1)] = compute_slope(asteroid1, asteroid2)
    checked.append(asteroid1)

visible = defaultdict(int)
for asteroid1 in asteroid_locations:
    all_slopes = []
    all_quadrants = defaultdict(list)
    for asteroid2 in asteroid_locations:
        # do any asteroids block these two?
        if asteroid1 == asteroid2:
            continue
        all_slopes.append(slopes[asteroid1, asteroid2])
        all_quadrants[slopes[asteroid1, asteroid2]].append(get_quadrant(asteroid1, asteroid2))
    visible[asteroid1] = sum([len(set(q)) for q in all_quadrants.values()])

base_location = sorted(visible.items(), key=operator.itemgetter(1), reverse=True)[0][0]
print(base_location)

# for each asteroid, order based on relative slope / quad, then by dist to base
relative_angles = defaultdict(list)
for asteroid in asteroid_locations:
    if asteroid == base_location:
        continue
    relative_angles[get_relative_angle(base_location, asteroid)].append((asteroid,
        distance(asteroid, base_location)))
ordered_angles = sorted(list(relative_angles.keys()))


for angle in ordered_angles:
    relative_angles[angle] = sorted(relative_angles[angle], key=operator.itemgetter(1))


i = 0
for angle in ordered_angles:
    try:
        potential = relative_angles[angle].pop(0)
    except IndexError:
        continue
    print(i, ':', potential[0])
    i += 1
    if i > 205:
        break
