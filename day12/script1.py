import os

def read_input():
    path = os.path.dirname(os.path.realpath(__file__))
    data = open(f"{path}/input.txt", "r").read().strip().split("\n")
    return data

data = read_input()
rows, cols = len(data), len(data[0])

def valid(r, c, rows, cols, visited, curr_letter):
    return 0 <= r < rows and 0 <= c < cols and not (visited[r][c]) and (curr_letter == data[r][c])

def valid_boundary(r, c, rows, cols, curr_letter):
    return not (0 <= r < rows and 0 <= c < cols) or (curr_letter != data[r][c])

def get_regions():
    visited = [[False for _ in range(cols)] for _ in range(rows)]
    regions = []
    for i in range(rows):
        for j in range(cols):
            if visited[i][j]:
                continue
            region = []
            name = data[i][j]
            q = []
            q.append((name, i, j)) # r, c
            visited[i][j] = True
            while q:
                curr_letter, r, c = q.pop(0)
                region.append((r, c))
                if valid(r+1, c, rows, cols, visited, curr_letter):
                    q.append((data[r+1][c], r+1, c))
                    visited[r+1][c] = True
                if valid(r-1, c, rows, cols, visited, curr_letter):
                    q.append((data[r-1][c], r-1, c))
                    visited[r-1][c] = True
                if valid(r, c+1, rows, cols, visited, curr_letter):
                    q.append((data[r][c+1], r, c+1))
                    visited[r][c+1] = True
                if valid(r, c-1, rows, cols, visited, curr_letter):
                    q.append((data[r][c-1], r, c-1))
                    visited[r][c-1] = True

            regions.append((name, region))
    return regions

def get_perimeter(regions):
    perim = 0
    for region in regions:
        name, coords = region
        perimmini = 0
        for r, c in coords:
            perimmini += valid_boundary(r + 1, c, rows, cols, name) + valid_boundary(r - 1, c, rows, cols, name)\
            + valid_boundary(r, c + 1, rows, cols, name) + valid_boundary(r, c - 1, rows, cols, name)
        perim += perimmini * len(coords)
    return perim

regions = get_regions()
print(get_perimeter(regions))
