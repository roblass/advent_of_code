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


def move_ship(w_x, w_y, s_x, s_y, times):
    for i in range(times):
        s_x += w_x
        s_y += w_y
    return s_x, s_y

def update_waypoint(x, y, direction, orientation):
    if direction == 'R':
      if orientation == 90:
          return y, -1 * x
      elif orientation == 180:
         return -1 * x, -1 * y
      elif orientation == 270:
          return -1 * y, x
    if direction == 'L':
      if orientation == 90:
          return -1 * y, x
      elif orientation == 180:
          return -1 * x, -1 * y
      elif orientation == 270:
          return y, -1 * x


w_x = 10
w_y = 1
s_x = 0
s_y = 0
for instruction in open(sys.argv[1], 'r'):
    direction = instruction[0]
    distance = int(instruction[1:])
    print(f'direction is {direction}, distance is {distance}')
    if direction in ['N', 'S', 'E', 'W']:
        w_x, w_y = update_coordinates(direction, distance, w_x, w_y)
    elif direction == 'F':
        #x, y = update_coordinates(orientation_lookup[orientation], distance, x, y)
        s_x, s_y = move_ship(w_x, w_y, s_x, s_y, distance)
    elif direction == 'R':
        w_x, w_y = update_waypoint(w_x, w_y, direction, distance)
    elif direction == 'L':
        w_x, w_y = update_waypoint(w_x, w_y, direction, distance)

    print(f'ship = ({s_x}, {s_y}), waypoint = ({w_x}, {w_y}), distance = {math.fabs(s_x) + math.fabs(s_y)}')
