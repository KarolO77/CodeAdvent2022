with open('day9.txt') as file:
    data = [i.split() for i in file.read().strip().splitlines()]

board = [['.' for i in range(50)] for _ in range(50)]


directions = {'R':[1,0], 'L':[-1,0], 'U':[0,1], 'D':[0,-1]}
rope = [[11,15] for _ in range(10)]
visitedPositions = set()


for command in data:

    givenDirection, lengthOfMove = command[0], int(command[1])
    direction = directions[givenDirection]

    for _ in range(lengthOfMove):

        rope[0][0] += direction[0]
        rope[0][1] += direction[1]

        for section in range(len(rope)-1):
            H = rope[section]
            T = rope[section+1]

            dx = H[0] - T[0]
            dy = H[1] - T[1]

            if abs(dx) > 1 or abs(dy) > 1:
                if dx == 0:
                    T[1] += dy // 2
                elif dy == 0:
                    T[0] += dx // 2
                else:
                    T[0] += 1 if dx > 0 else -1
                    T[1] += 1 if dy > 0 else -1

        visitedPositions.add((T[0],T[1]))
print(len(visitedPositions))