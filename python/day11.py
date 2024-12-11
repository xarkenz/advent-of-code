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

# count at each step, resulting digits
# digit_expansions: list[tuple[int, list[int]]] = [
#     ([1, 1, 2, 4], [2, 0, 2, 4]),
#     ([1, 2, 4], [2, 0, 2, 4]),
#     ([1, 2, 4], [4, 0, 4, 8]),
#     ([1, 2, 4], [6, 0, 7, 2]),
#     ([1, 2, 4], [8, 0, 9, 6]),
#     ([1, 1, 2, 4, 8], [2, 0, 4, 8, 2, 8, 8, 0]),
#     ([1, 1, 2, 4, 8], [2, 4, 5, 7, 9, 4, 5, 6]),
#     ([1, 1, 2, 4, 8], [2, 8, 6, 7, 6, 0, 3, 2]),
#     ([1, 1, 2, 4, 8], [3, 2, 7, 7, 2, 6, 0, 8]),
#     ([1, 1, 2, 4, 8], [3, 6, 8, 6, 9, 1, 8, 4]),
# ]

# def is_power_of_two(n):
#     return (n != 0) and (n & (n - 1) == 0)

# def predict_count(digit: int, blinks_left: int, *, memo: dict[tuple[int, int], int] = {}) -> int:
#     if blinks_left == 0:
#         return 1
#     if (digit, blinks_left) in memo:
#         return memo[digit, blinks_left]
#     blinks, new_digits = digit_expansions[digit]
#     if len(blinks) > blinks_left:
#         memo[digit, blinks_left] = blinks[blinks_left - 1]
#         return blinks[blinks_left - 1]
#     new_blinks_left = blinks_left - len(blinks)
#     total = 0
#     for new_digit in new_digits:
#         total += predict_count(new_digit, new_blinks_left)
#     memo[digit, blinks_left] = total
#     return total

# blink_limit = 25

# stone_count = 0
# stones: list[tuple[int, int]] = [(0, stone) for stone in init_stones]
# while stones:
#     blinks, stone = stones.pop()
#     while True:
#         if blinks == blink_limit:
#             stone_count += 1
#             break
#         blinks += 1
#         if stone == 0:
#             stone = 1
#         else:
#             s = str(stone)
#             if len(s) % 2 == 0:
#                 if is_power_of_two(len(s)):
#                     for digit in s:
#                         stone_count += predict_count(int(digit), blink_limit - blinks)
#                     break
#                 else:
#                     stones.append((blinks, int(s[: len(s) // 2])))
#                     stone = int(s[len(s) // 2 :])
#             else:
#                 stone *= 2024

# print(stone_count)

# stones = [1]
# limit = 11
# for _ in range(limit):
#     new_stones = []
#     for stone in stones:
#         if stone == 0:
#             new_stones.append(1)
#         else:
#             s = str(stone)
#             if len(s) % 2 == 0:
#                 new_stones.append(int(s[:len(s) // 2]))
#                 new_stones.append(int(s[len(s) // 2:]))
#             else:
#                 new_stones.append(stone * 2024)
#     stones = new_stones
#     print(stones)
# print(len(stones))
# print(predict_count(1, limit))

print_time_elapsed()
