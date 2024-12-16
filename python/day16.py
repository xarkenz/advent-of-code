from utils import *

import heapq

grid = get_input_tile_map("day16.txt")

for point, tile in grid:
    if tile == "S":
        start_pos = point
    elif tile == "E":
        end_pos = point
grid.put(start_pos, ".")
grid.put(end_pos, ".")

directions: list[Point] = [
    Point(1, 0),
    Point(0, 1),
    Point(-1, 0),
    Point(0, -1),
]

grid2 = grid.copy()

@dataclass(order=True)
class FrontierPoint:
    cost: int
    path: list[Point] = field(compare=False)
    direction: Point = field(compare = False)

frontier: list[FrontierPoint] = [FrontierPoint(0, [start_pos], Point(0, 1))]
heapq.heapify(frontier)
test_later: list[FrontierPoint] = []
least_cost = None
least_paths = []
while frontier:
    frontier_point = heapq.heappop(frontier)
    cost, path, prev_dir = frontier_point.cost, frontier_point.path, frontier_point.direction
    if path[-1] == end_pos:
        if least_cost is not None and cost > least_cost:
            break
        least_cost = cost
        least_paths.append(path)
        for point in path:
            grid2.put(point, ".")
        for test in test_later:
            heapq.heappush(frontier, test)
        test_later.clear()
        continue
    tile = grid2.get(path[-1])
    if tile == ".":
        grid2.put(path[-1], ",")
    elif tile == ",":
        test_later.append(frontier_point)
        continue
    else:
        continue
    heapq.heappush(frontier, FrontierPoint(cost + 1, path + [path[-1] + prev_dir], prev_dir))
    left_dir = prev_dir.rotate_90_ccw()
    right_dir = prev_dir.rotate_90_cw()
    heapq.heappush(frontier, FrontierPoint(cost + 1001, path + [path[-1] + left_dir], left_dir))
    heapq.heappush(frontier, FrontierPoint(cost + 1001, path + [path[-1] + right_dir], right_dir))

best_seats: set[Point] = set()
for path in least_paths:
    for point in path:
        best_seats.add(point)

print(grid2)
print(least_cost)
print(len(best_seats))
print_time_elapsed()
