import sys

# this works on the example, but not my unique input
# 85626110370 is too low


def pretty_print(disk):
    s = ""
    for char, num in disk:
        if num==0:
            print("what the fuck")
            print(disk)
        s += str(char) * num
    return s


def main():
    disk = []
    with open(sys.argv[1], "r", encoding="utf-8") as file:
        for line in file: # should only be one line
            is_file = True
            file_id = 0
            for c in line[:-1]:
                if is_file:
                    disk.append([file_id, int(c)])
                    file_id += 1
                else:
                    disk.append([".", int(c)])
                is_file = not is_file

    # traverse the disk and shuffle data like the second part of the stupid problem asks
    file_index = len(disk)
    while file_index >= 0:
        print(file_index)
        file_index -= 1
        if disk[file_index][0] != ".":
            space_index = 0

            while True:
                if space_index >= len(disk):
                    break
                if disk[space_index][0] != ".":
                    space_index += 1
                    continue
                if int(disk[space_index][1]) < int(disk[file_index][1]):
                    space_index += 1
                    continue
                break
            if space_index >=  file_index:
                continue
            if space_index < len(disk):
                old_space = disk[space_index] # save the old amount of space
                disk[space_index] = disk[file_index] # copy the file over
                space_diff = old_space[1] - disk[file_index][1]
                # can we insert it directly, or do we merge with the next or previous spot?
                if disk[space_index-1][0] != "." and disk[space_index+1][0] != ".":
                    disk[file_index] = [".", disk[space_index][1]]
                    if space_diff > 0:
                        disk.insert(space_index+1, [".", space_diff])
                        file_index += 1
                elif disk[space_index-1][0] == "." and (space_index == len(disk) or
                                                        disk[space_index+1][0] != "."):
                    disk[space_index-1][1] += space_diff
                    _ = disk.pop(space_index)
                    file_index -= 1
                # merge them all
                elif disk[space_index-1][0] == "." and disk[space_index+1][0] == ".":
                    disk[space_index-1][1] += space_diff + disk[space_index+1][1]
                    _ = disk.pop(space_index)
                    _ = disk.pop(space_index)
                    file_index -= 2
                elif disk[space_index+1][0] == ".":
                    if space_diff > 0:
                        disk[space_index+1][1] += space_diff
                        _ = disk.pop(space_index)
                    file_index -= 1
                else:
                    print("This is not possible")

    # compute checksum
    checksum = 0
    for i, n in enumerate(pretty_print([d for d in disk if d[1] > 0])):
        if n != ".":
            checksum += i * int(n)

    print(checksum)


if __name__ == "__main__":
    main()
