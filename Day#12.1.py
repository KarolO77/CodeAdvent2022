from collections import deque

with open('day12.txt') as file:
    data = [[z for z in i] for i in file.read().strip().splitlines()]

for lineIndex, line in enumerate(data):
    for letterIndex, letter in enumerate(line):
        if letter == 'S':
            startRow = lineIndex
            startColumn = letterIndex
            data[lineIndex][letterIndex] = 'a'
        if letter == 'E':
            endRow = lineIndex
            endColumn = letterIndex
            data[lineIndex][letterIndex] = 'z'

allWays = deque()
allWays.append((0, startRow, startColumn))
visited = set((startRow, startColumn))

while allWays:
    length, row, column = allWays.popleft()
    for indexRow, indexColumn in [(row+1, column),(row-1, column),(row, column-1),(row, column+1)]:
        if indexRow >= len(data) or indexRow < 0 or indexColumn >= len(data[0]) or indexColumn < 0:
            continue
        if (indexRow, indexColumn) in visited:
            continue
        if ord(data[indexRow][indexColumn]) - ord(data[row][column]) > 1:
            continue
        if endRow == indexRow and endColumn == indexColumn:
            print(length+1)
            exit()

        visited.add((indexRow, indexColumn))
        allWays.append((length+1, indexRow, indexColumn))