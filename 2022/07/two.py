import sys
from collections import defaultdict

data = open(sys.argv[1], 'r').read().replace("$ ", "").split('\n')

dir_sizes = defaultdict(int)
cwd = "/"
path = [cwd]

for line in data:
    tokens = line.split()
    if not tokens or tokens[0] == "ls" or tokens[0] == "dir":
        continue
    elif tokens[0].isdigit():
        dir_sizes[cwd] += int(tokens[0])
    elif tokens[0] == "cd":
        if tokens[1] == "..":
            subdir_size = dir_sizes.get(cwd)
            path.pop()
            cwd = ''.join(path)
            dir_sizes[cwd] += subdir_size
        elif tokens[1] == '/':
            cwd = '/'
        else:
            path.append(tokens[1] + '/')
            cwd = ''.join(path)

for _ in range(len(path) - 1):
    subdir_size = dir_sizes.get(cwd)
    path.pop()
    cwd = ''.join(path)
    dir_sizes[cwd] += subdir_size

print(min(v for v in dir_sizes.values() if v > (30000000 - (70000000 - dir_sizes['/']))))
