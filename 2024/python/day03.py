from utils import *

start_time: float = get_start_time()

import re

text = get_input_text("day03.txt")

matches: list[str] = re.findall("mul\\([0-9]{1,3},[0-9]{1,3}\\)", text)

result = 0
for item in matches:
    x, y = item[4:-1].split(",")
    result += int(x) * int(y)

print("[03p1] Sum of multiplications:", result)

matches: list[str] = re.findall("mul\\([0-9]{1,3},[0-9]{1,3}\\)|do\\(\\)|don't\\(\\)", text)

result = 0
enabled = True
for item in matches:
    if item.startswith("don't"):
        enabled = False
    elif item.startswith("do"):
        enabled = True
    elif enabled:
        x, y = item[4:-1].split(",")
        result += int(x) * int(y)

print("[03p2] Sum of enabled multiplications:", result)

print_time_elapsed(start_time)
