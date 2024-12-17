from utils import *

reg_a = 46337277
reg_b = 0
reg_c = 0
program = [(2,4),(1,1),(7,5),(4,4),(1,4),(0,3),(5,5),(3,0)]
# 0: B = A % 8
# 1: B = B ^ 1 (flip bit 0)
# 2: C = A >> B
# 3: B = B ^ C
# 4: B = B ^ 4 (flip bit 2)
# 5: A = A / 8
# 6: output B
# 7: if A != 0 goto 0

# B=k <- B^4=k <- B^C^4=k <- B^(A>>B)^4=k <- B^(A>>(B^1))^5=k

pc = 0
output = []
def combo(operand):
    return [0, 1, 2, 3, reg_a, reg_b, reg_c][operand]
while pc < len(program):
    opcode, operand = program[pc]
    if opcode == 0: # ADV
        reg_a = reg_a >> combo(operand)
    elif opcode == 1: # BXL
        reg_b ^= operand
    elif opcode == 2: # BST
        reg_b = combo(operand) % 8
    elif opcode == 3: # JNZ
        if reg_a != 0:
            pc = operand // 2
            continue
    elif opcode == 4: # BXC
        reg_b ^= reg_c
    elif opcode == 5: # OUT
        output.append(combo(operand) % 8)
    elif opcode == 6: # BDV
        reg_b = reg_a >> combo(operand)
    elif opcode == 7: # CDV
        reg_c = reg_a >> combo(operand)
    pc += 1

print(",".join(str(i) for i in output))

program_flat = [2,4,1,1,7,5,4,4,1,4,0,3,5,5,3,0]

a_options = None
for i, digit in enumerate(program_flat):
    place = i * 3
    shared7_options = {}
    for first10 in range(0b10000000000):
        b = first10 & 0b111
        result = b ^ 5 ^ ((first10 >> (b ^ 1)) & 0b111)
        if result == digit:
            shared7 = first10 & 0b1111111
            last3_options = shared7_options.get(shared7, [])
            last3_options.append(first10 >> 7)
            shared7_options[shared7] = last3_options
    if a_options is None:
        a_options = [shared7 | (last3 << 7) for shared7, last3_options in shared7_options.items() for last3 in last3_options]
    else:
        a_options = [a | (last3 << (place + 7)) for a in a_options for last3 in shared7_options.get(a >> place, [])]

print(a_options)
print(min(a_options))

reg_a = min(a_options)
reg_b = 0
reg_c = 0

pc = 0
output = []
def combo(operand):
    return [0, 1, 2, 3, reg_a, reg_b, reg_c][operand]
while pc < len(program):
    opcode, operand = program[pc]
    if opcode == 0: # ADV
        reg_a = reg_a >> combo(operand)
    elif opcode == 1: # BXL
        reg_b ^= operand
    elif opcode == 2: # BST
        reg_b = combo(operand) % 8
    elif opcode == 3: # JNZ
        if reg_a != 0:
            pc = operand // 2
            continue
    elif opcode == 4: # BXC
        reg_b ^= reg_c
    elif opcode == 5: # OUT
        output.append(combo(operand) % 8)
    elif opcode == 6: # BDV
        reg_b = reg_a >> combo(operand)
    elif opcode == 7: # CDV
        reg_c = reg_a >> combo(operand)
    pc += 1

print(",".join(str(i) for i in program_flat))
print(",".join(str(i) for i in output))

print_time_elapsed()
