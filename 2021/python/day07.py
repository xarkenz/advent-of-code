from utils import *

start_time: float = get_start_time()

crabs: dict[int, int] = {}

for position in get_input_text("day07.txt").strip().split(","):
#for position in "16,1,2,0,4,2,7,1,2,14".split(","):
    position = int(position)
    crabs[position] = crabs.get(position, 0) + 1

min_position: int = min(crabs)
max_position: int = max(crabs)

best_position: int = min_position
best_fuel: int = sum((position - best_position) * count for position, count in crabs.items())
fuel: int = best_fuel

count_left: int = crabs[min_position]
count_right: int = sum(crabs.values()) - count_left

for position in range(min_position + 1, max_position + 1):
    fuel += count_left - count_right
    if fuel < best_fuel:
        best_fuel = fuel
        best_position = position
    if position in crabs:
        count = crabs[position]
        count_left += count
        count_right -= count

print("[07p1] Fuel spent (constant):", best_fuel)

def increasing_fuel(n: int) -> int:
    return n * (n + 1) // 2

best_position: int = min_position
best_fuel: int = sum(increasing_fuel(position - best_position) * count for position, count in crabs.items())

for position in range(min_position + 1, max_position + 1):
    fuel = sum(increasing_fuel(abs(crab_position - position)) * count for crab_position, count in crabs.items())
    if fuel < best_fuel:
        best_fuel = fuel
        best_position = position

print("[07p2] Fuel spent (increasing):", best_fuel)

print_time_elapsed(start_time)
