with open("day18.txt") as file:
    data = [tuple([int(j) for j in i.split(",")]) for i in file.read().splitlines()]

sides = [(0,0,0.5),(0,0.5,0),(0.5,0,0),(0,0,-0.5),(0,-0.5,0),(-0.5,0,0)]
droplets = dict()

for dx,dy,dz in data: #droplet
    for x,y,z in sides: #checks the space around the droplet
        pos = (dx+x,dy+y,dz+z)
        if pos not in droplets:
            droplets[pos] = 0
        droplets[pos] += 1


result = list(droplets.values()).count(1)
print(result)

xlst = [i[0][0] for i in droplets.items()]
mx, Mx = int(min(xlst)+0.5), int(max(xlst)-0.5)

ylst = [i[0][1] for i in droplets.items()]
my, My = int(min(ylst)+0.5), int(max(ylst)-0.5)

zlst = [i[0][2] for i in droplets.items()]
mz, Mz = int(min(zlst)+0.5), int(max(zlst)-0.5)

print(f"    | x | y | z |")
print(f"min | {mx} | {my} | {mz} |")
print(f"max | {Mx} | {My} | {Mz} |")


air = set()
for x in range(mx,Mx):
    for y in range(my,My):
        for z in range(mz,Mz):
            air.add((x,y,z))

""" for bx,by,bz in air:
    c = 0
    for x,y,z in sides:
        if droplets.get((bx+x+0.5,by+y+0.5,bz+z+0.5)) == 1:
            c += 1
    if c == 6:
        result =- 6
    elif 0 < c:
        c  """


sort = sorted(droplets)
print(result)