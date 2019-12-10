import operator
import sys
from collections import defaultdict
from math import sqrt

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
    run = a[0] - b[0]
    rise = a[1] - b[1]

    if run > 0 and rise > 0:
        return 1
    elif run < 0 and rise > 0:
        return 2
    elif run < 0 and rise < 0:
        return 3
    elif run > 0 and rise < 0:
        return 4
    elif run > 0 and rise == 0:
        return 5
    elif run < 0 and rise == 0:
        return 6
    elif run == 0 and rise < 0:
        return 7
    else:
        return 8


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
    print(asteroid1, ':', sum([len(set(q)) for q in all_quadrants.values()]))
    visible[asteroid1] = sum([len(set(q)) for q in all_quadrants.values()])

best = sorted(visible.items(), key=operator.itemgetter(1), reverse=True)[0]
print('The best location:', best)
