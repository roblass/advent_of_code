import sys


data = []
with open(sys.argv[1], "r", encoding="utf-8") as file:
    for line in file:
        data.append(list(line)[:-1])

##
# HORIZONTAL
##
num_xmases = 0
for j, line  in enumerate(data):
    for i in range(len(line)):
        if line[i] == "X":
            try: # forwards
                if line[i+1] == "M" and line[i+2] == "A" and line[i+3] == "S":
                    print(f"Horizontal forwards: {i}, {j}")
                    num_xmases += 1
            except IndexError: # too close to the end of the line
                pass # can't exit loop since we have to look backwards still

            try: # backwards
                if i > 2 and line[i-1] == "M" and line[i-2] == "A" and line[i-3] == "S":
                    print(f"Horizontal backwards: {i}, {j}")
                    num_xmases += 1
            except IndexError: # too close to the end of the line
                break

##
# VERTICAL
##
for i in range(len(data)):
    for j in range(len(data[i])):
        if data[i][j] == "X":
            try: # forwards
                if data[i+1][j] == "M" and data[i+2][j] == "A" and data[i+3][j] == "S":
                    print(f"Vertical forwards: {j}, {i}")
                    num_xmases += 1
            except IndexError: # too close to the end of the line
                pass # can't exit loop since we have to look backwards still

            try: # backwards
                if i > 2 and data[i-1][j] == "M" and data[i-2][j] == "A" and data[i-3][j] == "S":
                    print(f"Vertical backwards: {j}, {i}")
                    num_xmases += 1
            except IndexError: # too close to the end of the line
                break

##
# DIAGONAL: POSITIVE SLOPE
##
for i in range(len(data)):
    for j in range(len(data[i])):
        if data[i][j] == "X":
            try: # forwards
                if data[i+1][j+1] == "M" and data[i+2][j+2] == "A" and data[i+3][j+3] == "S":
                    print(f"Diagonal positive forwards: {j}, {i}")
                    num_xmases += 1
            except IndexError: # too close to the end of the line
                pass # can't exit loop since we have to look backwards still

            try: # backwards
                if i > 2 and j > 2 and data[i-1][j-1] == "M" and data[i-2][j-2] == "A" and data[i-3][j-3] == "S":
                    print(f"Diagonal positive backwards: {j}, {i}")
                    num_xmases += 1
            except IndexError: # too close to the end of the line
                pass

            try: #backwards
                if j > 2 and data[i+1][j-1] == "M" and data[i+2][j-2] == "A" and data[i+3][j-3] == "S":
                    print(f"Diagonal negative backwards: {j}, {i}")
                    num_xmases += 1
            except IndexError: # too close to the end of the line
                pass # can't exit loop since we have to look forwards still

            try: # backwards
                if i > 2 and data[i-1][j+1] == "M" and data[i-2][j+2] == "A" and data[i-3][j+3] == "S":
                    print(f"Diagonal negative forwards: {j}, {i}")
                    num_xmases += 1
            except IndexError: # too close to the end of the line
                break

print(num_xmases)
