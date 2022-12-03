import sys


filename = sys.argv[1]

opponent_map = {'A': 'rock', 'B': 'paper', 'C': 'scissors'}
winning_shape = {'rock': 'paper', 'paper': 'scissors', 'scissors': 'rock'}
losing_shape = {'paper': 'rock', 'scissors': 'paper', 'rock': 'scissors'}
my_values = {'rock': 1, 'paper': 2, 'scissors': 3}
total_score = 0
for line in open(filename, 'r'):
    opponent = opponent_map[line.split()[0]]
    me = line.split()[1]

    if me == 'X':
        #print(f"{opponent} vs {losing_shape[opponent]}")

        score = my_values[losing_shape[opponent]]
    elif me == 'Y':
        score = 3 + my_values[opponent]
    elif me == 'Z':
        score = 6 + my_values[winning_shape[opponent]]

    #print(score)

    total_score += score
print(total_score)
