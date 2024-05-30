import re

with open("day15.txt") as file:
    data = [i.strip() for i in file.read().splitlines()]

Y = 2000000

BeaconsInY = set()
rowY = set() #signals in Y

for line in data:
    SX, SY, BX, BY = map(int, re.findall(r"-?\d+", line))
    rangeOfSignal = abs(SX - BX) + abs(SY - BY)

    o = rangeOfSignal - abs(SY - Y) #difference of lens -- delta and SYtoY
    if o < 0:
        continue

    mX = SX - o
    pX = SX + o
    for x in range(mX, pX+1):
        rowY.add(x)

    if BY == Y:
        BeaconsInY.add((BX,BY))

result = len(rowY-BeaconsInY)
print(result)