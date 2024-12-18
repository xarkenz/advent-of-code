from utils import *

frequency_antennas: dict[str, list[Point]] = {}

row_count: int = 0
col_count: int = 0

for row, line in enumerate(get_input_lines("day08.txt")):
    row_count += 1
    col_count = len(line)
    for col, frequency in enumerate(line):
        if frequency != ".":
            if frequency not in frequency_antennas:
                frequency_antennas[frequency] = [Point(row, col)]
            else:
                frequency_antennas[frequency].append(Point(row, col))

def is_in_bounds(point: Point):
    return point.row >= 0 and point.row < row_count and point.col >= 0 and point.col < col_count

antinodes: set[Point] = set()

for antennas in frequency_antennas.values():
    for i in range(len(antennas)):
        for j in range(i + 1, len(antennas)):
            diff = antennas[i] - antennas[j]
            test1 = antennas[i] + diff
            if is_in_bounds(test1):
                antinodes.add(test1)
            test2 = antennas[j] - diff
            if is_in_bounds(test2):
                antinodes.add(test2)

print("[day08p1] Unique antinodes:", len(antinodes))

for antennas in frequency_antennas.values():
    for i in range(len(antennas)):
        for j in range(i + 1, len(antennas)):
            antinodes.add(antennas[i])
            antinodes.add(antennas[j])
            diff = antennas[i] - antennas[j]
            test1 = antennas[i] + diff * 2
            while is_in_bounds(test1):
                antinodes.add(test1)
                test1 += diff
            test2 = antennas[j] - diff * 2
            while is_in_bounds(test2):
                antinodes.add(test2)
                test2 -= diff

print("[day08p2] Unique antinodes:", len(antinodes))

print_time_elapsed()
