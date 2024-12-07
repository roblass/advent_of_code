import copy
import sys


def walk_map(guard_location, guard_orientation, the_map, check_loop):
    visited = []
    visited_orientation = []

    while True:
        x, y = guard_location
        visited.append((x, y))

        if guard_orientation  == "UP":
            # is the guard hitting something?
            try:
                if y == 0:
                    break
                if the_map[y-1][x] == "#":
                    guard_orientation = "RIGHT"
                    if check_loop:
                        if (x, y, guard_orientation) in visited_orientation:
                            return visited, True
                    continue

            except IndexError: # out of bounds now
                break
            guard_location[1] -= 1

        elif guard_orientation  == "RIGHT":
            # is the guard hitting something?
            try:
                if x == len(the_map[0]) - 1: # boundary
                    break
                if the_map[y][x+1] == "#":
                    guard_orientation = "DOWN"
                    if check_loop:
                        if (x, y, guard_orientation) in visited_orientation:
                            return visited, True
                    continue

            except IndexError: # out of bounds now
                break
            guard_location[0] += 1

        elif guard_orientation  == "DOWN":
            # is the guard hitting something?
            try:
                if y == len(the_map) - 1: # boundary
                    break
                if the_map[y+1][x] == "#":
                    guard_orientation = "LEFT"
                    if check_loop:
                        if (x, y, guard_orientation) in visited_orientation:
                            return visited, True
                    continue
            except IndexError: # out of bounds now
                break
            guard_location[1] += 1

        elif guard_orientation  == "LEFT":
            # is the guard hitting something?
            try:
                if x == 0: # boundary
                    break
                if the_map[y][x-1] == "#":
                    guard_orientation = "UP"
                    if check_loop:
                        if (x, y, guard_orientation) in visited_orientation:
                            return visited, True
                    continue
            except IndexError: # out of bounds now
                break
            guard_location[0] -= 1

        visited_orientation.append((x, y, guard_orientation))
    return visited, False

def main():
    the_map = []
    y = 0
    with open(sys.argv[1], "r", encoding="utf-8") as file:
        for line in file:
            if "^" in line:
                guard_location = [line.index("^"), y]
                guard_orientation = "UP"
                line = line.replace("^", ".")
            elif "v" in line:
                guard_location = [line.index("v"), y]
                guard_orientation = "DOWN"
                line = line.replace("v", ".")
            elif "<" in line:
                guard_location = [line.index("<"), y]
                guard_orientation = "LEFT"
                line = line.replace("<", ".")
            elif ">" in line:
                guard_location = [line.index("<"), y]
                guard_orientation = "RIGHT"
                line = line.replace(">", ".")
            the_map.append(list(line[:-1]))
            y += 1


    original_guard_location = guard_location.copy()
    original_guard_orientation = guard_orientation
    visited, _ = walk_map(guard_location, guard_orientation, the_map, False)


    # naive approach: put an obstacle in every location the guard visited and check for loop
    num_loop_positions = 0
    locations = []
    i = 0
    for location in list(set(visited)):
        new_map = copy.deepcopy(the_map)
        x, y = location
        new_map[y][x] = "#"
        guard_location = original_guard_location.copy()
        guard_orientation = original_guard_orientation
        _, is_loop = walk_map(guard_location, guard_orientation, new_map, True)

        if is_loop:
            locations.append((x, y))
            num_loop_positions += 1
        i += 1


    print(num_loop_positions)


if __name__ == "__main__":
    main()
