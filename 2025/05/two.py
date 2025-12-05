import sys

with open(sys.argv[1], 'r', encoding="utf-8") as data:
    ranges = []
    for line in data:
        if line == "\n":
            break
        begin, end = line.strip().split('-')
        ranges.append([int(begin), int(end)])

ranges.sort()

merged_ranges = [ranges[0]]
for i, current_range in enumerate(ranges):
    last_range = merged_ranges[-1]

    if current_range[0] <= last_range[1]:
        last_range[1] = max(last_range[1], current_range[1])
    else:
        merged_ranges.append(current_range)

print(merged_ranges)

num_fresh = 0
for r in merged_ranges:
    num_fresh += 1 + r[1] - r[0]

print(num_fresh)
