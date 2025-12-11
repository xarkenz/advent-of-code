from utils import *
import math

start_time: float = get_start_time()

@dataclass
class Packet:
    length: int
    version: int
    type_id: int
    content: int | list["Packet"]

def read_bits(bits: int, count: int) -> tuple[int, int]:
    reversed_bits = bits & ((1 << count) - 1)
    result_bits = 0
    for _ in range(count):
        result_bits = (result_bits << 1) | (reversed_bits & 1)
        reversed_bits >>= 1
    return bits >> count, result_bits

def parse_packet(bits: int) -> tuple[int, Packet]:
    bits, version = read_bits(bits, 3)
    bits, type_id = read_bits(bits, 3)
    length = 6
    if type_id == 4:
        # Literal
        prefix_bit = 1
        value = 0
        while prefix_bit:
            bits, group = read_bits(bits, 5)
            length += 5
            prefix_bit = group >> 4
            value = (value << 4) | (group & 0b1111)
        return bits, Packet(length, version, type_id, value)
    else:
        # Operator
        uses_subpacket_count = (bits & 1) != 0
        bits >>= 1
        length += 1
        subpackets: list[Packet] = []
        if uses_subpacket_count:
            bits, subpacket_count = read_bits(bits, 11)
            length += 11
            for _ in range(subpacket_count):
                bits, subpacket = parse_packet(bits)
                length += subpacket.length
                subpackets.append(subpacket)
        else:
            bits, content_length = read_bits(bits, 15)
            length += 15
            current_content_length = 0
            while current_content_length < content_length:
                bits, subpacket = parse_packet(bits)
                length += subpacket.length
                current_content_length += subpacket.length
                subpackets.append(subpacket)
            if current_content_length > content_length:
                print("invalid content length")
        return bits, Packet(length, version, type_id, subpackets)

# The bits are all reversed to make for easier access (bit 0 = index 0)
hexadecimal_bits: dict[str, int] = {
    "0": 0b0000,
    "1": 0b1000,
    "2": 0b0100,
    "3": 0b1100,
    "4": 0b0010,
    "5": 0b1010,
    "6": 0b0110,
    "7": 0b1110,
    "8": 0b0001,
    "9": 0b1001,
    "A": 0b0101,
    "B": 0b1101,
    "C": 0b0011,
    "D": 0b1011,
    "E": 0b0111,
    "F": 0b1111,
}

full_bits = 0
for digit in reversed(get_input_text("day16.txt").strip()):
    full_bits = (full_bits << 4) | hexadecimal_bits[digit]

full_bits, full_packet = parse_packet(full_bits)

def sum_versions(packet: Packet) -> int:
    if packet.type_id == 4:
        return packet.version
    else:
        return packet.version + sum(sum_versions(subpacket) for subpacket in packet.content)

def compute_expression(packet: Packet) -> int:
    if packet.type_id == 0:
        return sum(compute_expression(subpacket) for subpacket in packet.content)
    elif packet.type_id == 1:
        return math.prod(compute_expression(subpacket) for subpacket in packet.content)
    elif packet.type_id == 2:
        return min(compute_expression(subpacket) for subpacket in packet.content)
    elif packet.type_id == 3:
        return max(compute_expression(subpacket) for subpacket in packet.content)
    elif packet.type_id == 4:
        return packet.content
    elif packet.type_id == 5:
        return int(compute_expression(packet.content[0]) > compute_expression(packet.content[1]))
    elif packet.type_id == 6:
        return int(compute_expression(packet.content[0]) < compute_expression(packet.content[1]))
    elif packet.type_id == 7:
        return int(compute_expression(packet.content[0]) == compute_expression(packet.content[1]))
    else:
        raise ValueError

print("[16p1] Sum of version numbers:", sum_versions(full_packet))
print("[16p2] Expression result:", compute_expression(full_packet))

print_time_elapsed(start_time)
