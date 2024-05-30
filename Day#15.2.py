import re

with open("day15.txt") as file:
    data = [i.strip() for i in file.read().splitlines()]

mini,maxi = 0,4000000

grid = [["." for _ in range(30)] for l in range(30)]
ids = {}

for Y in range(maxi+1):
    intervals = []

    for line in data:
        SX, SY, BX, BY = map(int, re.findall(r"-?\d+", line))
        rangeOfSignal = abs(SX - BX) + abs(SY - BY)
        ysDifference = rangeOfSignal - abs(SY-Y)

        if ysDifference < 0: continue

        lx = SX - ysDifference
        hx = SX + ysDifference

        intervals.append((lx,hx)) #adding the range on its x

    intervals.sort()

    q = []

    for low, high in intervals:
        if not q:
            q.append([low,high])
            continue
            
        qlow, qhigh = q[-1]

        if low > qhigh + 1:
            q.append([low,high])
            continue

        q[-1][1] = max(qhigh, high)
    
    x = 0
    for low, high in q:
        if x < low:
            print(x * maxi + Y)
            exit()
        x = max(x,high+1)
        if x > maxi:
            break

