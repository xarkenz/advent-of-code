from utils import *

grid = get_input_tile_map("day12.txt")
checked_regions: set[Point] = set()

directions: list[Point] = [
    Point(1, 0),
    Point(0, 1),
    Point(-1, 0),
    Point(0, -1),
]

total_price_p1: int = 0
total_price_p2: int = 0

start_queue: dict[Point, str] = {Point(0, 0): grid.get((0, 0))}
while start_queue:
    start, region_type = start_queue.popitem()
    if start in checked_regions:
        continue
    checked_regions.add(start)
    region: set[Point] = {start}
    perimeter_check_region: set[Point] = {start}
    frontier: list[Point] = [start]
    while frontier:
        point = frontier.pop()
        for direction_index, direction in enumerate(directions):
            new_point = point + direction
            if new_point not in region:
                new_region_type = grid.get(new_point)
                if new_region_type == region_type:
                    region.add(new_point)
                    perimeter_check_region.add(new_point)
                    checked_regions.add(new_point)
                    frontier.append(new_point)
                else:
                    if direction_index >= 2: # left or up
                        perimeter_check_region.add(new_point)
                        perimeter_check_region.add(point + (-1, -1))
                    if new_region_type != " ":
                        start_queue[new_point] = new_region_type
    perimeter: int = 0
    side_count: int = 0
    for point in perimeter_check_region:
        inside = point in region
        d_inside = point + (1, 0) in region
        r_inside = point + (0, 1) in region
        dr_inside = point + (1, 1) in region
        if inside != r_inside:
            if d_inside == dr_inside or inside == dr_inside:
                side_count += 1
            perimeter += 1
        if inside != d_inside:
            if r_inside == dr_inside or inside == dr_inside:
                side_count += 1
            perimeter += 1
    total_price_p1 += len(region) * perimeter
    total_price_p2 += len(region) * side_count

print("[day12p1] Total fence price:", total_price_p1)
print("[day12p2] Total fence price:", total_price_p2)

print_time_elapsed()
