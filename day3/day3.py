from operator import add

with open("input.txt", "r") as f:
    lines =  f.readlines()

# part 1
mcb = [0] * 12
for i in list(map(lambda x: [int(i) for i in x], map(lambda x: x.strip(),lines))): mcb = list(map(add, mcb, i))
print(int("".join([str(i) for i in [(0 if i < 500 else 1) for i in mcb]]), 2) * int("".join([str(i) for i in [(0 if i > 500 else 1) for i in mcb]]), 2))


# part 2
test = """00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010"""



l = [i for i in list(map(lambda x: [int(i) for i in x], map(lambda x: x.strip(),lines)))]

ll = l
oxy = 0
for pos in range(12):
    cb = False if sum(list(map(lambda x: x[pos], ll))) < len(ll)/2 else True
    if sum(list(map(lambda x: x[pos], ll))) == len(ll)/2:
        cb = True
    ll = list(filter(lambda x: x[pos] == cb, ll))
    if len(ll) == 1:
        oxy = int("".join([str(i) for i in ll[0]]), 2)
        break

ll = l
c2 = 0
for pos in range(12):
    cb = False if sum(list(map(lambda x: x[pos], ll))) > len(ll)/2 else True
    if sum(list(map(lambda x: x[pos], ll))) == len(ll)/2:
        cb = False
    ll = list(filter(lambda x: x[pos] == cb, ll))
    if len(ll) == 1:
        c2 = int("".join([str(i) for i in ll[0]]), 2)
        break



print(oxy*c2)