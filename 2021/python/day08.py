from utils import *

start_time: float = get_start_time()

segments_to_digit: dict[int, int] = {
    # gfedcba <- segment names
    0b1110111: 0,
    0b0100100: 1,
    0b1011101: 2,
    0b1101101: 3,
    0b0101110: 4,
    0b1101011: 5,
    0b1111011: 6,
    0b0100101: 7,
    0b1111111: 8,
    0b1101111: 9,
    # 7947868 <- segment frequencies
}
segment_indices: dict[str, int] = {chr(ord("a") + index): index for index in range(7)}
easy_digit_count: int = 0
output_sum: int = 0

def get_segments(pattern: str) -> list[bool]:
    segments = [False] * 7
    for segment_char in pattern:
        segments[segment_indices[segment_char]] = True
    return segments

def assign_unassigned_segment(signal_to_segment: list[Optional[int]], digits: list[list[bool]], target_signal_count: int, segment: int) -> None:
    target_digit = next(digit for digit in digits if sum(digit) == target_signal_count)
    signal_index = next(index for index, signal in enumerate(target_digit) if signal and signal_to_segment[index] is None)
    signal_to_segment[signal_index] = segment

def decode_digit(signals: list[bool], signal_to_segment: list[int]) -> int:
    return segments_to_digit[sum(1 << signal_to_segment[index] for index, signal in enumerate(signals) if signal)]

for line in get_input_lines("day08.txt"):
    digits, output = [[get_segments(pattern) for pattern in part.split()] for part in line.split(" | ")]
    easy_digit_count += sum(sum(digit) in (2, 3, 4, 7) for digit in output)

    signal_to_segment: list[Optional[int]] = [None] * 7
    signal_frequencies: list[int] = [sum(signals) for signals in zip(*digits)]

    # Find b as the only signal present in 6 digits
    signal_to_segment[signal_frequencies.index(6)] = 1
    # Find e as the only signal present in 4 digits
    signal_to_segment[signal_frequencies.index(4)] = 4
    # Find f as the only signal present in 9 digits
    signal_to_segment[signal_frequencies.index(9)] = 5
    # Find c as the only unassigned segment in the digit 1
    assign_unassigned_segment(signal_to_segment, digits, 2, 2)
    # Find a as the only unassigned segment in the digit 7
    assign_unassigned_segment(signal_to_segment, digits, 3, 0)
    # Find d as the only unassigned segment in the digit 4
    assign_unassigned_segment(signal_to_segment, digits, 4, 3)
    # Find g as the only unassigned segment in the digit 8
    assign_unassigned_segment(signal_to_segment, digits, 7, 6)

    output_value: int = 0
    for digit in output:
        output_value *= 10
        output_value += decode_digit(digit, signal_to_segment)
    output_sum += output_value

print("[08p1] Number of times 1/4/7/8 appear:", easy_digit_count)
print("[08p2] Sum of output values:", output_sum)

print_time_elapsed(start_time)
