import sys
from collections import Counter

original_input = open(sys.argv[1]).read().split('\n')[:-1]

print(original_input)

def get_counts(input, i):
    return Counter([e[i] for e in input])

input = original_input
for i in range(len(input[0])):
    counts = get_counts(input, i)
    new_input = []
    for row in input:
        if counts['1'] >= counts['0'] and row[i] == '1':
            new_input.append(row)
        elif counts['0'] > counts['1'] and row[i] == '0':
            new_input.append(row)
    if len(new_input) == 1:
        break

    input = new_input
    print(new_input)

oxygen_rating = int(new_input[0], 2)
print(f"oxygen generator rating = {new_input[0]} = {int(new_input[0], 2)}")

input = original_input
for i in range(len(input[0])):
    counts = get_counts(input, i)
    new_input = []
    for row in input:
        if counts['1'] < counts['0'] and row[i] == '1':
            new_input.append(row)
        elif counts['0'] <= counts['1'] and row[i] == '0':
            new_input.append(row)
    if len(new_input) == 1:
        break

    input = new_input
    print(new_input)

co2_rating = int(new_input[0], 2)
print(f"co2 scrubber rating = {new_input[0]} = {int(new_input[0], 2)}")


print(f"Answer is {co2_rating} * {oxygen_rating} = {co2_rating * oxygen_rating}")
