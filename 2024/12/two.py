import sys
from collections import defaultdict, deque

# 258594 & 283420 are too low, this solution doesn't properly take "E" type regions into account


def find_plots(grid):
    rows, cols = len(grid), len(grid[0])
    visited = [[False] * cols for _ in range(rows)]
    connected_components = defaultdict(list)

    # only check up down left right
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    def bfs(start_row, start_col):
        char = grid[start_row][start_col]
        queue = deque([(start_row, start_col)])
        component = []

        while queue:
            row, col = queue.popleft()
            if visited[row][col]:
                continue
            visited[row][col] = True
            component.append((row, col))

            for dr, dc in directions:
                new_row, new_col = row + dr, col + dc
                if (0 <= new_row < rows and 0 <= new_col < cols and
                        not visited[new_row][new_col] and
                        grid[new_row][new_col] == char):
                    queue.append((new_row, new_col))

        return component, char

    for r in range(rows):
        for c in range(cols):
            if not visited[r][c]:
                component, char = bfs(r, c)
                if component:
                    connected_components[char].append(component)

    return connected_components


def get_num_touchers(plot, spot):
    row, col = spot
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    touchers = 0
    for dr, dc in directions:
        check_r, check_c = row + dr, col + dc
        if (check_r, check_c) in plot:
            touchers += 1
    return touchers


def get_num_sides(plot):
    xes = [p[0] for p in plot]
    yes = [p[1] for p in plot]

    x_min = min(xes)
    x_max = max(xes)

    y_min = min(yes)
    y_max = max(yes)

    # compute all the points in the minimum bounding box
    new_grid = []
    for x in range(x_min, x_max + 1):
        new_line = []
        for y in range(y_min, y_max + 1):
            if (x, y) in plot:
                new_line.append("A")
            else:
                new_line.append("B")
        new_grid.append(new_line)

    # the non-plot elements in this bounding box
    connected_components = find_plots(new_grid)["B"]

    sides = 4
    for component in connected_components:
        # if it's completely inside the plot, add four sides
        all_xes = [c[0] for c in component]
        all_yes = [c[1] for c in component]
        if len([c for c in component if x_min < c[0] < x_max and y_min < c[1] < y_max]) == \
            len(component):
            sides += 4
        # if any part of it touches the outside of the bounding box, add three sides (indentation)
        elif x_min in all_xes or x_max in all_xes or y_min in all_yes or y_max in all_yes:
            sides += 4
        # otherwise, add two sides (it' like a corner)
        else:
            sides += 2
    return sides


def main():
    garden = []
    with open(sys.argv[1], "r", encoding="utf-8") as file:
        for line in file:
            garden.append(list(line)[:-1])

    all_plots = find_plots(garden)

    cost = 0
    for letter, plots in all_plots.items():
        for plot in plots:
            print(f"Letter {letter} area is {len(plot)}.")
            num_sides = get_num_sides(plot)
            print(num_sides)
            cost += num_sides* len(plot)
    print(cost)


if __name__ == "__main__":
    main()
