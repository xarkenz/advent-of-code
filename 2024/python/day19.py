from utils import *

start_time: float = get_start_time()

lines: list[str] = get_input_lines("day19.txt")
towels: list[str] = lines[0].split(", ")

# Original part 1 solution
def is_design_possible(design: str) -> bool:
    if not design:
        return True
    for towel in towels:
        if design.startswith(towel) and is_design_possible(design[len(towel):]):
            return True
    return False

# This memoization technique is still cursed
def design_possibilities(design: str, *, memo: dict[str, int] = {}) -> int:
    if not design:
        return 1
    elif design in memo:
        return memo[design]
    possibilities: int = 0
    for towel in towels:
        if design.startswith(towel):
            possibilities += design_possibilities(design[len(towel):])
    memo[design] = possibilities
    return possibilities

possible_design_count: int = 0
total_design_possibilities: int = 0

for design in lines[2:]:
    possibilities = design_possibilities(design)
    if possibilities != 0:
        possible_design_count += 1
    total_design_possibilities += possibilities

print("[19p1] Possible designs:", possible_design_count)
print("[19p2] Sum of design possibilities:", total_design_possibilities)

print_time_elapsed(start_time)
