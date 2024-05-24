with open("day10.txt") as file:
    data = [i.strip().split() for i in file.read().splitlines()]

cycle = 0
X = 1
result = 0

for line in data:
    command = line[0]
    amount = line[-1]
    cycle += 1

    if (cycle - 19) % 40 == 0:
        result += X + X * cycle

    if command == 'addx':
        cycle += 1
        X += int(amount)
        if (cycle - 19) % 40 == 0:
            result += X + X * cycle

print(result)