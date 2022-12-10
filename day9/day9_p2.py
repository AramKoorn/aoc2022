from collections import defaultdict


f = open("input.txt", "r")
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
    # Diagonal Logic: first move same direction as prev node and then close gap 
    else:
        if h[0] > t[0] and h[1] > t[1]:
            t = (t[0] + 1, t[1] + 1)
            t = tuple(map(int, t))
            paths[k + 1].append(t)
            update_tail(d, k + 1)
        if h[0] > t[0] and h[1] < t[1]:
            t = (t[0] + 1, t[1] - 1)
            t = tuple(map(int, t))
            paths[k + 1].append(t)
            update_tail(d, k + 1)
        if h[0] < t[0] and h[1] < t[1]:
            t = (t[0] - 1, t[1] - 1)
            t = tuple(map(int, t))
            paths[k + 1].append(t)
            update_tail(d, k + 1)
        if h[0] < t[0] and h[1] > t[1]:
            t = (t[0] - 1, t[1] + 1)
            t = tuple(map(int, t))
            paths[k + 1].append(t)
            update_tail(d, k + 1)
    return


for d, steps in lines:
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
            x = 2

    if d == "U":
        for i in range(steps):
            h = paths[0][-1]
            h = (h[0], h[1] + 1)
            paths[0].append(h)
            update_tail(d, 0)
            x = 2

    if d == "D":
        for i in range(steps):
            h = paths[0][-1]
            h = (h[0], h[1] - 1)
            paths[0].append(h)
            update_tail(d, 0)

print(len(set(paths[9])))