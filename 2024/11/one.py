import sys


NUM_ITERATIONS = 25

def main():
    with open(sys.argv[1], "r", encoding="utf-8") as file:
        for line in file:
            stones = [int(l) for l in line.split()]
    print(stones)

    # execute rules, keeping track of previous states:
    num_times = 0
    while num_times < NUM_ITERATIONS:
        done_stones = []
        while stones:
            stone = stones.pop()
            stone_len = len(str(stone))
            if stone == 0:
                done_stones.append(1)
            elif stone_len % 2 == 0:
                new_stone = int(str(stone)[:stone_len // 2])
                done_stones.append(new_stone)
                done_stones.append(int(str(stone)[stone_len // 2:]))
            else:
                done_stones.append(stone * 2024)
        print("exited while")
        stones = done_stones
        num_times += 1
        print(num_times)
    print(done_stones)
    print(len(done_stones))


if __name__ == "__main__":
    main()
