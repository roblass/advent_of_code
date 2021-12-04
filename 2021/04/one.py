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
for draw in draws:
    # mark all the spots matching this number
    for b, board in enumerate(boards):
        for r, row in enumerate(board):
            for e, element in enumerate(row):
                if element == draw:
                    boards[b][r][e] = '*'

    for b, board in enumerate(boards):
        if won_horizontal(board):
            print(f"Winner on the horizontal! {board}")
            done = True
            break
        if won_vertical(board):
            print(f"Winner on the vertical! {board}")
            done = True
            break
    if done:
        print(f"Last draw was {draw}")
        total = sum([sum([int(r) for r in row if r != '*']) for row in board])
        print(f"Total unmarked = {total}")
        print(f"Answer is {total * int(draw)}")
        break
