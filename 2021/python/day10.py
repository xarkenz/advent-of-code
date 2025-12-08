from utils import *

start_time: float = get_start_time()

opening_chars: dict[str, str] = {
    "(": ")",
    "[": "]",
    "{": "}",
    "<": ">",
}
point_values: dict[str, int] = {
    ")": (3, 1),
    "]": (57, 2),
    "}": (1197, 3),
    ">": (25137, 4),
}

total_syntax_score: int = 0
autocomplete_scores: list[int] = []

for line in get_input_lines("day10.txt"):
    expected_stack: list[str] = []
    for char in line:
        if char in opening_chars:
            expected_stack.append(opening_chars[char])
        else:
            expected = expected_stack.pop()
            if char != expected:
                total_syntax_score += point_values[char][0]
                expected_stack = []
                break

    if expected_stack:
        autocomplete_score: int = 0
        for char in reversed(expected_stack):
            autocomplete_score *= 5
            autocomplete_score += point_values[char][1]
        autocomplete_scores.append(autocomplete_score)

autocomplete_scores.sort()

print("[10p1] Total syntax score:", total_syntax_score)
print("[10p2] Winning autocomplete score:", autocomplete_scores[len(autocomplete_scores) // 2])

print_time_elapsed(start_time)
