#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

def get_color_maxes(game):
    data = game.split()[1:]
    game_id = int(data[0][:-1])
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

    return game_id, rgb_max_seen


def main(filename):
    RGB_MAXES= (12, 13, 14)

    possible_sum = 0
    with open(filename, 'r') as data:
        for line in data:
            game_id, maxes = get_color_maxes(line)
            valid = True
            print(RGB_MAXES, maxes)
            for i in range(3):
                if maxes[i] > RGB_MAXES[i]:
                    print(f"Not valid: {maxes[i]} > {RGB_MAXES[i]:}")
                    valid = False
            if valid:
                possible_sum += game_id
    print(possible_sum)


if __name__ == '__main__':
    main(sys.argv[1])
