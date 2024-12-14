import os
import re

def read_input():
    path = os.path.dirname(os.path.realpath(__file__))
    data = open(f"{path}/input.txt", "r").read().strip().split("\n")
    return data

# A few assumptions here, namely that the lengths of digits are always 2. For completeness' sake one can just use regex with \d+ or something.
# Also, the question assumes the existence of a middle number, so I won't handle even-numbered cases.
data = read_input()
idx = data.index("")
first, second = data[0: idx], data[idx + 1: ]

total = 0
for line in second:
    flag = True
    for order in first:
        num1, num2 = order.split("|")
        if num1 in line and num2 in line and (not bool(re.match(f".*{num1},.*{num2}.*", line))):
            flag = False
            break
    if flag:
        pages = line.split(",")
        middle = int(pages[len(pages) // 2])
        total += middle

print(total)
