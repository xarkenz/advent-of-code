from utils import *

start_time: float = get_start_time()

instructions: list[tuple[str, int]] = [(direction, int(amount)) for direction, amount in (line.split() for line in get_input_lines("day02.txt"))]

position_p1: int = 0
depth_p1: int = 0
position_p2: int = 0
depth_p2: int = 0
aim_p2: int = 0
for direction, amount in instructions:
    if direction == "forward":
        position_p1 += amount
        position_p2 += amount
        depth_p2 += aim_p2 * amount
    elif direction == "down":
        depth_p1 += amount
        aim_p2 += amount
    elif direction == "up":
        depth_p1 -= amount
        aim_p2 -= amount

print("[02p1] Final horizontal position times depth:", position_p1 * depth_p1)
print("[02p2] Final horizontal position times depth:", position_p2 * depth_p2)

print_time_elapsed(start_time)
