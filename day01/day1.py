f = open("input.txt", "r")
lines = f.readlines()
lines = [x.strip('\n') for x in lines]

cal = []

tmp = []
for x in lines:
    if x != "":
        tmp.append(int(x))
    else:
        cal.append(tmp)
        tmp = []

# part 1
print(max([sum(x) for x in cal]))

# part 2
print(sum(sorted([sum(x) for x in cal])[-3:]))