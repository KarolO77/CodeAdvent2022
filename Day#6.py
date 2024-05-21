with open("day6.txt") as file:
    data = [i for i in file.read().strip().splitlines()]
    data = "".join(data)
    data = [i for i in data]

for i in range(4, len(data)):
    storage = set(data[(i - 4) : i])
    if len(storage) == 4:
        print("Answer to part 1:", i)
        break

for i in range(14, len(data)):
    storage = set(data[(i - 14) : i])
    if len(storage) == 14:
        print("Answer to part 2:", i)
        break
