from functools import cache

cnt = 0

@cache
def dfs(t):

    global  cnt

    if t == 0:
        return

    for _ in ["a", "b", "c", "d"]:
        if t == 10:
            cnt += 1
        print(t, _)
        dfs(t - 1)

dfs(10)
print("10s: ", cnt)