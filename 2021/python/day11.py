from utils import *

start_time: float = get_start_time()

adjacents: list[Point] = [
    Point(1, 0),
    Point(1, 1),
    Point(0, 1),
    Point(-1, 1),
    Point(-1, 0),
    Point(-1, -1),
    Point(0, -1),
    Point(1, -1),
]

octopuses: list[list[int]] = [[int(energy) for energy in line] for line in get_input_lines("day11.txt")]
row_count: int = len(octopuses)
col_count: int = len(octopuses[0])
flash_count: int = 0

step: int = 0
while True:
    step += 1
    to_increment: list[Point] = []
    for row in range(row_count):
        for col in range(col_count):
            octopuses[row][col] += 1
            if octopuses[row][col] > 9:
                to_increment.append(Point(row, col))

    flashed: set[Point] = set()
    while to_increment:
        point = to_increment.pop(0)
        if octopuses[point.row][point.col] < 9 or point in flashed:
            octopuses[point.row][point.col] += 1
            continue
        for offset in adjacents:
            adjacent = point + offset
            if adjacent.row in range(row_count) and adjacent.col in range(col_count):
                to_increment.append(adjacent)
        flashed.add(point)
        flash_count += 1
    for point in flashed:
        octopuses[point.row][point.col] = 0

    if step == 100:
        print("[11p1] Number of flashes after 100 steps:", flash_count)
    if len(flashed) == row_count * col_count:
        break

print("[11p2] Synchronizing step:", step)

print_time_elapsed(start_time)
