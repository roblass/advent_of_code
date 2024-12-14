import sys

from collections import defaultdict
from itertools import combinations
# works on example, but not on my unique input.  253 & 267 are too high


def get_antinodes(pair):
    p1, p2 = pair
    rise = p1[1] - p2[1]
    run = p1[0] - p2[0]

    new_x = p1[0] + run
    new_y = p1[1] + rise
    ant1 = (new_x, new_y)

    new_x = p2[0] - run
    new_y = p2[1] - rise
    ant2 = (new_x, new_y)

    print(f"{p1} and {p2} generate {ant1} and {ant2}")

    return ant1, ant2


def main():
    ants = defaultdict(list)
    all_antinodes = []
    with open(sys.argv[1], "r", encoding="utf-8") as file:
        y = 0
        for line in file:
            for x, c in enumerate(list(line)[:-1]):
                if c != ".":
                    ants[c].append((x, y))
            y += 1

        y_max = y
        x_max = len(line)

    # iterate over each pair
    for ant in ants:
        for pair in combinations(ants[ant], 2):
            antinode1, antinode2 = get_antinodes(pair)
            all_antinodes.append(antinode1)
            all_antinodes.append(antinode2)

    # we only care about unique points inside the board
    good_ants = [a for a in set(all_antinodes) if 0 <= a[0] <= x_max and 0 <= a[1] <= y_max]
    print(good_ants)
    print(len(good_ants))

    answers = [(6, 5)]
    with open("output.txt", "r", encoding="utf-8") as file:
        y = 0
        for line in file:
            for x, c in enumerate(list(line)[:-1]):
                if c == "#":
                    answers.append((x, y))
            y += 1

    print(f"Answers: {answers}")


if __name__ == "__main__":
    main()
