import sys
import threading
from collections import deque
from itertools import permutations

import numpy as np


def get_parameters(param_modes, program, _i):
    parameters = []
    i = _i

    for index in [0, 1]: #mode in param_modes:
        try:
            mode = param_modes[index]
        except:
            mode = 0

        if mode == 0:
            try:
                parameters.append(int(program[program[i]]))
            except:
                print('fuck', i)
                print('fuck', program)
                print('fuck', program[program[i]])
        elif mode == 1:
            parameters.append(int(program[i]))
        i += 1

    return parameters


class IntMachine(threading.Thread):
    def __init__(self):
        super(IntMachine, self).__init__()
        self.i = 0
        self.check_input = threading.Condition()
        self.check_output = threading.Condition()
        self.input_queue = deque([])
        self.output_queue = deque([])

        with open(sys.argv[1], 'r') as f:
            self.program = [int(i) for i in f.read().split(',')]

    def get_output(self):
        while len(self.output_queue) == 0:
            self.check_output.acquire()
            self.check_output.wait()
            self.check_output.release()
        return self.output_queue.popleft()



    def insert_input(self, elements):
        self.input_queue.extend(elements)
        self.check_input.acquire()
        self.check_input.notify()
        self.check_input.release()

    def run(self):
        while self.i < len(self.program):
            # figure out parameter mode
            if self.program[self.i] > 100:
                param_modes = [int(p) for p in str(self.program[self.i])[:-2]]
                param_modes.reverse()
                opcode = int(str(self.program[self.i])[-2:])
            else:
                param_modes = None
                opcode = self.program[self.i]

            if opcode == 1:
                storage = self.program[self.i + 3]
                val1, val2 = get_parameters(param_modes, self.program, self.i + 1)
                self.program[storage] = val1 + val2
                self.i += 4
            elif opcode == 2:
                storage = self.program[self.i + 3]
                val1, val2 = get_parameters(param_modes, self.program, self.i + 1)
                self.program[storage] = val1 * val2
                self.i += 4
            elif opcode == 3:  # store it in a location
                # get the value from the queue when it exists
                while len(self.input_queue) == 0:
                    self.check_input.acquire()
                    self.check_input.wait()
                    self.check_input.release()
                value = self.input_queue.popleft()
                if value == None:
                    print('what the fuck!')
                    aoeu()
                self.program[self.program[self.i + 1]] = value
                self.i += 2
            elif opcode == 4:  # output the value at some address
                if param_modes is not None and param_modes[0] == 1:
                    output = self.program[self.i + 1]
                else:
                    output = self.program[self.program[self.i + 1]]
                print(output)
                self.output_queue.append(output)
                self.check_output.acquire()
                self.check_output.notify()
                self.check_output.release()
                self.i += 2
            elif opcode == 5:  # jump if true
                val1, val2 = get_parameters(param_modes, self.program, self.i + 1)
                if val1 != 0:
                    self.i = val2
                else:
                    self.i += 3
            elif opcode == 6:  # jump if false
                val1, val2 = get_parameters(param_modes, self.program, self.i + 1)
                if val1 == 0:
                    self.i = val2
                else:
                    self.i += 3
            elif opcode == 7:  # jump if less than
                val1, val2 = get_parameters(param_modes, self.program, self.i + 1)
                if val1 < val2:
                    self.program[self.program[self.i + 3]] = 1
                else:
                    self.program[self.program[self.i + 3]] = 0
                self.i += 4
            elif opcode == 8:  # jump if equals
                val1, val2 = get_parameters(param_modes, self.program, self.i + 1)
                if val1 == val2:
                    self.program[self.program[self.i + 3]] = 1
                else:
                    self.program[self.program[self.i + 3]] = 0
                self.i += 4
            elif opcode == 99:
                return
            else:
                print('Got into a bad state')
                print(opcode)
                print(self.program)
                print(self.i)
                sys.exit()


phase_setting = 0
best_output = -np.inf
best_signal = None
for permutation in permutations('01234'):

    #construct machines
    machines = [IntMachine() for i in range(5)]

    #start machines
    [m.start() for m in machines]

    # give them the input they need
    last_output = phase_setting
    machines[0].insert_input([permutation[0], last_output])
    for i in range(4):
        last_output = machines[i].get_output()
        machines[i + 1].insert_input([permutation[i + 1], last_output])

    last_output = machines[4].get_output()

    if last_output > best_output:
        best_output = last_output
        best_signal = permutation
print('best output', best_output)
print('best signal', best_signal)
