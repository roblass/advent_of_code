from math import floor

with open('input', 'r') as f:
    total_fuel = 0
    for line in f:
        mass = int(line)
        fuel = floor(mass / 3) - 2
        total_fuel += fuel

print(total_fuel)
