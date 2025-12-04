import sys

banks = []
with open(sys.argv[1], 'r', encoding="utf-8") as data:
    for line in data:
        banks.append([int(e) for e in str(line[:-1])])

joltage = 0
for bank in banks:
    max_val1 = max(bank[:-1])
    max_pos = bank.index(max_val1)
    max_val2 = max(bank[max_pos + 1:])
    joltage += max_val1 * 10 + max_val2

print(joltage)
