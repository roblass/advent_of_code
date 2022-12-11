# these print statements are only valid for the test case, ignore them on the "real" input
import sys

rows = open(sys.argv[1], 'r').read().split('\n')[:-1]

trees = {}
height = len(rows)
width = len(rows[0])
for row, r_val in enumerate(rows):
    for col, c_val in enumerate(r_val):
        trees[(int(col), int(row))] = int(c_val)

# check left edge
visible = []
for h in range(height):
    biggest = -1
    for w in range(width):
        if biggest < trees[(w, h)]:
            if (w, h) not in ((1, 1), (2, 1), (1, 2), (3, 2), (2, 3)) and not (w == 0 or h == 0)\
                    and not (w == 4 or h == 4):
                print(f"Error with {w, h} (left) biggest = {biggest} v = {trees[(w,h)]}")
            biggest = trees[(w, h)]
            visible.append((w, h))

# check right edge
for h in range(height):
    biggest = -1
    for w in range(width - 1, -1, -1):
        if biggest < trees[(w, h)]:
            if (w, h) not in ((1, 1), (2, 1), (1, 2), (3, 2), (2, 3)) and not (w == 0 or h == 0)\
                and not (w == 4 or h == 4):
                print(f"Error with {w, h} (right) biggest = {biggest} v = {trees[(w,h)]}")
            biggest = trees[(w, h)]
            visible.append((w, h))

# check top edge
for w in range(width):
    biggest = -1
    for h in range(height):
        if biggest < trees[(w, h)]:
            if (w, h) not in ((1, 1), (2, 1), (1, 2), (3, 2), (2, 3)) and not (w == 0 or h == 0)\
                and not (w == 4 or h == 4):
                print(f"Error with {w, h} (top) biggest = {biggest} v = {trees[(w,h)]}")
            biggest = trees[(w, h)]
            visible.append((w, h))

# check bottom edge
for w in range(width):
    biggest = -1
    for h in range(height - 1, -1, -1):
        if biggest < trees[(w, h)]:
            if (w, h) not in ((1, 1), (2, 1), (1, 2), (3, 2), (2, 3)) and not (w == 0 or h == 0)\
                and not (w == 4 or h == 4):
                print(f"Error with {w, h} (bottom) biggest = {biggest} v = {trees[(w,h)]}")
            biggest = trees[(w, h)]
            visible.append((w, h))



# should see all the (0, x) and (x, 0) plus (1, 1), (2, 1), (1, 2), (3, 2), (2, 3)
print(set(visible))
print(len(set(visible)))
