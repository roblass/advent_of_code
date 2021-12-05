import math
import sys
from collections import Counter, defaultdict

input = open(sys.argv[1], 'r').read().split('\n')[:-1]

input = [i.split('->') for i in input]
input = [(i[0].split(','), i[1].split(',')) for i in input]

filtered = [i for i in input if i[0][0].strip() == i[1][0].strip() or i[0][1].strip() ==
        i[1][1].strip()]
inverse_filtered = [i for i in input if i[0][0].strip() != i[1][0].strip() and i[0][1].strip() !=
        i[1][1].strip()]


def pretty_print(occupied):
    for y in range(10):
        for x in range(10):
            if occupied[(x, y)] == 0:
                print('.', end='')
            else:
                print(occupied[(x, y)], end='')

        print('')

occupied = defaultdict(int)
for line in filtered:
    x1, y1 = line[0]
    x2, y2 = line[1]
    x1 = int(x1.strip())
    x2 = int(x2.strip())

    y1 = int(y1.strip())
    y2 = int(y2.strip())

    # handle horizontal and vertical
    if x1 > x2: # y must be equal 
        for i in range(x1 - x2 + 1):
            occupied[(x2 + i, y1)] += 1
    elif x2 > x1: # y must be equal
        for i in range(x2 - x1 + 1):
            occupied[(x1 + i, y1)] += 1
    elif y1 > y2: # x must be equal 
        for i in range(y1 - y2 + 1):
            occupied[(x1, y2 + i)] += 1
    elif y2 > y1: # x must be equal 
        for i in range(y2 - y1 + 1):
            occupied[(x1, y1 + i)] += 1

for line in inverse_filtered:
    x1, y1 = line[0]
    x2, y2 = line[1]
    x1 = int(x1.strip())
    x2 = int(x2.strip())

    y1 = int(y1.strip())
    y2 = int(y2.strip())

    #check if it's 45 degrees
    if abs(x1 - x2) != abs(y1 - y2):
        continue

    if x1 > x2 and y1 > y2:
        for i in range(abs(x1-x2) + 1):
            occupied[(x2 + i, y2 + i)] += 1
    elif x1 > x2 and y1 < y2:
        for i in range(abs(x1-x2) + 1):
            occupied[(x2 + i, y2 - i)] += 1
    elif x1 < x2 and y1 < y2:
        for i in range(abs(x1-x2) + 1):
            occupied[(x1 + i, y1 + i)] += 1
    elif x1 < x2 and y1 > y2:
        for i in range(abs(x1-x2) + 1):
            occupied[(x2 - i, y2 + i)] += 1

print(len([o for o in occupied.values() if o >= 2]))
