with open('day9.txt') as file:
    data = [i.split() for i in file.read().strip().splitlines()]

head_pos = [0,0]
tail_pos = [0,0]
all_ele_pos = set()

directions = {'R':[1,0], 'L':[-1,0], 'U':[0,1], 'D':[0,-1]}

for i in data:

    direction = i[0]
    len_of_move = int("".join(i[1:]))
    present_move = directions[direction]
    
    for i in range(len_of_move):
        head_pos[0] = head_pos[0] + present_move[0]
        head_pos[1] = head_pos[1] + present_move[1]

        dx = head_pos[0] - tail_pos[0]
        dy = head_pos[1] - tail_pos[1]

        if dx >= 2 or dx <= -2 or dy >= 2 or dy <= -2:
            dx = max(-1, min(1, dx))
            dy = max(-1, min(1, dy))
            tail_pos[0] += dx
            tail_pos[1] += dy

        all_ele_pos.add((tail_pos[0], tail_pos[1]))

print("Answer to part 1:", len(all_ele_pos))