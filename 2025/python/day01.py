from utils import *

start_time: float = get_start_time()

dial: int = 50
stop_zero_count: int = 0
pass_zero_count: int = 0

for line in get_input_lines("day01.txt"):
    direction = line[0]
    distance = int(line[1:])
    if direction == "R":
        dial += distance
        while dial >= 100:
            dial -= 100
            pass_zero_count += 1
    elif direction == "L":
        if dial == 0:
            pass_zero_count -= 1
        dial -= distance
        while dial < 0:
            dial += 100
            pass_zero_count += 1
        if dial == 0:
            pass_zero_count += 1
    if dial == 0:
        stop_zero_count += 1

print("[01p1] Times dial stopped at zero:", stop_zero_count)
print("[01p2] Times dial passed zero:", pass_zero_count)

print_time_elapsed(start_time)
