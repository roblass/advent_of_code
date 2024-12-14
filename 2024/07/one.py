# -*- coding: utf-8 -*-

import sys

from itertools import product


def evaluate_left_to_right(tokens):
    result = int(tokens.pop(0))
    while tokens:
        operator = tokens.pop(0)
        operand = int(tokens.pop(0))
        if operator == '+':
            result = result + operand
        elif operator == '-':
            result = result - operand
        elif operator == '*':
            result = result * operand
        elif operator == '/':
            result = result / operand
    return result


def is_valid(value, operands):
    for operators in product(["+", "*"], repeat=len(operands) - 1):
        eq = [i for item in zip(operands, list(operators) + [None]) for i in item if i is not None]
        if value == evaluate_left_to_right(eq):
            return True
    return False


def main():
    total = 0
    with open(sys.argv[1], "r", encoding="utf-8") as file:
        for line in file:
            value, operands = line.split(":")
            value = int(value)
            operands = operands.split()

            if is_valid(value, operands):
                total += value

    print(total)


if __name__ == '__main__':
    main()
