import sys


def is_in_map(guard_location, the_map):
    if guard_location[0] < 0 or guard_location[1] < 0:
        return False
    if guard_location[0] >= len(the_map[0]) or guard_location[1] >= len(the_map):
        return False
    return True


def walk_map(guard_location, guard_orientation, the_map):
    visited = []
    while is_in_map(guard_location, the_map):
        #print(f"{guard_location}, {guard_orientation}")
        x, y = guard_location
        visited.append((x, y))

        if guard_orientation  == "UP":
            # is the guard hitting something?
            try:
                if the_map[y-1][x] == "#":
                    guard_orientation = "RIGHT"
                    continue
            except IndexError: # out of bounds now
                pass
            guard_location[1] -= 1

        elif guard_orientation  == "RIGHT":
            # is the guard hitting something?
            try:
                if the_map[y][x+1] == "#":
                    guard_orientation = "DOWN"
                    continue

            except IndexError: # out of bounds now
                pass
            guard_location[0] += 1

        elif guard_orientation  == "DOWN":
            # is the guard hitting something?
            try:
                if the_map[y+1][x] == "#":
                    guard_orientation = "LEFT"
                    continue
            except IndexError: # out of bounds now
                pass
            guard_location[1] += 1

        elif guard_orientation  == "LEFT":
            # is the guard hitting something?
            try:
                if the_map[y][x-1] == "#":
                    guard_orientation = "UP"
                    continue
            except IndexError: # out of bounds now
                pass
            guard_location[0] -= 1

    return visited

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


    visited = walk_map(guard_location, guard_orientation, the_map)
    print(len(set(visited)))


if __name__ == "__main__":
    main()
