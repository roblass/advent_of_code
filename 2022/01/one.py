import sys

filename = sys.argv[1]

elves = [[]]
for line in open(filename, 'r'):
    try:
        calories = int(line)
        elves[-1].append(calories)
    except ValueError:
        elves.append([])

print(max([sum(e) for e in elves]))
