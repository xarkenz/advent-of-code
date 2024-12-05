orderings = []
updates = []

with open("input/day05.txt") as f:
    getting_updates = False
    for line in f.readlines():
        if line.isspace():
            getting_updates = True
        elif getting_updates:
            updates.append([int(x) for x in line.split(",")])
        else:
            orderings.append([int(x) for x in line.split("|")])

def check_update(update):
    for x, y in orderings:
        if x in update and y in update and update.index(x) > update.index(y):
            return False
    return True

middle_total = 0
for update in updates:
    if check_update(update):
        middle_total += update[len(update) // 2]

print(middle_total)

def check_update_p2(update):
    if check_update(update):
        return False
    while not check_update(update):
        for x, y in orderings:
            if x in update and y in update and update.index(x) > update.index(y):
                i = update.index(x)
                j = update.index(y)
                update[i], update[j] = update[j], update[i]
    return True

middle_total = 0
for update in updates:
    if check_update_p2(update):
        middle_total += update[len(update) // 2]

print(middle_total)
