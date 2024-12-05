import sys


data = []
with open(sys.argv[1], "r", encoding="utf-8") as file:
    for line in file:
        data.append(list(line)[:-1])

num_xmases = 0
for i in range(len(data)):
    for j in range(len(data[i])):
        if i == 0 or j == 0:
            continue
        if data[i][j] == "A":
            try:
                if data[i+1][j+1] == "S" and data[i-1][j+1] == "S" and data[i+1][j-1] == "M" and data[i-1][j-1] == "M":
                    print(f"Found one at {j}, {i}")
                    num_xmases += 1
                elif data[i+1][j+1] == "M" and data[i-1][j+1] == "M" and data[i+1][j-1] == "S" and data[i-1][j-1] == "S":
                    print(f"Found one at {j}, {i}")
                    num_xmases += 1
                elif data[i+1][j+1] == "M" and data[i-1][j+1] == "S" and data[i+1][j-1] == "M" and data[i-1][j-1] == "S":
                    print(f"Found one at {j}, {i}")
                    num_xmases += 1
                elif data[i+1][j+1] == "S" and data[i-1][j+1] == "M" and data[i+1][j-1] == "S" and data[i-1][j-1] == "M":
                    print(f"Found one at {j}, {i}")
                    num_xmases += 1
            except IndexError:
                continue


print(num_xmases)
