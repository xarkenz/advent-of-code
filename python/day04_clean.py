from utils import *

grid: TileMap = TileMap()

with open("input/day04.txt") as input_file:
    for row, line in enumerate(input_file.readlines()):
        grid.put((row, 0), line)

def check_word(grid: TileMap, point: Point, direction: Point):
    for letter in "XMAS":
        if grid.get(point) != letter:
            return False
        point = point + direction
    return True

directions: list[Point] = [
    Point(1, 0),
    Point(0, 1),
    Point(-1, 0),
    Point(0, -1),
    Point(1, 1),
    Point(1, -1),
    Point(-1, 1),
    Point(-1, -1),
]

xmas_count: int = 0

for point, tile in grid:
    for direction in directions:
        if check_word(grid, point, direction):
            xmas_count += 1

print(xmas_count)

def check_x(grid, r, c):
    if get(grid, r, c) == 'A':
        tl = get(grid, r - 1, c - 1)
        tr = get(grid, r - 1, c + 1)
        bl = get(grid, r + 1, c - 1)
        br = get(grid, r + 1, c + 1)
        return ((tl == 'M' and br == 'S') or (tl == 'S' and br == 'M')) and ((tr == 'M' and bl == 'S') or (tr == 'S' and bl == 'M'))

xmas_count = 0

for r in range(len(grid)):
    for c in range(len(grid[r])):
        if check_x(grid, r, c):
            xmas_count += 1

print(xmas_count)
