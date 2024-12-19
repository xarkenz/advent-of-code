from utils import *

start_time: float = get_start_time()

scenarios: list[list[Point]] = []
for line in get_input_lines("day13.txt"):
    if line.startswith("Button A"):
        x, y = line[12:].split(", Y+")
        scenarios.append([Point(int(x), int(y))])
    elif line.startswith("Button B"):
        x, y = line[12:].split(", Y+")
        scenarios[-1].append(Point(int(x), int(y)))
    elif line.startswith("Prize"):
        x, y = line[9:].split(", Y=")
        scenarios[-1].append(Point(int(x), int(y)))

def calculate_tokens(a_move: Point, b_move: Point, prize_pos: Point) -> int:
    ax, ay = a_move.row, a_move.col
    bx, by = b_move.row, b_move.col
    px, py = prize_pos.row, prize_pos.col
    determinant = ax * by - bx * ay
    a_presses_numerator = by * px - bx * py
    b_presses_numerator = ax * py - ay * px
    a_presses, a_remainder = divmod(a_presses_numerator, determinant)
    b_presses, b_remainder = divmod(b_presses_numerator, determinant)
    if a_remainder == 0 and b_remainder == 0:
        return a_presses * 3 + b_presses * 1
    else:
        return 0

token_count_p1: int = 0
token_count_p2: int = 0

for a_move, b_move, prize_pos in scenarios:
    token_count_p1 += calculate_tokens(a_move, b_move, prize_pos)
    prize_pos += Point(10000000000000, 10000000000000)
    token_count_p2 += calculate_tokens(a_move, b_move, prize_pos)

print("[13p1] Tokens required:", token_count_p1)
print("[13p2] Tokens required:", token_count_p2)

print_time_elapsed(start_time)

# My first solution works and I'm still proud of it so I'm keeping it here

# def reducefrac(frac):
#     g = gcd(abs(frac[0]), abs(frac[1]))
#     if frac[0] < 0 and frac[1] < 0:
#         return -frac[0] // g, -frac[1] // g
#     else:
#         return frac[0] // g, frac[1] // g

# def subfrac(frac1, frac2):
#     n1, d1 = frac1
#     n2, d2 = frac2
#     return reducefrac((n1 * d2 - n2 * d1, d1 * d2))

# def mulfrac(frac1, frac2):
#     return reducefrac((frac1[0] * frac2[0], frac1[1] * frac2[1]))

# def divfrac(frac1, frac2):
#     return reducefrac((frac1[0] * frac2[1], frac1[1] * frac2[0]))

# tokens = 0
# for a_move, b_move, prize in cases:
#     prize += Point(10000000000000, 10000000000000)
#     a = (a_move.row, 1)
#     b = (b_move.row, 1)
#     c = (a_move.col, 1)
#     d = (b_move.col, 1)
#     y1 = (prize.row, 1)
#     y2 = (prize.col, 1)
#     y1 = divfrac(y1, a)
#     b = divfrac(b, a)
#     a = (1, 1)
#     y2 = subfrac(y2, mulfrac(y1, c))
#     d = subfrac(d, mulfrac(b, c))
#     c = (0, 1)
#     y2 = divfrac(y2, d)
#     d = (1, 1)
#     y1 = subfrac(y1, mulfrac(y2, b))
#     b = (0, 1)
#     print(f"{a} {b} {y1}\n{c} {d} {y2}\n")
#     if y1[1] == 1 and y2[1] == 1 and y1[0] >= 0 and y2[0] >= 0:
#         tokens += 3 * y1[0] + y2[0]
# print(tokens)
