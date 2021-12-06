NUM_OF_DAYS = 256

with open("input.txt", "r") as f:
    content = [int(i) for i in f.read().strip().split(",")]

fish_list = [0]*10
for i in content:
    fish_list[i] += 1

for i in range(0, NUM_OF_DAYS):
    # add old fishes to 6
    fish_list[6+1] += fish_list[0]
    # add new fishes to 8
    fish_list[8+1] += fish_list[0]

    fish_list.pop(0)
    fish_list += [0]

print(sum(fish_list))

# Short version
fish_list = [0]*10
for i in content: fish_list[i] += 1
for i in range(0, NUM_OF_DAYS):
    fish_list[6+1] += fish_list[0]
    fish_list[8+1] += fish_list[0]
    fish_list.pop(0)
    fish_list += [0]
