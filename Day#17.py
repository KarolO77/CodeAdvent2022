
with open("day17.txt") as file:
    movess = [i for i in "".join(file.read().splitlines())]
    moves = [i for i in ">>><<><>><<<>><>>><<<>>><<<><<<>><>><<>>"]
    

part1 = 2022
part2 = 1000

def give_next_move(mc):
    x = moves[mc]
    if x == ">":
        return 1
    elif x == "<":
        return -1

def solve(part):
    
    mc,pc = -1,0
    height = 0
    filled = {x - 1j for x in range(7)}
    patterns = [
                [0, 1, 2, 3],
                [1, 1j, 1 + 1j, 2 + 1j, 1 + 2j],
                [0, 1, 2, 2 + 1j, 2 + 2j],
                [0, 1j, 2j, 3j],
                [0, 1, 1j, 1 + 1j]
                ]

    for _ in range(part):

        module = {x + 2 + (height + 3) * 1j for x in patterns[pc]}

        while True:
            if mc == len(moves) - 1: mc = -1
            mc += 1

            move = give_next_move(mc)
            moved = {i + move for i in module}

            if all(0 <= x.real < 7 and x not in filled for x in moved): #will move left/right if any element of body doesnt hit the border
                module = moved
            if all(x - 1j not in filled for x in module): #will move down if it doesnt crush with sth
                module = {x - 1j for x in module}
            else: #instruction what should be done with module if he reach the floor or touch other module
                [filled.add(i) for i in module]
                height = int(max(filled, key=lambda x: x.imag).imag + 1)
                pc = (pc + 1) % 5
                break

    return height

#Answer 1: 3219
p1 = solve(part1)
print(p1)

part2 = 1000000000000 #1000^4

x = solve(len(moves))
y = solve(len(moves)*2)
z = solve(len(moves)*3)

print(x,y,z)
#idk 15151515151
#p2: 1514285714288