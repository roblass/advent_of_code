import sys


with open(sys.argv[1], 'r', encoding="utf-8") as data:
    ranges = []
    availables = []
    mode = "RANGE"
    for line in data:
        if line == "\n":
            mode = "AVAILABLE"
        elif mode == "RANGE":
            begin, end = line.strip().split('-')
            ranges.append((int(begin), int(end)))
        elif mode == "AVAILABLE":
            num = int(line.strip())
            for begin, end in ranges:
                if begin <= num <= end:
                    availables.append(num)
                    break
print(availables)
print(len(availables))
