import sys

sack = []
priority_total = 0
for line in open(sys.argv[1], 'r'):
    comp1 = set(line[:len(line) // 2])
    comp2 = set(line[len(line) // 2:-1])
    in_both = list(comp1.intersection(comp2))[0]
    if ord(in_both) > 96:
        priority = ord(in_both) - 96
    else:
        priority = ord(in_both) - 38
    priority_total += priority

print(priority_total)
