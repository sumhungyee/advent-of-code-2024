import os
def read_input():
    path = os.path.dirname(os.path.realpath(__file__))
    data = open(f"{path}/input.txt", "r").read().strip().split("\n")
    return data[:data.index("")][0].split(", "), data[data.index("") + 1:]
left, right = read_input()

constructible = {}
constructible[""] = 0
def check(can):
    if can not in constructible:
        constructible[can] = 0
        for word in left:
            if can.endswith(word):
                remaining = can[:len(can) - len(word)]
                number = check(remaining)
                constructible[can] += number
        return constructible[can]
    else:
        return constructible[can]

ll = sorted([(len(l), l) for l in left], key=lambda x: x[0])

minlen = ll[0][0]
blocks = []
while ll:
    length, out = ll.pop(0)
    if length == minlen:
        constructible[out] = 1
    else:
        constructible[out] = check(out) + 1

naur = 0
for candidate in right:
    num = check(candidate)
    naur += num
print(naur)