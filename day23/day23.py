import numpy as np
from collections import Counter


PLOT = False

f = open("input.txt", "r")
lines = f.readlines()
lines = [l.split("\n") for l in lines]

grid = []
for x in lines:
    grid.append([x for x in x[0]])

n = len(grid)
m = len(grid[0])

elves = set()
print(np.array(grid))

for i in reversed(range(n)):
    for j in range(m):
        if grid[i][j] == "#":
            test = 2
            elves.add((j, m - 1 - i))

def plot():
    import matplotlib.pyplot as plt
    plt.scatter(x=[x[0] for x in elves], y=[x[1] for x in elves])
    plt.grid()
    plt.show()


n_elves = len(elves)

order = ["N", 'S', "W", "E"]


def direction(cords, rnd):

    x, y = cords

    for idx in range(rnd, rnd + 4):

        if rnd == 9:
            test = 2
        d = order[idx % 4]

        if d == "N":
            a = (x, y + 1)
            b = (x - 1, y + 1)
            c = (x + 1, y + 1)

        elif d == "S":
            a = (x, y - 1)
            b = (x - 1, y - 1)
            c = (x + 1, y - 1)

        elif d == "W":
            a = (x - 1, y)
            b = (x - 1, y - 1)
            c = (x - 1, y + 1)

        elif d == "E":
            a = (x + 1, y)
            b = (x + 1, y - 1)
            c = (x + 1, y + 1)
        else:
            raise KeyError("No direction")

        if a not in elves and b not in elves and c not in elves:
            proposals.add((cords, a))
            return


def check_move(cords):
    offset = ((1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (-1, 1), (1, -1), (-1, -1))
    for dx, dy in offset:
        if (cords[0] + dx, cords[1] + dy) in elves:
            return True
    return False


def simulate(rounds):

    for rnd in range(rounds):

        # draw grid
        if PLOT:
            plot()
        assert len(elves) == n_elves

        global proposals
        proposals = set()
        # print(proposals)

        for e in elves:
            if check_move(e):
                direction(e, rnd)

        # remove all proposals that go to same point
        # print(proposals)
        moves = [x[1] for x in proposals]
        c = Counter(moves)
        for k, v in c.items():
            if v > 1:
                proposals = [x for x in proposals if x[1] != k]
        if len(proposals) == 0:
            print(rnd + 1)
            return

        # move all elves

        while len(proposals) > 0:
            e, cords = proposals.pop()
            elves.remove(e)
            elves.add(cords)

    empty = n_empty()
    print(empty)


def n_empty():

    xmin = min(x[0] for x in elves)
    xmax = max(x[0] for x in elves) + 1
    ymin = min(x[1] for x in elves)
    ymax = max(x[1] for x in elves) + 1

    return abs(xmax - xmin) * abs(ymax - ymin) - len(elves)


#part 1
# simulate(rounds=10)

#part 2
simulate(rounds=1000)



