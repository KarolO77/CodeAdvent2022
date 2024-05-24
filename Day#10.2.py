from math import ceil

with open("day10.txt") as file:
    data = [i.strip().split() for i in file.read().splitlines()]

X = 1
cycle, result, multipleFourty = 0, 0, 0    #multipleForty for correct index
image = [list(' '*40) for _ in range(6)]   #Image to print for part 2
pattern = list('###'+' '*37)               #Used in part 2 to see where ### are after addx

for line in data:

    command = line[0]
    amount = line[-1]
    pattern =  (X-1)*" " + "###" + (38-X)*" "

    if command == 'noop':
        cycle += 1

        if cycle % 40 == 0:
            result += X * cycle
            pattern = list('###'+' '*37)
            multipleFourty += 40

        curRow = image[int(ceil(cycle/40))-1]
        curIndex = cycle - multipleFourty - 1

        if pattern[curIndex] == '#':
            curRow[curIndex] = '#'
        elif pattern[curIndex] == ' ':
            curRow[curIndex] = ' '


    if command == 'addx':
        for _ in range(2):
            cycle += 1

            if cycle % 40 == 0:
                result += X * cycle
                pattern = list('###'+' '*37)
                multipleFourty += 40

            curRow = image[int(ceil(cycle/40))-1]
            curIndex = cycle - multipleFourty - 1

            if pattern[curIndex] == '#':
                curRow[curIndex] = '#'
            elif pattern[curIndex] == ' ':
                curRow[curIndex] = ' '

        X += int(amount)


[print("".join(i)) for i in image]