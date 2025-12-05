from utils import *

start_time: float = get_start_time()

# total_output_joltage: int = 0

# for bank in get_input_lines("day03.txt"):
#     bank = [int(digit) for digit in bank]
#     max_digit = max(bank)
#     max_index = bank.index(max_digit)
#     if max_index == len(bank) - 1:
#         next_max_digit = max(bank[:max_index])
#         total_output_joltage += next_max_digit * 10 + max_digit
#     else:
#         next_max_digit = max(bank[max_index + 1:])
#         total_output_joltage += max_digit * 10 + next_max_digit

# print("[03p1] Total output joltage:", total_output_joltage)

def get_total_output_joltage(select_count: int) -> int:
    total_output_joltage: int = 0

    for bank in get_input_lines("day03.txt"):
        max_joltage = ""
        start_index = 0
        for position in reversed(range(select_count)):
            max_digit = max(bank[start_index : len(bank) - position])
            max_joltage += max_digit
            start_index = bank.index(max_digit, start_index) + 1
        total_output_joltage += int(max_joltage)

    return total_output_joltage

print("[03p1] Total output joltage:", get_total_output_joltage(2))
print("[03p2] Total output joltage:", get_total_output_joltage(12))

print_time_elapsed(start_time)
