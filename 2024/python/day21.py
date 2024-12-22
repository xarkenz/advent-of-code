from utils import *

start_time: float = get_start_time()

codes = get_input_lines("day21.txt")

# 7 8 9
# 4 5 6
# 1 2 3
#   0 A
numeric: dict[str, Point] = {
    "A": Point(3, 2),
    "0": Point(3, 1),
    "1": Point(2, 0),
    "2": Point(2, 1),
    "3": Point(2, 2),
    "4": Point(1, 0),
    "5": Point(1, 1),
    "6": Point(1, 2),
    "7": Point(0, 0),
    "8": Point(0, 1),
    "9": Point(0, 2),
}
numeric_bad: Point = Point(3, 0)

#   ^ A
# < v >
directional: dict[str, Point] = {
    "A": Point(0, 2),
    "^": Point(0, 1),
    "<": Point(1, 0),
    "v": Point(1, 1),
    ">": Point(1, 2),
}
directional_bad: Point = Point(0, 0)

def get_paths(start: Point, target: Point, bad: Point, memo: dict[tuple[Point, Point], list[list[tuple[str, int]]]]) -> list[list[tuple[str, int]]]:
    if (start, target) in memo:
        return memo[start, target]
    diff = target - start
    submit = ("A", 1)
    horizontal = ("<" if diff.col < 0 else ">", abs(diff.col))
    vertical = ("^" if diff.row < 0 else "v", abs(diff.row))
    if diff.row == 0 and diff.col == 0:
        paths = [[submit]]
    elif diff.row == 0:
        paths = [[horizontal, submit]]
    elif diff.col == 0:
        paths = [[vertical, submit]]
    else:
        paths = []
        # Horizontal then vertical
        if start.row != bad.row or target.col != bad.col:
            paths.append([horizontal, vertical, submit])
        # Vertical then horizontal
        if start.col != bad.col or target.row != bad.row:
            paths.append([vertical, horizontal, submit])
    memo[start, target] = paths
    return paths

def get_numeric_paths(start: str, target: str, *, memo: dict[tuple[Point, Point], list[list[tuple[str, int]]]] = {}) -> list[list[tuple[str, int]]]:
    return get_paths(numeric[start], numeric[target], numeric_bad, memo)

def get_directional_paths(start: str, target: str, *, memo: dict[tuple[Point, Point], list[list[tuple[str, int]]]] = {}) -> list[list[tuple[str, int]]]:
    return get_paths(directional[start], directional[target], directional_bad, memo)

# Cost for a press means the minimum number of button presses needed from the top level (you) to go from start to target and press the target.
def calculate_cost(paths: list[list[tuple[str, int]]], parent_costs: dict[tuple[str, str], int]) -> int:
    minimum_cost = None
    for path in paths:
        cost = 0
        button = "A"
        for next_button, presses in path:
            # First press
            cost += parent_costs[button, next_button]
            button = next_button
            # Subsequent presses
            cost += presses - 1
        if minimum_cost is None or cost < minimum_cost:
            minimum_cost = cost
    return minimum_cost

directional_count = 25

robot_press_costs: list[dict[tuple[str, str], int]] = [None] * (directional_count + 1)
robot_press_costs.append({(start, target): 1 for start in directional for target in directional})
for robot in reversed(range(1, directional_count + 1)):
    parent_costs = robot_press_costs[robot + 1]
    robot_press_costs[robot] = {(start, target): calculate_cost(get_directional_paths(start, target), parent_costs) for (start, target) in parent_costs}
parent_costs = robot_press_costs[1]
robot_press_costs[0] = {(start, target): calculate_cost(get_numeric_paths(start, target), parent_costs) for start in numeric for target in numeric}

complexity_sum = 0
for code in codes:
    minimum_presses = 0
    button = "A"
    for next_button in code:
        if next_button == button:
            minimum_presses += 1
        else:
            minimum_presses += robot_press_costs[0][button, next_button]
            button = next_button
    complexity_sum += int(code[:3]) * minimum_presses
print(complexity_sum)

print_time_elapsed(start_time)
