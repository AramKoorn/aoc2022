from collections import defaultdict
import numpy as np
np.set_printoptions(linewidth=np.inf)

f = open("input_test2.txt", "r")
lines = f.readlines()
lines = [x.strip('\n').split(" ") for x in lines]
lines = [[x, int(y)] for x, y in lines]


paths = defaultdict(list)

# 0 is head
# 9 is tail
knots = list(range(10))
for i in knots:
    paths[i].append((0, 0))

def update_tail(d, k, diagonal=False):

    if k == 9:
        return

    h = paths[k][-1]
    t = paths[k + 1][-1]

    # Check overlapping
    if h == t:
        return

    # Check if same height
    if t[1] == h[1]:
        if abs(h[0] - t[0]) > 1:
            t = ((int(h[0] + t[0]) / 2), h[1])
            t = tuple(map(int, t))
            paths[k + 1].append(t)
            update_tail(d, k + 1)
            return
        else:
            return

    # Check same column
    if t[0] == h[0]:
        if abs(h[1] - t[1]) > 1:
            t = (t[0], int((h[1] + t[1]) / 2))
            t = tuple(map(int, t))
            paths[k + 1].append(t)
            update_tail(d, k + 1)
            return
        else:
            return

    # Not same row and column (so move diagonally)
    # Check if distance is still 1
    if abs(h[0] - t[0]) == 1 and abs(h[1] - t[1]) == 1:
        return
    else:
        if not diagonal:
            if d == "U":
                t = (h[0], h[1] - 1)
                paths[k + 1].append(t)
            if d == "D":
                t = (h[0], h[1] + 1)
                paths[k + 1].append(t)
            if d == "L":
                t = (h[0] + 1, h[1])
                paths[k + 1].append(t)
            if d == "R":
                t = (h[0] - 1, h[1])
                paths[k + 1].append(t)
            update_tail(d, k + 1, True)
        # move the same direction as previous knot
        else:
            if d == "U":
                t = ((t[0] + h[0]) / 2, t[1] + 1)
                t = tuple(map(int, t))
                paths[k + 1].append(t)
                update_tail(d, k + 1, True)

            if d == "D":
                t = ((t[0] + h[0]) / 2, t[1] - 1)
                t = tuple(map(int, t))
                paths[k + 1].append(t)
                update_tail(d, k + 1, True)

            if d == "L":
                t = (t[0] - 1, (t[1] + h[1]) / 2)
                t = tuple(map(int, t))
                paths[k + 1].append(t)
                update_tail(d, k + 1, True)

            if d == "R":
                t = (t[0] + 1, (t[1] + h[1]) / 2)
                t = tuple(map(int, t))
                paths[k + 1].append(t)
                update_tail(d, k + 1, True)

    return


s = (16, 12)
def print_grid(n=22, m=26):
    grid = [["." for x in range(m)] for x in range(n)]
    for k, v in paths.items():
        x, y = v[-1]
        if grid[s[0] - 1 - y][s[1] + x] == ".":
            grid[s[0] - 1 - y][s[1] + x] = k

    print(np.array(grid))
    print("\n")

# def print_grid():
#     return


for d, steps in lines:
    print_grid()
    if d == "L" and steps == 8:
        x = 2
    if d == "R":
        for i in range(steps):
            h = paths[0][-1]
            h = (h[0] + 1, (h[1]))
            paths[0].append(h)
            update_tail(d, 0)
            # print_grid()

    if d == "L":
        for i in range(steps):
            h = paths[0][-1]
            h = (h[0] - 1, h[1])
            paths[0].append(h)
            update_tail(d, 0)
            print_grid()
            x = 2

    if d == "U":
        for i in range(steps):
            h = paths[0][-1]
            h = (h[0], h[1] + 1)
            paths[0].append(h)
            update_tail(d, 0)
            print_grid()
            x = 2

    if d == "D":
        for i in range(steps):
            h = paths[0][-1]
            h = (h[0], h[1] - 1)
            paths[0].append(h)
            update_tail(d, 0)

print_grid()
print(len(set(paths[9])))