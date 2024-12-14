import os

def read_input():
    path = os.path.dirname(os.path.realpath(__file__))
    data = open(f"{path}/input.txt", "r").read().strip().split("\n")
    return data

def toposort(adjlist: dict):
    vertices = adjlist.keys()
    indeg = {k: 0 for k in vertices}
    for key in vertices:
        for out in adjlist[key]:
            indeg[out] += 1
    queue = [v for v in vertices if indeg[v] == 0]
    result = []
    while queue:
        vertex = queue.pop(0)
        result.append(vertex)
        for item in adjlist[vertex]:
            indeg[item] -= 1
            if indeg[item] <= 0:
                indeg[item] = 0
                queue.append(item)
    return result

data = read_input()
idx = data.index("")
first, second = data[0: idx], data[idx + 1: ]


total = 0
ordered_set = dict()
for order in first:
    k, v = order.split("|")
    if k not in ordered_set:
        ordered_set[k] = [v]
    else:
        ordered_set[k].append(v)

for line in second:
    correct = True
    nums = line.split(",")
    reduced_ordered_set = {k: [idx for idx in v if idx in nums] for k, v in ordered_set.items() if k in nums}
    curr = nums[0]
    for i in range(1, len(nums)):
        if nums[i] not in reduced_ordered_set[curr]:
            correct = False
            break
        curr = nums[i]

    if not correct:
        ls = toposort(reduced_ordered_set)
        total += int(ls[len(ls) // 2])
print(total)

