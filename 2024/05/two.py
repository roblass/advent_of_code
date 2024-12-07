import sys

from collections import defaultdict


# this doesn't work if there is more than one pair
def fix_ordering(update, wrong_pairs, rules):
    invalid = True
    while invalid: # stupid hack because i'm not finding all pairs the first time
        for before, after in wrong_pairs:
            update.remove(before)
            index = update.index(after)
            update.insert(index, before)
        invalid, wrong_pairs = find_ooo(update, rules)
    return int(update[len(update) // 2])


def find_ooo(update, rules):
    invalid = False
    update.reverse()
    wrong_pairs = []
    for i, u in enumerate(update):
        for j in range(len(update) - i):
            if update[i + j] in rules[u]:
                wrong_pairs.append((u, update[i + j]))
                invalid = True

    update.reverse()
    return invalid, wrong_pairs

def main():
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

    page_sum = 0
    for update in updates:
        invalid, wrong_pairs = find_ooo(update, rules)
        if invalid:
            middle = fix_ordering(update, wrong_pairs, rules)
            page_sum += middle

    print(page_sum)

if __name__ == "__main__":
    main()
