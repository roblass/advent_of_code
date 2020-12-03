#not 16
terrain = [list(l) for l in open('input.txt', 'r').read().split('\n')[:-1]]
terrain_width = len(terrain[0])

done = False
position = [0, 0] # backwards like terrain which is (y, x)
trees_seen = 0
while not done:
    # check position
    try:
        spot = terrain[position[0]][position[1]]
        if spot == '#':
            trees_seen += 1
    except IndexError: # done
        done = True
        continue

    # update position
    position[0] += 1
    position[1] += 3
    if position[1] >= terrain_width:
        position[1] -= terrain_width

print(f'trees seen = {trees_seen}')
