from collections import deque
from functools import reduce


class Monkey:
    def __init__(self, n):
        self.n = n
        self.items = None
        self.n_inspections = 0

        # Placeholder functions
        self.op = lambda: None
        self.throw = lambda: None

    def __repr__(self):
        return f"Monkey: {self.n}"

    def inspect(self):
        while len(self.items) > 0:
            self.n_inspections += 1
            item = self.items.popleft()
            item = self.op(item)
            item = item // 3

            to = self.throw(item)
            monkeys[to].items.append(item)

    def parse_items(self, line):
        line = [x.strip(",") for x in line]
        items = list(map(int, line[4:]))
        self.items = deque(items)

    def parse_op(self, line):
        expression = "".join(line[5:])
        self.op = lambda old: eval(expression)

    def parse_condition(self, line):
        self.throw = lambda item: line[1] if item % line[0] == 0 else line[-1]

monkeys = {}

f = open("input.txt", "r")
f = f.readlines()

idx = 0
for i, x in enumerate(f):
    x = x.strip("\n")
    x = x.split(" ")
    if x[0] == "Monkey":
        m = Monkey(int(x[1][0]))
        continue

    if x == [""]:
        monkeys[idx] = m
        idx += 1
        continue

    if x[2] == "Starting":
        m.parse_items(line=x)

    if x[2] == "Operation:":
        m.parse_op(line=x)

    if x[2] == "Test:":
        c = []
        lines = f[i: i + 3]
        lines = list(map(int, [x.strip("\n").split(" ")[-1] for x in lines]))
        m.parse_condition(lines)


monkeys[idx] = m


for i in range(20):
    for m in monkeys.values():
        m.inspect()


res = []
for k, v in monkeys.items():
    res.append(v.n_inspections)

res.sort()
print(reduce(lambda x, y: x * y, res[-2:]))