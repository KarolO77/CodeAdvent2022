with open("day1.txt") as file:
    data = [
        i for i in file.read().strip().split("\n")
    ]  # func strip usuwa niepotrzebne spacje z przodu i z tyłu elementu


maximum = 0
maximum2 = 0
maximum3 = 0
suma = 0

for item in data:
    if item == "":
        suma = 0
    else:
        num = int(item)
        suma += num

    if suma > maximum:
        maximum = suma
    elif suma > maximum2:
        maximum2 = suma
    elif suma > maximum3:
        maximum3 = suma

top3 = maximum + maximum2 + maximum3

print(maximum)
print(top3)
