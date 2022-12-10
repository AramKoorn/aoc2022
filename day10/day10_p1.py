f = open("input.txt", "r")
lines = f.readlines()
lines = [x.strip('\n').split(" ") for x in lines]

cnt = 0
v = 1
prev = 0
targets = [20, 60, 100, 140, 180, 220]
signal = []


def update_cycle(n, cnt):
    for _ in range(1, n + 1):
        cnt += 1
        if cnt in targets:
            signal.append(v * cnt)
    return cnt


for x in lines:
    v += prev
    if x[0] == "noop":
        prev = 0
        cnt = update_cycle(1, cnt)
    if x[0] == "addx":
        prev = int(x[1])
        cnt = update_cycle(2, cnt)

print(sum(signal))
