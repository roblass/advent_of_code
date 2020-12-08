import sys



instructions = open(sys.argv[1], 'r').read().split('\n')[:-1]

i = 0
accumulator = 0
lines_seen = []
while True:
    op, arg = instructions[i].split()
    if op == 'acc':
        accumulator += int(arg)
        i += 1
    elif op == 'jmp':
        i += int(arg)
    elif op == 'nop':
        i += 1
    else:
        print(f'invalid op {op}')
        break

    if i in lines_seen:
        print(f'the accumulator has a value of {accumulator}')
        break
    lines_seen.append(i)
