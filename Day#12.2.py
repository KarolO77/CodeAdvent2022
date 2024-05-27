from collections import deque

with open('day12.txt') as file:
    data = [[z for z in i] for i in file.read().strip().splitlines()]

allWays = deque()
visited = set()

for lineIndex, line in enumerate(data):
    for letterIndex, letter in enumerate(line):
        if letter == 'S':
            data[lineIndex][letterIndex] = 'a'
        if letter == 'E':
            endRow = lineIndex
            endColumn = letterIndex
            data[lineIndex][letterIndex] = 'z'
            visited.add((endRow,endColumn))
            allWays.append((0,endRow,endColumn))

while allWays:
    length, row, column = allWays.popleft()
    for indexRow, indexColumn in [(row+1, column),(row-1, column),(row, column-1),(row, column+1)]:
        if indexRow >= len(data) or indexRow < 0 or indexColumn >= len(data[0]) or indexColumn < 0:
            continue
        if (indexRow, indexColumn) in visited:
            continue
        if ord(data[row][column]) - ord(data[indexRow][indexColumn]) > 1:
            continue
        if data[indexRow][indexColumn] == 'a':
            print(length+1)
            exit()
        visited.add((indexRow, indexColumn))
        allWays.append((length+1, indexRow, indexColumn))