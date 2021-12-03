from operator import add

with open("input.txt", "r") as f:
    lines = f.readlines()

# part 1
mcb = [0] * 12
for i in list(map(lambda x: [int(i) for i in x], map(lambda x: x.strip(),lines))): mcb = list(map(add, mcb, i))
print(int("".join([str(i) for i in [(0 if i < 500 else 1) for i in mcb]]), 2) * int("".join([str(i) for i in [(0 if i > 500 else 1) for i in mcb]]), 2))

# shorter one line version
print((lambda mcb: int("".join(mcb), 2)*int("".join(list(map(lambda x:str(0 if int(x) else 1), mcb))), 2))((lambda l: [str(0 if sum(list(map(lambda x: x[pos], l))) < len(l)/2 else 1) for pos in range(len(l[0]))])([i for i in list(map(lambda x: [int(i) for i in x], map(lambda x: x.strip(),lines)))])))



# part 2 - unfinished but works
l = [i for i in list(map(lambda x: [int(i) for i in x], map(lambda x: x.strip(),lines)))]
ll = l

print("")
oxy = 0
for pos in range(12):
    cb = False if sum(list(map(lambda x: x[pos], ll))) < len(ll)/2 else True
    if sum(list(map(lambda x: x[pos], ll))) == len(ll)/2:
        cb = True
    ll = list(filter(lambda x: x[pos] == cb, ll))
    if len(ll) == 1:
        oxy = int("".join([str(i) for i in ll[0]]), 2)
        break

# attempt for one line version
# for c2 version use lambda to invert <
a = [(False if (sum(list(map(lambda x: x[pos], l))) < len(l)/2) or (sum(list(map(lambda x: x[pos], l))) == len(l)/2) else True) for pos in range(len(l[0]))]

b = [(False if (sum(list(map(lambda x: x[pos], l))) < len(l)/2) or (sum(list(map(lambda x: x[pos], l))) == len(l)/2) else True) for pos in range(len(l[0]))]


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
