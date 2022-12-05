from collections import defaultdict
from copy import deepcopy


f = open("input.txt", "r")
lines = f.readlines()
lines = [x.strip('\n').split(",") for x in lines]
stacks = defaultdict(list)

ok = True
instructions = []

i_inst = 0
while ok:
    for x in lines:
        i_inst += 1
        if x == [""]:
            ok = False
            break
        for idx, i in enumerate(range(1, len(x[0]), 4)):
            val = x[0][i]
            if val != " ":
                stacks[idx].append(val)

for v in stacks.values():
    v.pop()
    v.reverse()

stacks2 = deepcopy(stacks)
# create list with instructions
for x in lines[i_inst:]:
    x = x[0].split(" ")
    instructions.append((int(x[1]), int(x[3]), int(x[5])))

# part 1
for moves, frm, to in instructions:
    for i in range(moves):
        crate = stacks[frm - 1].pop()
        stacks[to - 1].append(crate)

res = ""
for i in sorted(list(stacks)):
    res += stacks[i][-1]
print(res)


# part 2
for moves, frm, to in instructions:
    to_append = []
    for _ in range(moves):
        crate = stacks2[frm - 1].pop()
        to_append.append(crate)
    to_append.reverse()
    stacks2[to - 1] += to_append
    del to_append
    x = 2

res = ""
for i in sorted(list(stacks)):
    res += stacks2[i][-1]
print(res)
