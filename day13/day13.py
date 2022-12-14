from functools import reduce
from itertools import chain


f = open("input.txt", "r")
lines = f.readlines()
lines = [l.strip("\n") for l in lines]


pairs = []
p = ()
for x in lines:
    if x != "":
        p += (eval(x), )
    else:
        pairs.append(p)
        p = ()
pairs.append(p)


def compare(l: list, r: list):

    for i in range(max(len(l), len(r))):
        if i == len(l):
            return True

        if i == len(r):
            return False
        # print(l[i], r[i])

        l_t, r_t = type(l[i]), type(r[i])
        if l_t == int and r_t == int:
            if l[i] != r[i]:
                return l[i] < r[i]
        elif l_t == int and r_t == list:
            res = compare([l[i]], r[i])
            if res is not None:
                return res
        elif l_t == list and r_t == int:
            res = compare(l[i], [r[i]])
            if res is not None:
                return res
        # both list
        else:
            res = compare(l[i], r[i])
            if res is not None:
                return res

# part 1
idx = 1
res = 0
for left, right in pairs:
    if compare(left, right):
        res += idx
    idx += 1
print(res)

# Part 2
pairs.append(([[2]], [[6]]))
chained = list(chain(*pairs))
n = len(chained)
arr = chained
for i in range(n):
    for j in range(0, n - i - 1):
        if not compare(arr[j], arr[j + 1]):
            arr[j], arr[j + 1] = arr[j + 1], arr[j]
print(reduce(lambda x, y: x * y, [i + 1 for i, x in enumerate(arr) if x == [[2]] or x == [[6]]]))
