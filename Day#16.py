import re
with open("day16.txt") as file:
    pattern = r"[A-Z0-9]+"
    data = [re.findall(pattern,i)[1:] for i in file.read().splitlines()]

minutes = 30
valves = {i[0]:i[1] for i in data}
tunnels = {i[0]:i[2:] for i in data}
distances = {}



while minutes > 0:
    flow,valve = data[1],data[0]
    minutes -= 1


for valve in valves:
    if valve != "AA" and valves[valve]:
        continue


print(valves)
print(tunnels)
#tbc