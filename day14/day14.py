f = open("input_test.txt", "r")
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

def print_grid():
    norm = min(list(rocks))[0]
    cords = [(x - norm, y) for x, y in list(rocks)]
    sand_cords = [(x - norm, y) for x, y in list(sand)]
    grid = [["." for x in range(10)] for x in range(10)]

    # Draw rocks
    for x, y in cords:
        grid[y][x] = "#"

    for x, y in sand_cords:
        grid[y][x] = "0"
    # draw sand
    import numpy as np
    print(np.array(grid))



max_depth = max([x[1] for x in list(rocks)])
sand = set()

def fall(x, y):
    # falling
    if (x, y) not in rocks:
        if y > max_depth:
            return
        return fall(x, y + 1)
    # We hit a rock or sand
    else:
        if (x - 1, y) in rocks and (x + 1, y) in rocks:
            rocks.add((x, y - 1))
            sand.add((x, y - 1))
            print_grid()
            return fall(500, 0)
        elif (x, y) in rocks and (x - 1, y) not in rocks:
            return fall(x - 1, y)
        elif (x, y) in rocks and (x + 1, y) not in rocks:
            return fall(x + 1, y)
        else:
            return


fall(500, 0)
print(sand)
print(len(sand))

