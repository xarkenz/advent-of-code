from utils import *

start_time: float = get_start_time()

@dataclass
class Cave:
    name: str
    adjacents: list["Cave"]
    visits: int

caves: dict[str, Cave] = {}

for line in get_input_lines("day12.txt"):
    name_1, name_2 = line.split("-")
    if name_1 not in caves:
        caves[name_1] = Cave(name_1, [], 0)
    if name_2 not in caves:
        caves[name_2] = Cave(name_2, [], 0)
    caves[name_1].adjacents.append(caves[name_2])
    caves[name_2].adjacents.append(caves[name_1])

path_count: int = 0

def visit(cave: Cave) -> None:
    if cave.name == "end":
        global path_count
        path_count += 1
        return
    elif cave.name.islower() and cave.visits > 0:
        return
    cave.visits += 1
    for adjacent in cave.adjacents:
        visit(adjacent)
    cave.visits -= 1

visit(caves["start"])

print("[12p1] Number of paths:", path_count)

path_count: int = 0

def visit(cave: Cave, repeated_small_cave: bool = False) -> None:
    if cave.name == "end":
        global path_count
        path_count += 1
        return
    elif cave.name.islower() and cave.visits > 0:
        if repeated_small_cave or cave.name == "start" or cave.visits > 1:
            return
        repeated_small_cave = True
    cave.visits += 1
    for adjacent in cave.adjacents:
        visit(adjacent, repeated_small_cave)
    cave.visits -= 1

visit(caves["start"])

print("[12p2] Number of paths:", path_count)

print_time_elapsed(start_time)
