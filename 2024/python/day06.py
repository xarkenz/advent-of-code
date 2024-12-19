from utils import *

start_time: float = get_start_time()

directions: list[Point] = [
    Point(1, 0),
    Point(0, 1),
    Point(-1, 0),
    Point(0, -1),
]

base_grid: TileMap = get_input_tile_map("day06.txt")

for point, tile in base_grid:
    if tile == "^":
        base_grid.put(point, ".")
        init_guard_dir = Point(-1, 0)
        init_guard_pos = point
        break
else:
    print("no guard")
    exit()

for point, tile in base_grid:
    if tile == "#":
        for direction in directions:
            adjacent = point + direction
            if base_grid.get(adjacent) == ".":
                base_grid.put(adjacent, ",")

waypoints: set[tuple[Point, Point]] = {(init_guard_pos, init_guard_dir)}
looping_walls: set[Point] = set()

def log_waypoint(waypoints: set[tuple[Point, Point]], guard_pos: Point, guard_dir: Point) -> bool:
    if (guard_pos, guard_dir) in waypoints:
        return True
    else:
        waypoints.add((guard_pos, guard_dir))
        return False

def is_loop_detected(grid: TileMap, waypoints: set[tuple[Point, Point]], guard_pos: Point, guard_dir: Point, placed_wall: Point) -> bool:
    current_tile = grid.get(guard_pos)
    while True:
        next_guard_pos = guard_pos + guard_dir
        next_tile = grid.get(next_guard_pos)
        if next_tile == " ":
            return False
        elif next_tile == "#" or next_guard_pos == placed_wall:
            guard_dir = guard_dir.rotate_90_cw()
        else:
            if current_tile == "," or guard_pos.manhattan_distance_to(placed_wall) == 1:
                if log_waypoint(waypoints, guard_pos, guard_dir):
                    return True
            current_tile = next_tile
            guard_pos = next_guard_pos

path_grid = base_grid.copy()
guard_pos = init_guard_pos
guard_dir = init_guard_dir

current_tile = path_grid.get(guard_pos)
while True:
    next_guard_pos = guard_pos + guard_dir
    next_tile = path_grid.get(next_guard_pos)
    if next_tile == "#":
        guard_dir = guard_dir.rotate_90_cw()
    else:
        path_grid.put(guard_pos, "X")
        if next_tile != "X":
            if next_guard_pos not in looping_walls:
                if is_loop_detected(base_grid, waypoints.copy(), guard_pos, guard_dir, next_guard_pos):
                    looping_walls.add(next_guard_pos)
            if next_tile == " ":
                break
        if current_tile == ",":
            log_waypoint(waypoints, guard_pos, guard_dir)
        current_tile = next_tile
        guard_pos = next_guard_pos

print("[06p1] Distinct tiles visited:", sum(tile == "X" for _, tile in path_grid))
print("[06p2] Loop-causing obstructions:", len(looping_walls))

print_time_elapsed(start_time)
