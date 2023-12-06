#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
from collections import defaultdict


class CategoryMapper:
    def __init__(self):
        self.ranges = defaultdict(list)


    def add_range(self, cat_name, start, end, offset):
        self.ranges[cat_name].append((start, end, offset))
        self.ranges[cat_name].sort() # store sorted so search works


    def get_offset(self, cat_name, number): # probably overkill, but so are these stupid puzzles
        low, high = 0, len(self.ranges[cat_name]) - 1
        while low <= high:
            mid = (low + high) // 2
            start, end, offset = self.ranges[cat_name][mid]
            if start <= number <= end:
                return offset
            if number < start:
                high = mid - 1
            else:
                low = mid + 1
        return 0 # if we don't find it, it maps to itself


def convert_category(src, dst, cat_range):
    cat_map = {}
    for i in range(cat_range):
        cat_map[dst + i] = src + i
    return cat_map


def lookup_next(src2dst_map, cat_map, src):
    return src2dst_map[cat_map][src]


def build_map(filename, category_mapper):
    with open(filename, "r") as almanac:
        for line in almanac:
            if line.startswith("seeds:"):
                seeds_to_plant = [int(s) for s in line.split()[1:]]
            elif "map:" in line:
                cat_name = line.split()[0]
            elif [s.isdigit() for s in line.split()] and len(line.split()) == 3:
                dst, src, cat_range = [int(s) for s in line.split()]
                category_mapper.add_range(cat_name, src, src + cat_range, dst - src)
    return seeds_to_plant


def main(filename):

    category_mapper = CategoryMapper()

    seeds_to_plant = build_map(filename, category_mapper)

    locations = []
    for seed in seeds_to_plant:
        next_num = seed
        for cat_map in ["seed-to-soil", "soil-to-fertilizer", "fertilizer-to-water",
                        "water-to-light", "light-to-temperature", "temperature-to-humidity",
                        "humidity-to-location"]:
            # print(f"{cat_map} converts {next_num} to {next_num + category_mapper.get_offset(cat_map, next_num)}")
            next_num = next_num + category_mapper.get_offset(cat_map, next_num)

        locations.append(next_num)
    print(min(locations))


if __name__ == '__main__':
    main(sys.argv[1])
    #print(convert_category(60, 56, 37))
