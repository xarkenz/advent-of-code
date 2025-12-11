from utils import *

start_time: float = get_start_time()

device_outputs: dict[str, list[str]] = {"out": []}

for line in get_input_lines("day11.txt"):
    device, outputs = line.split(": ")
    device_outputs[device] = outputs.split()

device_order: list[str] = []
devices_finished: dict[str, bool] = {}

def visit_device(device: str) -> None:
    finished = devices_finished.get(device)
    if finished is None:
        devices_finished[device] = False
        for output in device_outputs[device]:
            visit_device(output)
        devices_finished[device] = True
        device_order.append(device)
    elif not finished:
        raise ValueError("cycle detected")

visit_device("you")

def get_paths(start_index: int, end_index: int) -> int:
    paths_to_device: dict[str, int] = {device_order[start_index]: 1}
    for device in device_order[start_index : end_index : -1]:
        paths = paths_to_device.get(device, 0)
        for output in device_outputs[device]:
            paths_to_device[output] = paths_to_device.get(output, 0) + paths
    return paths_to_device[device_order[end_index]]

print("[11p1] Paths from 'you' to 'out':", get_paths(len(device_order) - 1, 0))

device_order.clear()
devices_finished.clear()
visit_device("svr")

checkpoint_1 = device_order.index("dac")
checkpoint_2 = device_order.index("fft")
if checkpoint_1 < checkpoint_2:
    checkpoint_1, checkpoint_2 = checkpoint_2, checkpoint_1

first = get_paths(len(device_order) - 1, checkpoint_1)
second = get_paths(checkpoint_1, checkpoint_2)
third = get_paths(checkpoint_2, 0)

print("[11p2] Paths from 'svr' to 'out' through 'dac' and 'fft':", first * second * third)

print_time_elapsed(start_time)
