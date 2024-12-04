def get(grid, r, c):
    if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[r]):
        return '.'
    else:
        return grid[r][c]

def check(grid, r, c, dr, dc):
    for ch in "XMAS":
        if get(grid, r, c) != ch:
            return False
        r += dr
        c += dc
    return True

with open("input/day04.txt") as f:
    grid = f.readlines()

count = 0
dirs = [(1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]

for r in range(len(grid)):
    for c in range(len(grid[r])):
        for dr, dc in dirs:
            if check(grid, r, c, dr, dc):
                count += 1

print(count)

def check_x(grid, r, c):
    if get(grid, r, c) == 'A':
        tl = get(grid, r - 1, c - 1)
        tr = get(grid, r - 1, c + 1)
        bl = get(grid, r + 1, c - 1)
        br = get(grid, r + 1, c + 1)
        return ((tl == 'M' and br == 'S') or (tl == 'S' and br == 'M')) and ((tr == 'M' and bl == 'S') or (tr == 'S' and bl == 'M'))

count = 0

for r in range(len(grid)):
    for c in range(len(grid[r])):
        if check_x(grid, r, c):
            count += 1

print(count)
