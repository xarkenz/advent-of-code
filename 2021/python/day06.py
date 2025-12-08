from utils import *

start_time: float = get_start_time()

# Count of lanternfish with each possible timer value
lanternfish: list[int] = [0] * 9

for number in get_input_text("day06.txt").strip().split(","):
    lanternfish[int(number)] += 1

population_80: Optional[int] = None

for day in range(256):
    if day == 80:
        population_80 = sum(lanternfish)
    creating_new = lanternfish.pop(0)
    lanternfish[6] += creating_new
    lanternfish.append(creating_new)

print("[06p1] Population after 80 days:", population_80)
print("[06p2] Population after 256 days:", sum(lanternfish))

print_time_elapsed(start_time)
