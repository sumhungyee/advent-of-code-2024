import os
import re
rows, cols = 103, 101
# rows, cols = 7, 11
def read_input():
    path = os.path.dirname(os.path.realpath(__file__))
    data = open(f"{path}/input.txt", "r").read().strip().split("\n")
    data = [[[int(u) for u in re.findall("-?\d+", t)] for t in s.split(" ")] for s in data]
    return data

def move(bot):
    movex, movey = bot[1]
    currx, curry = bot[0]
    bot[0] = [(currx + movex) % cols, (curry + movey) % rows]

data = read_input()
for _ in range(100):
    q1 = q2 = q3 = q4 = 0
    for bot in data:
        move(bot)
        x, y = bot[0]
        if 0 <= x < cols // 2:
            if 0 <= y < rows // 2:
                q1 += 1
            elif y > rows // 2:
                q2 += 1
        elif x > cols // 2:
            if 0 <= y < rows // 2:
                q3 += 1
            elif y > rows // 2:
                q4 += 1
                
print(q1 * q2 * q3 * q4)
