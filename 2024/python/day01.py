from utils import *

start_time: float = get_start_time()

left: list[int] = []
right: list[int] = []

for line in get_input_lines("day01.txt"):
    left_id, right_id = line.split()
    left.append(int(left_id))
    right.append(int(right_id))

left.sort()
right.sort()

print("[01p1] Total distance:", sum(abs(x - y) for x, y in zip(left, right)))

print("[01p2] Similarity score:", sum(i * right.count(i) for i in left))

print_time_elapsed(start_time)
