import sys

sack = []
priority_total = 0
elves_in_group = 0

for line in open(sys.argv[1], 'r'):
    priority = 0
    elves_in_group += 1
    sack.append(set(line[:-1]))
    if elves_in_group == 3:
        in_all = list(sack[0].intersection(sack[1]).intersection(sack[2]))[0]

        if ord(in_all) > 95:
            priority = ord(in_all) - 96
        else:
            priority = ord(in_all) - 38
        priority_total += priority

        sack = []
        elves_in_group = 0

print(priority_total)
