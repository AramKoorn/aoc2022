import re
from functools import cache


f = open("input.txt")
lines = f.readlines()
blueprints = [list(map(int, re.findall( "-?\d+", l))) for l in lines]
print(blueprints)


@cache
def dfs(t=24, minerals=(0, 0, 0, 0), robots=(1, 0, 0, 0)):

    ore, clay, obs, geode = minerals
    r_1, r_2, r_3, r_4 = robots

    global mx
    global f_geode

    if t == 0:
        # prev = mx
        mx = max(mx, minerals[3])
        # if mx > prev:
        #     print(mx)
        return

    # kill branch if we can't beat best case scenario
    if t * robots[3] + ((t - 1) * t / 2) + minerals[3] <= mx:
        return

    if (24 - t) > f_geode and robots[3] == 0:
        return

    for r, c in r_costs.items():

        if r == "ore" and ore >= c:
            minerals = (ore - c + robots[0], clay + robots[1], obs + robots[2], geode + robots[3])
            rob = (r_1 + 1, r_2, r_3, r_4)
            dfs(t - 1, minerals=minerals, robots=rob)
        elif r == "clay" and ore >= c:
            minerals = (ore + robots[0] - c, clay + robots[1], obs + robots[2], geode + robots[3])
            rob = (r_1, r_2 + 1, r_3, r_4)
            dfs(t - 1, minerals=minerals, robots=rob)
        elif r == "obsidian" and ore >= c[0] and clay >= c[1]:
            minerals = (ore + robots[0] - c[0], clay - c[1] + robots[1], obs + robots[2], geode + robots[3])
            rob = (r_1, r_2, r_3 + 1, r_4)
            dfs(t - 1, minerals=minerals, robots=rob)
        elif r == "geode" and ore >= c[0] and obs >= c[1]:
            f_geode = min(24 - t, f_geode)
            minerals = (ore + robots[0] - c[0], clay + robots[1], obs - c[1] + robots[2], geode + robots[3])
            rob = (r_1, r_2, r_3, r_4 + 1)
            dfs(t - 1, minerals=minerals, robots=rob)
        else:
            minerals = (ore + robots[0], clay + robots[1], obs + robots[2], geode + robots[3])
            rob = (r_1, r_2, r_3, r_4)
            dfs(t - 1, minerals=minerals, robots=rob)
    return


# Part 1
res = 0
for i, b in enumerate(blueprints):
    print(i)
    r_costs = {"ore": b[1], "clay": b[2], "obsidian": b[3:5], "geode": b[5:7]}

    minerals = (0, 0, 0, 0)
    robots = (1, 0, 0, 0)

    mx = 0
    f_geode = float("inf")
    dfs(t=24, minerals=minerals, robots=robots)
    print(mx)
    dfs.cache_clear()
    res += mx * (i + 1)
print(res)

# # Part 2
res = 1
for i, b in enumerate(blueprints[:3]):
    print(i)
    r_costs = {"ore": b[1], "clay": b[2], "obsidian": b[3:5], "geode": b[5:7]}

    minerals = (0, 0, 0, 0)
    robots = (1, 0, 0, 0)

    mx = 0
    f_geode = float("inf")
    dfs(t=32, minerals=minerals, robots=robots)
    res *= mx
    dfs.cache_clear()
print(res)
