import os
def read_input():
    path = os.path.dirname(os.path.realpath(__file__))
    data = open(f'{path}/input.txt', 'r').read().strip().split('\n')
    return data


data = [line.split() for line in read_input()]
safenum = 0
for report in data:
    numport = [int(num) for num in report]
    window = [numport[i+1] - numport[i] for i in range(len(numport) - 1)]
    flag = [num > 0 and abs(num) < 4 for num in window]
    negflag = [num < 0 and abs(num) < 4 for num in window]
    if sum(flag) == len(window) or sum(negflag) == len(window):
        safenum += 1
    

print(safenum)