from utils import *

points: dict[str, list[Point]] = {}

row_count = 0
col_count = 0

with open("input/day08.txt") as input_file:
    for row, line in enumerate(input_file.readlines()):
        col_count = max(col_count, len(line.strip()))
        for col, char in enumerate(line.strip()):
            if char == ".":
                continue
            if char not in points:
                points[char] = []
            points[char].append(Point(row, col))
        row_count += 1

def is_inside(point: Point):
    global row_count, col_count
    return point.row >= 0 and point.row < row_count and point.col >= 0 and point.col < col_count

antinodes: set[Point] = set()

for freq, antennas in points.items():
    for i in range(len(antennas)):
        for j in range(i + 1, len(antennas)):
            diff = antennas[i] - antennas[j]
            test1 = antennas[i] + diff
            if is_inside(test1):
                antinodes.add(test1)
            test2 = antennas[j] - diff
            if is_inside(test2):
                antinodes.add(test2)

print(len(antinodes))

for freq, antennas in points.items():
    for i in range(len(antennas)):
        for j in range(i + 1, len(antennas)):
            diff = antennas[i] - antennas[j]
            test1 = antennas[i] + diff
            while is_inside(test1):
                antinodes.add(test1)
                test1 += diff
            # This was intended to be "antennas[j] - diff"... but the typo got me the right answer!
            # I hadn't realized that the antennas were now included
            test2 = antennas[j] + diff
            while is_inside(test2):
                antinodes.add(test2)
                test2 -= diff

print(len(antinodes))

print_time_elapsed()
