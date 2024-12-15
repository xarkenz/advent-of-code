from utils import *

dir_chars = {"^": Point(-1, 0), ">": Point(0, 1), "<": Point(0, -1), "v": Point(1, 0)}

grid = get_input_tile_map("day15.txt")
moves = [dir_chars[c] for c in get_input_text("day15_move.txt") if c in dir_chars]

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

gps = 0
for point, tile in grid:
    if tile == "O":
        gps += 100 * point.row + point.col
print(grid)
print(gps)

grid = grid_p2 #lazy
robot = robot_p2

def print_grid():
    grid.put(robot, "@")
    print(grid)
    grid.put(robot, ".")

def move_robot_p2(move):
    global robot
    target = robot + move
    target_tile = grid.get(target)
    if target_tile == ".":
        robot = target
    elif target_tile in "[]":
        if move.row == 0:
            to_shift = [(target, target_tile)]
            test = target + move
            test_tile = grid.get(test)
            while test_tile in "[]":
                to_shift.append((test, test_tile))
                test = test + move
                test_tile = grid.get(test)
            if test_tile == ".":
                while to_shift:
                    test, test_tile = to_shift.pop()
                    grid.put(test + move, test_tile)
                grid.put(target, ".")
                robot = target
        else:
            tests = [target]
            to_shift = []
            clear_to_move = True
            while tests:
                test = tests.pop()
                test_tile = grid.get(test)
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
                    grid.put(test + move, test_tile)
                    if grid.get(test) == test_tile:
                        grid.put(test, ".")
                robot = target

for move in moves:
    move_robot_p2(move)

gps = 0
for point, tile in grid:
    if tile == "[":
        gps += 100 * point.row + point.col
print_grid()
print(gps)

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
