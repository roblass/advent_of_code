#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

filename = sys.argv[1]

with open(filename, 'r') as data:
    calibration_values = []
    for line in data:
        calibration_value = []
        for c in line:
            if c.isdigit():
                calibration_value.append(c)
        calibration_values.append(int(calibration_value[0] + calibration_value[-1]))

print(sum(calibration_values))
