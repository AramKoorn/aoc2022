from copy import deepcopy


f = open("input.txt")
lines = f.readlines()
seq = [int(x.strip("\n")) for x in lines]
n = len(seq)


def mix(d):
    l = deepcopy(d)
    for i in range(n):

        (idx, val) = [x for x in l if x[0] == i][0]
        idx = l.index((idx, val))
        l.pop(idx)
        l.insert((idx + val) % (n - 1), (i, val))

    return l

s = deepcopy(list(enumerate(seq)))
mixed = mix(s)

f = [1000, 2000, 3000]
res = 0
mixed = [x[1] for x in mixed]

for x in f:
    res += mixed[(mixed.index(0) + x) % n]
print(res)
del mixed

# part 2
seq = [x * 811589153 for x in seq]
s = deepcopy(list(enumerate(seq)))
for _ in range(10):
    s = mix(s)

s = [x[1] for x in s]
res = 0
for x in f:
    res += s[(s.index(0) + x) % n]
print(res)





