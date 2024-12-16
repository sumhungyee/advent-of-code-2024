import os

def read_input():
    path = os.path.dirname(os.path.realpath(__file__))
    data = open(f"{path}/input.txt", "r").read().strip().split("\n")
    return data

data = read_input()[0].split()
things = {int(k): 1 for k in data}

def add_dict(things, item, repeats):
    if item in things:
        things[item] += repeats
    else:
        things[item] = repeats

def remove_dict(things, item, repeats):
    if things[item] > repeats:
        things[item] -= repeats
    else:
        del things[item]

for i in range(int(input("Steps: "))):
    items =  things.items()
    items = list(items).copy()
    for k, v in items:
        remove_dict(things, k, v)
        if k == 0:
            add_dict(things, 1, v)
        elif len(str(k)) % 2 == 0:
            string = str(k)
            k1 = string[:len(string) // 2]
            k2 = string[len(string) // 2:]
  
            add_dict(things, int(k1), v)
            add_dict(things, int(k2), v)
        else:
            add_dict(things, k * 2024, v)

print(sum(v for _, v in things.items()))