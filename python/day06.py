from utils import *

grid: TileMap = TileMap()

with open("input/day06.txt") as input_file:
    for row, line in enumerate(input_file.readlines()):
        grid.put((row, 0), line.strip())

init_guard_dir = Point(-1, 0)
for point, tile in grid:
    if tile == "^":
        grid.put(point, ".")
        init_guard_pos = point
        break
else:
    print("no guard")
    exit()

grid1 = grid.copy()
guard_pos = init_guard_pos
guard_dir = init_guard_dir
while True:
    grid1.put(guard_pos, "X")
    next_guard_pos = guard_pos + guard_dir
    tile = grid.get(next_guard_pos)
    if tile == ".":
        guard_pos = next_guard_pos
    elif tile == "#":
        guard_dir = Point(guard_dir.col, -guard_dir.row)
    else:
        break

count = 0
for point, tile in grid1:
    if tile == "X":
        count += 1

print(count)

dir_tiles = {(1, 0): "v", (0, 1): ">", (0, -1): "<", (-1, 0): "^"}
tile_dirs = {"v": Point(1, 0), ">": Point(0, 1), "<": Point(0, -1), "^": Point(-1, 0)}

tested = TileMap()
tested.put(init_guard_pos, "Y")

loop_positions = 0

def test(grid: TileMap, guard_pos: Point, guard_dir: Point):
    while True:
        next_guard_pos = guard_pos + guard_dir
        tile = grid.get(next_guard_pos)
        if tile == "." or tile in tile_dirs:
            orig_tile = grid.get(guard_pos)
            if orig_tile in tile_dirs and tile_dirs[orig_tile] == guard_dir:
                return True
            grid.put(guard_pos, dir_tiles[guard_dir.row, guard_dir.col])
            guard_pos = next_guard_pos
        elif tile == "#":
            guard_dir = Point(guard_dir.col, -guard_dir.row)
        else:
            return False

grid2 = grid.copy()
guard_pos = init_guard_pos
guard_dir = init_guard_dir
while True:
    next_guard_pos = guard_pos + guard_dir
    tile = grid.get(next_guard_pos)
    if tile == "#":
        guard_dir = Point(guard_dir.col, -guard_dir.row)
    else:
        if tested.get(next_guard_pos) != "Y" and grid2.get(next_guard_pos) == ".":
            test_grid = grid2.copy()
            test_grid.put(next_guard_pos, "#")
            if test(test_grid, guard_pos, guard_dir):
                tested.put(next_guard_pos, "Y")
                loop_positions += 1
        if tile == ".":
            grid2.put(guard_pos, dir_tiles[guard_dir.row, guard_dir.col])
            guard_pos = next_guard_pos
        else:
            break

print(loop_positions)

print_time_elapsed()
