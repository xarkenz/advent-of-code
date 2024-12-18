from utils import *

init_robots: list[tuple[Point, Point]] = []

for line in get_input_lines("day14.txt"):
    pos, vel = line[2:].split(" v=")
    pos = pos.split(",")
    vel = vel.split(",")
    init_robots.append((Point(int(pos[1]), int(pos[0])), Point(int(vel[1]), int(vel[0]))))

grid_rows = 103
center_row = 51
grid_cols = 101
center_col = 50
seconds = 100

q1_count = 0
q2_count = 0
q3_count = 0
q4_count = 0
for init_pos, vel in init_robots:
    row = (init_pos.row + vel.row * seconds) % grid_rows
    col = (init_pos.col + vel.col * seconds) % grid_cols
    if row < center_row:
        if col < center_col:
            q1_count += 1
        elif col > center_col:
            q2_count += 1
    elif row > center_row:
        if col < center_col:
            q3_count += 1
        elif col > center_col:
            q4_count += 1

print("[day14p1] Safety factor after 100 seconds:", q1_count * q2_count * q3_count * q4_count)

robots: list[tuple[Point, Point]] = init_robots.copy()
min_s = -1
min_avg_dist = grid_rows + grid_cols
min_robots = []
for s in range(1, 10000):
    total_row = 0
    total_col = 0
    for i in range(len(robots)):
        pos, vel = robots[i]
        pos = Point((pos.row + vel.row) % grid_rows, (pos.col + vel.col) % grid_cols)
        robots[i] = pos, vel
        total_row += pos.row
        total_col += pos.col
    avg_row = total_row / len(robots)
    avg_col = total_col / len(robots)
    total_dist = 0
    for pos, _ in robots:
        total_dist += pos.manhattan_distance_to((avg_row, avg_col))
    avg_dist = total_dist / len(robots)
    if avg_dist < min_avg_dist:
        if avg_dist < min_avg_dist:
            min_s = s
            min_avg_dist = avg_dist
            min_robots = robots.copy()

print("[day14p2] Seconds until christmas tree appears:", min_s)

print_time_elapsed()
