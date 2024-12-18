from utils import *

dir_chars: dict[str, Point] = {
    "v": Point(1, 0),
    ">": Point(0, 1),
    "^": Point(-1, 0),
    "<": Point(0, -1),
}

grid: TileMap = TileMap()
moves: list[Point] = []
in_moves_section: bool = False
for row, line in enumerate(get_input_lines("day15.txt")):
    if not line:
        in_moves_section = True
    elif in_moves_section:
        moves.extend(dir_chars[char] for char in line if char in dir_chars)
    else:
        grid.put((row, 0), line)

grid_p2 = TileMap()
for point, tile in grid:
    if tile == "@":
        robot = point
        robot_p2 = Point(point.row, point.col * 2)
        grid_p2.put((point.row, point.col * 2), ".")
        grid_p2.put((point.row, point.col * 2 + 1), ".")
    elif tile == ".":
        grid_p2.put((point.row, point.col * 2), ".")
        grid_p2.put((point.row, point.col * 2 + 1), ".")
    elif tile == "#":
        grid_p2.put((point.row, point.col * 2), "#")
        grid_p2.put((point.row, point.col * 2 + 1), "#")
    elif tile == "O":
        grid_p2.put((point.row, point.col * 2), "[")
        grid_p2.put((point.row, point.col * 2 + 1), "]")
grid.put(robot, ".")

for move in moves:
    target = robot + move
    target_tile = grid.get(target)
    if target_tile == ".":
        robot = target
    elif target_tile == "O":
        to_shift = []
        test = target + move
        test_tile = grid.get(test)
        while test_tile == "O":
            to_shift.append(test)
            test = test + move
            test_tile = grid.get(test)
        if test_tile == ".":
            to_shift.append(test)
            while to_shift:
                test = to_shift.pop()
                grid.put(test, "O")
            grid.put(target, ".")
            robot = target

gps_coord_sum: int = 0
for point, tile in grid:
    if tile == "O":
        gps_coord_sum += 100 * point.row + point.col

print("[day15p1] Sum of GPS coordinates:", gps_coord_sum)

def print_grid(grid: TileMap, robot: Point):
    grid.put(robot, "@")
    print(grid)
    grid.put(robot, ".")

def move_robot_p2(move: Point):
    global robot_p2
    target: Point = robot_p2 + move
    target_tile: str = grid_p2.get(target)
    if target_tile == ".":
        robot_p2 = target
    elif target_tile in "[]":
        if move.row == 0:
            to_shift: list[tuple[Point, str]] = [(target, target_tile)]
            test: Point = target + move
            test_tile: str = grid_p2.get(test)
            while test_tile in "[]":
                to_shift.append((test, test_tile))
                test = test + move
                test_tile = grid_p2.get(test)
            if test_tile == ".":
                while to_shift:
                    test, test_tile = to_shift.pop()
                    grid_p2.put(test + move, test_tile)
                grid_p2.put(target, ".")
                robot_p2 = target
        else:
            tests: list[Point] = [target]
            to_shift: list[tuple[Point, str]] = []
            clear_to_move: bool = True
            while tests:
                test: Point = tests.pop()
                test_tile: str = grid_p2.get(test)
                if test_tile == "[":
                    tests.append(test + move)
                    tests.append(test + move + (0, 1))
                    to_shift.append((test, test_tile))
                    to_shift.append((test + (0, 1), "]"))
                elif test_tile == "]":
                    tests.append(test + move)
                    tests.append(test + move + (0, -1))
                    to_shift.append((test, test_tile))
                    to_shift.append((test + (0, -1), "["))
                elif test_tile == "#":
                    clear_to_move = False
                    break
            if clear_to_move:
                while to_shift:
                    test, test_tile = to_shift.pop()
                    grid_p2.put(test + move, test_tile)
                    if grid_p2.get(test) == test_tile:
                        grid_p2.put(test, ".")
                robot_p2 = target

for move in moves:
    move_robot_p2(move)

gps_coord_sum: int = 0
for point, tile in grid_p2:
    if tile == "[":
        gps_coord_sum += 100 * point.row + point.col

print("[day15p2] Sum of scaled-up GPS coordinates:", gps_coord_sum)

# i = input()
# while i:
#     if i == "w":
#         move_robot_p2(Point(-1, 0))
#     if i == "a":
#         move_robot_p2(Point(0, -1))
#     if i == "s":
#         move_robot_p2(Point(1, 0))
#     if i == "d":
#         move_robot_p2(Point(0, 1))
#     print_grid()
#     i = input()

print_time_elapsed()
