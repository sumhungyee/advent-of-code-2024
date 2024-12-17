import os
import re 
def read_input():
    path = os.path.dirname(os.path.realpath(__file__))
    data = open(f"{path}/input.txt", "r").read().strip().split("\n")
    return data

def replace_all(string):
    string = string.replace("#", "##")
    string = string.replace("O", "[]")
    string = string.replace(".", "..")
    string = string.replace("@", "@.")
    return string

data = read_input()
split = data.index("")
instructions = data[split + 1:]

grid = list(map(lambda x: list(replace_all(x)), data[: split]))
### expand this thing

rows, cols = len(grid), len(grid[0])
pos = (-1, -1)
for row in range(len(grid)):
    found = "".join(grid[row]).find("@")
    if found > -1:
        pos = row, found
    

def move(grid, r, c, direction):
    to_move = [("@", r, c)]
    assert grid[r][c] == "@"
    movable = True
    queue = [(r, c)]
    while queue:
        curr_r, curr_c = queue.pop(0)
        if direction == "^" or direction == "v":
            new_r = curr_r - 1 if direction == "^" else curr_r + 1
            if grid[new_r][curr_c] == "#":
                movable = False
            elif grid[new_r][curr_c] in "[]":
                
                queue.append((new_r, curr_c))
                candidate = ("]", new_r, curr_c + 1) if grid[new_r][curr_c] == "[" else ("[", new_r, curr_c - 1)
                queue.append(candidate[1:])
                to_move.extend([(grid[new_r][curr_c], new_r, curr_c), candidate])
        else:
            new_c = curr_c - 1 if direction == "<" else curr_c + 1
            if grid[curr_r][new_c] == "#":
                movable = False
            elif grid[curr_r][new_c] in "[]":
                to_move.append((grid[curr_r][new_c], curr_r, new_c))
                queue.append((curr_r, new_c))
    if movable:
        new_robot_coords = None
        for _, row, col in to_move:
            grid[row][col] = "."

        for char, row, col in to_move:
            next_r, next_col = None, None
            if direction == "^":
                next_r, next_col = row - 1, col
            elif direction == "<":
                next_r, next_col = row, col - 1
            elif direction == "v":
                next_r, next_col = row + 1, col  
            elif direction == ">":
                next_r, next_col = row, col + 1
            else:
                raise ValueError()
            
            grid[next_r][next_col] = char
            if char == "@":
                new_robot_coords = (next_r, next_col)

        return new_robot_coords
    else:
        return r, c


for line in instructions:
    for direction in line:
        pos = move(grid, pos[0], pos[1], direction)
        # print(direction)
        # for g in grid:
        #     print("".join(g))
        # print()

for g in grid:
    print("".join(g))
print()
i_really_hate_computing_these_values = 0
for i in range(rows):
    for j in range(cols):
        if grid[i][j] == "[":
            i_really_hate_computing_these_values += (i * 100) + j
            
print(i_really_hate_computing_these_values)
    
