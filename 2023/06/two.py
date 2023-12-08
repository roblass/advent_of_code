#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math
import sys


def solve_diophantine_inequality(total_time, record):
# solve as a quadratic equation: $time_{total}^2 - time_{hold}\times time_{total} + score \gt 0$.
    # coefficients
    a = 1
    b = -total_time
    c = record

    # calculate the discriminant
    discriminant = b**2 - 4*a*c

    # real roots exist?
    if discriminant >= 0:
        # calculating the float roots
        root1 = (-b + math.sqrt(discriminant)) / (2 * a)
        root2 = (-b - math.sqrt(discriminant)) / (2 * a)

        # find int value bounds
        lower_bound = math.ceil(min(root1, root2))
        upper_bound = math.floor(max(root1, root2))

        # generating int values between bounds, handle edge cases where it equals the record
        return [x for x in range(lower_bound, upper_bound + 1) if x*total_time - x**2 > record]
    else:
        # no real roots, like a lump of coal in your stocking
        return []

def main(filename):
    with open(filename, "r") as data:
        data = data.read().splitlines()
        time = int("".join(data[0].split()[1:]))
        distance = int("".join(data[1].split()[1:]))
        print(len(solve_diophantine_inequality(time, distance)))

if __name__ == '__main__':
    main(sys.argv[1])

