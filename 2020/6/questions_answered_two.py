import sys

s = open(sys.argv[1], 'r').read()
groups = [a.split('\n') for a in s.split('\n\n')]
total_yes = 0
for group in groups:
    first = True
    remaining = set([])
    for g in [g for g in group if len(g) > 0]:
        if first:
            remaining = set(list(g))
            first = False
        else:
            remaining = remaining.intersection(set(list(g))) 

    total_yes += len(remaining)
print(total_yes)
