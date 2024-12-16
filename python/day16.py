from utils import *

grid: TileMap = get_input_tile_map("day16.txt")

start_pos: Point
end_pos: Point
for point, tile in grid:
    if tile == "S":
        start_pos = point
    elif tile == "E":
        end_pos = point
grid.put(start_pos, ".")
grid.put(end_pos, ".")

@dataclass(order=True)
class FrontierPoint:
    score: int
    path: list[Point] = field(compare=False)
    direction: Point = field(compare=False)

frontier: MinHeap[FrontierPoint] = MinHeap()
frontier.push(FrontierPoint(0, [start_pos], Point(0, 1)))
retryable_points: list[FrontierPoint] = []
lowest_score: Optional[int] = None
best_paths_points: set[Point] = set()
while frontier:
    frontier_point = frontier.pop()
    score, path, prev_dir = frontier_point.score, frontier_point.path, frontier_point.direction
    if lowest_score is not None and score > lowest_score:
        break
    if path[-1] == end_pos:
        lowest_score = score
        for point in path:
            grid.put(point, ".")
            best_paths_points.add(point)
        for retry_point in retryable_points:
            frontier.push(retry_point)
        retryable_points.clear()
        continue
    tile = grid.get(path[-1])
    if tile == ".":
        grid.put(path[-1], "+")
    elif tile == "+":
        retryable_points.append(frontier_point)
        continue
    else:
        continue
    frontier.push(FrontierPoint(score + 1, path + [path[-1] + prev_dir], prev_dir))
    left_dir = prev_dir.rotate_90_ccw()
    frontier.push(FrontierPoint(score + 1001, path + [path[-1] + left_dir], left_dir))
    right_dir = prev_dir.rotate_90_cw()
    frontier.push(FrontierPoint(score + 1001, path + [path[-1] + right_dir], right_dir))

print("[day16p1] Lowest possible score:", lowest_score)
print("[day16p2] Tiles on best paths:", len(best_paths_points))

print_time_elapsed()
