import sys

def decode(ticket):
    row = int(ticket[:7].replace('F', '0').replace('B', '1'), 2)
    col = int(ticket[7:].replace('L', '0').replace('R', '1'), 2)
    return row * 8 + col

max_seat = -1
for ticket in open(sys.argv[1], 'r').read().split('\n')[:-1]:
    seat_id = decode(ticket)
    if seat_id > max_seat:
        max_seat = seat_id

print(max_seat)
