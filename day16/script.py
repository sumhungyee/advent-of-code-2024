import os
import re
from queue import PriorityQueue 

def read_input():
    path = os.path.dirname(os.path.realpath(__file__))
    data = open(f"{path}/input.txt", "r").read().strip().split("\n")
    return data

data = read_input()
graph = [data.copy() for _ in range(4)]
s_loc = None
e_locs = []
for i in range(4):
    d = graph[i]
    for r_num in range(len(d)):
        if "S" in d[r_num]:
            s_loc = (0, r_num, d[r_num].index("S"))
            d[r_num] = d[r_num].replace("S", ".")
        if "E" in d[r_num]:
            e_locs.append((i, r_num, d[r_num].index("E")))
            d[r_num] = d[r_num].replace("E", ".")
    graph[i] = list(d)

def djikstra(s_loc, graph):
    q = PriorityQueue()
    dist = dict()
    prev = dict()
    dist[s_loc] = 0
    q.put((0, s_loc))
    for i in range(4):
        for r in range(len(graph[i])):
            for c in range(len(graph[i][r])):
                if (i, r, c) != s_loc and graph[i][r][c] == ".":
                    dist[(i, r, c)] = float("inf")
                    prev[(i, r, c)] = []
                    
    while not q.empty():
        tup = q.get()[1]
        i, r, c = tup
        verts = [((i + 1) % 4, r, c), ((i - 1) % 4, r, c)]
        for vertical in verts:
            alt = dist[(i, r, c)] + 1000
            if alt < dist[vertical]:
                prev[vertical] = [(i, r, c)]
                dist[vertical] = alt
                q.put((alt, vertical))

            elif alt == dist[vertical]:
                prev[vertical].append((i, r, c))

        if i == 0:
            nxt = (i, r, c + 1)
        elif i == 1:
            nxt = (i, r + 1, c)
        elif i == 2:
            nxt = (i, r, c - 1)
        else:
            nxt = (i, r - 1, c)
        if graph[nxt[0]][nxt[1]][nxt[2]] == ".":
            alt = dist[(i, r, c)] + 1
            if alt < dist[nxt]:
                prev[nxt] = [(i, r, c)]
                dist[nxt] = alt
                q.put((alt, nxt))
            elif alt == dist[nxt]:
                prev[nxt].append((i, r, c))

    return dist, prev

dist, prev = djikstra(s_loc, graph)
min_dist = min([dist[e_loc] for e_loc in e_locs])
print(min_dist)
            
good_dest = [dest for dest in e_locs if dist[dest] == min_dist]


path_items = [s_loc[1:]]
for dest in good_dest:
    pred = [dest]
    while s_loc not in pred:
        next_pred = []
        for p in pred:
            path_items.append(p[1:])
            next_pred.extend(prev[p])
        pred = next_pred

print(len(set(path_items)))
