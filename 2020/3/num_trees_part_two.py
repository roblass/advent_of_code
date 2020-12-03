#not 16
terrain = [list(l) for l in open('input.txt', 'r').read().split('\n')[:-1]]
terrain_width = len(terrain[0])

final_answer = 1
slopes = ((1, 1), (1, 3), (1, 5), (1, 7), (2, 1))
for slope in slopes:
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
        position[0] += slope[0] 
        position[1] += slope[1] 
        if position[1] >= terrain_width:
            position[1] -= terrain_width

    print(f'for slope {slope}, num trees seen = {trees_seen}')
    final_answer *= trees_seen
print(f'final answer is {final_answer}')
