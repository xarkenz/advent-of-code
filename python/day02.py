from utils import *

reports = [[int(i) for i in line.split()] for line in get_input_lines("day02.txt")]

safe_count = 0

for report in reports:
    increasing = None
    for i in range(len(report) - 1):
        left, right = report[i], report[i + 1]
        if (increasing is not None and left != right and (left < right) != increasing) or not (1 <= abs(left - right) <= 3):
            break
        elif left != right:
            increasing = left < right
    else:
        safe_count += 1

print("[day02p1] Safe reports:", safe_count)

safe_count = 0

for report in reports:
    increasing = None
    for i in range(len(report) - 1):
        left, right = report[i], report[i + 1]
        if (increasing is not None and left != right and (left < right) != increasing) or not (1 <= abs(left - right) <= 3):
            break
        elif left != right:
            increasing = left < right
    else:
        safe_count += 1
        continue
    for j in range(len(report)):
        increasing = None
        temp_report = report.copy()
        temp_report.pop(j)
        for i in range(len(temp_report) - 1):
            left, right = temp_report[i], temp_report[i + 1]
            if (increasing is not None and left != right and (left < right) != increasing) or not (1 <= abs(left - right) <= 3):
                break
            elif left != right:
                increasing = left < right
        else:
            safe_count += 1
            break

print("[day02p2] Safe reports:", safe_count)

print_time_elapsed()
