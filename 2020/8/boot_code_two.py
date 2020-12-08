import sys

original_instructions = open(sys.argv[1], 'r').read().split('\n')[:-1]


def run_program(instructions):
    print(f'instructions = {instructions}')
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
            return

        if i in lines_seen:
            # we have the whole set
            print(f'no good')
            return (accumulator, lines_seen)
        lines_seen.append(i)

        if i == len(instructions):
            print('program completed')
            return (accumulator, [])


# try re-doing all the opcodes
accumulator, lines_seen = run_program(original_instructions)
if lines_seen:
    for i in range(len(lines_seen)):
        if original_instructions[lines_seen[i]].split()[0] == 'nop':
            print('switching to nop')
            new_instructions = original_instructions[:lines_seen[i]] +\
                [f'jmp {original_instructions[lines_seen[i]].split()[1]}'] +\
                original_instructions[lines_seen[i]+1:]
            accumulator, new_lines_seen = run_program(new_instructions)
            if new_lines_seen == []:
                print(f'done, accumulator = {accumulator}')
                break
        elif original_instructions[lines_seen[i]].split()[0] == 'jmp':
            print('switching to jmp')
            new_instructions = original_instructions[:lines_seen[i]] + ['nop 1337'] +\
                original_instructions[lines_seen[i]+1:]
            accumulator, new_lines_seen = run_program(new_instructions)
            if new_lines_seen == []:
                print(f'done, accumulator = {accumulator}')
                break
