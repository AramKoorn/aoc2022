f = open("input.txt", "r")
lines = f.readlines()
lines = [x.strip('\n').split(" ") for x in lines]

# build filesystem
curr = "/"
fs = {}

# Quick visual how I want to implement file system
# {"/":  {"a": {"e": {"files": ["file_i"]}}, "files": ["file_f", "file_g", "file_h"]}, "files": []}

curr = ["/"]
fs["/"] = {'files': []}

# build filesystem in a dictionary
for x in lines[1:]:
    if x[1] == "ls":
        continue
    if x[0] == "dir":
        tmp = fs
        for d in curr:
            tmp = tmp[d]
        tmp.update({x[1]: {"files": []}})
    # we are adding a file
    if x[0] != "$" and x[0] != "dir":
        tmp = fs
        for d in curr:
            tmp = tmp[d]
            tmp["files"].append((x[0], x[1]))
    if x[1] == "cd":
        if x[2] == "..":
            curr.pop()
        else:
            curr.append(x[2])

# Part 1
sizes = []
lim = int(1e5)

# part 2
def rec(d):
    for k, v in d.items():
        t = 0
        if k == "files":
            for f_size, _ in v:
                t += int(f_size)
            sizes.append(t)
        if isinstance(v, dict):
            rec(v)

rec(fs)
print(sum([x for x in sizes if x < lim]))

# part 2
t = 0
for f, _ in fs["/"]["files"]:
    t += int(f)
unused = 70000000 - t
req = 30000000 - unused

sizes.sort()
for x in sizes:
    if x >= req:
        print(x)
        break
