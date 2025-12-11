import sys

machines = []
with open(sys.argv[1], 'r', encoding="utf-8") as data:
    for line in data:
        tokens = line.split()
        lights = None
        buttons = []

        for token in tokens:
            if token[0] == '[':
                lights = token[1:-1]
                lights.split()
                lights = [False if l == '.' else l for l in lights]
                lights = [True if l == '#' else l for l in lights]
            elif token[0] == '(':
                buttons.append([int(e) for e in token[1:-1].split(",")])
            elif token[0] == '{':
                pass
            else:
                print(f"Unrecognized token {token}.")

        machines.append({"target_lights": lights, "lights": [False] * len(lights),
                         "buttons": buttons})


def expand(lights, button):
    #print(f"input {lights}")
    for index in button:
        lights[index] = not lights[index]
    #print(f"returning {lights}")
    return lights


total_presses = 0
for machine in machines:
    #print(f"Solving {machine}")
    queue = [(machine["lights"], [])]
    explored = []
    solution = None

    while len(queue) > 0:
        q = queue.pop(0)
        if q[0] in explored:
            #print(f"Already explored {q[0]}")
            continue

        #print(f"q is {q}")
        if q[0] == machine["target_lights"]:
            solution = q[1]
            break
        if q[0] in explored:
            continue
        explored.append(q[0])
        for button in machine["buttons"]:
            next_state = expand(q[0].copy(), button)
            queue.append((next_state, q[1] + [button]))

    print(f"Solution = {solution}")
    total_presses += len(solution)
print(f"Solved with a total of {total_presses} button presses.")
