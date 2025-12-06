import sys

from functools import reduce


worksheet= []
with open(sys.argv[1], 'r', encoding="utf-8") as data:
    for line in data:
        worksheet.append(list(line[:-1]))

worksheet = [list(col) for col in zip(*worksheet[::-1])]

result = 0
begin = True
numbers = []
for col in worksheet:
    if begin:
        operator = col[0]
        number = ''.join(col[1:][::-1]).strip()
        if number != '':
            numbers.append(int(number))
        begin = False
    elif len([c for c in col if c != ' ']) == 0:
        if operator == "+":
            result += reduce(lambda x, y: x + y, numbers)
        elif operator == "*":
            result += reduce(lambda x, y: x * y, numbers)
        else:
            print(f"Error: unknown operator {operator}.")
        begin = True
        numbers = []
    else:
        number = ''.join(col[::-1]).strip()
        if number != '':
            numbers.append(int(number))

if operator == "+":
    result += reduce(lambda x, y: x + y, numbers)
elif operator == "*":
    result += reduce(lambda x, y: x * y, numbers)
else:
    print(f"Error: unknown operator {operator}.")

print(result)
