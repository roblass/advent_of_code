import sys


with open('input', 'r') as f:
    program = [int(i) for i in f.read().split(',')]

program[1] = 12
program[2] = 2

i = 0
while i < len(program):
    if program[i] == 1:
        storage = program[i+3]
        program[storage] = program[int(program[i+1])] + program[int(program[i+2])]
        i += 4
    elif program[i] == 2:
        storage = program[i+3]
        program[storage] = program[int(program[i+1])] * program[int(program[i+2])]
        i += 4
    elif program[i] == 99:
        print('halted.  position zero is ', program[0])
        break
    else:
        print('Got into a bad state')
        sys.exit()
