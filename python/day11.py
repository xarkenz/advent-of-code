from utils import *

init_stones = [int(i) for i in get_input_text("day11.txt").split()]

stones = init_stones
for _ in range(25):
    new_stones = []
    for stone in stones:
        if stone == 0:
            new_stones.append(1)
        else:
            s = str(stone)
            if len(s) % 2 == 0:
                new_stones.append(int(s[:len(s) // 2]))
                new_stones.append(int(s[len(s) // 2:]))
            else:
                new_stones.append(stone * 2024)
    stones = new_stones

print(len(stones))

def get_stones(stone: int, blinks_left: int, *, memo: dict[tuple[int, int], int] = {}) -> int:
    if blinks_left == 0:
        return 1
    elif (stone, blinks_left) in memo:
        return memo[stone, blinks_left]
    count = 0
    if stone == 0:
        count = get_stones(1, blinks_left - 1)
    elif len(str(stone)) % 2 == 0:
        s = str(stone)
        count = get_stones(int(s[:len(s) // 2]), blinks_left - 1) + get_stones(int(s[len(s) // 2:]), blinks_left - 1)
    else:
        count = get_stones(stone * 2024, blinks_left - 1)
    memo[stone, blinks_left] = count
    return count

total = 0
for stone in init_stones:
    total += get_stones(stone, 75)
print(total)

print_time_elapsed()
