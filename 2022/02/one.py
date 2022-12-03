import sys


filename = sys.argv[1]

opponent_map = {'A': 'rock', 'B': 'paper', 'C': 'scissors'}
my_map = {'X': 'rock', 'Y': 'paper', 'Z': 'scissors'}
my_values = {'rock': 1, 'paper': 2, 'scissors': 3}
total_score = 0
for line in open(filename, 'r'):
    opponent = opponent_map[line.split()[0]]
    me = my_map[line.split()[1]]

    score = my_values[me]
    if me == 'rock':
        if opponent == 'scissors':
            score += 6
        elif opponent == 'rock':
            score += 3

    elif me == 'paper':
        if opponent == 'rock':
            score += 6
        elif opponent == 'paper':
            score += 3

    elif me == 'scissors':
        if opponent == 'paper':
            score += 6
        elif opponent == 'scissors':
            score += 3

    total_score += score

print(total_score)
