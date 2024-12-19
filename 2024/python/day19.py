from utils import *

start_time: float = get_start_time()

towels = []
lines = get_input_lines("day19.txt")
for towel in lines[0].split(", "):
    towels.append(towel)

def design_possibilities(design: str, *, memo: dict[str, int] = {}) -> int:
    if not design:
        return 1
    elif design in memo:
        return memo[design]
    possibilities = 0
    for towel in towels:
        if design.startswith(towel):
            possibilities += design_possibilities(design[len(towel):])
    memo[design] = possibilities
    return possibilities

possible = 0
total_possibilities = 0

for design in lines[2:]:
    possibilities = design_possibilities(design)
    if possibilities != 0:
        possible += 1
    total_possibilities += possibilities

print(possible)
print(total_possibilities)

print_time_elapsed(start_time)
