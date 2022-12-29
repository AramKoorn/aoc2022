from collections import deque


f = open("input.txt", "r")
lines = f.readlines()
points = [tuple(map(int, x.strip('\n').split(","))) for x in lines]


def find_neighbours(x, y, z):
    cords = [(x + 1, y, z), (x - 1, y, z), (x, y + 1, z), (x, y - 1, z), (x, y, z + 1), (x, y, z - 1)]

    cnt = 0
    for p in cords:
        if p not in points:
            cnt += 1
    return cnt


# part 1
cnt = 0
for x, y, z in points:
    cnt += find_neighbours(x, y, z)
print(cnt)


def show(xmax, ymax, zmax, points):

    """ Render a visualisation of our droplet """
    import numpy as np
    import matplotlib.pyplot as plt
    from mpl_toolkits.mplot3d import Axes3D  # noqa: F401 unused import

    axes = [xmax + 1, ymax + 1, zmax + 1]  # set bounds

    grid = np.zeros(axes, dtype=np.int8)  # Initialise 3d grid to empty
    for x, y, z in points:  # set our array to filled for all filled cubes
        grid[x, y, z] = 1

    facecolors = np.where(grid == 1, 'red', 'black')

    # Plot figure
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.voxels(grid, facecolors=facecolors, edgecolors="grey", alpha=0.3)
    ax.set_aspect('equal')
    # plt.axis("off")
    plt.show()


xmax = max(points, key=lambda x: x[0])[0] + 1
xmin = min(points, key=lambda x: x[0])[0] - 1

ymax = max(points, key=lambda x: x[1])[1] + 1
ymin = min(points, key=lambda x: x[1])[1] - 1

zmax = max(points, key=lambda x: x[2])[2] + 1
zmin = min(points, key=lambda x: x[2])[2] - 1

show(xmax, ymax, zmax, points)


'''
1. put a box around the cubes
2. Fill the box with water (use BFS)
3. Total surface area are all sides touched by the water
'''

seen = set()
stack = deque()
start = (xmax, ymax, zmax)
stack.append(start)


def check_inside(x, y, z):
    return x >= xmin and x <= xmax and y >= ymin and y <= ymax and z >= zmin and z <= zmax


offset = ((1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1))
while len(stack) > 0:
    _x, _y, _z = stack.popleft()

    for dx, dy, dz in offset:
        x = _x + dx
        y = _y + dy
        z = _z + dz

        if (x, y, z) not in points and (x, y, z) not in seen and check_inside(x, y, z):
            stack.append((x, y, z))
            seen.add((x, y, z))


# look at all sides that touch the water
def find_neighbours(x, y, z):
    cords = [(x + 1, y, z), (x - 1, y, z), (x, y + 1, z), (x, y - 1, z), (x, y, z + 1), (x, y, z - 1)]

    cnt = 0
    for p in cords:
        if p in points:
            cnt += 1
    return cnt


cnt = 0
for x, y, z in seen:
    cnt += find_neighbours(x, y, z)
print(cnt)
