import sys

import numpy as np
from scipy.optimize import milp, LinearConstraint, Bounds


machines = []
with open(sys.argv[1], 'r', encoding="utf-8") as data:
    for line in data:
        tokens = line.split()
        lights = None
        buttons = []

        for token in tokens:
            if token[0] == '[':
                pass
            elif token[0] == '(':
                buttons.append([int(e) for e in token[1:-1].split(",")])
            elif token[0] == '{':
                target_joltage = [int(e) for e in token[1:-1].split(",")]
            else:
                print(f"Unrecognized token {token}.")

        machines.append({"target_joltage": target_joltage, "joltages": [0] * len(target_joltage),
                         "buttons": buttons})

total_presses = 0
for machine in machines:
    num_vars = len(machine["target_joltage"])
    num_exprs = len(machine["buttons"])

    A = np.zeros((num_vars, num_exprs))

    for col, indices in enumerate(machine["buttons"]):
        for row in indices:
            A[row, col] = 1

    constraints = LinearConstraint(A, lb=machine["target_joltage"], ub=machine["target_joltage"])
    result = milp(c=np.ones(num_exprs), constraints=constraints, integrality=np.ones(num_exprs),
               bounds=Bounds(lb=0, ub=np.inf))

    if result.success:
        solution = np.round(result.x).astype(int)
    else:
        solution = None

    if solution is not None:
        total_presses += solution.sum()
    else:
        print("No solution!")

print(f"Solved with a total of {total_presses} button presses.")
