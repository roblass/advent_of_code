import sys

with open(sys.argv[1], 'r') as f:
    program = [int(i) for i in f.read().split(',')]

i = 0


def get_parameters(param_modes, program, _i):
    parameters = []
    i = _i

    for index in [0, 1]: #mode in param_modes:
        try:
            mode = param_modes[index]
        except:
            mode = 0

        if mode == 0:
            parameters.append(int(program[program[i]]))
        elif mode == 1:
            parameters.append(int(program[i]))
        i += 1

    return parameters


while i < len(program):
    # figure out parameter mode
    if program[i] > 100:
        param_modes = [int(p) for p in str(program[i])[:-2]]
        param_modes.reverse()
        opcode = int(str(program[i])[-2:])
    else:
        param_modes = None
        opcode = program[i]

    if opcode == 1:
        storage = program[i + 3]
        val1, val2 = get_parameters(param_modes, program, i + 1)
        program[storage] = val1 + val2
        i += 4
    elif opcode == 2:
        storage = program[i + 3]
        val1, val2 = get_parameters(param_modes, program, i + 1)
        program[storage] = val1 * val2
        i += 4
    elif opcode == 3:  # store it in a location
        value = input("Enter your value: ")
        program[program[i + 1]] = value
        i += 2
    elif opcode == 4:  # output the value at some address
        if param_modes is not None and param_modes[0] == 1:
            output = program[i + 1]
        else:
            output = program[program[i + 1]]
        print(output)
        i += 2
    elif opcode == 5:  # jump if true
        val1, val2 = get_parameters(param_modes, program, i + 1)
        if val1 != 0:
            i = val2
        else:
            i += 3
    elif opcode == 6:  # jump if false
        val1, val2 = get_parameters(param_modes, program, i + 1)
        if val1 == 0:
            i = val2
        else:
            i += 3
    elif opcode == 7:  # jump if less than
        val1, val2 = get_parameters(param_modes, program, i + 1)
        if val1 < val2:
            program[program[i + 3]] = 1
        else:
            program[program[i + 3]] = 0
        i += 4
    elif opcode == 8:  # jump if equals
        val1, val2 = get_parameters(param_modes, program, i + 1)
        if val1 == val2:
            program[program[i + 3]] = 1
        else:
            program[program[i + 3]] = 0
        i += 4
    elif opcode == 99:
        break
    else:
        print('Got into a bad state')
        print(opcode)
        print(program)
        print(i)
        sys.exit()
