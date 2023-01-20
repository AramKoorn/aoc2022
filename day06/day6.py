f = open("input.txt", "r")
lines = f.readlines()
lines = [x.strip('\n').split(",") for x in lines]

s = lines[0][0]
s = [x for x in s]

# part 1
for i in range(len(s) - 4):
    if len(set(s[i:i + 4])) == 4:
        print(i + 4)
        break

# part 2
for i in range(len(s) - 14):
    if len(set(s[i:i + 14])) == 14:
        print(i + 14)
        break
