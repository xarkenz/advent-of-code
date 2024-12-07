from utils import *

from math import floor, log10

equations = []

with open("input/day07.txt") as input_file:
    for line in input_file.readlines():
        test, operands = line.strip().split(": ")
        equations.append((int(test), [int(operand) for operand in operands.split()]))

# this is actually worse
def check(test: int, operands: list[int]):
    operator_stack = [0]
    lhs_stack = [operands[0]]
    while operator_stack:
        lhs = lhs_stack[-1]
        rhs = operands[len(operator_stack)]
        operator = operator_stack[-1]
        if operator == 0:
            result = lhs + rhs
        elif operator == 1:
            result = lhs * rhs
        elif operator == 2:
            result = lhs * 10 ** (floor(log10(rhs)) + 1) + rhs
        lhs_stack.append(result)
        if len(lhs_stack) == len(operands) or result > test:
            if result == test:
                return True
            lhs_stack.pop()
            while operator_stack:
                operator_stack[-1] += 1
                if operator_stack[-1] <= 2:
                    break
                operator_stack.pop()
                lhs_stack.pop()
        else:
            operator_stack.append(0)
    return False

total_calibration = 0

for test, operands in equations:
    if check(test, operands):
        total_calibration += test

print(total_calibration)

print_time_elapsed()
