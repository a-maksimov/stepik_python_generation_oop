class TicTacToe:
    _PLAYERS = {
        True: 'X',
        False: 'O'
    }

    def __init__(self):
        self._board = [[' '] * 3 for _ in range(3)]
        self._current_player = True
        self._winner = None

    def mark(self, row, col):
        if self._winner:
            print('Игра окончена')
            return

        if not self._check_free_cell(row, col):
            return print('Недоступная клетка')

        self._board[row - 1][col - 1] = self._PLAYERS[self._current_player]
        self._check_winner(row, col)
        self._current_player = not self._current_player

    def _check_free_cell(self, row, col):
        is_free = True
        if not self._board[row - 1][col - 1] == ' ':
            return not is_free

        return is_free

    def _check_winner(self, row, col):
        if all(self._board[x][col - 1] == self._PLAYERS[self._current_player] for x in range(3)):
            self._winner = self._PLAYERS[self._current_player]
            return

        if all(self._board[row - 1][y] == self._PLAYERS[self._current_player] for y in range(3)):
            self._winner = self._PLAYERS[self._current_player]
            return

        if all(self._board[x][x] == self._PLAYERS[self._current_player] for x in range(3)):
            self._winner = self._PLAYERS[self._current_player]
            return

        if all(self._board[x][x] == self._PLAYERS[self._current_player] for x in range(2, -1, -1)):
            self._winner = self._PLAYERS[self._current_player]
            return

        if not sum(self._check_free_cell(x, y) for x in range(1, 4) for y in range(1, 4)):
            self._winner = 'Ничья'
            return

    def show(self):
        for i, row in enumerate(self._board):
            print(*[col for col in row], sep='|')
            if i == 2:
                break
            print('-----')

    def winner(self):
        return self._winner


# TEST_3:
tictactoe = TicTacToe()

tictactoe.mark(1, 1)
tictactoe.mark(3, 2)
tictactoe.mark(1, 3)
tictactoe.mark(1, 2)
tictactoe.mark(3, 3)
tictactoe.mark(2, 3)
tictactoe.mark(3, 1)
tictactoe.mark(2, 1)
tictactoe.mark(2, 2)

print(tictactoe.winner())
tictactoe.show()
tictactoe.mark(2, 2)

# TEST_3:
# X
# X|O|X
# -----
# O|X|O
# -----
# X|O|X
# Игра окончена
