import statistics

with open("input.txt", "r") as f:
    content = [int(i) for i in f.read().strip().split(",")]

def calc(calc_fn, pos: int = 0):
    final_fuel = 2 ** 31
    for num in range(pos, (pos+1) if pos else max(content)):
        final_fuel = min(final_fuel, sum(calc_fn(num, i) for i in content))
    return final_fuel

print(calc(lambda x, y: abs(x-y)))
print(calc(lambda x, y: (abs(x-y) * (abs(x-y) + 1)) // 2))

# short way
print(calc(lambda x, y: abs(x-y), int(statistics.median(content))))
print(calc(lambda x, y: (abs(x-y) * (abs(x - y) + 1)) // 2, int(sum(content) / (len(content)))))