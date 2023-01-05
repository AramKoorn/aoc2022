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


def move(curr, steps, part2=False):
    x, y = curr[1]
    d = curr[0]
    for step in range(steps):
        if d == ">":
            if y + 1 == m:
                if part2:
                    _d, _x, _y = rotate(d, x, y)
                    if grid[_x][_y] == "#":
                        return d, x, y
                    else:
                        d, x, y = _d, _x, _y
                x, y = teleport(d, x, y)
            elif grid[x][y + 1] == "#":
                return d, x, y
            elif grid[x][y + 1] == ".":
                y += 1
                continue
            #  we hit empty
            else:
                if part2:
                    _d, _x, _y = rotate(d, x, y)
                    if grid[_x][_y] == "#":
                        return d, x, y
                    else:
                        d, x, y = _d, _x, _y
                x, y = teleport(d, x, y)

        if d == "<":
            if y - 1 < 0:
                if part2:
                    _d, _x, _y = rotate(d, x, y)
                    if grid[_x][_y] == "#":
                        return d, x, y
                    else:
                        d, x, y = _d, _x, _y
                x, y = teleport(d, x, y)
            elif grid[x][y - 1] == "#":
                return d, x, y
            elif grid[x][y - 1] == ".":
                y -= 1
                continue
            #  we hit empty
            else:
                if part2:
                    _d, _x, _y = rotate(d, x, y)
                    if grid[_x][_y] == "#":
                        return d, x, y
                    else:
                        d, x, y = _d, _x, _y
                x, y = teleport(d, x, y)

        if d == "v":
            if x + 1 == n:
                if part2:
                    _d, _x, _y = rotate(d, x, y)
                    if grid[_x][_y] == "#":
                        return d, x, y
                    else:
                        d, x, y = _d, _x, _y
                x, y = teleport(d, x, y)
            elif grid[x + 1][y] == "#":
                return d, x, y
            elif grid[x + 1][y] == ".":
                x += 1
                continue
            else:
                if part2:
                    _d, _x, _y = rotate(d, x, y)
                    if grid[_x][_y] == "#":
                        return d, x, y
                    else:
                        d, x, y = _d, _x, _y
                x, y = teleport(d, x, y)
        if d == "^":
            if x - 1 < 0:
                if part2:
                    _d, _x, _y = rotate(d, x, y)
                    if grid[_x][_y] == "#":
                        return d, x, y
                    else:
                        d, x, y = _d, _x, _y
                x, y = teleport(d, x, y)
            elif grid[x - 1][y] == "#":
                return d, x, y
            elif grid[x - 1][y] == ".":
                x -= 1
                continue
            else:
                if part2:
                    _d, _x, _y = rotate(d, x, y)
                    if grid[_x][_y] == "#":
                        return d, x, y
                    else:
                        d, x, y = _d, _x, _y
                x, y = teleport(d, x, y)
    return d, x, y


def walk(start, part2=False):
    curr = start
    for i in instr:
        # print(curr)
        if i != "R" and i != "L":
            d, x, y = move(curr, i, part2=part2)
            curr = (d, (x, y))
        elif i == "L":
            idx = directions.index(curr[0])
            new_direction = directions[(idx - 1) % 4]
            curr = (new_direction, curr[1])
        else:
            idx = directions.index(curr[0])
            new_direction = directions[(idx + 1) % 4]
            curr = (new_direction, curr[1])

    facings = {">": 0, "v": 1, "<": 2, "^": 3}
    f = facings[curr[0]]
    r = curr[1][0] + 1
    c = curr[1][1] + 1
    # print(r, c)
    print(1000 * r + 4 * c + f)


def rotate(d, x, y):
    dx, dy = x % 50, y % 50
    f1, f2 = x // 50, y // 50

    # A to J
    if (f1, f2) == (0, 1) and d == "^":
        d = ">"
        x = 150 + dy
        y = 0

    # B to I
    elif (f1, f2) == (0, 2) and d == "^":
        d = "^"
        x = 199
        y = dy

    # from C to F
    elif (f1, f2) == (0, 2) and (d == ">"):
        d = "<"
        x = 149 - dx
        y = 99

    # From D to E
    elif (f1, f2) == (0, 2) and d == "v":
        d = "<"
        x = 50 + dy
        y = 99

    # From E to D
    elif (f1, f2) == (1, 1) and d == ">":
        d = "^"
        x = 49
        y = 100 + dx

    # From F to C
    elif (f1, f2) == (2, 1) and d == ">":
        d = "<"
        x = 49 - dx
        y = 149

    # From G to H
    elif (f1, f2) == (2, 1) and d == "v":
        d = "<"
        x = 150 + dy
        y = 49

    # From H to G
    elif (f1, f2) == (3, 0) and d == ">":
        d = "^"
        x = 149
        y = 50 + dx

    # From I to B
    elif (f1, f2) == (3, 0) and d == "v":
        d = "v"
        x = 0
        y = 100 + dy

    # From J to A
    elif (f1, f2) == (3, 0) and d == "<":
        d = "v"
        x = 0
        y = 50 + dx

    # from K to N
    elif (f1, f2) == (2, 0) and d == "<":
        d = ">"
        x = 49 - dx
        y = 50

    # from L to M
    elif (f1, f2) == (2, 0) and d == "^":
        d = ">"
        x = 50 + dy
        y = 50
    # from M to L
    elif (f1, f2) == (1, 1) and d == "<":
        d = "v"
        x = 100
        y = dx
    # From N to K
    elif (f1, f2) == (0, 1) and d == "<":
        x = 149 - dx
        y = 0
        d = ">"
    else:
        raise ValueError("No match")

    return d, x, y


walk(start=curr)
walk(start=curr, part2=True)
