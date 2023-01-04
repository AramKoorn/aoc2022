import re

f = open("input.txt")
lines = f.readlines()
lines = [x.strip("\n") for x in lines]
grid = [[x for x in l] + [" " for _ in range(150 - len(l))] for l in lines[:-2]]
print(grid)

instr = lines[-1]
instr = re.split('(\d+)', instr)[1:-1]
instr = [int(x) if x.isdigit() else x for x in instr]
print(instr)

n = len(grid)
m = len(grid[0])

directions = [">", "v", "<", "^"]

curr = (">", (0, grid[0].index(".")))


def teleport(d, x, y):

    if d == ">":
        i = 0
        while True:
            if grid[x][i] == " ":
                i += 1
                continue
            elif grid[x][i] == ".":
                return x, i
            if grid[x][i] == "#":
                return x, y

    if d == "<":
        i = m - 1
        while True:
            if grid[x][i] == " ":
                i -= 1
                continue
            elif grid[x][i] == ".":
                return x, i
            if grid[x][i] == "#":
                return x, y

    if d == "v":
        i = 0
        while True:
            if grid[i][y] == " ":
                i += 1
                continue
            elif grid[i][y] == ".":
                return i, y
            if grid[i][y] == "#":
                return x, y
    if d == "^":
        i = n - 1
        if i == 199:
            test = 2
        while True:
            if grid[i][y] == " ":
                i -= 1
                continue
            elif grid[i][y] == ".":
                return i, y
            if grid[i][y] == "#":
                return x, y
    return x, y


def move(curr, steps):
    x, y = curr[1]
    d = curr[0]
    for step in range(steps):
        if d == ">":
            if y + 1 == m:
                x, y = teleport(d, x, y)
            elif grid[x][y + 1] == "#":
                return x, y
            elif grid[x][y + 1] == ".":
                y += 1
                continue
            #  we hit empty
            else:
                x, y = teleport(d, x, y)

        if d == "<":
            if y - 1 < 0:
                x, y = teleport(d, x, y)
            elif grid[x][y - 1] == "#":
                return x, y
            elif grid[x][y - 1] == ".":
                y -= 1
                continue
            #  we hit empty
            else:
                x, y = teleport(d, x, y)

        if d == "v":
            if x + 1 == n:
                x, y = teleport(d, x, y)
            elif grid[x + 1][y] == "#":
                return x, y
            elif grid[x + 1][y] == ".":
                x += 1
                continue
            else:
                x, y = teleport(d, x, y)
        if d == "^":
            if x - 1 < 0:
                x, y = teleport(d, x, y)
            elif grid[x - 1][y] == "#":
                return x, y
            elif grid[x - 1][y] == ".":
                x -= 1
                continue
            else:
                x, y = teleport(d, x, y)
    return x, y


for i in instr:
    print(curr)
    if i != "R" and i != "L":
        x, y = move(curr, i)
        curr = (curr[0], (x, y))
    elif i == "L":
        idx = directions.index(curr[0])
        new_direction = directions[(idx - 1) % 4]
        curr = (new_direction, curr[1])
    else:
        idx = directions.index(curr[0])
        new_direction = directions[(idx + 1) % 4]
        curr = (new_direction, curr[1])
    # print(curr)

facings = {">": 0, "v": 1, "<": 2, "^": 3}
f = facings[curr[0]]
r = curr[1][0] + 1
c = curr[1][1] + 1
print(r, c)
print(1000 * r + 4 * c + f)






