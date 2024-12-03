import re

with open("input/day03.txt") as f:
    text = f.read()

matches = re.findall("mul\\([0-9]{1,3},[0-9]{1,3}\\)", text)

result = 0
for item in matches:
    x, y = item[4:-1].split(",")
    result += int(x) * int(y)

print(result)

matches = re.findall("mul\\([0-9]{1,3},[0-9]{1,3}\\)|do\\(\\)|don't\\(\\)", text)

result = 0
enabled = True
for item in matches:
    if item.startswith("don't"):
        enabled = False
    elif item.startswith("do"):
        enabled = True
    elif enabled:
        x, y = item[4:-1].split(",")
        result += int(x) * int(y)

print(result)
