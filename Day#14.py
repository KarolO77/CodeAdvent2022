with open('day14.txt') as file:
    data = [[list(map(int, e.split(","))) for e in i.split('->')]
            for i in file.read().splitlines()]

rocksPositions = set()
for line in data:
    oldX = line[0][0]
    oldY = line[0][1]
    for X, Y in line:
        rocksPositions.add((X, Y))
        if Y != oldY:
            for num in range(min(oldY, Y), max(oldY, Y)):
                rocksPositions.add((X, num))
        if X != oldX:
            for num in range(min(oldX, X), max(oldX, X)):
                rocksPositions.add((num, Y))
        oldX, oldY = X, Y

XS = [i[0] for i in rocksPositions]
YS = [i[1] for i in rocksPositions]
sandGrains = 0
border = max(YS)+1

while (500, 0) not in rocksPositions:
    X, Y = 500, 0
    while True:
        if Y == border:
            break
        if (X,Y+1) not in rocksPositions:
            Y += 1
        elif (X-1,Y+1) not in rocksPositions:
            X -= 1
            Y += 1
        elif (X+1,Y+1) not in rocksPositions:
            X += 1
            Y += 1
        else:
            break
    rocksPositions.add((X,Y))
    sandGrains += 1

print(sandGrains)