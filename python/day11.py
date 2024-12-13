from utils import *

init_stones = [int(i) for i in get_input_text("day11.txt").split()]

# Very devious way to have a static variable in a function because default values are only instantiated once
def get_stone_count(stone: int, blinks_left: int, *, memo: dict[tuple[int, int], int] = {}) -> int:
    if blinks_left == 0:
        return 1
    elif (stone, blinks_left) in memo:
        return memo[stone, blinks_left]
    count = 0
    if stone == 0:
        count = get_stone_count(1, blinks_left - 1)
    elif len(str(stone)) % 2 == 0:
        s = str(stone)
        count = get_stone_count(int(s[:len(s) // 2]), blinks_left - 1) + get_stone_count(int(s[len(s) // 2:]), blinks_left - 1)
    else:
        count = get_stone_count(stone * 2024, blinks_left - 1)
    memo[stone, blinks_left] = count
    return count

stone_count_p1: int = 0
stone_count_p2: int = 0
for init_stone in init_stones:
    stone_count_p1 += get_stone_count(init_stone, 25)
    stone_count_p2 += get_stone_count(init_stone, 75)

print("[day11p1] Stones after 25 blinks:", stone_count_p1)
print("[day11p2] Stones after 75 blinks:", stone_count_p2)

print_time_elapsed()
