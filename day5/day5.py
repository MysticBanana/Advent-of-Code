with open("input.txt", "r") as f:
    content = list(map(lambda x: [int(c) for i in x.strip().split(" -> ") for c in i.split(",")], f.readlines()))

# part 1
ground = dict()
for x1, y1, x2, y2 in content:
    if y1 != y2 and x1 != x2:
        continue
    for x in ((i for i in range(x1, x2+1)) if x1 < x2 else (i for i in range(x1, x2-1, -1))):
        for y in ((i for i in range(y1, y2+1)) if y1 < y2 else (i for i in range(y1, y2-1, -1))):
            if (x, y) not in ground.keys():
                ground[(x, y)] = 0
            ground[(x, y)] += 1

print(len([i for i in ground.values() if i > 1]))


# part 2
ground = dict()
for x1, y1, x2, y2 in content:
    if y1 != y2 and x1 != x2:
        for x, y in zip(((i for i in range(x1, x2+1)) if x1 < x2 else (i for i in range(x1, x2-1, -1))), ((i for i in range(y1, y2+1)) if y1 < y2 else (i for i in range(y1, y2-1, -1)))):
            if (x, y) not in ground.keys():
                ground[(x, y)] = 0
            ground[(x, y)] += 1

    else:
        for x in ((i for i in range(x1, x2+1)) if x1 < x2 else (i for i in range(x1, x2-1, -1))):
            for y in ((i for i in range(y1, y2+1)) if y1 < y2 else (i for i in range(y1, y2-1, -1))):
                if (x, y) not in ground.keys():
                    ground[(x, y)] = 0

                ground[(x, y)] += 1

print(len([i for i in ground.values() if i > 1]))
