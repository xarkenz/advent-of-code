from utils import *

from math import floor, log10

equations = []

with open("input/day07.txt") as input_file:
    for line in input_file.readlines():
        goal, operands = line.strip().split(": ")
        equations.append((int(goal), [int(operand) for operand in operands.split()]))

def check(goal: int, lhs: int, operands: list[int], rhs_index: int, use_concat: bool) -> bool:
    if rhs_index == len(operands):
        return lhs == goal
    elif lhs > goal:
        return False
    rhs = operands[rhs_index]
    if check(goal, lhs + rhs, operands, rhs_index + 1, use_concat):
        return True
    elif check(goal, lhs * rhs, operands, rhs_index + 1, use_concat):
        return True
    elif use_concat and check(goal, lhs * (10 ** (floor(log10(rhs)) + 1)) + rhs, operands, rhs_index + 1, use_concat):
        return True
    return False

total_calibration_p1 = 0
total_calibration_p2 = 0

for goal, operands in equations:
    if check(goal, operands[0], operands, 1, False):
        total_calibration_p1 += goal
    if check(goal, operands[0], operands, 1, True):
        total_calibration_p2 += goal

print("[day07p1] Total calibration result:", total_calibration_p1)
print("[day07p2] Total calibration result:", total_calibration_p2)

print_time_elapsed()
