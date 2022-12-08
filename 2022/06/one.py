import sys

input_datastream = sys.argv[1]

test_datastreams = ["mjqjpqmgbljsphdztnvjfqwrcgsmlb", "bvwbjplbgvbhsrlpgdmjqwftvncz",
                    "nppdvjthqldpwncqszvftbrmjlhg", "nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg",
                    "zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw"]

test_answers = [7, 5, 6, 10, 11]

def find_marker(datastream):
    pot = []
    loc = 0
    for char in datastream:
        pot += char
        loc += 1
        if len(pot) < 4:
            continue
        elif len(pot) == 5:
            _ = pot.pop(0)

        if len(set(pot)) == 4:
            return loc
    return -1


for i in range(len(test_datastreams)):
    if find_marker(test_datastreams[i]) != test_answers[i]:
        print(f"Fail!  Returned {find_marker(test_datastreams[i])} on the {i}th element, should have been {test_answers[i]}.")

print(find_marker(input_datastream))
