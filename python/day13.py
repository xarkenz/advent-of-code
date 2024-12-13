from utils import *

def sign(x: int) -> int:
    return 0 if x == 0 else x // abs(x)

def cmpdirs(p1: Point, p2: Point) -> int:
    return p1.row * p2.col - p1.col * p2.row

def reaches(p1: Point, p2: Point) -> bool:
    rdiv, rmod = divmod(p2.row, p1.row)
    if rmod != 0:
        return False
    cdiv, cmod = divmod(p2.col, p1.col)
    if cmod != 0:
        return False
    return rdiv == cdiv

cases: list[list[Point]] = []
for line in get_input_lines("day13.txt"):
    if line.startswith("Button A"):
        x, y = line[12:].split(", Y+")
        cases.append([Point(int(x), int(y))])
    elif line.startswith("Button B"):
        x, y = line[12:].split(", Y+")
        cases[-1].append(Point(int(x), int(y)))
    elif line.startswith("Prize"):
        x, y = line[9:].split(", Y=")
        cases[-1].append(Point(int(x), int(y)))

# tokens = 0
# for a_move, b_move, prize in cases:
#     for a_times in range(100):
#         for b_times in range(100):
#             claw = a_move * a_times + b_move * b_times
#             if claw == prize:
#                 tokens += 3 * a_times + b_times
#                 break
#         if claw == prize:
#                 break
# print(tokens)

# tokens = 0
# for a_move, b_move, prize in cases:
#     prize += Point(10000000000000, 10000000000000)
#     a_dir = cmpdirs(a_move, prize)
#     b_dir = cmpdirs(b_move, prize)
#     if sign(a_dir) == sign(b_dir):
#         continue
#     elif b_dir == 0 and a_dir == 0:
#         print("oh no")
#         continue
#     elif b_dir == 0:
#         if reaches(b_move, prize):
#             tokens += prize.row // b_move.row
#         continue
#     elif a_dir == 0:
#         if reaches(a_move, prize):
#             tokens += 3 * (prize.row // a_move.row)
#         continue
#     down_move, up_move, down_tokens, up_tokens = (a_move, b_move, 3, 1) if a_dir > b_dir else (b_move, a_move, 1, 3)
#     current_pos = down_move
#     current_tokens = down_tokens
#     unreachable = False
#     print(f"{prize=}")
#     while not reaches(current_pos, prize):
#         current_dir = cmpdirs(current_pos, prize)
#         if current_dir > 0:
#             current_pos += up_move
#             current_tokens += up_tokens
#         elif current_dir < 0:
#             current_pos += down_move
#             current_tokens += down_tokens
#         else:
#             unreachable = True
#             break
#     if unreachable:
#         print("unreachable")
#         continue
#     times = prize.row // current_pos.row
#     tokens += times * current_tokens
#     print("done")
# print(tokens)

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

tokens = 0
for a_move, b_move, prize in cases:
    prize += Point(10000000000000, 10000000000000)
    ax, ay = a_move.col, a_move.row
    bx, by = b_move.col, b_move.row
    px, py = prize.col, prize.row
    d = ax * by - bx * ay
    an = by * px - bx * py
    bn = ax * py - ay * px
    a, arem = divmod(an, d)
    b, brem = divmod(bn, d)
    if arem == 0 and brem == 0:
        tokens += 3 * a + b
print(tokens)

print_time_elapsed()
