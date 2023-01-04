from collections import deque, defaultdict


f = open("input.txt", "r")
lines = f.readlines()
lines = [l.split("\n") for l in lines]


grid = []
for x in lines:
    grid.append([x for x in x[0]])


n = len(grid)
m = len(grid[0])


hor = m - 2
vert = n - 2

h_blizz = defaultdict(set)
v_blizz = defaultdict(set)
blizzards = defaultdict(set)


def plot_grid(idx):
    grid = [["." for x in range(m)] for x in range(n)]
    for i in range(n):
        for j in range(m):
            if i == 0 or i == n - 1:
                grid[i][j] = "#"
            if j == 0 or j == m - 1:
                grid[i][j] = "#"

    for d, cords in blizzards[idx]:
        i, j = cords
        if grid[i][j] == ".":
            grid[i][j] = d
        else:
            try:
                grid[i][j] += 1
            except:
                grid[i][j] = 2

    import numpy as np
    print(np.array(grid))


# initialize
for i in range(n):
    for j in range(m):
        if grid[i][j] == ">" or grid[i][j] == "<" or grid[i][j] == "v" or grid[i][j] == "^":
            blizzards[0].add((grid[i][j], (i, j)))


for i in range(max(vert, hor)):
    if blizzards[i] == set():
        for d, cords in blizzards[i - 1]:
            x, y = cords
            if d == "<":
                if grid[x][y - 1] != "#":
                    blizzards[i].add((d, (x, y - 1)))
                else:
                    blizzards[i].add((d, (x, hor)))
            if d == ">":
                if grid[x][y + 1] != "#":
                    blizzards[i].add((d, (x, y + 1)))
                else:
                    blizzards[i].add((d, (x, 1)))
            if d == "v":
                if grid[x + 1][y] != "#":
                    blizzards[i].add((d, (x + 1, y)))
                else:
                    blizzards[i].add((d, (1, y)))
            if d == "^":
                if grid[x - 1][y] != "#":
                    blizzards[i].add((d, (x - 1, y)))
                else:
                    blizzards[i].add((d, (vert, y)))


for k, v in blizzards.items():
    for d, cords in v:
        if d == "<" or d == ">":
            h_blizz[k].add(cords)
        else:
            v_blizz[k].add(cords)


# BFS
start = (0, grid[0].index("."))
end = (n - 1, grid[n - 1].index("."))


def inside(x, y):
    return 0 <= x < n and 0 <= y < m


def bfs(start, end, c):

    stack = deque([(c, start)])
    offset = ((0, 1), (1, 0), (-1, 0), (0, -1), (0, 0))
    visited = set()

    while stack:
        cnt, cords = stack.popleft()
        x, y = cords

        # position of blizzards at time cnt
        blizz = set(h_blizz[(cnt + 1) % hor] | v_blizz[(cnt + 1) % vert])

        if (x, y) == end:
            return cnt

        for dx, dy in offset:
            xnew = x + dx
            ynew = y + dy

            if not inside(xnew, ynew):
                continue

            if grid[xnew][ynew] != "#" and (cnt, (xnew, ynew)) not in visited and (xnew, ynew) not in blizz:
                stack.append([cnt + 1, (xnew, ynew)])
                visited.add((cnt, (xnew, ynew)))


first = bfs(start=start, end=end, c=0)
print(first)
second = bfs(start=end, end=start, c=first + 1)
print(second)
third = bfs(start=start, end=end, c=second + 1)
print(third)