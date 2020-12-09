import sys

history = int(sys.argv[1])
line_no = 0
prev_num = []
done = False
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
            done = True
            break
