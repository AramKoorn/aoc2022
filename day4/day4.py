f = open("input.txt", "r")
lines = f.readlines()
lines = [x.strip('\n') for x in lines]
lines = [x.split(",") for x in lines]

# Part 1
res = 0
for l, r in lines:
    l = l.split("-")
    r = r.split("-")
    if int(l[0]) >= int(r[0]) and int(l[-1]) <= int(r[-1]):
        res += 1
        continue

    if int(r[0]) >= int(l[0]) and int(r[-1]) <= int(l[-1]):
        res += 1
        continue
print(res)

# part 2
res = 0
for l, r in lines:
    l = l.split("-")
    r = r.split("-")

    l = list(range(int(l[0]), int(l[-1]) + 1))
    r = list(range(int(r[0]), int(r[-1]) + 1))

    for x in l:
        if x in r:
            res += 1
            break

print(res)