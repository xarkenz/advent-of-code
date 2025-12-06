from utils import *
import math

start_time: float = get_start_time()

lines: list[str] = get_input_lines("day06.txt", strip=False)
rows: list[list[str]] = [line.strip().split() for line in lines]
grand_total: int = 0

for column in zip(*rows):
    operation = column[-1]
    numbers = map(int, column[:-1])
    if operation == "+":
        grand_total += sum(numbers)
    elif operation == "*":
        grand_total += math.prod(numbers)
    else:
        print("invalid operation")

print("[06p1] Grand total:", grand_total)

grand_total: int = 0
current_value: int = 0
operation: Optional[str] = None

for column in zip(*lines):
    if all(c.isspace() for c in column):
        grand_total += current_value
        operation = None
        continue
    elif operation is None:
        operation = column[-1]
        if operation == "+":
            current_value = 0
        elif operation == "*":
            current_value = 1
        else:
            print("invalid operation")
    number = int("".join(c for c in column if c.isdigit()))
    if operation == "+":
        current_value += number
    elif operation == "*":
        current_value *= number
if operation is not None:
    grand_total += current_value

print("[06p2] Grand total:", grand_total)

print_time_elapsed(start_time)
