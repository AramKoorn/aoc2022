from functools import reduce


def print_priority(s):
    res = 0
    for x in s:
        if x.islower():
            res += ord(x) - 96
        else:
            res += ord(x.lower()) - 96 + 26

    print(res)


f = open("input.txt", "r")
lines = f.readlines()
lines = [x.strip('\n') for x in lines]

s = ""
for x in lines:
    n = int(len(x) / 2)
    left, right = set(x[:n]), set(x[n:])
    ch = left & right
    s += list(ch)[0]

print_priority(s)

# Part 2
groups = [lines[n: n + 3] for n in range(0, len(lines), 3)]
s = ""
for g in groups:
    f = reduce(lambda x, y: set(x) & set(y), g)
    s += list(f)[0]

print_priority(s)
