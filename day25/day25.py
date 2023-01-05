from functools import reduce


f = open("input.txt")
lines = f.readlines()
lines = [x.strip("\n") for x in lines]
print(lines)
print(lines[0])


def to_decimal(s):

    d = 0
    l = [5 ** i for i in reversed(range(len(s)))]

    for i, c in enumerate(s):
        if c.isdigit():
            d += int(c) * l[i]
        elif c == "=":
            d -= 2 * l[i]
        elif c == "-":
            d -= 1 * l[i]
    return d


def to_snafu(d):
    snafu = ""
    while d:
        remainder = d % 5
        if remainder == 0:
            snafu += "0"
        elif remainder == 1:
            snafu += "1"
        elif remainder == 2:
            snafu += "2"
        elif remainder == 3:
            snafu += "="
            d += 2
        elif remainder == 4:
            snafu += "-"
            d += 1
        d //= 5
    return snafu[::-1]


d = sum([to_decimal(s) for s in lines])
print(d)
print(to_snafu(d))
