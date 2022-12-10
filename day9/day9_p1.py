f = open("input.txt", "r")
lines = f.readlines()
lines = [x.strip('\n').split(" ") for x in lines]
lines = [[x, int(y)] for x, y in lines]

trace = []
t_t = set()

h, t = (0, 0), (0, 0),


def update_tail(h, t, d):

    # Check overlapping
    if h == t:
        return t

    # Check if same height
    if t[1] == h[1]:
        if abs(h[0] - t[0]) > 1:
            t = ((int(h[0] + t[0]) / 2), h[1])
            t = tuple(map(int, t))
            return t
        else:
            return t

    # Check same column
    if t[0] == h[0]:
        if abs(h[1] - t[1]) > 1:
            t = (t[0], int((h[1] + t[1]) / 2))
            t = tuple(map(int, t))
            return t
        else:
            return t

    # Not same row and column (so move diagonally)
    # Check if distance is still 1
    if abs(h[0] - t[0]) == 1 and abs(h[1] - t[1]) == 1:
        return t
    else:
        if d == "U":
            t = (h[0], h[1] - 1)
        if d == "D":
            t = (h[0], h[1] + 1)
        if d == "L":
            t = (h[0] + 1, h[1])
        if d == "R":
            t = (h[0] - 1, h[1])
    return t


for d, steps in lines:
    if d == "R":
        for i in range(steps):
            h = (h[0] + 1, (h[1]))
            t = update_tail(h, t, d)
            t_t.add(t)
            trace.append(h)

    if d == "L":
        for i in range(steps):
            h = (h[0] - 1, h[1])
            t = update_tail(h, t, d)
            trace.append(h)
            t_t.add(t)

    if d == "U":
        for i in range(steps):
            h = (h[0], h[1] + 1)
            t = update_tail(h, t, d)
            t_t.add(t)
            trace.append(h)

    if d == "D":
        for i in range(steps):
            h = (h[0], h[1] - 1)
            t = update_tail(h, t, d)
            t_t.add(t)
            trace.append(h)

print(len(t_t))

