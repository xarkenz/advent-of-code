from utils import *

directions: list[Point] = [
    Point(1, 0),
    Point(0, 1),
    Point(-1, 0),
    Point(0, -1),
]

grid = get_input_tile_map("day10.txt")

trailheads: list[Point] = [point for point, tile in grid if tile == "0"]

scores = 0

for trailhead in trailheads:
    score = 0
    frontier: set[Point] = {trailhead}
    last_frontier_size = 0
    while last_frontier_size != len(frontier):
        last_frontier_size = len(frontier)
        for point in frontier.copy():
            orig_tile = grid.get(point)
            for direction in directions:
                new_point = point + direction
                if new_point in frontier:
                    continue
                new_tile = grid.get(new_point)
                if ord(new_tile) == ord(orig_tile) + 1:
                    if new_tile == "9":
                        score += 1
                    frontier.add(new_point)
    scores += score

print(scores)

scores = 0

def count_paths(path: list[Point]) -> int:
    point = path[-1]
    orig_tile = grid.get(point)
    count = 0
    for direction in directions:
        new_point = point + direction
        new_tile = grid.get(new_point)
        if ord(new_tile) == ord(orig_tile) + 1:
            if new_tile == "9":
                count += 1
            else:
                path.append(new_point)
                count += count_paths(path)
    path.pop()
    return count

for trailhead in trailheads:
    path: list[Point] = [trailhead]
    score = count_paths(path)
    scores += score

print(scores)

print_time_elapsed()
