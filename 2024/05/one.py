import sys

from collections import defaultdict

doing_rules = True
rules = defaultdict(list)
updates = []
with open(sys.argv[1], "r", encoding="utf-8") as file:
    for line in file:
        if line.strip() == "":
            doing_rules = False
            continue
        if doing_rules:
            before, after = line[:-1].split("|")
            rules[before].append(after)
        else:
            updates.append(line[:-1].split(","))

# go through each update and see if it is valid
page_sum = 0
for update in updates:
    invalid = False
    update.reverse()
    for i, u in enumerate(update):
        for j in range(len(update) - i):
            if update[i + j] in rules[u]:
                invalid = True
                break
        if invalid:
            break

    # it is valid, add he middle number to our running total
    if not invalid:
        page_sum += int(update[len(update) // 2])

print(page_sum)
