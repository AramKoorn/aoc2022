f = open("input.txt", "r")
lines = f.readlines()
lines = [x.strip('\n') for x in lines]
lines = [x.split(",") for x in lines]

# Part 1
res = 0
for l, r in lines:
    l = list(map(int, l.split("-")))
    r = list(map(int, r.split("-")))

    if l[0] >= r[0] and l[-1] <= r[-1] or r[0] >= l[0] and r[-1] <= l[-1]:
        res += 1
print(res)

# part 2
res = 0
for l, r in lines:
    l = list(map(int, l.split("-")))
    r = list(map(int, r.split("-")))

    l = range(l[0], l[-1] + 1)
    r = range(r[0], r[-1] + 1)

    if len(set(l) & set(r)) > 0:
        res += 1

print(res)