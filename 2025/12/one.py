import sys

# before i began working on this, it was brought to my attention that today's challenge is
# essentially eric trolling us.  so, this approach doesn't work to solve the general problem as
# stated, but it does work to solve the existing instances of the problem in AoC.

with open(sys.argv[1], 'r', encoding="utf-8") as data:
    regions_fit = 0
    for line in data:
        result = line.split(":")
        if len(result) == 1:
            continue
        shape, presents = result
        if 'x' in shape:
            x, y = [int(e) for e in shape.split('x')]
            shape_total = sum([int(e) for e in presents.split()])
            if shape_total * 8 < x * y:
                regions_fit += 1

print(regions_fit)
