import sys
from itertools import permutations

lines = [e.strip() for e in open(sys.argv[1], 'r').read().split('\n')[:-1]]

originals = {
    "abcefg": 0,
    "cf": 1,
    "acdeg": 2,
    "acdfg": 3,
    "bcdf": 4,
    "abdfg": 5,
    "abdefg": 6,
    "acf": 7,
    "abcdefg": 8,
    "abcdfg": 9,
}

count = 0
for line in lines:
    input, output = line.split('|')

    for permutation in permutations("abcdefg"):
        letters = "abcdefg"
        possible_map = {letters[i]: permutation[i] for i in range(7)}

        unpossible = False
        for value in input.split():
            new = "".join(sorted([possible_map[c] for c in value]))
            if new not in originals:
                unpossible = True
                break

        if unpossible:
            continue

        output_value = 0
        place = 1000
        for value in output.split():
            final_output = "".join(sorted([possible_map[c] for c in value]))
            output_value += originals[final_output] * place
            place /= 10

        count += output_value
        break

print(int(count))
