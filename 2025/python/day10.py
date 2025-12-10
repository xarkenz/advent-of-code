from utils import *

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

for line_no, line in enumerate(get_input_lines("test.txt")):
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
    matrix: list[list[Fraction]] = [[Fraction() for _ in range(len(buttons) + 1)] for _ in range(state_size)]
    for col, button in enumerate(buttons):
        for row in range(state_size):
            matrix[row][col] = Fraction((button >> row) & 1)
    for row, value in enumerate(target_joltage):
        matrix[row][-1] = Fraction(value)
    independent_cols = matrix_rref(matrix)
    for row in matrix:
        print("  ".join(map(str, row)))
    if independent_cols[-1] == len(buttons):
        print("uh oh")
        break
    elif len(independent_cols) == len(buttons):
        total_joltage_press_count += sum((row[-1] for row in matrix), Fraction()).numerator
    else:
        row_muls: list[int] = [max(value.denominator for value in row) for row in matrix]
        parameters: list[list[int]] = [[(row[col] * mul).numerator for row, mul in zip(matrix, row_muls)] for col in range(len(matrix[0])) if col not in independent_cols]
        target_vector: list[int] = parameters.pop()
        parameter_inputs: list[int] = [0] * len(parameters)
        min_presses: Optional[int] = None
        while min_presses is None or sum(parameter_inputs) < min_presses:
            # print(line_no, min_presses, parameter_inputs)
            presses: int = sum(parameter_inputs)
            for row in range(len(independent_cols)):
                difference = target_vector[row] - sum(parameter_input * parameter[row] for parameter_input, parameter in zip(parameter_inputs, parameters))
                if difference < 0:
                    break
                quotient, remainder = divmod(difference, row_muls[row])
                if remainder != 0:
                    break
                presses += quotient * row_muls[row]
            else:
                if min_presses is None or presses < min_presses:
                    min_presses = presses
            increment_parameter_inputs(parameter_inputs)
        total_joltage_press_count += min_presses
    print("done", line_no)

print("[10p1] Fewest button presses:", total_lights_press_count)
print("[10p2] Fewest button presses:", total_joltage_press_count)

print_time_elapsed(start_time)
