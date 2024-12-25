from utils import *

from collections import deque
from copy import deepcopy

#             ___
# x00 ----@--\\  '-, result
#         |  ||XOR  >------------------------------------ z00
# y00 --@-|--//__,-'
#       | |  ______
#       | +--|     \ carry         ___
#       |    | AND  |----------@--\\  '-, result
#       +----|_____/           |  ||XOR  >--------------- z01
#             ___            +-|--//__,-'
# x01 ----@--\\  '-, rawadd  | |  ______
#         |  ||XOR  >--------@ +--|     \ checkcarry1
# y01 --@-|--//__,-'         |    | AND  |--,  ____    
#       | |  ______          +----|_____/   '--\   '-, carry
#       | +--|     \ checkcarry2                | OR  >--
#       |    | AND  |--------------------------/___,-' 
#       +----|_____/

RESULT = "result"
CARRY = "carry"
CHECKCARRY1 = "checkcarry1"
CHECKCARRY2 = "checkcarry2"
RAWADD = "rawadd"

start_time: float = get_start_time()

init_nodes: dict[str, tuple[bool, list[str]]] = {}
init_gates: list[tuple[str, str, str, str]] = []

getting_gates = False
for line in get_input_lines("day24.txt"):
    if not line:
        getting_gates = True
    elif getting_gates:
        in1, gate, in2, _, out = line.split()
        init_gates.append((in1, gate, in2, out))
    else:
        name, value = line.split(": ")
        init_nodes[name] = value != "0", [name]

def simulate(gates: list[tuple[str, str, str, str]], nodes: dict[str, tuple[bool, list[str]]]):
    roles: dict[str, tuple[str, int]] = {}
    unresolved = deque(gates)
    while unresolved:
        in1, gate, in2, out = unresolved.popleft()
        if in1 not in nodes or in2 not in nodes:
            unresolved.append((in1, gate, in2, out))
            continue
        value1, origins1 = nodes[in1]
        value2, origins2 = nodes[in2]
        if gate == "AND":
            nodes[out] = value1 and value2, origins1 + origins2
        elif gate == "OR":
            nodes[out] = value1 or value2, origins1 + origins2
        elif gate == "XOR":
            nodes[out] = value1 != value2, origins1 + origins2
        else:
            print("what")
        if in1[0] + in2[0] in ("xy", "yx"):
            if gate == "AND":
                roles[out] = (CARRY, 1) if in1[1:] == "00" else (CHECKCARRY2, int(in1[1:]))
            elif gate == "XOR":
                roles[out] = (RESULT, 0) if in1[1:] == "00" else (RAWADD, int(in1[1:]))
            else:
                print("ohno1")
        elif gate == "XOR":
            role1, bit1 = roles[in1]
            role2, bit2 = roles[in2]
            if bit1 != bit2:
                print("bad xor bit:", role1, bit1, in1, role2, bit2, in2, out)
            elif (role1, role2) not in ((CARRY, RAWADD), (RAWADD, CARRY)):
                print("bad xor roles:", role1, bit1, in1, role2, bit2, in2, out)
            roles[out] = (RESULT, bit2)
            if out[0] != "z":
                print("bad xor out:", out)
        elif gate == "OR":
            role1, bit1 = roles[in1]
            role2, bit2 = roles[in2]
            if bit1 != bit2:
                print("bad or bit:", role1, bit1, in1, role2, bit2, in2, out)
            elif (role1, role2) not in ((CHECKCARRY1, CHECKCARRY2), (CHECKCARRY2, CHECKCARRY1)):
                print("bad or roles:", role1, bit1, in1, role2, bit2, in2, out)
            roles[out] = (CARRY, bit2 + 1)
        elif gate == "AND":
            role1, bit1 = roles[in1]
            role2, bit2 = roles[in2]
            if bit1 != bit2:
                print("bad and bit:", role1, bit1, in1, role2, bit2, in2, out)
            elif (role1, role2) not in ((CARRY, RAWADD), (RAWADD, CARRY)):
                print("bad and roles:", role1, bit1, in1, role2, bit2, in2, out)
            roles[out] = (CHECKCARRY1, bit2)
    for name, (role, bit) in roles.items():
        if name[0] == "z":
            if role != RESULT:
                print("should be result:", role, bit, name)
        elif role == RESULT:
            print("should not be result:", role, bit, name)

def get_integer(nodes: dict[str, tuple[bool, list[str]]], prefix: str) -> int:
    bits = [name for name in nodes if name.startswith(prefix)]
    bits.sort()
    number = 0
    while bits:
        number = (number << 1) | nodes[bits.pop()][0]
    return number

nodes = deepcopy(init_nodes)
gates = init_gates.copy()
simulate(gates, nodes)

z_value = get_integer(nodes, "z")

print(z_value)

print_time_elapsed(start_time)
