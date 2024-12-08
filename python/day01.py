from utils import *

left = []
right = []

for line in get_input_lines("day01.txt"):
    left_id, right_id = [int(i) for i in line.split()]
    left.append(left_id)
    right.append(right_id)

left.sort()
right.sort()

print("[day01p1] Total distance:", sum(abs(x - y) for x, y in zip(left, right)))

print("[day01p2] Similarity score:", sum(i * right.count(i) for i in left))

print_time_elapsed()
