import os
import re
def read_input_raw():
    path = os.path.dirname(os.path.realpath(__file__))
    data = open(f'{path}/input.txt', 'r').read().strip()
    return data

data = read_input_raw()
funcs = re.findall(r"mul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\)", data)
toggle = True
funcs2 = []
for e in funcs:
    if e.startswith("do()"):
        toggle = True
    elif e.startswith("don't()"):
        toggle = False
    elif toggle:
        funcs2.append(e)

evaluated = [(lambda x, y: int(x)*int(y))(*re.findall(r'\d+', exp)) for exp in funcs2]
print(sum(evaluated))
