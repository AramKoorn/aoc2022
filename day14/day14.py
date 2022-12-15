f = open("input_test.txt", "r")
lines = f.readlines()
lines = [[x.split(",") for x in x.strip("\n").split(" -> ")] for x in lines]

cords = []
for x in lines:
    for i in range(len(x) - 1):
        # create points
        first = list(map(int, x[i]))
        second = list(map(int, x[i + 1]))
        r1 = list(range(first[0], second[0] + 1))
        r2 = list(range(first[1], second[1] + 1))

        if len(r1) == 1:
            for v in r2:
                cords.append((r1[0], v))
        else:
            for v in r1:
                cords.append((v, r2[0]))
print(cords)





