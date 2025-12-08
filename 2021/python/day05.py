from utils import *

start_time: float = get_start_time()

hv_point_counts: dict[Point, int] = {}
all_point_counts: dict[Point, int] = {}

for line in get_input_lines("day05.txt"):
    x1, y1, x2, y2 = [int(value) for point in line.split(" -> ") for value in point.split(",")]
    dx = 0 if x1 == x2 else (x2 - x1) // abs(x2 - x1)
    dy = 0 if y1 == y2 else (y2 - y1) // abs(y2 - y1)
    steps = max(abs(x2 - x1), abs(y2 - y1)) + 1
    for step in range(steps):
        point = Point(y1 + dy * step, x1 + dx * step)
        if x1 == x2 or y1 == y2:
            hv_point_counts[point] = hv_point_counts.get(point, 0) + 1
        all_point_counts[point] = all_point_counts.get(point, 0) + 1

print("[05p1] Overlapping points (H/V only):", sum(count > 1 for count in hv_point_counts.values()))
print("[05p2] Overlapping points (all):", sum(count > 1 for count in all_point_counts.values()))

print_time_elapsed(start_time)
