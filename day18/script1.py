import os
from queue import PriorityQueue

ROWS, COLS = 71, 71
def read_input():
    path = os.path.dirname(os.path.realpath(__file__))
    data = open(f"{path}/input.txt", "r").read().strip().split("\n")
    return [tuple(map(int, d.split(","))) for d in data]
data = read_input()

graph = [["." for _ in range(COLS)] for _ in range(ROWS)]
fallen = data[:1024]
for f in fallen:
    x, y = f
    graph[y][x] = "#"

for r in graph:
    print("".join(r))

def djikstra(s_loc, graph):
    q = PriorityQueue()
    dist = dict()
    prev = dict()
    dist[s_loc] = 0
    q.put((0, s_loc))
    
    for y in range(ROWS):
        for x in range(COLS):
            if  (x, y) != s_loc and graph[y][x] == ".":
                dist[(x, y)] = float("inf")
                prev[(x, y)] = []
                    
    while not q.empty():
        tup = q.get()[1]
        x, y = tup
        nbrs = nbrs = [(i, j) for i, j in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)] if 0 <= i < COLS and 0 <= j < ROWS]
        nbrs = [coord for coord in nbrs if graph[coord[1]][coord[0]] == "."]
        for nbr in nbrs:
            alt = dist[(x, y)] + 1
            if alt < dist[nbr]:
                prev[nbr] = [(x, y)]
                dist[nbr] = alt
                q.put((alt, nbr))

            elif alt == dist[nbr]:
                prev[nbr].append((x, y))

    return dist, prev

dist, prev = djikstra((0, 0), graph)
end = (COLS - 1, ROWS - 1)
print(dist[end])
