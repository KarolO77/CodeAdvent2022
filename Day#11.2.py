import re
with open('day11.txt') as file:
    data = [i.strip() for i in file.read().strip().splitlines() if i != '']
    Monkeys = [data[x:x+6] for x in range(0, len(data), 6)]

for Monkey in Monkeys:
    Monkey[0] = "".join(re.findall(r'[a-zA-Z0-9]', Monkey[0]))
    Monkey[1] = [int(i) for i in "".join(re.findall(r'[0-9 ]', Monkey[1])).split()]
    Monkey[2] = (re.findall(r'= .*', Monkey[2])[0][2:]).split()
    Monkey[3] = int("".join(re.findall(r'[0-9]', Monkey[3])))
    Monkey[4] = int("".join(re.findall(r'[0-9]', Monkey[4])))
    Monkey[5] = int("".join(re.findall(r'[0-9]', Monkey[5])))

monkeyScores = {f'Monkey{i}':0 for i in range(8)}

# 1-items, 2-new, 3-division, 4-TrueTest, 5-FalseTest

dividers = [Monkey[3] for Monkey in Monkeys]
divider = 1
for ele in dividers: divider *= ele

for Round in range(10000):
    for Monkey in Monkeys:

        if len(Monkey[1]) == 0:
            continue

        for item in Monkey[1]:
            monkeyScores[Monkey[0]] += 1
            if Monkey[2][1] == '+':
                if Monkey[2][2] == 'old':
                    new = item*2
                else:
                    new = item + int(Monkey[2][2])
            elif Monkey[2][1] == '*':
                if Monkey[2][2] == 'old':
                    new = item**2
                else:
                    new = item * int(Monkey[2][2])

            new = new % divider

            if new % Monkey[3] == 0:
                Monkeys[Monkey[4]][1].append(new)
            else:
                Monkeys[Monkey[5]][1].append(new)

        Monkey[1] = []

sortedScores = sorted(monkeyScores.items(), key=lambda x:x[1])
result = sortedScores[-1][1] * sortedScores[-2][1]
print(result)