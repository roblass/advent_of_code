import sys


def get_area(p1, p2):
    return (p1[0] - p2[0] + 1) * (p1[1] - p2[1] + 1)

points = []
with open(sys.argv[1], 'r', encoding="utf-8") as data:
    for line in data:
        points.append([int(e) for e in line.split(",")])

biggest = -1
for p1 in points:
    for p2 in points:
        size = get_area(p1, p2)
        biggest = max(size, biggest)

print(biggest)
