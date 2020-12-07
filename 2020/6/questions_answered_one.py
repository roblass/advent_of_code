import sys

s = open(sys.argv[1], 'r').read()
groups = [a.split('\n') for a in s.split('\n\n')]
total_yes = 0
for group in groups:
    s = ""
    for g in group:
        s += g
    remaining = set(list(s))

    total_yes += len(remaining)
print(total_yes)
