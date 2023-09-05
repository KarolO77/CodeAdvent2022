stacks = [
    ['Q', 'F', 'L', 'S', 'R'],
    ['T', 'P', 'G', 'Q', 'Z', 'N'],
    ['B', 'Q', 'M', 'S'],
    ['Q', 'B', 'C', 'H', 'J', 'Z', 'G', 'T'],
    ['S', 'F', 'N', 'B', 'M', 'H', 'P'],
    ['G', 'V', 'L', 'S', 'N', 'Q', 'C', 'P'],
    ['F', 'C', 'W'],
    ['M', 'P', 'V', 'W', 'Z', 'G', 'H', 'Q'],
    ['R', 'N', 'C', 'L', 'D', 'Z', 'G']
]


with open('day5.txt') as file:
    data = [i for i in file.read().strip().split("\n")]


for command in data:
    command = command.split(' ')
    for i in reversed(command):
        if i.isnumeric() == False:
            command.remove(i)
        else:
            continue

    crate_number = int(command[0])
    from_stack = int(command[1])
    to_stack = int(command[2])

    crates = stacks[from_stack-1][:crate_number]
    crates.reverse()
    for crate in crates:
        stacks[from_stack-1].remove(crate)
        stacks[to_stack-1].insert(0, crate)

for stack in stacks:
    print(stack[0], end='')

"""
            [Q]     [G]     [M]    
            [B] [S] [V]     [P] [R]
    [T]     [C] [F] [L]     [V] [N]
[Q] [P]     [H] [N] [S]     [W] [C]
[F] [G] [B] [J] [B] [N]     [Z] [L]
[L] [Q] [Q] [Z] [M] [Q] [F] [G] [D]
[S] [Z] [M] [G] [H] [C] [C] [H] [Z]
[R] [N] [S] [T] [P] [P] [W] [Q] [G]
 1   2   3   4   5   6   7   8   9 

['1', '2', '6']
['3', '7', '9']
['7', '9', '4']
['2', '5', '3']
['3', '2', '8']
['14', '4', '5']
['1', '2', '1']
"""
