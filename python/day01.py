with open("day01.txt") as f:
    lines = f.readlines()

left = []
right = []

for line in lines:
    left_id, right_id = [int(i) for i in line.split()]
    left.append(left_id)
    right.append(right_id)

left.sort()
right.sort()

print(sum(abs(x - y) for x, y in zip(left, right)))

print(sum(i * right.count(i) for i in left))
