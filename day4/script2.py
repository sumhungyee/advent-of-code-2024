import os

def read_input():
    path = os.path.dirname(os.path.realpath(__file__))
    data = open(f"{path}/input.txt", "r").read().strip().split("\n")
    return data

def search_2(i, j, matrix):
    count = 0
    if {matrix[i+1][j+1], matrix[i-1][j-1]} == {matrix[i-1][j+1], matrix[i+1][j-1]} == {"M", "S"}:
        count+=1
    
    return count

matrix = read_input()
r, c = len(matrix), len(matrix[0])
coords = [(i, j) for i in range(r) for j in range(c) if matrix[i][j] == "A" and (0 < i < r-1 and 0 < j < c-1)] # No need to check bounds here if you just count
cnt = 0
for coord in coords:
    cnt += search_2(coord[0], coord[1], matrix)

print(f"Total 'XMAS' occurrences: {cnt}")
