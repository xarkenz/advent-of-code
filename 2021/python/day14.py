from utils import *

start_time: float = get_start_time()

lines: list[str] = get_input_lines("day14.txt")
initial_polymer: str = lines[0]
rules: dict[str, tuple[str, str]] = {}

for rule in lines[2:]:
    pair, insertion = rule.split(" -> ")
    rules[pair] = (pair[0] + insertion, insertion + pair[1])

pair_counts: dict[str, int] = {}

for pair in itertools.pairwise(initial_polymer):
    pair = pair[0] + pair[1]
    pair_counts[pair] = pair_counts.get(pair, 0) + 1

def get_answer() -> int:
    element_counts: dict[str, int] = {initial_polymer[0]: 1}
    for pair, count in pair_counts.items():
        element_counts[pair[1]] = element_counts.get(pair[1], 0) + count
    return max(element_counts.values()) - min(element_counts.values())

answer_after_10: Optional[int] = None

for step in range(40):
    if step == 10:
        answer_after_10 = get_answer()
    new_pair_counts: dict[str, int] = {}
    for pair, count in pair_counts.items():
        for new_pair in rules[pair]:
            new_pair_counts[new_pair] = new_pair_counts.get(new_pair, 0) + count
    pair_counts = new_pair_counts

print("[14p1] After 10 iterations:", answer_after_10)
print("[14p2] After 40 iterations:", get_answer())

print_time_elapsed(start_time)
