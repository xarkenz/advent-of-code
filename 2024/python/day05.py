from utils import *

start_time: float = get_start_time()

orderings: list[list[int]] = []
updates: list[list[int]] = []

getting_updates = False
for line in get_input_lines("day05.txt"):
    if not line:
        getting_updates = True
    elif getting_updates:
        updates.append([int(x) for x in line.split(",")])
    else:
        orderings.append([int(x) for x in line.split("|")])

def is_ordered(update: list[int]) -> bool:
    for x, y in orderings:
        if x in update and y in update and update.index(x) > update.index(y):
            return False
    return True

def is_reorderable(update: list[int]):
    while not is_ordered(update):
        for x, y in orderings:
            if x not in update or y not in update:
                continue
            i = update.index(x)
            j = update.index(y)
            if i > j:
                update[i], update[j] = update[j], update[i]
    return True

middle_total: int = 0
reordered_middle_total: int = 0

for update in updates:
    if is_ordered(update):
        middle_total += update[len(update) // 2]
    elif is_reorderable(update):
        reordered_middle_total += update[len(update) // 2]

print("[05p1] Correctly ordered total:", middle_total)
print("[05p2] Reordered total:", reordered_middle_total)

print_time_elapsed(start_time)
