class Submarine:
    depth = 0
    horizontal = 0
    aim = 0

    def __init__(self, aim=False):
        self.is_aim = aim
        self.operation = {
            "forward": self.forward,
            "up": self.up,
            "down": self.down
        }

    def forward(self, value):
        self.horizontal += value

        if self.is_aim:
            self.depth += self.aim * value

    def up(self, value):
        if self.is_aim:
            self.aim -= value
            return
        self.depth -= value

    def down(self, value):
        if self.is_aim:
            self.aim += value
            return
        self.depth += value

    def navigate(self, navigation: list):
        for i in navigation:
            self.operation[i[0]](int(i[1]))

    def __str__(self):
        return str(self.depth * self.horizontal)


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        input_list = list()
        for i in f.readlines():
            input_list.append(i.strip().split(" "))

    # first
    submarine = Submarine()
    submarine.navigate(input_list)
    print(submarine)

    # second
    submarine_aim = Submarine(aim=True)
    submarine_aim.navigate(input_list)
    print(submarine_aim)