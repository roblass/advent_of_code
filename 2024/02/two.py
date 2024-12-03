import sys


def count_num_safe(reports):
    first = True
    direction = None
    i = 1
    for i, report in enumerate(reports):
        report = int(report)
        if first:
            last_val = report
            first = False
            continue
        diff = report - last_val
        abs_diff = abs(diff)

        if direction is None: # if diff is zero it's unsafe anyway, so ignore that case
            if diff > 0:
                direction = "up"
            elif diff < 0:
                direction = "down"

        if diff == 0: # not safe, same value
            print("diff is zero")
            return 0, i
        if abs_diff > 3: # not safe, more than three
            print("diff is > 3")
            return 0, i
        if direction == "up" and diff < 0: # was increasing, now decreasing
            print("was increasing, now decreasing")
            return 0, i
        if direction == "down" and diff > 0: # was decreasing, now increasing
            print("was decreasing, now increasing")
            return 0, i

        last_val = report

    return 1, -1


with open(sys.argv[1], "r", encoding="utf-8") as file:
    total_safe = 0
    for line in file:
        raw_reports = line.split()
        num_safe, index = count_num_safe(raw_reports)
        if num_safe == 0: # remove the one where we first see the problem
            num_safe, _ = count_num_safe(raw_reports[:index] + raw_reports[index+1:])
        if num_safe == 0: # handle the first report being the problem
            num_safe, _ = count_num_safe(raw_reports[1:])
        if num_safe == 0: # handle the one before the first unsafe causing the problem
            num_safe, _ = count_num_safe(raw_reports[:index-1] + raw_reports[index:])
        total_safe += num_safe

print(total_safe)
