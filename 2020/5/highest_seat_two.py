import sys
from math import fabs

from collections import defaultdict

def decode(ticket):
    row = int(ticket[:7].replace('F', '0').replace('B', '1'), 2)
    col = int(ticket[7:].replace('L', '0').replace('R', '1'), 2)
    return row * 8 + col

all_ids = defaultdict(list)
master_all_ids = []
for ticket in open(sys.argv[1], 'r').read().split('\n')[:-1]:
    seat_id = decode(ticket)
    index = seat_id % 10
    all_ids[index].append(seat_id)
    master_all_ids.append(seat_id)

master_all_ids = set(master_all_ids)

for i in range(1, 9):
    for id1 in all_ids[i-1]:
        for id2 in all_ids[i+1]:
            if fabs(id1 - id2) == 2 and (id1 + id2) / 2 not in master_all_ids:
                print(f'{id1} and {id2} are your neighbors, you are {int((id1+id2)/2)}')

# handle nine going back around to zero
for id1 in all_ids[0]:
    for id2 in all_ids[9]:
        if fabs(id1 - id2) == 2 and (id1 + id2) / 2 not in master_all_ids:
            print(f'{id1} and {id2} are your neighbors {int((id1+id2)/2)}')
