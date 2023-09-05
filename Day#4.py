with open("day4.txt") as file:
    data = [i for i in file.read().strip().split("\n")]

total = 0

for section in data:
    p1, p2 = section.split(",")
    p1 = [int(i) for i in p1.split("-")]
    p2 = [int(i) for i in p2.split("-")]
    if p1[0] <= p2[0] and p1[1] >= p2[1]:
        total += 1
    elif p1[0] >= p2[0] and p1[1] <= p2[1]:
        total += 1

print("Answer to part 1: ", total)


"part 2"

total = 0

for section in data:
    p1, p2 = section.split(",")
    p1 = [int(i) for i in p1.split("-")]
    p2 = [int(i) for i in p2.split("-")]
    if p1[0] in range(p2[0], p2[1] + 1) or p1[1] in range(p2[0], p2[1] + 1):
        total += 1
    elif p2[0] in range(p1[0], p1[1] + 1) or p2[1] in range(p1[0], p1[1] + 1):
        total += 1

print("Answer to part 2: ", total)
