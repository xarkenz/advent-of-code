from utils import *

start_time: float = get_start_time()

fold_axes: dict[str, int] = {
    "x": 1,
    "y": 0,
}

dots: set[Point] = set()
folds: list[tuple[int, int]] = []

for line in get_input_lines("day13.txt"):
    if not line:
        continue
    elif line.startswith("fold"):
        folds.append((fold_axes[line[11]], int(line[13:])))
    else:
        x, y = map(int, line.split(","))
        dots.add(Point(y, x))

dots_after_first_fold: Optional[int] = None

for fold_axis, fold_position in folds:
    folded_dots: set[Point] = set()
    for dot in dots:
        if dot[fold_axis] > fold_position:
            dot_components = [dot.row, dot.col]
            dot_components[fold_axis] -= fold_position
            dot_components[fold_axis] *= -1
            dot_components[fold_axis] += fold_position
            folded_dots.add(Point(*dot_components))
        else:
            folded_dots.add(dot)

    dots = folded_dots
    if dots_after_first_fold is None:
        dots_after_first_fold = len(dots)

tile_map: TileMap = TileMap()

for dot in dots:
    tile_map.put(dot, "#")

print("[13p1] Dots visible after first fold:", dots_after_first_fold)
print("[13p2] System activation code:", )
print(tile_map)

print_time_elapsed(start_time)
