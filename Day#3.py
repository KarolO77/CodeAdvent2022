# rearranged - uporządkowane
# compartments - przedziały
# rucksack - plecak

with open('day3.txt') as file:
    rucksacks = [i for i in file.read().split("\n")]

valuesOfLetters = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5,
                   'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10,
                   'k': 11, 'l': 12, 'm': 13, 'n': 14, 'o': 15,
                   'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20,
                   'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25, 'z': 26,
                   'A': 27, 'B': 28, 'C': 29, 'D': 30, 'E': 31,
                   'F': 32, 'G': 33, 'H': 34, 'I': 35, 'J': 36,
                   'K': 37, 'L': 38, 'M': 39, 'N': 40, 'O': 41,
                   'P': 42, 'Q': 43, 'R': 44, 'S': 45, 'T': 46,
                   'U': 47, 'V': 48, 'W': 49, 'X': 50, 'Y': 51, 'Z': 52,
                   0: 0
                   }

total = 0

for rucksack in rucksacks:
    half = len(rucksack) // 2
    firstHalf = set(rucksack[:half])
    secondHalf = set(rucksack[half:])
    keyLetters = list(firstHalf.intersection(secondHalf))
    total += valuesOfLetters[keyLetters[0]]

print("Answer to part 1:", total)

# part 2

total = 0
k = 3

for element in range(0, len(rucksacks), 3):
    groupOfRucksacks = rucksacks[element:k]
    k += 3
    gor1 = set(groupOfRucksacks[0])
    gor2 = set(groupOfRucksacks[1])
    gor3 = set(groupOfRucksacks[2])
    firstChecking = gor1.intersection(gor2)
    finalChecking = firstChecking.intersection(gor3)
    keys = list(finalChecking)
    total += valuesOfLetters[keys[0]]

print("Answer to part 2:", total)
