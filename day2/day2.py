f = open("input.txt", "r")
lines = f.readlines()
lines = [x.strip('\n').split(" ") for x in lines]

# X, A rock
# Y, B paper
# Z, C scissors
scores = {"X": 1, "Y": 2, "Z": 3}
wins = {"X": "C", "Y": "A", "Z": "B"}
wins_r = {v: k for k, v in wins.items()}
draws = {"X": "A", "Y": "B", "Z": "C"}
draws_r = {v: k for k, v in draws.items()}
lose = {"A": "Z", "B": "X", "C": "Y"}

# Part 1
score = 0
for x, y in lines:

    score += scores[y]
    if x == draws[y]:
        score += 3
        continue

    if wins[y] == x:
        score += 6

print(score)

# Part 2
score = 0
for x, y in lines:

    # need to lose
    if y == "X":
        score += scores[lose[x]]
        continue

    # need to draw
    if y == "Y":
        score += 3
        score += scores[draws_r[x]]
        continue

    # need to win
    if y == "Z":
        score += 6
        score += scores[wins_r[x]]

print(score)
