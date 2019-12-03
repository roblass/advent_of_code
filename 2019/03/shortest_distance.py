import sys

import numpy as np
from scipy.spatial.distance import cdist


def get_locations(moves):
    locations = [(0, 0)]
    for move in moves:
        direction = move[0]
        magnitude = int(move[1:])

        new_location = locations[-1]
        for i in range(magnitude):
            if direction == 'R':
                new_location = (new_location[0] + 1, new_location[1])
            if direction == 'U':
                new_location = (new_location[0], new_location[1] + 1)
            if direction == 'L':
                new_location = (new_location[0] - 1, new_location[1])
            if direction == 'D':
                new_location = (new_location[0], new_location[1] - 1)
            locations.append(new_location)
    return set(locations)


with open(sys.argv[1], 'r') as f:
    wire1_moves = f.readline()[:-1].split(',')
    wire2_moves = f.readline()[:-1].split(',')

wire1_locations = get_locations(wire1_moves)
wire2_locations = get_locations(wire2_moves)

intersection_points = wire1_locations.intersection(wire2_locations)
print(intersection_points)

distance = np.inf
closest_point = None
for point in intersection_points:
    new_distance = int(cdist([point], [(0, 0)], metric='cityblock')[0][0])
    if new_distance < distance and 0 not in point:
        distance = new_distance
        closest_point = point

print('The closest point is ', closest_point, 'with a distance of', distance)
