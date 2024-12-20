import os
import time

REQUIREMENT = 100
def read_input():
    path = os.path.dirname(os.path.realpath(__file__))
    data = open(f"{path}/input.txt", "r").read().strip().split("\n")
    return data
data = read_input()

start_time = time.time()
start, end = None, None
rows, cols = len(data), len(data[0])

for r in  range(len(data)):
    c1 =  data[r].find('S')
    c2 =  data[r].find('E')
    if c1 > -1:
        start = (r, c1)
    if c2 > -1:
        end = (r, c2)

def search(start):
    prev = {}
    q = []
    visited = [[False for _ in range(len(data))] for _ in range(len(data[0]))]
    visited[start[0]][start[1]] = True
    q.append(start)
    
    while q:
        r, c = q.pop(0)
        
        nbrs = [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]
        nbrs = [(r, c) for r, c in nbrs if data[r][c] in ".ES"]
        for newr, newc in nbrs:
            if not visited[newr][newc] and data[newr][newc]:
                visited[newr][newc] = True
                q.append((newr, newc))
                prev[(newr, newc)] = (r, c)
    return prev

prev = search(start)
print(end)     
curr = end
ls = [curr]
while curr in prev:
    curr = prev[curr]
    ls.append(curr)

ls = ls[::-1]

def im_ashamed_i_did_dijkstra(start):
    def in_bounds(r, c):
        return 0 <= r < rows and 0 <= c < cols
    dist = {}
    for i in range(-20, 21):
        for j in range(-20, 21):
            if abs(i) + abs(j) <= 20 and in_bounds(start[0] + i, start[1] + j):
                dist[(start[0] + i, start[1] + j)] = abs(i) + abs(j)
    return dist


num = 0
indices = {ls[i]: i for i in range(len(ls))}
for p in range(len(ls)):
    r, c = ls[p]
    d = im_ashamed_i_did_dijkstra((r, c))
    for rchble in d:
        if rchble in indices:
            idx = indices[rchble]
            diff = idx - p
            if diff - d[rchble] >= REQUIREMENT:
                num += 1

print(f"{time.time() - start_time} seconds elapsed") # ~5.2 seconds
print(num)