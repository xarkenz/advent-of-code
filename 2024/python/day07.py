from utils import *

from math import floor, log10

equations: list[tuple[int, list[int]]] = []

for line in get_input_lines("day07.txt"):
    goal, operands = line.split(": ")
    equations.append((int(goal), [int(operand) for operand in operands.split()]))

def check_p1(goal: int, lhs: int, operands: list[int], rhs_index: int) -> bool:
    if rhs_index == len(operands):
        return lhs == goal
    elif lhs > goal:
        return False
    rhs = operands[rhs_index]
    # Addition
    if check_p1(goal, lhs + rhs, operands, rhs_index + 1):
        return True
    # Multiplication
    elif check_p1(goal, lhs * rhs, operands, rhs_index + 1):
        return True
    else:
        return False

def check_p2(goal: int, lhs: int, operands: list[int], rhs_index: int) -> bool:
    if rhs_index == len(operands):
        return lhs == goal
    elif lhs > goal:
        return False
    rhs = operands[rhs_index]
    # Addition
    if check_p2(goal, lhs + rhs, operands, rhs_index + 1):
        return True
    # Multiplication
    elif check_p2(goal, lhs * rhs, operands, rhs_index + 1):
        return True
    # Concatenation
    elif check_p2(goal, lhs * (10 ** (floor(log10(rhs)) + 1)) + rhs, operands, rhs_index + 1):
        return True
    else:
        return False

total_calibration_p1: int = 0
total_calibration_p2: int = 0

for goal, operands in equations:
    if check_p1(goal, operands[0], operands, 1):
        total_calibration_p1 += goal
    if check_p2(goal, operands[0], operands, 1):
        total_calibration_p2 += goal

print("[day07p1] Total calibration result:", total_calibration_p1)
print("[day07p2] Total calibration result:", total_calibration_p2)

print_time_elapsed()
