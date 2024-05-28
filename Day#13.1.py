import json
with open('day13.txt') as file:
    data = [i for i in file.read().splitlines() if i != '']
    data = [json.loads(data[i]) for i in range(len(data))]
    data = [data[x:x+2] for x in range(0, len(data), 2)]

def func(x, y):
    if type(x) == int:
        if type(y) == int:
            return x - y
        else:
            return func([x], y)
    else:
        if type(y) == int:
            return func(x, [y])
    
    for a, b in zip(x, y):
        v = func(a, b)
        if v:
            return v
    
    return len(x) - len(y)

results = 0

for i, (a, b) in enumerate(data):
    if func(a, b) < 0:
        results += i + 1

print(results)