import sys

manifold = []
with open(sys.argv[1], 'r', encoding="utf-8") as data:
    for line in data:
        manifold.append(line[:-1])

beams = [manifold[0].find('S')]

num_splits = 0
for line in manifold:
    new_beams = []
    for i, c in enumerate(line):
        if i in beams:
            if c == '^':
                num_splits += 1
                new_beams.extend([i + 1, i - 1])
            else:
                new_beams.append(i)

    beams = list(set(new_beams))
    print(line, beams)

print(num_splits)
