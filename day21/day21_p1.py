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


print(mappings["root"])
