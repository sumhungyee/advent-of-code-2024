import os

def read_input():
    path = os.path.dirname(os.path.realpath(__file__))
    data = open(f"{path}/input.txt", "r").read().strip().split("\n")
    return data



d = dict()
data = read_input()
antinodes = set()
rows, cols = len(data), len(data[0])
for i in range(len(data)):
    for j in range(len(data[i])):
        if data[i][j] != ".":
            if data[i][j] not in d:
                d[data[i][j]] = [(i, j)]
            else:
                d[data[i][j]].append((i, j))
for key in d:
    coords = d[key]
    for p1 in coords:
        for p2 in coords:
            if p1 != p2:
                dx = p2[0] - p1[0]
                dy = p2[1] - p1[1]
                antinodes.add((p2[0] + dx, p2[1] + dy)) if -1 < p2[0] + dx < cols and -1 < p2[1] + dy < rows else ...

print(len(antinodes))
