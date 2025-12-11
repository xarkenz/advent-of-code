from utils import *

start_time: float = get_start_time()

target_x_range, target_y_range = get_input_text("day17.txt").strip().removeprefix("target area: ").split(", ")
target_min_x, target_max_x = map(int, target_x_range.removeprefix("x=").split(".."))
target_min_y, target_max_y = map(int, target_y_range.removeprefix("y=").split(".."))

min_y_vel = target_min_y
max_y_vel = abs(target_min_y) - 1
highest_y = max_y_vel * (max_y_vel + 1) // 2

print("[17p1] Highest y position:", highest_y)

min_x_vel = next(x_vel for x_vel in itertools.count() if x_vel * (x_vel + 1) // 2 >= target_min_x)
max_x_vel = target_max_x

vel_count = 0
for init_y_vel in range(min_y_vel, max_y_vel + 1):
    for init_x_vel in range(min_x_vel, max_x_vel + 1):
        x = 0
        y = 0
        x_vel = init_x_vel
        y_vel = init_y_vel
        while x <= target_max_x and y >= target_min_y:
            if target_min_x <= x <= target_max_x and target_min_y <= y <= target_max_y:
                vel_count += 1
                break
            x += x_vel
            y += y_vel
            x_vel = max(0, x_vel - 1)
            y_vel -= 1

print("[17p2] Number of starting velocities:", vel_count)

print_time_elapsed(start_time)
