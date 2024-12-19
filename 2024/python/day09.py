from utils import *

start_time: float = get_start_time()

blocks: list[int] = []

is_file_block = True
file_starts: list[int] = []
for size in get_input_text("day09.txt").strip():
    size = int(size)
    if is_file_block:
        file_id = len(file_starts)
        file_starts.append(len(blocks))
        blocks += [file_id] * size
    else:
        blocks += [None] * size
    is_file_block = not is_file_block

blocks_p1 = blocks.copy()
while True:
    file_id = blocks_p1.pop()
    while file_id is None:
        file_id = blocks_p1.pop()
    while blocks_p1[-1] is None:
        blocks_p1.pop()
    if None in blocks_p1:
        pos = blocks_p1.index(None)
        blocks_p1[pos] = file_id
    else:
        blocks_p1.append(file_id)
        break

print("[09p1] Filesystem checksum:", sum(pos * file_id for pos, file_id in enumerate(blocks_p1)))

for pos in reversed(file_starts):
    file_id = blocks[pos]
    size = 1
    while pos + size < len(blocks) and blocks[pos + size] == file_id:
        size += 1
    try:
        new_pos = blocks.index(None, 0, pos)
        while not all(block is None for block in blocks[new_pos : new_pos + size]):
            new_pos = blocks.index(None, new_pos + 1, pos)
        for i in range(size):
            blocks[pos + i] = None
        for i in range(size):
            blocks[new_pos + i] = file_id
    except ValueError:
        pass

print("[09p2] Filesystem checksum:", sum(pos * file_id for pos, file_id in enumerate(blocks) if file_id is not None))

print_time_elapsed(start_time)
