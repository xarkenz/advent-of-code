from utils import *

start_time: float = get_start_time()

class Pair:
    def __init__(self, left: Union[int, "Pair"], right: Union[int, "Pair"], parent: Optional["Pair"] = None) -> None:
        self.left = left
        if isinstance(left, Pair):
            left.parent = self
        self.right = right
        if isinstance(right, Pair):
            right.parent = self
        self.parent = parent

    def make_copy(self, parent: Optional["Pair"] = None) -> "Pair":
        return Pair(
            self.left.make_copy() if isinstance(self.left, Pair) else self.left,
            self.right.make_copy() if isinstance(self.right, Pair) else self.right,
            parent,
        )

def parse_regular_number(raw: str) -> tuple[str, int]:
    return raw[1:], int(raw[0])

def parse_snailfish_number(raw: str) -> tuple[str, Pair]:
    if raw[0] != "[": raise ValueError
    raw, left = parse_snailfish_number(raw[1:]) if raw[1] == "[" else parse_regular_number(raw[1:])
    if raw[0] != ",": raise ValueError
    raw, right = parse_snailfish_number(raw[1:]) if raw[1] == "[" else parse_regular_number(raw[1:])
    if raw[0] != "]": raise ValueError
    return raw[1:], Pair(left, right)

def try_explode(pair: Pair, depth: int = 0) -> bool:
    if depth < 4:
        return (
            (isinstance(pair.left, Pair) and try_explode(pair.left, depth + 1)) or
            (isinstance(pair.right, Pair) and try_explode(pair.right, depth + 1))
        )
    else:
        if isinstance(pair.left, Pair) or isinstance(pair.right, Pair): raise ValueError

        left_target = pair
        while left_target.parent is not None:
            if left_target.parent.left != left_target:
                if isinstance(left_target.parent.left, Pair):
                    left_target = left_target.parent.left
                    while isinstance(left_target.right, Pair):
                        left_target = left_target.right
                    left_target.right += pair.left
                else:
                    left_target.parent.left += pair.left
                break
            left_target = left_target.parent

        right_target = pair
        while right_target.parent is not None:
            if right_target.parent.right != right_target:
                if isinstance(right_target.parent.right, Pair):
                    right_target = right_target.parent.right
                    while isinstance(right_target.left, Pair):
                        right_target = right_target.left
                    right_target.left += pair.right
                else:
                    right_target.parent.right += pair.right
                break
            right_target = right_target.parent

        if pair.parent.left == pair:
            pair.parent.left = 0
        else:
            pair.parent.right = 0

        return True

def try_split(pair: Pair) -> bool:
    if isinstance(pair.left, Pair):
        if try_split(pair.left):
            return True
    elif pair.left > 9:
        half = pair.left // 2
        pair.left = Pair(half, pair.left - half, pair)
        return True

    if isinstance(pair.right, Pair):
        if try_split(pair.right):
            return True
    elif pair.right > 9:
        half = pair.right // 2
        pair.right = Pair(half, pair.right - half, pair)
        return True

    return False

def add_numbers(pair_1: Pair, pair_2: Pair) -> Pair:
    new_pair = Pair(pair_1.make_copy(), pair_2.make_copy())
    while try_explode(new_pair) or try_split(new_pair):
        pass
    return new_pair

def get_magnitude(pair: Pair) -> int:
    magnitude_left = get_magnitude(pair.left) if isinstance(pair.left, Pair) else pair.left
    magnitude_right = get_magnitude(pair.right) if isinstance(pair.right, Pair) else pair.right
    return 3 * magnitude_left + 2 * magnitude_right

snailfish_numbers: list[Pair] = []
current_sum: Optional[Pair] = None

for line in get_input_lines("day18.txt"):
    remaining_line, snailfish_number = parse_snailfish_number(line)
    if remaining_line:
        print("not all of the line was parsed")
    snailfish_numbers.append(snailfish_number)
    if current_sum is None:
        current_sum = snailfish_number
    else:
        current_sum = add_numbers(current_sum, snailfish_number)

print("[18p1] Magnitude of snailfish number sum:", get_magnitude(current_sum))

largest_magnitude: int = 0

for pair_1 in snailfish_numbers:
    for pair_2 in snailfish_numbers:
        if pair_1 == pair_2:
            continue
        result = add_numbers(pair_1, pair_2)
        magnitude = get_magnitude(result)
        if magnitude > largest_magnitude:
            largest_magnitude = magnitude

print("[18p2] Largest possible magnitude:", largest_magnitude)

print_time_elapsed(start_time)
