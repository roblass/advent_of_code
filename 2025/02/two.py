# -*- coding: utf-8 -*-
import sys


def split_chunks(s):
    n = len(s)
    result = []
    for size in range(1, n + 1):
        if n % size == 0:  # only sizes that divide evenly
            chunks = [s[i:i+size] for i in range(0, n, size)]
            result.append(chunks)
    return result


def is_valid(number):
    n = str(number)
    chunks = split_chunks(n)
    for chunk in chunks:
        if len(chunk) == 1:
            continue
        if len(set(chunk)) == 1:
            print(f"{number} is invalid due to {chunk}")
            return False
    return True


with open(sys.argv[1], 'r', encoding="utf-8") as data:
    ranges = data.read().split(',')

invalids = []
for the_range in ranges:
    begin, end = [int(e) for e in the_range.split('-')]

    invalids.extend([x for x in range(begin, end+1) if not is_valid(x)])

print(sum(invalids))
