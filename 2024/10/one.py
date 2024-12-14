import sys

from collections import defaultdict, deque


def bfs(graph, start, target_value, data):
    queue = deque([[start]])
    all_paths = []
    while queue:
        path = queue.popleft()
        node = path[-1]

        i, j = node
        if str(data[i][j]) == str(target_value):
            all_paths.append(path)
        else:
            for neighbor in graph.get(node, []):
                if neighbor not in path:
                    new_path = path + [neighbor]
                    queue.append(new_path)

    return all_paths


def is_valid(data, i, j, x, y):
    if data[x][y] == ".":
        return False
    if int(data[x][y]) - int(data[i][j]) == 1:
        return True
    return False


def main():
    data = []
    with open(sys.argv[1], "r", encoding="utf-8") as file:
        for line in file:
            data.append(list([l for l in line if l != "\n"]))

    topo_map = defaultdict(list)
    trailheads = []
    for i in range(len(data)):
        for j in range(len(data[0])):
            if data[i][j] == ".":
                continue

            if data[i][j] == "0":
                trailheads.append((i, j))

            try: # below
                if is_valid(data, i, j, i + 1, j):
                    topo_map[(i, j)].append((i+1, j))
            except IndexError:
                pass

            # above
            if i > 0 and is_valid(data, i, j, i - 1, j):
                topo_map[(i, j)].append((i - 1, j))

            try: # right
                if is_valid(data, i, j, i, j + 1):
                    topo_map[(i, j)].append((i, j + 1))
            except IndexError:
                pass

            # left
            if j > 0 and is_valid(data, i, j, i, j - 1):
                topo_map[(i, j)].append((i, j-1))

    print(topo_map)

    score = 0
    for trailhead in trailheads:
        all_paths = bfs(topo_map, trailhead, "9", data)
        destinations = []
        for path in all_paths:
            destinations.append(path[-1])
        score += len(set(destinations))
    print(score)


if __name__ == "__main__":
    main()
