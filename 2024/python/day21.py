from utils import *

start_time: float = get_start_time()

codes = get_input_lines("day21.txt")

# +---+---+---+
# | 7 | 8 | 9 |
# +---+---+---+
# | 4 | 5 | 6 |
# +---+---+---+
# | 1 | 2 | 3 |
# +---+---+---+
#     | 0 | A |
#     +---+---+

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

#     +---+---+
#     | ^ | A |
# +---+---+---+
# | < | v | > |
# +---+---+---+

directional: dict[str, Point] = {
    "A": Point(0, 2),
    "^": Point(0, 1),
    "<": Point(1, 0),
    "v": Point(1, 1),
    ">": Point(1, 2),
}
directional_bad: Point = Point(0, 0)

def map_numeric(code: str) -> list[str]:
    paths: list[tuple[list[Point]], str] = [([numeric["A"]], "")]
    for button in code:
        target = numeric[button]
        new_paths = []
        for path, seq in paths:
            orig_len = len(path)
            seq1 = seq
            path1 = path.copy()
            while path1[-1].col < target.col:
                path1.append(path1[-1] + (0, 1))
                seq1 += ">"
            while path1[-1].row < target.row:
                path1.append(path1[-1] + (1, 0))
                seq1 += "v"
            while path1[-1].row > target.row:
                path1.append(path1[-1] + (-1, 0))
                seq1 += "^"
            while path1[-1].col > target.col:
                path1.append(path1[-1] + (0, -1))
                seq1 += "<"
            seq1 += "A"
            if numeric_bad not in path1[orig_len:]:
                new_paths.append((path1, seq1))
            seq2 = seq
            path2 = path
            while path2[-1].row < target.row:
                path2.append(path2[-1] + (1, 0))
                seq2 += "v"
            while path2[-1].col < target.col:
                path2.append(path2[-1] + (0, 1))
                seq2 += ">"
            while path2[-1].col > target.col:
                path2.append(path2[-1] + (0, -1))
                seq2 += "<"
            while path2[-1].row > target.row:
                path2.append(path2[-1] + (-1, 0))
                seq2 += "^"
            seq2 += "A"
            if seq2 != seq1 and numeric_bad not in path2[orig_len:]:
                new_paths.append((path2, seq2))
        paths = new_paths
    return [seq for _, seq in paths]

def calc_score(seq: str) -> int:
    current = seq[0]
    score = 0
    for button in seq[1:]:
        if button != current:
            score += 1
            current = button
    return score

@dataclass(order=True)
class Path:
    score: int
    seq: str = field(compare=False)
    point: Point = field(compare=False)

def map_directional(code: str, *, memo: dict[str, list[str]] = {}) -> list[str]:
    if code in memo:
        return memo[code]
    paths: MinHeap[Path] = MinHeap()
    paths.push(Path(0, "", directional["A"]))
    for button in code:
        target = directional[button]
        new_paths: MinHeap[Path] = MinHeap()
        while paths:
            path = paths.pop()
            seq1 = path.seq
            path1 = [path.point]
            while path1[-1].col < target.col:
                path1.append(path1[-1] + (0, 1))
                seq1 += ">"
            while path1[-1].row < target.row:
                path1.append(path1[-1] + (1, 0))
                seq1 += "v"
            while path1[-1].row > target.row:
                path1.append(path1[-1] + (-1, 0))
                seq1 += "^"
            while path1[-1].col > target.col:
                path1.append(path1[-1] + (0, -1))
                seq1 += "<"
            seq1 += "A"
            if directional_bad not in path1:
                new_paths.push(Path(calc_score(seq1), seq1, path1[-1]))
            seq2 = path.seq
            path2 = [path.point]
            while path2[-1].row < target.row:
                path2.append(path2[-1] + (1, 0))
                seq2 += "v"
            while path2[-1].col < target.col:
                path2.append(path2[-1] + (0, 1))
                seq2 += ">"
            while path2[-1].col > target.col:
                path2.append(path2[-1] + (0, -1))
                seq2 += "<"
            while path2[-1].row > target.row:
                path2.append(path2[-1] + (-1, 0))
                seq2 += "^"
            seq2 += "A"
            if seq2 != seq1 and directional_bad not in path2:
                new_paths.push(Path(calc_score(seq2), seq2, path2[-1]))
        paths = new_paths
        if len(paths.items) > 1000:
            paths.items[len(paths.items) // 2 :] = []
        print(len(paths.items))
    result = [path.seq for path in paths.items]
    memo[code] = result
    return result

def get_min_len(dir_code: str, count: int, *, memo: dict[str, int] = {}) -> int:
    if count == 0:
        return len(dir_code)
    elif dir_code in memo:
        return memo[dir_code]
    else:
        result = min(get_min_len(code, count - 1) for code in map_directional(dir_code))
        memo[dir_code] = result
        return result

directional_count = 25

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
