from utils import *

start_time: float = get_start_time()

keys: list[list[int]] = []
locks: list[list[int]] = []
current = None
is_lock = False
for line in get_input_lines("day25.txt"):
    if not line:
        current = None
        continue
    elif current is None:
        is_lock = line[0] == "#"
        current = [-1] * len(line)
        (locks if is_lock else keys).append(current)
        print(line, is_lock)
    for index, char in enumerate(line):
        if char == "#":
            current[index] += 1
print(keys[0], locks[0])
height = 5

matching = 0
for key in keys:
    for lock in locks:
        if all(key_pin + lock_pin <= height for key_pin, lock_pin in zip(key, lock)):
            matching += 1
print(matching)

print_time_elapsed(start_time)
