import sys

lines = [e.strip() for e in open(sys.argv[1], 'r').read().split('\n')[:-1]]

score = 0
stack = []
matches = {')': '(', ']': '[', '}': '{', '>': '<'}
points = {')': 3, ']': 57, '}': 1197, '>': 25137}
for line in lines:
    for i, char in enumerate(line):
        if char in matches.values():
            stack.append(char)
        elif matches[char] == stack[-1]:
            stack.pop()
        else:
            score += points[char]
            break
print(score)
