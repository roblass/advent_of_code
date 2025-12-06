import sys

from functools import reduce

worksheet= []
operators = None
with open(sys.argv[1], 'r', encoding="utf-8") as data:
    for line in data:
        try:
            worksheet.append([int(e) for e in line.split()])
        except ValueError: # the operator line
            operators = line.split()

print(worksheet)

result = 0
for i in range(len(worksheet[1])):
    to_add = [line[i] for line in worksheet]
    if operators[i] == "+":
        result += reduce(lambda x, y: x + y, [line[i] for line in worksheet])
    elif operators[i] == "*":
        result += reduce(lambda x, y: x * y, [line[i] for line in worksheet])
    else:
        print(f"Error: unknown operator {operators[i]}.")

print(result)
