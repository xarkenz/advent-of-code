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

tile_map: TileMap = get_input_tile_map("day04.txt")

initial_accessible_count: int = None
removable_count: int = 0

accessible_points: list[Point] = None
while accessible_points or accessible_points is None:
    accessible_points = []

    for point, tile in tile_map:
        if tile != "@":
            continue
        adjacent_rolls = 0
        for adjacent in adjacents:
            if tile_map.get(point + adjacent) == "@":
                adjacent_rolls += 1
                if adjacent_rolls >= 4:
                    break
        else:
            accessible_points.append(point)

    if initial_accessible_count is None:
        initial_accessible_count = len(accessible_points)
    removable_count += len(accessible_points)

    for point in accessible_points:
        tile_map.put(point, ".")

print("[04p1] Initially accessible paper rolls:", initial_accessible_count)
print("[04p2] Removable paper rolls:", removable_count)

print_time_elapsed(start_time)
