import os 

def read_input():
    path = os.path.dirname(os.path.realpath(__file__))
    data = open(f'{path}/input.txt', 'r').read().strip().split('\n')
    return data


data = read_input()
loc1, loc2 = zip(*list(map(lambda line: [int(e) for e in line.split()], data)))
loc1 = sorted(list(loc1))
loc2 = sorted(list(loc2))
print(sum([abs(loc1[i] - loc2[i]) for i in range(len(loc1))]))

