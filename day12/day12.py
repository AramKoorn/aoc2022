from collections import deque

f = open("input.txt", "r")
lines = f.readlines()
lines = [l.split("\n") for l in lines]

# Create grid
grid = []
for i, x in enumerate(lines):

    if "S" in x[0]:
        start = (x[0].index("S"), i)
    grid.append([ord(x) if x != "E" else ord("z") + 1 for x in x[0]])
grid[0][0] = ord("a")

n = len(grid)
m = len(grid[0])

# implement BFS
stack = deque()
stack.append((0, start))
offset = ((0, 1), (1, 0), (-1, 0), (0, -1))
visited = set((0, 0))

while stack:
    cnt, cords = stack.popleft()

    if grid[cords[0]][cords[1]] == ord("z") + 1:
        print(cnt)
        break

    for x, y in offset:
        dx, dy = x + cords[0], y + cords[1]
        # check if inside the grid
        if 0 <= dx < n and 0 <= dy < m:
            if grid[dx][dy] - 1 <= grid[cords[0]][cords[1]]:
                if (dx, dy) not in visited:
                    stack.append((cnt + 1, (dx, dy)))
                    visited.add((dx, dy))

# Part 2
res = float("inf")
for i in range(n):
    for j in range(m):
        if grid[i][j] == ord("a"):
            start = (i, j)

            stack = deque()
            stack.append((0, start))
            offset = ((0, 1), (1, 0), (-1, 0), (0, -1))
            visited = set((0, 0))

            while stack:
                cnt, cords = stack.popleft()

                if grid[cords[0]][cords[1]] == ord("z") + 1:
                    res = min(res, cnt)
                    break

                for x, y in offset:
                    dx, dy = x + cords[0], y + cords[1]
                    # check if inside the grid
                    if 0 <= dx < n and 0 <= dy < m:
                        if grid[dx][dy] - 1 <= grid[cords[0]][cords[1]]:
                            if (dx, dy) not in visited:
                                stack.append((cnt + 1, (dx, dy)))
                                visited.add((dx, dy))

print(res)
