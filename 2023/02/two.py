#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

def get_color_maxes(game):
    data = game.split()[1:]
    rgb_max_seen = [0, 0, 0]
    index = 1
    while index  < len(data):
        num = int(data[index])
        try:
            color = data[index+1]
            if color[-1] not in ("e", "d", "n"):
                color = color[:-1]
        except ValueError:
            color = data[index+1][:-1]
        if color == "red" and num > rgb_max_seen[0]:
            rgb_max_seen[0] = num
        elif color == "green" and num > rgb_max_seen[1]:
            rgb_max_seen[1] = num
        elif color == "blue" and num > rgb_max_seen[2]:
            rgb_max_seen[2] = num
        index += 2

    return rgb_max_seen


def main(filename):
    with open(filename, 'r') as data:
        total_power = 0
        for line in data:
            maxes = get_color_maxes(line)
            power = maxes[0] * maxes[1] * maxes[2]
            total_power += power
    print(total_power)


if __name__ == '__main__':
    main(sys.argv[1])
