with open("day2.txt") as file:
    rounds = [i for i in file.read().strip().split("\n")]

countedPoints = 0
countedPointsPt2 = 0

results = {
    "A X": 4,
    "A Y": 8,
    "A Z": 3,
    "B X": 1,
    "B Y": 5,
    "B Z": 9,
    "C X": 7,
    "C Y": 2,
    "C Z": 6,
}

for round in rounds:
    countedPoints += results[round]


resultsPt2 = {
    "A X": 3,
    "A Y": 4,
    "A Z": 8,
    "B X": 1,
    "B Y": 5,
    "B Z": 9,
    "C X": 2,
    "C Y": 6,
    "C Z": 7,
}

for round in rounds:
    countedPointsPt2 += resultsPt2[round]


print("Answer to pt1:", countedPoints)
print("Answer to pt2:", countedPointsPt2)
