import sys

input = [e.strip() for e in open(sys.argv[1], 'r').read().split(',')]
print(input)

num_days = 0
keep_going = True
while num_days < 80:
    new_input = []
    to_append = []
    for i in input:
        new_i = int(i)- 1
        if i == 0:
            new_i = 6
            to_append.append(8)
        new_input.append(new_i)
    num_days += 1

    new_input.extend(to_append)
    input = new_input

print(len(input))
