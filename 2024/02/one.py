import sys

with open(sys.argv[1], "r", encoding="utf-8") as file:
    num_safe = 0
    for line in file:
        reports = line.split()

        first = True
        direction = None
        safe = True
        for report in reports:
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
                safe = False
            elif abs_diff > 3: # not safe, more than three
                print("diff is > 3")
                safe = False
            elif direction == "up" and diff < 0: # was increasing, now decreasing
                print("was increasing, now decreasing")
                safe = False
            elif direction == "down" and diff > 0: # was decreasing, now increasing
                print("was decreasing, now increasing")
                safe = False

            last_val = report

        if safe:
            num_safe += 1

    print(num_safe)
