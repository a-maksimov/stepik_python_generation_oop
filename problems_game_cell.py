import random


class Cell:
    def __init__(self, row, col, mine):
        self.row = row
        self.col = col
        self.mine = mine
        self.neighbours = 0

    def __repr__(self):
        return '|*|' if self.mine else '| |'


class Game:
    def __init__(self, rows, cols, mines):
        self.rows = rows
        self.cols = cols
        self.mines = mines
        self.board = [
            [Cell(row, col, False) for col in range(self.cols)]
            for row in range(self.rows)
        ]
        indices = [(i, j) for i in range(self.rows) for j in range(self.cols)]
        random.shuffle(indices)
        for i in range(self.mines):
            row, col = indices[i]
            self.board[row][col].mine = True

        self.mines_board = [
            [self.board[row][col].mine for col in range(self.cols)] for row in range(self.rows)
        ]

        for row in range(self.rows):
            for col in range(self.cols):
                _cell = self.board[row][col]
                if col + 1 < self.cols and self.mines_board[row][col + 1]:  # Right
                    _cell.neighbours += 1
                if col - 1 >= 0 and self.mines_board[row][col - 1]:  # Left
                    _cell.neighbours += 1
                if row + 1 < self.rows and self.mines_board[row + 1][col]:  # Down
                    _cell.neighbours += 1
                if row - 1 >= 0 and self.mines_board[row - 1][col]:  # Up
                    _cell.neighbours += 1
                if row + 1 < self.rows and col + 1 < self.cols and self.mines_board[row + 1][col + 1]:  # Down-right
                    _cell.neighbours += 1
                if row - 1 >= 0 and col - 1 >= 0 and self.mines_board[row - 1][col - 1]:  # Up-left
                    _cell.neighbours += 1
                if row + 1 < self.rows and col - 1 >= 0 and self.mines_board[row + 1][col - 1]:  # Down-left
                    _cell.neighbours += 1
                if row - 1 >= 0 and col + 1 < self.cols and self.mines_board[row - 1][col + 1]:  # Up-right
                    _cell.neighbours += 1


n, m = 10, 8
game = Game(n, m, 14)
total_mines = 0

for r in range(n):
    for c in range(m):
        if not game.board[r][c].mine:
            print(r, c, ';', game.board[r][c].neighbours)
        total_mines += game.board[r][c].mine


for row in game.board:
    print(row)

print(total_mines == game.mines)
print(total_mines)
print(game.mines)

