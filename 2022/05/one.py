import sys
from collections import defaultdict

def find_all(s, c):
    idx = s.find(c)
    while idx != -1:
        yield idx
        idx = s.find(c, idx + 1)

crates = defaultdict(list)
first_time = True
for line in open(sys.argv[1], 'r'):
    if '[' in line: # it's a crate line
        for loc in find_all(line, '['):
            crates[(loc) // 4].append(line[loc + 1])
    elif line.startswith('move'): # it's a command
        if first_time:
            _ = [crates[k].reverse() for k in crates.keys()]
            first_time = False
        words = line.split()
        times, source, dest = [int(words[i]) for i in [1, 3, 5]]

        for i in range(times):
            c = crates[source - 1].pop()
            crates[dest - 1].append(c)


print(''.join([crates[i][-1] for i in range(len(crates))]))
