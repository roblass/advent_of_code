# 990 is too high
import math
import sys


def update_coordinates(direction, distance, x, y):
    if direction == 'N':
        y += distance
    elif direction == 'S':
        y -= distance
    elif direction == 'E':
        x += distance
    elif direction == 'W':
        x -= distance
    return x, y


x = 0
y = 0
orientation = 90
orientation_lookup = {0: 'N', 90: 'E', 180: 'S', 270: 'W'}
for instruction in open(sys.argv[1], 'r'):
    direction = instruction[0]
    distance = int(instruction[1:])
    print(f'direction is {direction}, distance is {distance}')
    if direction in ['N', 'S', 'E', 'W']:
        x, y = update_coordinates(direction, distance, x, y)
    elif direction == 'F':
        x, y = update_coordinates(orientation_lookup[orientation], distance, x, y)
    elif direction == 'R':
        orientation += distance
        orientation = orientation % 360
    elif direction == 'L':
        orientation -= distance
        orientation = orientation % 360

    print(f'({x}, {y}, orientation = {orientation}, distance = {math.fabs(x) + math.fabs(y)}')
