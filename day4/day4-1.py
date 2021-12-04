with open('day4/day4.txt', 'r') as f:
    data = f.readlines()

data = [data for data in data if data != '\n']

callouts = data[0].replace('\n', '').split(',')

data = data[1:]

class BingoController:
    def __init__(self, boards):
        self.boards = boards

    def mass_move(self, callout):
        for board in self.boards:
            board.move(callout)
    
    def check_wins(self):
        for board in self.boards:
            if board.check_win():
                return board
        return False

    def get_board_count(self):
        return len(self.boards)

    

class BingoBoard:
    def __init__(self, layout):
        self.board = [layout[0].replace('\n', '').split(), layout[1].replace('\n', '').split(), layout[2].replace('\n', '').split(), layout[3].replace('\n', '').split(), layout[4].replace('\n', '').split()]

    def show_board(self):
        return self.board

    def move(self, callout):
        callout = str(callout)
        for i, row in enumerate(self.board):
            for j, square in enumerate(row):
                if square == callout:
                    self.board[i][j] = '*'

        return self.board

    def find_sum(self):
        sum = 0
        for row in self.board:
            for square in row:
                if square != '*':
                    sum = sum + int(square)
        return sum

    def check_win(self):
        for row in self.board:
            if row == ['*', '*', '*', '*', '*']:
                return True
        for i in range(5):
            if self.board[0][i] == self.board[1][i] == self.board[2][i] == self.board[3][i] == self.board[4][i] == '*':
                return True
        return False

layouts = [data[i:i+5] for i in range(0, len(data), 5)]

controller = BingoController(boards=[BingoBoard(layout=layouts[i]) for i in range(len(layouts))])

for callout in callouts:
    controller.mass_move(callout=callout)
    winning_board = controller.check_wins()
    if winning_board:
        winning_board_sum = winning_board.find_sum()
        print(f'Winning Board Score: {winning_board_sum * int(callout)}')
        break