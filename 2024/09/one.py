import sys


def main():
    disk = []
    with open(sys.argv[1], "r", encoding="utf-8") as file:
        for line in file: # should only be one line
            is_file = True
            file_id = 0
            for c in line[:-1]:
                if is_file:
                    disk.extend([file_id] * int(c))
                    file_id += 1
                else:
                    disk.extend(["."] * int(c))
                is_file = not is_file

    print(disk)

    # traverse the disk and shuffle data like the stupid problem asks
    i = 0
    j = -1
    for i in range(len(disk)):
        if disk[i] == ".":
            while disk[j] == ".":
                j -= 1
            if len(disk) + j < i:
                break
            disk[i] = disk[j]
            disk[j] = "."

    print(disk)

    # compute checksum
    checksum = 0
    for i, n in enumerate(disk):
        if n != ".":
            checksum += i * int(n)

    print(checksum)


if __name__ == "__main__":
    main()
