import sys

def get_num_neighbors(mapp, yi, xi):
    num_neighbors = 0
    for y, x in (
                 (yi - 1, xi),
                 (yi, xi - 1),
                 (yi - 1, xi - 1),
                 (yi + 1, xi),
                 (yi, xi + 1),
                 (yi + 1, xi + 1),
                 (yi - 1, xi + 1),
                 (yi + 1, xi - 1),
                 ):
        if y < 0 or x < 0 or y >= len(mapp) or x >= len(mapp[y]):
            continue
        if mapp[y][x] == "@":
            num_neighbors += 1
    return num_neighbors

mapp = []
with open(sys.argv[1], 'r', encoding="utf-8") as data:
    for line in data:
        mapp.append(list(line[:-1]))

for line in mapp:
    print(''.join(line))
print('\n')

num_accessible = 0
first_time = True
num_removed = 0
while num_accessible > 0 or first_time:
    first_time = False
    num_accessible = 0
    result_mapp = []
    for y, line in enumerate(mapp):
        result_mapp.append([])
        for x, elem in enumerate(line):
            if elem != "@":
                result_mapp[y].append(".")
                continue
            num_neighbors = get_num_neighbors(mapp, y, x)
            if num_neighbors < 4:
                result_mapp[y].append(".")
                num_accessible += 1
                num_removed += 1
            else:
                result_mapp[y].append("@")
    mapp = result_mapp

for line in result_mapp:
    print(''.join(line))
print('\n',  num_accessible, num_removed)
