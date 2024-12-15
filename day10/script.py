import os
from queue import Queue

def read_input():
    path = os.path.dirname(os.path.realpath(__file__))
    data = open(f"{path}/input.txt", "r").read().strip().split("\n")
    return data

def bfs(q, script = 1):
    routes = set()
    visitation = set()
    trails = 0
    # for part 1
    if script == 1:
        while not q.empty():
            n, x, y = q.get()
            
            if n == 9:
                routes.add((x, y))

            if x + 1 < rows and data[x + 1][y]== str(n + 1):
                visitation.add((x + 1, y))
                q.put((n + 1, x + 1, y))
            if x - 1 >= 0 and data[x - 1][y] == str(n + 1):
                visitation.add((x - 1, y))
                q.put((n + 1, x - 1, y))
            if y - 1 >= 0 and data[x][y - 1] == str(n + 1):
                visitation.add((x, y - 1))
                q.put((n + 1, x, y - 1))
            if y + 1 < cols and data[x][y + 1] == str(n + 1):
                visitation.add((x, y + 1)) 
                q.put((n + 1, x, y + 1))
        return len(routes)
    # for part 2
    else:
        trails = 0
        while not q.empty():
            n, x, y = q.get()
            
            if n == 9:
                trails += 1

            if x + 1 < rows and data[x + 1][y]== str(n + 1):
                visitation.add((x + 1, y))
                q.put((n + 1, x + 1, y))
            if x - 1 >= 0 and data[x - 1][y] == str(n + 1):
                visitation.add((x - 1, y))
                q.put((n + 1, x - 1, y))
            if y - 1 >= 0 and data[x][y - 1] == str(n + 1):
                visitation.add((x, y - 1))
                q.put((n + 1, x, y - 1))
            if y + 1 < cols and data[x][y + 1] == str(n + 1):
                visitation.add((x, y + 1)) 
                q.put((n + 1, x, y + 1))
        return trails


data = read_input()
q = Queue()
nines = []
rows, cols = len(data), len(data[0])
rs = 0
for i in range(rows):
    for j in range(cols):
        if data[i][j] == "0":
            q.put((0, i, j))
            rs += bfs(q)

print(rs)


