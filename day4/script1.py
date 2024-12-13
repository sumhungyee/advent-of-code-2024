import os

def read_input():
    path = os.path.dirname(os.path.realpath(__file__))
    data = open(f"{path}/input.txt", "r").read().strip().split("\n")
    return data

def is_in_bounds(i, j, rows, cols):
    return 0 <= i < rows and 0 <= j < cols

def search(i, j, matrix):
    count = 0
    rows, cols = len(matrix), len(matrix[0])
    directions = [
        (0, 1),   
        (0, -1),  
        (1, 0),   
        (-1, 0),  
        (1, 1),   
        (-1, 1),  
        (1, -1),  
        (-1, -1), 
    ]
    target = "MAS"

    for dx, dy in directions:
        found = True
        for t in range(3):
            ni, nj = i + dx * (t + 1), j + dy * (t + 1)
            if not is_in_bounds(ni, nj, rows, cols) or matrix[ni][nj] != target[t]:
                found = False
                break
        if found:
            count += 1

    return count

matrix = read_input()
r, c = len(matrix), len(matrix[0])
coords = [(i, j) for i in range(r) for j in range(c) if matrix[i][j] == "A"]
cnt = 0
for coord in coords:
    cnt += search(coord[0], coord[1], matrix)

print(f"Total 'XMAS' occurrences: {cnt}")
