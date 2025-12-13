import sys


device_graph = {}
with open(sys.argv[1], 'r', encoding="utf-8") as data:
    for line in data:
        device, outputs = line.split(":")
        outputs = outputs.split()
        device_graph[device] = outputs

queue = [("you", [])]
explored = []
solutions = []

while len(queue) > 0:
    q = queue.pop(0)

    if q[0] == "out":
        solutions.append(q[1])
        explored.append(q[1])
        continue
    explored.append(q[1])

    for next_state in device_graph[q[0]]:
        queue.append((next_state, q[1] + [q[0]]))

print(len(solutions))
