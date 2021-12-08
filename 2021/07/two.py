import math
import sys

input = [int(e.strip()) for e in open(sys.argv[1], 'r').read().split(',')]
print(input)


left = min(input)
right = max(input)

best_cost = math.inf
for point in range(left, right+1):
    cost = 0
    for crab in input:
        cost += (abs(point - crab) * (abs(point - crab) + 1)) / 2
    if cost < best_cost:
        best_cost = cost

print(int(best_cost))
