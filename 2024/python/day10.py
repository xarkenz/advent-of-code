from utils import *

start_time: float = get_start_time()

directions: list[Point] = [
    Point(1, 0),
    Point(0, 1),
    Point(-1, 0),
    Point(0, -1),
]

grid: TileMap = get_input_tile_map("day10.txt")

trailheads: list[Point] = [point for point, tile in grid if tile == "0"]

scores_total: int = 0
ratings_total: int = 0

for trailhead in trailheads:
    trail_ends: set[Point] = set()
    frontier: list[Point] = [trailhead]
    while frontier:
        new_frontier: list[Point] = []
        for point in frontier:
            tile = grid.get(point)
            for direction in directions:
                new_point = point + direction
                new_tile = grid.get(new_point)
                if ord(new_tile) == ord(tile) + 1:
                    if new_tile == "9":
                        if new_point not in trail_ends:
                            scores_total += 1
                            trail_ends.add(new_point)
                        ratings_total += 1
                    else:
                        new_frontier.append(new_point)
        frontier = new_frontier

print("[10p1] Trailhead score total:", scores_total)
print("[10p2] Trailhead rating total:", ratings_total)

print_time_elapsed(start_time)
