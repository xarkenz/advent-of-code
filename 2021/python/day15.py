from utils import *

start_time: float = get_start_time()

directions: list[Point] = [
    Point(1, 0),
    Point(0, 1),
    Point(-1, 0),
    Point(0, -1),
]

risk_levels: dict[Point, int] = {}
max_row: int = 0
max_col: int = 0

for row, line in enumerate(get_input_lines("day15.txt")):
    max_row = max(max_row, row)
    for col, digit in enumerate(line):
        max_col = max(max_col, col)
        risk_levels[Point(row, col)] = int(digit)

def get_risk_level_p2(point: Point) -> Optional[int]:
    if point.row < 0 or point.col < 0:
        return None
    v_repeat, src_row = divmod(point.row, max_row + 1)
    h_repeat, src_col = divmod(point.col, max_col + 1)
    if v_repeat >= 5 or h_repeat >= 5:
        return None
    return (risk_levels[Point(src_row, src_col)] + v_repeat + h_repeat - 1) % 9 + 1

@dataclass(order=True)
class FrontierPoint:
    distance: int
    point: Point = field(compare=False)

visited_points: set[Point] = set()
distances: dict[Point, int] = {Point(0, 0): 0}
frontier: MinHeap[FrontierPoint] = MinHeap([FrontierPoint(0, Point(0, 0))])

while frontier:
    current_point = frontier.pop().point
    if current_point in visited_points:
        continue
    visited_points.add(current_point)
    current_distance = distances[current_point]
    for direction in directions:
        test_point = current_point + direction
        if test_point in visited_points or test_point not in risk_levels:
            continue
        test_distance = current_distance + risk_levels[test_point]
        if test_point not in distances or test_distance < distances[test_point]:
            distances[test_point] = test_distance
        frontier.push(FrontierPoint(distances[test_point], test_point))

print("[15p1] Lowest total risk:", distances[Point(max_row, max_col)])

visited_points: set[Point] = set()
distances: dict[Point, int] = {Point(0, 0): 0}
frontier: MinHeap[FrontierPoint] = MinHeap([FrontierPoint(0, Point(0, 0))])

while frontier:
    current_point = frontier.pop().point
    if current_point in visited_points:
        continue
    visited_points.add(current_point)
    current_distance = distances[current_point]
    for direction in directions:
        test_point = current_point + direction
        if test_point in visited_points:
            continue
        risk_level = get_risk_level_p2(test_point)
        if risk_level is None:
            continue
        test_distance = current_distance + risk_level
        if test_point not in distances or test_distance < distances[test_point]:
            distances[test_point] = test_distance
        frontier.push(FrontierPoint(distances[test_point], test_point))

print("[15p2] Lowest total risk:", distances[Point(max_row * 5 + 4, max_col * 5 + 4)])

print_time_elapsed(start_time)
