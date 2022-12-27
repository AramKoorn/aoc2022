f = open("input_test.txt", "r")
lines = f.readlines()
instructions = [[i for i in x.strip("\n")] for x in lines][0]
print(instructions)


def draw_shape(shape, start):
    if shape == 0:
        '''
        ####
        '''
        cords = set([(x, start) for x in range(2, 6)])

    if shape == 1:
        '''
        .#.
        ###
        .#.
        '''
        start += 2
        cords = set([(3, start), (3, start - 1), (3, start - 2),  (2, start - 1), (4, start - 1)])

    if shape == 2:
        '''
        '''
        start += 2
        cords = set([(4, start), (4, start - 1), (4, start - 2),  (3, start - 2), (2, start - 2)])

    if shape == 3:

        '''
        #
        #
        #
        #
        '''
        start += 3
        cords = set([(2, start), (2, start - 1), (2, start - 2), (2, start - 3)])

    if shape == 4:
        '''
        ##
        ##
        '''
        start += 1
        cords = set([(2, start), (3, start), (2, start - 1), (3, start - 1)])

    return cords


def update_cords(shape, direction=">"):
    # print(shape)

    # print(f"moving {direction}")
    if direction == ">":
        upd = [(x + 1, y) for x, y in shape]
        for x, y in upd:
            if x > 6 or (x, y) in floor:
                return shape, False
        return set(upd), True

    if direction == "<":
        upd = [(x - 1, y) for x, y in shape]
        for x, y in upd:
            if x < 0 or (x, y) in floor:
                return shape, False
        return set(upd), True

    if direction == "v":
        upd = [(x, y - 1) for x, y in shape]
        # print(upd)
        # print(floor)
        for x, y in upd:
            if (x, y) in floor:
                return shape, False
        return set(upd), True


def update_floor(floor):

    points = sorted(floor, key= lambda x: (x[0], x[1]))
    for i in range(len(points) - 1):
        curr = points[i]
        if curr[0] == points[i + 1][0]:
            # remove from points
            floor = floor - {points[i]}

    return floor, max(floor, key= lambda x: x[1])[1]

# do simulation
floor = set([(i, 0) for i in range(7)])
start = 0
shape = 0
n_i = 0
t = 0
goal = 2022


while t < goal:

    t += 1
    start += 4
    # get shape
    cords = draw_shape(shape=shape, start=start)

    while True:

        # gas push
        cords, _ = update_cords(shape=cords, direction=instructions[n_i])
        n_i += 1
        if n_i == len(instructions):
            n_i = 0

        # move down if possible
        cords, moved = update_cords(shape=cords, direction="v")
        # print(cords)

        if not moved:
            break

    shape += 1
    if shape == 5:
        shape = 0

    # update floor
    floor = floor.union(cords)
    height = max(floor, key=lambda x: x[1])[1]
    #
    d_height = height - start
    start = height


print(start)
