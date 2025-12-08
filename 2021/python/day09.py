from utils import *

start_time: float = get_start_time()

directions: list[Point] = [
    Point(1, 0),
    Point(0, 1),
    Point(-1, 0),
    Point(0, -1),
]

heightmap: TileMap = get_input_tile_map("day09.txt")
basins: dict[Point, set[Point]] = {}
risk_level_sum: int = 0

for point, tile in heightmap:
    for direction in directions:
        other_tile = heightmap.get(point + direction)
        if other_tile != " " and other_tile <= tile:
            break
    else:
        basins[point] = {point}
        risk_level_sum += int(tile) + 1

print("[09p1] Sum of low point risk levels:", risk_level_sum)

for low_point, basin_region in basins.items():
    frontier: list[Point] = [low_point]
    while frontier:
        current_point = frontier.pop(0)
        current_tile = heightmap.get(current_point)
        for direction in directions:
            test_point = current_point + direction
            if test_point in basin_region:
                continue
            test_tile = heightmap.get(test_point)
            if "0" <= test_tile <= "8" and test_tile >= current_tile:
                basin_region.add(test_point)
                frontier.append(test_point)

basin_sizes: list[int] = [len(region) for region in basins.values()]
basin_sizes.sort(reverse=True)

print(f"[09p2] Three largest basins: {basin_sizes[0]} * {basin_sizes[1]} * {basin_sizes[2]} = {basin_sizes[0] * basin_sizes[1] * basin_sizes[2]}")

print_time_elapsed(start_time)
