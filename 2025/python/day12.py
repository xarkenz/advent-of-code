from utils import *

#  O     OO   O    O     O   O    O   OO
#  OOO  OO   OOO   OO  OOO  OO   OOO   OO
#   O    O     O  OO    O    OO  O     O

start_time: float = get_start_time()

presents: list[frozenset[Point]] = []
current_present: list[Point] = []
current_row: int = 0
scenarios: list[tuple[Point, list[int]]] = []

for line in get_input_lines("day12.txt"):
    if not line:
        presents.append(frozenset(current_present))
        current_present = []
        current_row = 0
    elif len(line) <= 3:
        if ":" in line:
            continue
        current_present.extend(Point(current_row, col) for col, char in enumerate(line) if char == "#")
        current_row += 1
    else:
        dimensions, present_counts = line.split(": ")
        scenarios.append((
            Point(*map(int, dimensions.split("x"))),
            list(map(int, present_counts.split())),
        ))

def get_present_configurations(present: frozenset[Point]) -> set[frozenset[Point]]:
    configurations: set[frozenset[Point]] = {present}
    flipped = frozenset(Point(point.row, 2 - point.col) for point in present)
    configurations.add(flipped)
    for current in (present, flipped):
        for _ in range(3):
            # Rotate 90 degrees clockwise
            current = frozenset(Point(point.col, 2 - point.row) for point in current)
            configurations.add(current)
    return configurations

present_configurations: list[set[frozenset[Point]]] = [get_present_configurations(present) for present in presents]

fitting_region_count: int = 0

for dimensions, present_counts in scenarios:
    area = dimensions.row * dimensions.col
    if area < sum(len(present) * count for present, count in zip(presents, present_counts)):
        continue
    elif area >= 9 * sum(present_counts):
        fitting_region_count += 1
        continue

print("[12p1] Number of regions fitting all presents:", fitting_region_count)
print("[12p2] Finish decorating the North Pole!")

print_time_elapsed(start_time)
