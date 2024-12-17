# what the hell man, this is a terrible question imo. Also, despite what people say, the grid with the least safety factor is not necessarily the image. 
# Statistical analyses did not help either.
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

def print_grid(data):
    grid = [["l" for _ in range(cols)] for _ in range(rows)]
    for coords, _ in data:
        x, y = coords
        grid[y][x] = "X"
    for row in grid:
        print("".join(row))

data = read_input()
maxlinks = 0
beststep = 0
for step in range(1, rows * cols + 1):
    links = 0
    for bot in data:
        move(bot)
    for curr in data:
        curr_x, curr_y = curr[0]
        for other in data:
            other_x, other_y = other[0]
            if abs(other_x - curr_x) == 1 ^ abs(other_y - curr_y) == 1:
                links += 1
    if links > maxlinks:
        maxlinks = links
        beststep = step
        print(beststep)
        print_grid(data)
print(beststep)
