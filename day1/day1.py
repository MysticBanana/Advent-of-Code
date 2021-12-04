NUM_OF_SUM = 3

def count_increased_element(counting: list, step: int = 0):
    greater = 0
    for i in range(step, len(counting)-1):
        if counting[i-step] < counting[i+1]:
            greater += 1
    return greater

if __name__ == "__main__":
    with open("input.txt", "r") as f:
        counting = list()
        for i in f.readlines():
            counting.append(int(i.strip()))

        # silver
        print(count_increased_element(counting))

        # gold
        print(count_increased_element(counting, NUM_OF_SUM-1))

