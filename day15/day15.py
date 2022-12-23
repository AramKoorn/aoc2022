f = open("input.txt", "r")
lines = f.readlines()
lines = [x.strip("\n").strip("Sensor at ").replace("closest beacon is at ", "").strip() for x in lines]
lines = [x.split(":") for x in lines]
data = set()


for l, r in lines:
    l_split = l.split('x=')[1]
    r_split = r.split('x=')[1]

    left = (int(l_split.split(',')[0]), int(l_split.split('y=')[1]))
    right = (int(r_split.split(',')[0]), int(r_split.split('y=')[1]))

    # calculate distance
    dist = abs(left[0] - right[0]) + abs(left[1] - right[1])
    data.add((left, right, dist))


# part 1
def coverage_target(target, cover):
    for sensor, beacon, d in data:
        b.add(beacon)
        in_dist = abs(target - sensor[1])
        if in_dist < d:
            xmin, xmax = sensor[0] - (d - in_dist), sensor[0] + (d - in_dist)
            cover = cover.union(set([(x, target) for x in range(xmin, xmax + 1)]))
    return cover


b = set()
cover = coverage_target(int(2e6), set())
cnt = 0
for cords in cover:
    if cords not in b:
        cnt += 1
print(cnt)


def merge_intervals(intervals):
    if len(intervals) == 0 or len(intervals) == 1:
        return intervals
    intervals.sort(key=lambda x: x[0])
    result = [intervals[0]]
    for interval in intervals[1:]:
        if interval[0] <= result[-1][1]:
            result[-1][1] = max(result[-1][1], interval[1])
        else:
            result.append(interval)
    return result


def coverage_target(target):
    interval = None
    for sensor, beacon, d in data:
        in_dist = abs(target - sensor[1])
        if in_dist < d:
            xmin, xmax = sensor[0] - (d - in_dist), sensor[0] + (d - in_dist)
            xmin = 0 if xmin < 0 else xmin
            xmax = goal if xmax > goal else xmax

            # merge intervals
            if interval is None:
                interval = [[xmin, xmax]]
            interval.append([xmin, xmax])
            interval = merge_intervals(interval)
            if len(interval) == 2:
                if interval[0][1] + 1 == interval[1][0]:
                    interval = [[interval[0][0], interval[1][1]]]
            if interval == [[0, goal]]:
                return False
    return interval


# goal = 20
goal = int(4e6)
sorted(data, key=lambda x: x[0])
for i in range(goal + 1):
    interval = coverage_target(i)
    if interval:
        x = int((interval[0][1] + interval[1][0]) / 2)
        print(x * int(4e6) + i)
