import sys

for x in range(100):
    for y in range(100):

        with open('input', 'r') as f:
            program = [int(i) for i in f.read().split(',')]
        program[1] = x
        program[2] = y

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
                if program[0] == 19690720:
                    print('x = ', x)
                    print('y = ', y)
                    print(100 * x + y)
                    sys.exit()
                break
            else:
                print('Got into a bad state')
                print(program[i])
                print(i)
                sys.exit()
