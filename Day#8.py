with open('day8.txt') as file:
    grid = [i for i in file.read().strip().splitlines()]

o = 0
for i in grid:
    grid[o] = list(i)
    o += 1

visible_trees = 2*(len(grid)-2) + len(grid[0])*2
visible_lower_trees = 0
scores =[]

for row in range(1, len(grid)-1):
    for column in range(1, len(grid[0])-1):

        tree = grid[row][column]
        tree = int(tree)

        upper_trees = [grid[row-i][column] for i in range(1, row+1)]
        bottom_trees = [grid[row+i][column] for i in range(1, len(grid)-row)]
        left_trees = [grid[row][column-i] for i in range(1, column+1)]
        right_trees = [grid[row][column+i]
                       for i in range(1, len(grid[0])-column)]

        upmax = int(max(upper_trees))
        botmax = int(max(bottom_trees))
        leftmax = int(max(left_trees))
        rightmax = int(max(right_trees))

        if tree > upmax or tree > botmax or tree > rightmax or tree > leftmax:
            visible_trees += 1
        
        #part 2
        score = 1

        for lst in (upper_trees, bottom_trees, left_trees, right_trees):
            length_of_view = 0
            for i in range(len(lst)):
                ilst = int(lst[i])
                if ilst < tree:
                    length_of_view += 1
                elif ilst == tree:
                    length_of_view += 1
                    break
                else:
                    break
            score *= length_of_view

        scores.append(score)


print("Answer to part 1:", visible_trees)
print("Answer to part 2:", max(scores))