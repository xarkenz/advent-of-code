from utils import *

start_time: float = get_start_time()

fresh_ranges: IntervalSet = IntervalSet()
available_fresh_count: int = 0

for line in get_input_lines("day05.txt"):
    if not line:
        continue
    split = line.split("-")
    if len(split) == 2:
        start_id, end_id = map(int, split)
        fresh_ranges.insert(Interval(start_id, end_id + 1))
    elif int(line) in fresh_ranges:
        available_fresh_count += 1

print("[05p1] Available fresh ingredient IDs:", available_fresh_count)
print("[05p2] Total fresh ingredient IDs:", fresh_ranges.cardinality())

print_time_elapsed(start_time)
