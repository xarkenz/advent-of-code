from utils import *

start_time: float = get_start_time()

grid: TileMap = get_input_tile_map("day04.txt")

def check_xmas(grid: TileMap, point: Point, direction: Point) -> bool:
    for letter in "XMAS":
        if grid.get(point) != letter:
            return False
        point = point + direction
    return True

def check_x_mas(grid: TileMap, point: Point) -> bool:
    if grid.get(point) == "A":
        tl = grid.get(point + (-1, -1))
        tr = grid.get(point + (-1, 1))
        bl = grid.get(point + (1, -1))
        br = grid.get(point + (1, 1))
        return ((tl == "M" and br == "S") or (tl == "S" and br == "M")) and ((tr == "M" and bl == "S") or (tr == "S" and bl == "M"))

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
x_mas_count: int = 0

for point, _ in grid:
    for direction in directions:
        if check_xmas(grid, point, direction):
            xmas_count += 1
    if check_x_mas(grid, point):
        x_mas_count += 1

print("[04p1] XMAS appearances:", xmas_count)
print("[04p2] X-MAS appearances:", x_mas_count)

print_time_elapsed(start_time)
