f = open("input.txt", "r")
lines = f.readlines()
lines = [l.split("\n") for l in lines]

grid = []
for x in lines:
    grid.append([int(x) for x in x[0]])

n = len(grid)
m = len(grid[0])


def f_horizontal(i, j, d, target):

    move = j + d
    if move == -1 or move == n or move == m:
        return 1

    if grid[i][move] >= target:
        return 0
    else:
        return f_horizontal(i, move, d, target)


def f_vertical(i, j, d, target):

    move = i + d
    if move == -1 or move == n or move == m:
        return 1

    if grid[move][j] >= target:
        return 0
    else:
        return f_vertical(move, j, d, target)

res = 0
for i in range(n):
    for j in range(m):
        # look left
        if f_horizontal(i, j, -1, grid[i][j]) == 1:
            res += 1
            continue
        # look  right
        if f_horizontal(i, j, 1, grid[i][j]) == 1:
            res += 1
            continue
        # look up
        if f_vertical(i, j, 1, grid[i][j]) == 1:
            res += 1
            continue
        # look down
        if f_vertical(i, j, -1, grid[i][j]) == 1:
            res += 1
            continue
print(res)