from utils import *

start_time: float = get_start_time()

falling_bytes: list[Point] = []
for line in get_input_lines("day18.txt"):
    x, y = line.split(",")
    falling_bytes.append(Point(int(y), int(x)))

directions: list[Point] = [
    Point(1, 0),
    Point(0, 1),
    Point(-1, 0),
    Point(0, -1),
]

@dataclass(order=True)
class FrontierPoint:
    steps: int
    path: list[Point] = field(compare=False)

first_1k: set[Point] = set(falling_bytes[:1024])
max_row = 70
max_col = 70
frontier: MinHeap[FrontierPoint] = MinHeap()
frontier.push(FrontierPoint(0, [Point(0, 0)]))
traveled_points: set[Point] = set()
exit_pos: Point = Point(max_row, max_col)
min_steps = None
min_path = None
while frontier:
    frontier_point = frontier.pop()
    steps, path = frontier_point.steps, frontier_point.path
    if path[-1] == exit_pos:
        min_steps = steps
        min_path = path
        break
    if path[-1] in traveled_points:
        continue
    traveled_points.add(path[-1])
    for direction in directions:
        new_point = path[-1] + direction
        if new_point.row < 0 or new_point.col < 0 or new_point.row > max_row or new_point.col > max_col:
            continue
        if new_point not in first_1k and new_point not in traveled_points:
            frontier.push(FrontierPoint(steps + 1, path + [new_point]))

print("[18p1] Minimum steps after 1K fallen:", min_steps)

@dataclass(order=True)
class FrontierPoint2:
    manhattan_distance: int
    point: Point = field(compare=False)

fallen_bytes: set[Point] = set(falling_bytes[:1024])
blocking_byte = None
for fallen_byte in falling_bytes[1024:]:
    fallen_bytes.add(fallen_byte)
    frontier2: MinHeap[FrontierPoint2] = MinHeap()
    frontier2.push(FrontierPoint2(max_row + max_col, Point(0, 0)))
    traveled_points: set[Point] = set()
    while frontier2:
        point = frontier2.pop().point
        if point == exit_pos:
            break
        elif point in traveled_points:
            continue
        traveled_points.add(point)
        for direction in directions:
            new_point = point + direction
            if new_point.row < 0 or new_point.col < 0 or new_point.row > max_row or new_point.col > max_col:
                continue
            if new_point not in fallen_bytes and new_point not in traveled_points:
                frontier2.push(FrontierPoint2(new_point.manhattan_distance_to(exit_pos), new_point))
    else:
        blocking_byte = fallen_byte
        break

print(f"[18p2] Location of blocking byte: {blocking_byte.col},{blocking_byte.row}")

print_time_elapsed(start_time)
