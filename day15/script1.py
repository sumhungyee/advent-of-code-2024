import os
import re 
def read_input():
    path = os.path.dirname(os.path.realpath(__file__))
    data = open(f"{path}/input.txt", "r").read().strip().split("\n")
    return data

data = read_input()
split = data.index("")
instructions = data[split + 1:]
grid = list(map(lambda x: list(x), data[: split]))
rows, cols = len(grid), len(grid)
pos = (-1, -1)
for row in range(len(grid)):
    found = "".join(grid[row]).find("@")
    if found > -1:
        pos = row, found
    
def move(grid, r, c, direction):
    if direction == "^":
        new_r = r - 1
        new_c = c
    elif direction == "v":
        new_r = r + 1
        new_c = c
    elif direction == "<":
        new_r = r
        new_c = c - 1
    elif direction == ">":
        new_r = r
        new_c = c + 1
    else:
        raise ValueError()
    
    if grid[new_r][new_c] == ".":
        grid[new_r][new_c], grid[r][c] = grid[r][c], grid[new_r][new_c]
        return new_r, new_c
    
    elif grid[new_r][new_c] == "#":
        return r, c
    else:  
        move(grid, new_r, new_c, direction)
        if grid[new_r][new_c] == ".":
            grid[new_r][new_c], grid[r][c] = grid[r][c], grid[new_r][new_c]   
            return new_r, new_c
        return r, c
        
for g in grid:
    print("".join(g))

for line in instructions:
    for direction in line:
        pos = move(grid, pos[0], pos[1], direction)

thingineedtocalc = 0
for i in range(rows):
    for j in range(cols):
        if grid[i][j] == "O":
            thingineedtocalc += i * 100 + j
print(thingineedtocalc)