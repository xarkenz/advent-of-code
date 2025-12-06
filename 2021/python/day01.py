from utils import *

start_time: float = get_start_time()

measurements: list[int] = [int(measurement) for measurement in get_input_lines("day01.txt")]

measurement_increases: int = sum(x < y for x, y in itertools.pairwise(measurements))
print("[01p1] Measurement increases:", measurement_increases)

sums: list[int] = [sum(measurements[index : index + 3]) for index in range(len(measurements) - 2)]
sum_increases: int = sum(x < y for x, y in itertools.pairwise(sums))
print("[01p2] Sliding window sum increases:", sum_increases)

print_time_elapsed(start_time)
