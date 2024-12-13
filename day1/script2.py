import os 

def read_input():
    path = os.path.dirname(os.path.realpath(__file__))
    data = open(f'{path}/input.txt', 'r').read().strip().split('\n')
    return data

data = read_input()
loc1, loc2 = zip(*list(map(lambda line: [int(e) for e in line.split()], data)))

print(sum([num * loc2.count(num) for num in loc1]))
