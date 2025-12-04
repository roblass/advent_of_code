import sys


with open(sys.argv[1], 'r', encoding="utf-8") as data:
    total_joltage = 0
    for line in data:

        number = line.strip()
        skips_left = len(number) - 12

        stack = []
        for digit in number:
            while skips_left > 0 and stack and stack[-1] < digit:
                stack.pop()
                skips_left -= 1
            stack.append(digit)

        joltage = int("".join(stack[:12]))
        total_joltage += joltage

print(total_joltage)
