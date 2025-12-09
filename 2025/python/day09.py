from utils import *

start_time: float = get_start_time()

red_tiles: list[Point] = []

for line in get_input_lines("day09.txt"):
    x, y = map(int, line.split(","))
    red_tiles.append(Point(y, x))

def rectangle_area(p1: Point, p2: Point) -> int:
    return (abs(p1.row - p2.row) + 1) * (abs(p1.col - p2.col) + 1)

vertical_edges: dict[int, list[Interval]] = {}
horizontal_edges: dict[int, list[Interval]] = {}

for tile_1, tile_2 in itertools.pairwise(red_tiles):
    if tile_1.col == tile_2.col:
        first_row = min(tile_1.row, tile_2.row)
        if tile_1.col not in vertical_edges:
            vertical_edges[tile_1.col] = []
        vertical_edges[tile_1.col].append(Interval(first_row + 1, first_row + abs(tile_2.row - tile_1.row)))
    elif tile_1.row == tile_2.row:
        first_col = min(tile_1.col, tile_2.col)
        if tile_1.row not in horizontal_edges:
            horizontal_edges[tile_1.row] = []
        horizontal_edges[tile_1.row].append(Interval(first_col + 1, first_col + abs(tile_2.col - tile_1.col)))

def is_valid_rect(rect_min: Point, rect_max: Point) -> bool:
    for tile in red_tiles:
        if rect_min.row < tile.row < rect_max.row and rect_min.col < tile.col < rect_max.col:
            return False
    for col, row_intervals in vertical_edges.items():
        if not (rect_min.col < col < rect_max.col):
            continue
        for row_interval in row_intervals:
            if rect_min.row in row_interval and rect_max.row in row_interval:
                return False
    for row, col_intervals in horizontal_edges.items():
        if not (rect_min.row < row < rect_max.row):
            continue
        for col_interval in col_intervals:
            if rect_min.col in col_interval and rect_max.col in col_interval:
                return False
    return True

max_area_1: int = 0
max_area_2: int = 0

for index_1, tile_1 in enumerate(red_tiles):
    for index_2, tile_2 in enumerate(red_tiles):
        if index_2 <= index_1:
            continue
        area = rectangle_area(tile_1, tile_2)
        if area > max_area_1:
            max_area_1 = area
        if area > max_area_2:
            rect_min = Point(min(tile_1.row, tile_2.row), min(tile_1.col, tile_2.col))
            rect_max = Point(max(tile_1.row, tile_2.row), max(tile_1.col, tile_2.col))
            if is_valid_rect(rect_min, rect_max):
                max_area_2 = area

print("[09p1] Maximum area between two red tiles:", max_area_1)
print("[09p2] Maximum area using only red and green tiles:", max_area_2)

print_time_elapsed(start_time)
