import sys

lines = [e.strip() for e in open(sys.argv[1], 'r').read().split('\n')[:-1]]
print(lines)

num_unique = 0
for line in lines:
    input, output = line.split('|')
    print(input, output)
    for word in output.split():
        if len(set(sorted(word))) in [2, 3, 4, 7]:
            num_unique += 1

print(num_unique)
