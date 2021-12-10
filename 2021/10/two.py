import sys

lines = [e.strip() for e in open(sys.argv[1], 'r').read().split('\n')[:-1]]

score = 0
matches = {')': '(', ']': '[', '}': '{', '>': '<'}
rmatches = {v: k for k, v in matches.items()}
points = {')': 3, ']': 57, '}': 1197, '>': 25137}
all_missing = []
for line in lines:
    stack = []
    bad_line = False
    missing = []
    for i, char in enumerate(line):
        if char in matches.values():
            stack.append(char)
        elif matches[char] == stack[-1]:
            stack.pop()
        else:
            bad_line=True
            break
    if not bad_line:
        missing = [rmatches[e] for e in stack]
    all_missing.append(missing)

i_points = {')': 1, ']': 2, '}': 3, '>': 4}
scores = []
for missing in all_missing:
    total_score = 0
    for char in missing[::-1]:
        total_score *= 5
        total_score += i_points[char]
    if total_score:
        scores.append(total_score)


print(sorted(scores)[len(scores)//2])
