import sys

pairs = []
for line in open(sys.argv[1], 'r'):
    pairs.append(line.strip())

for i in range(len(pairs)):
    pairs[i] = pairs[i].split(',')
    pairs[i] = (pairs[i][0].split('-'), pairs[i][1].split('-'))

num_overlapping = 0
for first, second in pairs:
    if (int(first[0]) <= int(second[0]) <= int(first[1])) or \
        (int(first[0]) <= int(second[1]) <= int(first[1])) or \
        (int(second[0]) <= int(first[0]) <= int(second[1])) or \
        (int(second[0]) <= int(first[1]) <= int(second[1])):
        num_overlapping += 1


print(num_overlapping)
