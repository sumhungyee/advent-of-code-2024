import os
def read_input():
    path = os.path.dirname(os.path.realpath(__file__))
    data = open(f"{path}/input.txt", "r").read().strip().split("\n")
    return data[:data.index("")][0].split(", "), data[data.index("") + 1:]
left, right = read_input()
constructible = {l: True for l in left}
constructible[""] = False
def check(can):
    if can not in constructible:
        for word in left:
            if can.endswith(word):
                remaining = can[:len(can) - len(word)]
                if check(remaining):
                    constructible[can] = True
                    return True
        constructible[can] = False
        return False
    else:
        return constructible[can]
    
naur = 0
for candidate in right:
    if check(candidate):
        naur+=1
        
print(naur)