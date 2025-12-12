from utils import *
from scipy.optimize import linprog
import numpy

start_time: float = get_start_time()

def parse_target_state(string: str) -> int:
    result: int = 0
    for index, char in enumerate(string[1:-1]):
        result |= (char == "#") << index
    return result

def parse_button(string: str) -> int:
    result: int = 0
    for index in string[1:-1].split(","):
        result |= 1 << int(index)
    return result

def increment_parameter_inputs(parameter_inputs: list[int]) -> None:
    if not parameter_inputs:
        return
    elif len(parameter_inputs) == 1:
        parameter_inputs[0] += 1
        return
    
    if parameter_inputs[0] == 0:
        try:
            found_index = next(index for index, value in enumerate(parameter_inputs[:-1]) if value != 0)
            parameter_inputs[0] = parameter_inputs[found_index] - 1
            parameter_inputs[found_index + 1] += 1
            parameter_inputs[found_index] = 0
        except StopIteration:
            parameter_inputs[0] = parameter_inputs[-1] + 1
            parameter_inputs[-1] = 0
    else:
        parameter_inputs[0] -= 1
        parameter_inputs[1] += 1

total_lights_press_count: int = 0
total_joltage_press_count: int = 0

for line_no, line in enumerate(get_input_lines("day10.txt")):
    raw_target_lights, *raw_buttons, raw_target_joltage = line.split()
    state_size: int = len(raw_target_lights) - 2
    buttons: list[int] = [parse_button(button) for button in raw_buttons]

    target_lights: int = parse_target_state(raw_target_lights)
    press_counts: dict[int, int] = {0: 0}
    visit_queue: list[int] = [0]
    while visit_queue:
        lights = visit_queue.pop(0)
        press_count = press_counts[lights]
        if lights == target_lights:
            total_lights_press_count += press_count
            break
        for button in buttons:
            new_lights = lights ^ button
            if new_lights not in press_counts:
                press_counts[new_lights] = press_count + 1
                visit_queue.append(new_lights)

    target_joltage: tuple[int, ...] = tuple(int(value) for value in raw_target_joltage[1:-1].split(","))
    matrix: list[list[float]] = [[0.0 for _ in range(len(buttons))] for _ in range(state_size)]
    for col, button in enumerate(buttons):
        for row in range(state_size):
            matrix[row][col] = float((button >> row) & 1)
    np_matrix = numpy.array(matrix)
    np_target = numpy.array([float(value) for value in target_joltage])
    result = linprog(
        numpy.ones(len(buttons)),
        A_eq=np_matrix,
        b_eq=np_target,
        method="highs",
        integrality=1
    )
    total_joltage_press_count += sum(map(round, result.x))

print("[10p1] Fewest button presses:", total_lights_press_count)
print("[10p2] Fewest button presses:", total_joltage_press_count)

print_time_elapsed(start_time)
