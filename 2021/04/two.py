import sys
from collections import Counter

input = open(sys.argv[1], 'r').read().split('\n')[:-1]

draws = input[0].split(',')

boards = []

def won_horizontal(board):
    for row in board:
        if Counter(row)['*'] == 5:
            return True
    return False

def won_vertical(board):
    for i in range(len(board[0])):
        col = [e[i] for e in board]
        if Counter(col)['*'] == 5:
            return True
    return False


for i in range(0, len(input[2:]), 6):
    boards.append([r.split() for r in input[i+2:i+7]])

done = False
out_of_game = []
last_board = -1
for draw in draws:
    # mark all the spots matching this number
    for b, board in enumerate(boards):
        for r, row in enumerate(board):
            for e, element in enumerate(row):
                if element == draw:
                    boards[b][r][e] = '*'

    for b, board in enumerate(boards):
        if b in out_of_game:
            continue
        if won_horizontal(board):
            out_of_game.append(b)
            last_board = b
        elif won_vertical(board):
            out_of_game.append(b)
            last_board = b

    if len(out_of_game) == len(boards):
        print(f"Last draw was {draw}")
        total = sum([sum([int(r) for r in row if r != '*']) for row in boards[last_board]])
        print(f"Total unmarked = {total}")
        print(f"Answer is {total * int(draw)}")
        break
