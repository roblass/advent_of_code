import sys
from sympy import symbols, Eq, solve


def solve_exact(buttons, X, Y):
    n_a, n_b, t = symbols('n_a n_b t', integer=True)
    x_a, y_a = buttons[0]
    x_b, y_b = buttons[1]

    eq1 = Eq(x_a * n_a + x_b * n_b, X)
    eq2 = Eq(y_a * n_a + y_b * n_b, Y)

    solutions = solve((eq1, eq2), (n_a, n_b), dict=True)

    min_cost = float('inf')
    best_solution = None

    for sol in solutions:
        n_a_expr = sol[n_a]
        n_b_expr = sol[n_b]

        for t_val in range(-100, 101):
            n_a_val = n_a_expr.subs(t, t_val)
            n_b_val = n_b_expr.subs(t, t_val)

            if n_a_val.is_integer and n_b_val.is_integer and n_a_val >= 0 and n_b_val >= 0:
                cost = 3 * n_a_val + n_b_val
                if cost < min_cost:
                    min_cost = cost
                    best_solution = (int(n_a_val), int(n_b_val))

    return best_solution, min_cost


def main():
    with open(sys.argv[1], "r", encoding="utf-8") as file:
        step = 0
        machines = []
        buttons = []
        for line in file:
            if step in (0, 1):
                x, y = line.split()[2:]
                x = int(x.split("+")[1][:-1])
                y = int(y.split("+")[1])
                buttons.append((x, y))
            elif step == 2:
                x, y = line.split()[1:]
                x = int(x.split("=")[1][:-1]) + 10000000000000
                y = int(y.split("=")[1]) + 10000000000000
                machines.append((buttons, (x, y)))
            elif step == 3:
                buttons = []
                step = 0
                continue
            step += 1

    print(machines)

    total_cost = 0
    for buttons, (X, Y) in machines:
        solution = solve_exact(buttons, X, Y)
        print(solution)
        cost = solution[-1]
        if cost != float("inf"):
            total_cost += cost

    print(total_cost)

if __name__== "__main__":
    main()
