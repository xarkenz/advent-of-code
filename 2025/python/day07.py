from utils import *

start_time: float = get_start_time()

# Mapping from X-coordinate to the number of beams in that spot in different timelines
beams: dict[int, int] = {}
split_count: int = 0

for line in get_input_lines("day07.txt"):
    for x, ch in enumerate(line):
        if ch == "S":
            beams[x] = 1
        elif ch == "^" and x in beams:
            count = beams[x]
            del beams[x]
            beams[x - 1] = beams.get(x - 1, 0) + count
            beams[x + 1] = beams.get(x + 1, 0) + count
            split_count += 1

print("[07p1] Number of splits:", split_count)
print("[07p2] Number of timelines:", sum(beams.values()))

print_time_elapsed(start_time)
