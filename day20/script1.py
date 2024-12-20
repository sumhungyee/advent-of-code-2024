import os
import time

REQUIREMENT = 100
# YET ANOTHER GRID QUESTION, WHY

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
  #
 ###
#####
 ###
  #
def get_radius(r, c):
    rd = set()
    def in_bounds(r, c):
        return 0 <= r < rows and 0 <= c < cols
    # i guess it must really be a cheat
    steps = [(-1, 0), (1, 0), (0, 1), (0, -1)]
    for s in steps:
        step1 = (r + s[0], c + s[1])
        if data[step1[0]][step1[1]] == "#":
            for s2 in steps:
                step2 = (step1[0] + s2[0], step1[1] + s2[1])
                rd.add(step2)

    rd = {coord for coord in rd if in_bounds(*coord)}
    return rd

num = 0
for p in range(len(ls)):
    # p is my current idx
    r, c = ls[p]
    for nbr in get_radius(r, c):
        if nbr in ls:
            idx = ls.index(nbr)
            diff = idx - p
            if diff - 2 >= REQUIREMENT:
                # print(f"{nbr} OF {(r, c)}")
                num += 1

print(f"{time.time() - start_time} seconds elapsed")
print(num)