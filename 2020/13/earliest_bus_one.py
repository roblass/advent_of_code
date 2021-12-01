import sys

earliest, bus_ids = [l for l in open(sys.argv[1], 'r')][:2]

earliest_time = int(earliest)
bus_ids = [int(id) for id in bus_ids.split(',') if id != 'x']

earliest_bus = -1
earliest_difference = 99999 

for bus_id in bus_ids:
    new_bus_id = bus_id
    i = 1
    while new_bus_id < earliest_time:
        new_bus_id += bus_id
        i += 1
    if new_bus_id - earliest_time < earliest_difference:
        earliest_bus = bus_id
        earliest_difference = new_bus_id - earliest_time
        print(f'{earliest_bus} * {earliest_difference} = {earliest_bus * earliest_difference}')
