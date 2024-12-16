import os
import numpy as np
import re

def read_input():
    path = os.path.dirname(os.path.realpath(__file__))
    data = open(f"{path}/input.txt", "r").read().strip().split("\n")
    data = list(map(lambda x: [int(j) for j in re.findall("\d+", x)], data))
    data.append([])
    problems = []
    for i in range(len(data)):
        if i % 4 == 0:
            problem = [data[i]]
        elif i % 4 < 3:
            problem.append(data[i])
        else:
            matrix = np.column_stack([problem[0], problem[1]])
            final = np.array(problem[2])
            problems.append(np.linalg.solve(matrix, final))

    return problems

solutions = read_input()
tok = 0
for sol in solutions:
    if np.all(abs(sol - np.round(sol).astype(int)) < 1e-5):
        tok += 3 * sol[0] + sol[1]
print(int(tok))