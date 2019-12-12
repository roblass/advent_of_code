import sys
from itertools import permutations

class IntMachine:

    def __init__(self, program, debug=False):
        self.i = 0
        self.halt = False
        self.input_queue = []
        self.output_queue = []
        self.program = [int(i) for i in program.split(',')]
        self.debug = debug
        self.relative_base = 0
        self.opcode_param_num = {
            1: 3, # addition
            2: 3, # multiplication
            3: 1, # store value
            4: 1, # output value
            5: 2, # jump if true
            6: 2, # jump if false
            7: 3, # jump if less than
            8: 3, # jump if equal
            9: 1, # update relative base
            99: 0, # halt program
        }

    def get_parameters(self, opcode, modes):
        if self.debug:
            print('opcode', opcode, 'modes', modes)
        parameters = []
        for i in range(self.opcode_param_num[opcode]):
            if modes[i] == 0: # position
                parameters.append(self.program[self.program[self.i + i + 1]])
            elif modes[i] == 1: # immediate
                parameters.append(self.program[self.i + i + 1])
            elif modes[i] == 2: # relative
                parameters.append(self.program.get(self.program.get(self.i + i + 1 +
                                                                    self.relative_base, 0), 0))
        #Parameters that an instruction writes to will never be in immediate mode.
        if opcode == 3:
            parameters[0] = self.program[self.i + 1]
        if opcode in (1, 2):
            print('parameters', parameters)
            parameters[2] = self.program[self.i + 3]
        return parameters


    def decode_instruction(self):
        opcode = self.program[self.i]
        if opcode == 99 or opcode < 10:
            modes = [0] * self.opcode_param_num[opcode]
        else: # figure out parameters
            s_opcode = str(opcode)
            while len(s_opcode) < 5:
                s_opcode = '0' + s_opcode
            modes = [int(m) for m in list(s_opcode[0:3])]
            modes.reverse()
            opcode = int(s_opcode[-2:])

        params = self.get_parameters(opcode, modes)
        if self.debug:
            print('opcode=', opcode, 'params=', params)
        return opcode, params

    def execute_instruction(self, opcode, params):
        if opcode == 1:
            self.program[params[2]] = params[0] * params[1]
            self.i += self.opcode_param_num[opcode] + 1
        elif opcode == 2:
            self.program[params[2]] = params[0] * params[1]
            self.i += self.opcode_param_num[opcode] + 1
        elif opcode == 3:  # store input in a location
            try:
                value = self.input_queue.pop(0)
            except IndexError:
                value = input("Enter your value: ")
            self.program[params[0]] = value
            self.i += self.opcode_param_num[opcode] + 1
        elif opcode == 4:  # output the value at some address
            output = params[0]
            self.output_queue.append(output)
            print(output)
            self.i += self.opcode_param_num[opcode] + 1
        elif opcode == 5:  # jump if true
            if param[0] != 0:
                self.i = param[1]
            else:
                self.i += self.opcode_param_num[opcode] + 1
        elif opcode == 6:  # jump if false
            if param[0] == 0:
                self.i = param[1]
            else:
                self.i += self.opcode_param_num[opcode] + 1
        elif opcode == 7:  # jump if less than
            if param[0] < param[1]:
                self.program[param[2]] = 1
            else:
                self.program[param[2]] = 0
            self.i += self.opcode_param_num[opcode] + 1
        elif opcode == 8:  # jump if equals
            if param[0] == param[1]:
                self.program[param[2]] = 1
            else:
                self.program[param[2]] = 0
            self.i += self.opcode_param_num[opcode] + 1
        elif opcode == 9: # relative base offset
            relative_base += param[0]
            self.i += self.opcode_param_num[opcode] + 1
        elif opcode == 99:
            self.halt = True
        else:
            print('Got into a bad state')
            print(opcode)
            print(program)
            print(i)
            sys.exit()
        return False

    def run(self):
        while not self.halt:
            opcode, params = self.decode_instruction()
            should_pause = self.execute_instruction(opcode, params)
            if should_pause:
                return


if __name__ == '__main__':
    with open(sys.argv[1], 'r') as f:
        machine = IntMachine(f.read(), True)
        machine.run()
