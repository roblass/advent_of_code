# -*- coding: utf-8 -*-
import sys


def is_valid(number):
    n = str(number)
    if len(n) % 2 == 1:
        return True
    begin = n[:len(n) // 2]
    end = n[len(n) // 2:]
    if begin == end:
        return False
    return True


with open(sys.argv[1], 'r', encoding="utf-8") as data:
    ranges = data.read().split(',')

invalids = []
for the_range in ranges:
    begin, end = [int(e) for e in the_range.split('-')]

    invalids.extend([x for x in range(begin, end + 1) if not is_valid(x)])

print(sum(invalids))
