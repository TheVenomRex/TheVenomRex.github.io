grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]

xCoord = range(len(grid))
yCoord = range(len(grid[0])) # I don't want to do it like this
                             # but I don't know how to do it dynamicly

for y in yCoord:
    print("\n")
    for x in xCoord:
        print(grid[x][y], end="")

