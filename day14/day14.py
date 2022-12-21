from copy import deepcopy


f = open("input.txt", "r")
lines = f.readlines()
lines = [[x.split(",") for x in x.strip("\n").split(" -> ")] for x in lines]


rocks = set()
for x in lines:
    for i in range(len(x) - 1):
        # create points
        first = list(map(int, x[i]))
        second = list(map(int, x[i + 1]))

        # x cords are the same
        if first[0] == second[0]:
            xs = first[0]
            y = range(min(first[1], second[1]), max(first[1], second[1]) + 1)
            for i in y:
                rocks.add((xs, i))
        else:
            xs = range(min(first[0], second[0]), max(first[0], second[0]) + 1)
            y = first[1]
            for i in xs:
                rocks.add((i, y))


# For part 2
rocks2 = deepcopy(rocks)


max_depth = max([x[1] for x in list(rocks)])
sand = set()
def fall(x, y):
    # falling
    if (x, y) not in rocks:
        if y > max_depth:
            return True
        return fall(x, y + 1)
    # We hit a rock or sand
    else:
        if (x - 1, y) in rocks and (x + 1, y) in rocks:
            rocks.add((x, y - 1))
            sand.add((x, y - 1))
            return False
        elif (x, y) in rocks and (x - 1, y) not in rocks:
            return fall(x - 1, y)
        elif (x, y) in rocks and (x + 1, y) not in rocks:
            return fall(x + 1, y)


# # part 1
while True:
    void = fall(500, 0)
    # print_grid()
    if void:
        break
print(len(sand))

# part 2
max_depth += 2
xmin, xmax = min(rocks2)[0], max(rocks2)[0]
# 500 is arbitrary number could probably be much lower.
rocks = set([(x, max_depth) for x in range(xmin - 500, xmax + 500)] + list(rocks2))


while True:
    void = fall(500, 0)
    if (500, 0) in sand:
        break
print(len(sand))
