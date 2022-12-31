from copy import deepcopy


f = open("input.txt")
lines = f.readlines()
lines = [x.strip("\n").split(":") for x in lines]


mp = {k: v for k, v in lines}
ops = dict()
mappings = dict()


for k, v in mp.items():
    try:
        x = eval(v)
        mappings[k] = x
    except:
        ops[k] = v


mappings["humn"] = "xxx"

# prefill
prev = float("inf")
while prev != len(ops) > 0:
    prev = len(ops)
    for k, v in ops.items():
        left, op, right = v.strip().split(" ")
        if left in mappings:
            left = str(mappings[left])
        if right in mappings:
            right = str(mappings[right])
        expr = " ".join([left, op, right])
        try:
            x = eval(expr)
            ops.pop(k)
            mappings[k] = x
            break
        except:
            ops[k] = expr

goal = mappings["bsgz"]  # from looking at what is already filled in root


def evalu(m, o, xxx):

    mappings = deepcopy(m)
    ops = deepcopy(o)
    mappings["humn"] = xxx

    while len(ops) > 0:
        for k, v in ops.items():
            left, op, right = v.strip().split(" ")
            if left in mappings:
                left = str(mappings[left])
            if right in mappings:
                right = str(mappings[right])
            expr = " ".join([left, op, right])
            try:
                x = eval(expr)
                ops.pop(k)
                mappings[k] = x
                break
            except:
                ops[k] = expr
    return mappings["lsbv"]


def binary_search():
    low = 0
    high = 10000000000000 * 2
    mid = high / 2

    x = float("inf")
    while x != goal:
        x = evalu(mappings, ops, xxx=mid)
        if x < goal:
            high = mid
            mid = (mid + low) // 2
        elif x > goal:
            low = mid
            mid = (high + mid) // 2
        else:
            return mid


res = binary_search()
print(res)


