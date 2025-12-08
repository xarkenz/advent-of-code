from utils import *

start_time: float = get_start_time()

def distance_squared(p1: tuple[int, int, int], p2: tuple[int, int, int]) -> int:
    return sum((b - a) * (b - a) for a, b in zip(p1, p2))

junction_boxes: list[tuple[int, int, int]] = []

for line in get_input_lines("day08.txt"):
    x, y, z = map(int, line.split(","))
    junction_boxes.append((x, y, z))

connection_order: list[tuple[int, int]] = [(index_1, index_2) for index_1 in range(len(junction_boxes)) for index_2 in range(len(junction_boxes)) if index_1 < index_2]
connection_order.sort(key=(lambda connection: distance_squared(junction_boxes[connection[0]], junction_boxes[connection[1]])))
connections_made: int = 1000

connections: list[list[int]] = [[] for _ in junction_boxes]

for index_1, index_2 in connection_order[:connections_made]:
    connections[index_1].append(index_2)
    connections[index_2].append(index_1)

box_to_circuit: list[Optional[int]] = [None] * len(junction_boxes)
circuit_sizes: list[int] = []
start_indices: set[int] = set()

while any(circuit is None for circuit in box_to_circuit):
    start_index: int = box_to_circuit.index(None)
    start_indices.add(start_index)
    circuit_size: int = 0
    visit_queue: list[int] = [start_index]
    while visit_queue:
        current_index = visit_queue.pop(0)
        if box_to_circuit[current_index] is None:
            box_to_circuit[current_index] = start_index
            circuit_size += 1
            visit_queue.extend(connections[current_index])
    circuit_sizes.append(circuit_size)

circuit_sizes.sort(reverse=True)

print("[08p1] Product of 3 largest circuit sizes:", circuit_sizes[0] * circuit_sizes[1] * circuit_sizes[2])

while len(start_indices) > 1:
    index_1, index_2 = connection_order[connections_made]
    connections_made += 1
    to_circuit = box_to_circuit[index_1]
    from_circuit = box_to_circuit[index_2]
    if from_circuit != to_circuit:
        box_to_circuit = [to_circuit if circuit == from_circuit else circuit for circuit in box_to_circuit]
        start_indices.remove(from_circuit)

print("[08p2] Product of last connection Xs:", junction_boxes[index_1][0] * junction_boxes[index_2][0])

print_time_elapsed(start_time)

# originally I used a max heap lol

# @dataclass(order=True)
# class ConnectionCandidate:
#     # Always negated so as to act like a max heap
#     inv_distance_squared: int
#     index_1: int = field(compare=False)
#     index_2: int = field(compare=False)

# connection_candidates: MinHeap[ConnectionCandidate] = MinHeap()

# for index_1, point_1 in enumerate(junction_boxes):
#     for index_2, point_2 in enumerate(junction_boxes):
#         if index_2 <= index_1:
#             continue
#         connection_candidates.push(ConnectionCandidate(-distance_squared(point_1, point_2), index_1, index_2))
#         while len(connection_candidates) > 1000:
#             connection_candidates.pop()
