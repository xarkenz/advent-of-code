from utils import *

start_time: float = get_start_time()

# invalid_id_sum: int = 0

# for raw_range in get_input_text("day02.txt").strip().split(","):
#     raw_start_id, raw_end_id = raw_range.split("-")
#     start_id, end_id = int(raw_start_id), int(raw_end_id)

#     # Ensure start_id and end_id have the same (even) number of digits
#     start_digits = len(raw_start_id)
#     end_digits = len(raw_end_id)
#     if start_digits == end_digits:
#         if start_digits % 2 == 0:
#             # Same number of digits, even
#             digit_count = start_digits
#         else:
#             # Same number of digits, odd
#             continue # There is no possible invalid ID in this range
#     elif start_digits + 1 == end_digits:
#         if start_digits % 2 == 0:
#             # Starts even, ends odd
#             end_id = (10 ** start_digits) - 1
#             raw_end_id = str(end_id)
#             digit_count = start_digits
#         else:
#             # Starts odd, ends even
#             start_id = 10 ** (end_digits - 1)
#             raw_start_id = str(start_id)
#             digit_count = end_digits
#     else:
#         print("this shouldn't happen")
#         continue

#     start_half = int(raw_start_id[:digit_count // 2])
#     end_half = int(raw_end_id[:digit_count // 2])
#     high_mult = 10 ** (digit_count // 2)
#     for id_half in range(start_half, end_half + 1):
#         test_id = id_half * high_mult + id_half
#         if start_id <= test_id <= end_id:
#             invalid_id_sum += test_id

# print("[02p1] Sum of invalid IDs:", invalid_id_sum)

def get_digit_sequences(start: str, end: str) -> Generator[str, None, None]:
    # I'm sure there's a better way to do this but whatever
    for value in range(int(start), int(end) + 1):
        yield str(value)

invalid_id_sum_p1: int = 0
invalid_id_sum: int = 0

id_ranges = [raw.split("-") for raw in get_input_text("day02.txt").strip().split(",")]

while id_ranges:
    start_id, end_id = id_ranges.pop()

    digit_count = len(start_id)
    if digit_count + 1 == len(end_id):
        # Split the range into two ranges
        id_ranges.append(("1" + "0" * digit_count, end_id))
        end_id = "9" * digit_count
    if digit_count != len(end_id):
        print("this shouldn't happen")
        continue

    known_invalid_ids = set()
    for sequence_len in range(1, digit_count // 2 + 1):
        times, remainder = divmod(digit_count, sequence_len)
        if remainder != 0:
            continue
        for sequence in get_digit_sequences(start_id[:sequence_len], end_id[:sequence_len]):
            invalid_id = sequence * times
            if start_id <= invalid_id <= end_id:
                if invalid_id not in known_invalid_ids:
                    known_invalid_ids.add(invalid_id)
                    invalid_id_sum += int(invalid_id)
                if times == 2:
                    invalid_id_sum_p1 += int(invalid_id)

print("[02p1] Sum of invalid IDs:", invalid_id_sum_p1)
print("[02p2] Sum of invalid IDs:", invalid_id_sum)

print_time_elapsed(start_time)
