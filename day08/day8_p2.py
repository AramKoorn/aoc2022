from functools import reduce


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
        return 0

    if grid[i][move] < target:
        return f_horizontal(i, move, d, target) + 1
    else:
        return 1


def f_vertical(i, j, d, target):

    move = i + d

    if move == -1 or move == n or move == m:
        return 0

    if grid[move][j] < target:
        return f_vertical(move, j, d, target) + 1
    else:
        return 1


mx = float("-inf")
for i in range(1, n -1):
    for j in range(1, m - 1):
        views = []
        views.append(f_horizontal(i, j, -1, grid[i][j]))
        views.append(f_horizontal(i, j, 1, grid[i][j]))
        views.append(f_vertical(i, j, 1, grid[i][j]))
        views.append(f_vertical(i, j, -1, grid[i][j]))
        mx = max(mx, reduce(lambda x, y: x * y, views))

print(mx)

