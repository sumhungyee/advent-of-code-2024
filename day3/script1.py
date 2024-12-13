import os
import re
def read_input_raw():
    path = os.path.dirname(os.path.realpath(__file__))
    data = open(f'{path}/input.txt', 'r').read().strip()
    return data

data = read_input_raw()
funcs = re.findall(r'mul\(\d{1,3},\d{1,3}\)', data)
evaluated = [(lambda x, y: int(x)*int(y))(*re.findall(r'\d+', exp)) for exp in funcs]
print(sum(evaluated))
