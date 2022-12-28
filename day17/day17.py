f = open("input.txt", "r")
lines = f.readlines()
instructions = [[i for i in x.strip("\n")] for x in lines][0]
print(instructions)

'''
Part 2 hacky really hacky. Steps


CODE ONLY WORKS FOR THIS SPECIFIC INPUT DATA 
- find pattern cycle by looking at the detlas (mix of manually looking at sequence and let code find the pattern)
- if we know what the cycle pattern is we can quite easily findt the answer analytically for large N

'''

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
goal = 6000
cycle = []

while t < goal:

    cycle.append(start)

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

deltas = []
# part 2 get delta
for i in range(1, len(cycle)):
    deltas.append(cycle[i] - cycle[i -1])

deltas
find_pattern = [0, 0, 1, 2, 1, 2, 2, 1, 3, 0, 2, 2, 0, 0, 3, 4, 2, 1, 3, 2, 4, 0, 1]

# find where cycle starts
# for i in range(len(deltas)):
#     cnt = 0
#     ok = False
#     for j in range(len(find_pattern)):
#         if deltas[i + j] == find_pattern[j]:
#             cnt += 1
#         if cnt == len(find_pattern):
#             start_cycle = i
#             print(f"cycle {i}")
#             ok = True
#             cnt = 0
    # if ok:
    #     break
# Just manually looking at the delta and see if there is a recurrent cycle
print(f" cycles: {deltas[1433:3158]}")
assert deltas[1433: 3158] == deltas[3158: 4883]
cycle = [4, 0, 1, 2, 3, 0, 1, 1, 3, 2, 2, 0, 0, 2, 3, 4, 0, 1, 2, 1, 2, 0, 1, 2, 1, 2, 0, 1, 3, 2, 0, 0, 1, 3, 3]  # cycle for test input
cycle = deltas[1433:3158]
new_goal = 1000000000000

remaining = new_goal - goal
full_cycles = remaining // len(cycle)
left = remaining % len(cycle)


answer = start + (full_cycles * sum(cycle))

start_cycle = float("inf")
# find where cycle starts
for i in range(len(deltas)):
    cnt = 0
    ok = False
    for j in range(len(cycle)):
        if deltas[i + j] == cycle[j]:
            # print(cnt)
            cnt += 1
        if cnt == len(cycle):
            start_cycle = i
            ok = True
            cnt = 0
    if ok:
        break


print(f"cycle starts at: {start_cycle}")
at_cycle = ((new_goal - left) - start_cycle) % len(cycle)
print(f"at cycle: {at_cycle} and the length {len(cycle)} and left {left}")
# answer += sum(cycle[at_cycle: at_cycle + left])
# answer = ((goal - left) - at_cycle) % len(cycle)

for i in range(left):
    idx = (at_cycle + i) % len(cycle)
    answer += cycle[idx]
print(answer)
# 1541449275365
