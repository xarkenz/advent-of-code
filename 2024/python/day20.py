from utils import *

start_time: float = get_start_time()

grid = get_input_tile_map("day20.txt")
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

path: list[Point] = [start_pos]
path_indices: dict[Point, int] = {start_pos: 0}
while path[-1] != end_pos:
    for direction in directions:
        new_point = path[-1] + direction
        if new_point not in path_indices and grid.get(new_point) == ".":
            path_indices[new_point] = len(path)
            path.append(new_point)

saves_100 = 0
for index, point in enumerate(path):
    for direction in directions:
        after_point = point + direction * 2
        if grid.get(point + direction) == "#" and grid.get(after_point) == "." and after_point in path_indices:
            after_index = path_indices[after_point] - 2
            if after_index - index >= 100:
                saves_100 += 1

print(saves_100)

saves_100 = 0
for index1, point1 in enumerate(path[:-100]):
    for offset2, point2 in enumerate(path[index1 + 100:]):
        dist = point1.manhattan_distance_to(point2)
        if dist <= 20 and offset2 - dist >= 0:
            saves_100 += 1

print(saves_100)

print_time_elapsed(start_time)
