with open('day13.txt') as file:
    data = list(map(eval, file.read().split()))

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

i2 = 1
i6 = 2

for i in data:
    if func(i, [[2]]) < 0:
        i2 += 1
        i6 += 1
    elif func(i, [[6]]) < 0:
        i6 += 1
        
print(i2 * i6)