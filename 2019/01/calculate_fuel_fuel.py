from math import floor


def compute_fuel(mass):
    fuel = floor(mass / 3) - 2
    print fuel
    if fuel < 0:
        return 0
    if fuel < 3:
        return fuel
    else:
        return fuel + compute_fuel(fuel)


with open('input', 'r') as f:
    total_fuel = 0
    for line in f:
        total_fuel += compute_fuel(int(line))

print(total_fuel)
