import sys

history = int(sys.argv[1])
line_no = 0
prev_num = []
done = False
no_good = -1
for line in open(sys.argv[2], 'r'):
    if done:
        break
    if line_no < history:
        prev_num.append(int(line))
        line_no += 1
    else:
        passes = False
        for i in prev_num:
            for j in prev_num:
                if i + j == int(line):
                    passes = True
                    break
            if passes:
                break
        prev_num.pop(0)
        prev_num.append(int(line))
        if not passes:
            print(f'first no good {line}')
            no_good = int(line)
            done = True
            break



def do_it():
    all_nums = [int(l) for l in open(sys.argv[2], 'r').read().split('\n')[:-1]]
    for i in range(len(all_nums)):
            j = 0
            while sum(all_nums[i:j]) <= no_good:
                if sum(all_nums[i:j]) == no_good:
                    print(f'{min(all_nums[i:j])} is min and {max(all_nums[i:j])} is max')
                    print(f'    = {min(all_nums[i:j]) + max(all_nums[i:j])}')
                    return
                else:
                    j += 1

do_it()
