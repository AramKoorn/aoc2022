f = open("input.txt", "r")
lines = f.readlines()
lines = [x.strip('\n').split(" ") for x in lines]

cnt = 0
crt = ""
v = 1
prev = 0
sprite = 0


def update_cycle(n, cnt, crt):
    for _ in range(1, n + 1):
        cnt += 1
        if cnt == 41:
            cnt -= 40
        sprite_range = list(range(v, v + 3))
        if cnt in sprite_range:
            crt += "#"
        else:
            crt += "."
    return cnt, crt


for x in lines:
    v += prev
    if x[0] == "noop":
        prev = 0
        cnt, crt = update_cycle(1, cnt, crt)
    if x[0] == "addx":
        prev = int(x[1])
        cnt, crt = update_cycle(2, cnt, crt)

p = [x for x in crt]
p = [p[(i - 1) * 40 : i * 40] for i in range(1, 7)]
for x in p:
    print(x)