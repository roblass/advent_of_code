import sys
from itertools import permutations

import numpy as np


def get_parameters(param_modes, program, _i, relative_base=None):
    parameters = []
    i = _i

    for index in [0, 1]: #mode in param_modes:
        try:
            mode = param_modes[index]
        except:
            mode = 0

        if mode == 0:
            parameters.append(int(program.get(program.get(i, 0), 0)))
        elif mode == 1:
            parameters.append(int(program.get(i, 0)))
        elif mode == 2:
            assert relative_base is not None
            parameters.append(program.get(program.get(i + relative_base, 0), 0))
        i += 1

    return parameters

def run_program():

    i = 0
    relative_base = 0

    with open(sys.argv[1], 'r') as f:
        prog_list = [int(i) for i in f.read().split(',')]
        program = {k: v for k,v in enumerate(prog_list)}

    while i < len(program):
        print('executing i =', i, 'with opcode', program[i])
        # figure out parameter mode
        if program[i] > 100:
            param_modes = str(program[i])
            param_modes[::-1]
            param_modes = [int(p) for p in param_modes[1:]]
            opcode = int(str(program[i])[-2:])
        else:
            param_modes = None
            opcode = program[i]

        if opcode == 1:
            storage = program[i + 3]
            val1, val2 = get_parameters(param_modes, program, i + 1, relative_base)
            program[storage] = val1 + val2
            i += 4
        elif opcode == 2:
            print('here with', program[i], param_modes)
            storage = program[i + 3]
            val1, val2 = get_parameters(param_modes, program, i + 1, relative_base)
            program[storage] = val1 * val2
            i += 4
        elif opcode == 3:  # store it in a location
            value = input("Enter your value: ")
            program[program[i + 1]] = value
            i += 2
        elif opcode == 4:  # output the value at some address
            if param_modes is not None and param_modes[0] == 1:
                output = program[i + 1]
            elif param_modes is not None and param_modes[0] == 2:
                output = program.get(program.get(i + 1, 0) + relative_base, 0)
            else:
                output = program[program[i + 1]]
            print(output)
            i += 2
        elif opcode == 5:  # jump if true
            val1, val2 = get_parameters(param_modes, program, i + 1, relative_base)
            if val1 != 0:
                i = val2
            else:
                i += 3
        elif opcode == 6:  # jump if false
            val1, val2 = get_parameters(param_modes, program, i + 1, relative_base)
            if val1 == 0:
                i = val2
            else:
                i += 3
        elif opcode == 7:  # jump if less than
            val1, val2 = get_parameters(param_modes, program, i + 1, relative_base)
            if val1 < val2:
                program[program[i + 3]] = 1
            else:
                program[program[i + 3]] = 0
            i += 4
        elif opcode == 8:  # jump if equals
            val1, val2 = get_parameters(param_modes, program, i + 1, relative_base)
            if val1 == val2:
                program[program[i + 3]] = 1
            else:
                program[program[i + 3]] = 0
            i += 4
        elif opcode == 9: # relative base offset
            val1 = get_parameters(param_modes, program, i + 1, relative_base)[0]
            print(val1)
            relative_base += val1
            i += 2
        elif opcode == 99:
            return output
        else:
            print('Got into a bad state')
            print(opcode)
            print(program)
            print(i)
            sys.exit()


# <203 
run_program()
