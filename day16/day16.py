import re
from scipy.sparse.csgraph import floyd_warshall
from functools import cache
from itertools import chain, combinations

'''
some testing how I can make memoization work with sets

@cache
def add(z=frozenset({1, 2, 3}), i=5):
    print(i)
    if i == 0:
        return sum(z)
    return add(z - {4}, i= i - 1)

x = add()
'''


f = open("input.txt", "r")
lines = f.readlines()

lines = [x.strip('\n').replace("Valve ", "").replace("has flow rate=", "").replace("; tunnels lead to ", "").replace("; tunnel leads to ", "") for x in lines]
lines = [re.split("valves? ", x) for x in lines]

data = []
for l in lines:
    l1 = l[0].split(" ")
    l1[1] = int(l1[1])
    data.append(l1 + [[x.strip() for x in l[1].split(",")]])

connections = {k: v for k, _, v in data}
lookup = {x: i for i, (x, y, z) in enumerate(data)}
flow_rates = {v: f for v, f, _ in data}

# create matrix for all the shortest paths
graph = [[0 for x in range(len(lookup))] for x in range(len(lookup))]
for valve, idx in lookup.items():
    for v in connections[valve]:
        graph[idx][lookup[v]] = 1
shortest = floyd_warshall(graph)


def find_shortest(frm, to):
    frm_idx = lookup[frm]
    to_idx = lookup[to]
    return int(shortest[frm_idx][to_idx])

# Only consider flow rate > 0
cand = set([v for v, f, _ in data if f > 0])

@cache
def flows_part1(curr="AA", steps=30, valves=frozenset({"DD", "BB", "JJ", "HH", "EE", "CC"})):

    if steps < 1:
        return 0

    res = 0

    for v in valves:
        res = max(res, flow_rates[v] * (steps - find_shortest(curr, v) - 1) + flows_part1(curr=v,
                                                                                          steps=steps - find_shortest(
                                                                                              curr, v) - 1,
                                                                                          valves=valves - {v}))

    return res

'''
part 1
'''
print(flows_part1(valves=frozenset(cand)))


def remaining_valves(valves):
    return frozenset(cand - valves)

'''
Logic: if I know that we only have to open the valves [A, B, C]. Then we only have to figure out the distribution
of valves opened by whom. So we have to explore the following configuration.

([A, B, C], []), ([A, B], [C]), ([A], [B, C]), ([], [A, B, C] 

for example
ele = frozenset({"DD", "HH", "EE"})  -> we know from the test that the this is the optimal set for the elephant
person = remaining_valves(ele)
print(flows_part1(valves=ele, steps=26) + flows_part1(valves=person, steps=26))  # should print 1707
'''


def powerset(iterable):
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(1, len(s)+1))

'''
Unfortunately I couldn't make part 2 work to fully using lru_cache (lru_cache(maxsize=None) == cache). 
I'm not using memoization for all the possible subsets. Will revisit this later. 

'''
res = 0
for subs in list(powerset(cand)):
    ele = frozenset(set(subs))
    person = remaining_valves(ele)
    res = max(res, flows_part1(valves=ele, steps=26) + flows_part1(valves=person, steps=26))
print(res)
