from utils import *

start_time: float = get_start_time()

# 0: B1 = A1 % 8
# 1: B2 = B1 ^ 1 (flip bit 0)
# 2: C1 = A1 >> B2
# 3: B3 = B2 ^ C1
# 4: B4 = B3 ^ 4 (flip bit 2)
# 5: A2 = A1 / 8
# 6: output B4
# 7: if A2 != 0 goto 0

# B=k <- B^4=k <- B^C^4=k <- B^(A>>B)^4=k <- B^(A>>(B^1))^5=k

register_a: int
register_b: int
register_c: int
instruction_ptr: int
program: list[int]

def combo(operand):
    return [0, 1, 2, 3, register_a, register_b, register_c][operand]

def run_one_iteration() -> int:
    global instruction_ptr, register_a, register_b, register_c
    output: int
    while instruction_ptr < len(program):
        opcode, operand = program[instruction_ptr], program[instruction_ptr + 1]
        if opcode == 0: # ADV (A divide)
            register_a = register_a >> combo(operand)
        elif opcode == 1: # BXL (B xor literal)
            register_b = register_b ^ operand
        elif opcode == 2: # BST (B store)
            register_b = combo(operand) & 0b111
        elif opcode == 3: # JNZ (jump nonzero)
            if register_a != 0:
                instruction_ptr = operand * 2
                break
        elif opcode == 4: # BXC (B xor C)
            register_b = register_b ^ register_c
        elif opcode == 5: # OUT (output)
            output = combo(operand) & 0b111
        elif opcode == 6: # BDV (B divide)
            register_b = register_a >> combo(operand)
        elif opcode == 7: # CDV (C divide)
            register_c = register_a >> combo(operand)
        instruction_ptr += 2
    return output

for line in get_input_lines("day17.txt"):
    if line.startswith("Register A"):
        register_a = int(line[12:])
    elif line.startswith("Register B"):
        register_b = int(line[12:])
    elif line.startswith("Register C"):
        register_c = int(line[12:])
    elif line.startswith("Program"):
        program = [int(digit) for digit in line[9:].split(",")]
instruction_ptr = 0

outputs: list[int] = []
while instruction_ptr < len(program):
    outputs.append(run_one_iteration())

print("[17p1] Program output values:", ",".join(str(output) for output in outputs))

register_a_options: Optional[list[int]] = None
for ptr, target_value in enumerate(program):
    bit_offset: int = ptr * 3
    shared7_to_next3: dict[int, list[int]] = {}
    for current10 in range(0b10000000000):
        register_a = current10
        instruction_ptr = 0
        output = run_one_iteration()
        if output == target_value:
            shared7 = current10 & 0b1111111
            next3 = current10 >> 7
            shared7_to_next3.setdefault(shared7, []).append(next3)
    if register_a_options is None:
        # Create the initial list of options for the lowest 10 bits of A
        register_a_options = [
            (next3 << 7) | shared7
            for shared7, next3_options in shared7_to_next3.items()
            for next3 in next3_options
        ]
    else:
        # Filter the current set of options for A to ensure the 7 highest bits match the
        # lowest (shared) 7 bits of any 10 bit option just validated, then expand the options
        # to include the newly found 3 highest bits
        register_a_options = [
            (next3 << (bit_offset + 7)) | prev_a
            for prev_a in register_a_options
            for next3 in shared7_to_next3.get(prev_a >> bit_offset, [])
        ]

print("[17p2] Value of A causing self-replication:", min(register_a_options))

# register_a = min(register_a_options)
# register_b = 0
# register_c = 0
# instruction_ptr = 0
# outputs = []
# while instruction_ptr < len(program):
#     outputs.append(run_one_iteration())
# print(",".join(str(value) for value in program))
# print(",".join(str(output) for output in outputs))

print_time_elapsed(start_time)
