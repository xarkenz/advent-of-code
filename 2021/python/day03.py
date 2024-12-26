from utils import *

start_time: float = get_start_time()

report: list[str] = get_input_lines("day03.txt")

bit_count = len(report[0])
zero_counts: list[int] = [0] * bit_count
one_counts: list[int] = [0] * bit_count
for number in report:
    for index, bit in enumerate(number):
        (zero_counts if bit == "0" else one_counts)[index] += 1

gamma_rate: int = 0
for zero_count, one_count in zip(zero_counts, one_counts):
    gamma_rate = (gamma_rate << 1) | (one_count >= zero_count)
epsilon_rate: int = ~gamma_rate & ((1 << bit_count) - 1)

print("[03p1] Gamma rate times epsilon rate:", gamma_rate * epsilon_rate)

remaining_o2: list[str] = report
remaining_co2: list[str] = report
for index in range(bit_count):
    if len(remaining_o2) > 1:
        most_bit = "1" if sum(number[index] == "1" for number in remaining_o2) * 2 >= len(remaining_o2) else "0"
        remaining_o2 = [number for number in remaining_o2 if number[index] == most_bit]
    if len(remaining_co2) > 1:
        least_bit = "0" if sum(number[index] == "1" for number in remaining_co2) * 2 >= len(remaining_co2) else "1"
        remaining_co2 = [number for number in remaining_co2 if number[index] == least_bit]

print(remaining_o2, remaining_co2)

o2_gen_rating: int = 0
for bit in remaining_o2[0]:
    o2_gen_rating = (o2_gen_rating << 1) | (bit != "0")
co2_scrub_rating: int = 0
for bit in remaining_co2[0]:
    co2_scrub_rating = (co2_scrub_rating << 1) | (bit != "0")

print("[03p2] O2 generator rating times CO2 scrubber rating:", o2_gen_rating * co2_scrub_rating)

print_time_elapsed(start_time)
