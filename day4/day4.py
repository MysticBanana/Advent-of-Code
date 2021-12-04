class Board:
    def __init__(self, board_data: str):
        self.board = [list(filter(lambda x: x != "", r.split(" "))) for r in board_data.split("\n") if len(r) != 0]
        self.last_num = 0

    def draw_num(self, num: str):
        self.last_num = int(num)
        for row in range(len(self.board)):
            for col in range(len(self.board)):
                if self.board[row][col] == num:
                    self.board[row][col] = -1

        return True if self.is_bingo() else False

    def is_bingo(self):
        # check if one row is complete
        for i in self.board:
            if sum(list(map(lambda x: int(x), i))) == -5:
                return True

        # check if a column is complete
        for i in list(zip(*self.board)):
            if sum(list(map(lambda x: int(x), i))) == -5:
                return True

    @property
    def score(self):
        return sum([int(i) for row in self.board for i in row if i != -1])*int(self.last_num)

with open("input.txt", "r") as f:
    boards = f.read().split("\n\n")
    num_draw = boards[0].split(",")
    boards.pop(0)

board_list = list()
bingo_list = list()

for i in boards:
    board_list.append(Board(i))

for i in num_draw:
    for board in board_list:
        if board in bingo_list:
            continue
        score = board.draw_num(i)
        if score:
            bingo_list.append(board)

# for some reason 2 bingos appeared on one number and i had to other numbers and the result of bingo_list[-2] worked for me
# part 1
print(bingo_list[0].score)
# part 2
print(bingo_list[-1].score)