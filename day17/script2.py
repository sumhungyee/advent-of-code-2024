import os
import time

def read_input():
    path = os.path.dirname(os.path.realpath(__file__))
    data = open(f"{path}/input.txt", "r").read().strip().split("\n")
    left, right = data[:data.index("")], data[data.index("") + 1:]
    return left, right

def combo(operand):
    if operand < 4:
        return str(operand)
    elif operand == 4:
        return "a"
    elif operand == 5:
        return "b"
    else:
        return "c"

left, right = read_input()
inst = [int(j) for j in right[0].split(": ")[-1].split(",")]

l = [int(n[n.index(": ") + 2:]) for n in left]
variables = ["a", "b", "c", "ptr"]
ptr = 0
a, b, c = l
code = []
for i in range(0, len(inst) - 1, 2):
    opcode = inst[i]
    operand = inst[i+1]
    combo_result = combo(operand)
    
    match opcode:
        case 0:
            code.append(f"a = a >> {combo_result};ptr += 1")
        case 1:
            code.append(f"b = b ^ {operand};ptr += 1")
        case 2:
            code.append(f"b = {combo_result} & 0b111;ptr += 1")
        case 3:
            code.append(f"ptr = {operand // 2} if a != 0 else ptr + 1")
        case 4:
            code.append(f"b = b ^ c;ptr += 1")
        case 5:
            code.append(f"print({combo_result} & 0b111);ptr += 1")
        case 6:
            code.append(f"b = a >> {combo_result};ptr += 1")
        case 7:
            code.append(f"c = a >> {combo_result};ptr += 1")

while 0 <= ptr < len(code):
    print(f"INST: {code[ptr]}")
    exec(code[ptr])


######################################
# gotta read the printed code
# clearly, since the script has ended, a = 0 at the end
execution = [lin.split(";")[0] for lin in code]
for lin in execution:
    print(lin)

def simulate(inst, ans):
    if inst == []:
        return ans
    for t in range(8):
        a = (ans << 3) + t
        b = a & 0b111
        b = b ^ 1
        c = a >> b 
        b = b ^ 5
        b = b ^ c 
        a = a >> 3
        if (b & 0b111) == inst[-1]:
            nxt = simulate(inst[:-1], (ans << 3) + t)
            if not nxt:
                continue
            return nxt

print(simulate(inst, 0))


        


