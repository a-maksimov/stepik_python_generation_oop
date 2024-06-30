class Knight:
    def __init__(self, horizontal, vertical, color):
        self.horizontal = horizontal
        self.vertical = vertical
        self.color = color

    @property
    def horizontal(self):
        return self.int_to_char(self._horizontal)

    @horizontal.setter
    def horizontal(self, value):
        self._horizontal = self.char_to_int(value)

    @staticmethod
    def get_char():
        return 'N'

    @staticmethod
    def char_to_int(char):
        return abs(ord(char) - ord('a'))

    @staticmethod
    def int_to_char(num):
        return chr(ord('a') + num)

    def can_move(self, new_horizontal, new_vertical):
        new_horizontal = self.char_to_int(new_horizontal) + 1
        if abs(new_horizontal - (self._horizontal + 1)) == 2:
            if abs(self.vertical - new_vertical) == 1:
                return True
            else:
                return False
        elif abs(new_vertical - self.vertical) == 2:
            if abs(new_horizontal - (self._horizontal + 1)) == 1:
                return True
            else:
                return False
        else:
            return False

    def move_to(self, new_horizontal, new_vertical):
        if self.can_move(new_horizontal, new_vertical):
            self.horizontal = new_horizontal
            self.vertical = new_vertical

    def draw_board(self):
        desk = []
        for _ in range(8):
            desk.append(['.'] * 8)

        c = self._horizontal
        r = 8 - self.vertical

        desk[r][c] = 'N'

        for row in range(8):
            for col in range(8):
                if (
                        abs(r - row) == 1 and abs(c - col) == 2 or
                        abs(r - row) == 2 and abs(c - col) == 1
                ):
                    desk[row][col] = '*'

        for row in range(8):
            print(''.join(desk[row]))


knight = Knight('c', 3, 'white')

print(knight.horizontal, knight.vertical)
print(knight.can_move('e', 5))
print(knight.can_move('e', 4))

knight.move_to('e', 4)
print(knight.horizontal, knight.vertical)

# c 3
# False
# True
# e 4

# TEST_4:
# knight = Knight('e', 5, 'black')
#
# knight.draw_board()
# knight.move_to('d', 3)
# print()
# knight.draw_board()

# ........
# ...*.*..
# ..*...*.
# ....N...
# ..*...*.
# ...*.*..
# ........
# ........
#
# ........
# ........
# ........
# ..*.*...
# .*...*..
# ...N....
# .*...*..
# ..*.*...

# TEST_5:
# knight = Knight('a', 1, 'white')
#
# knight.draw_board()
# knight.move_to('e', 8)
# print()
# knight.draw_board()

# ........
# ........
# ........
# ........
# ........
# .*......
# ..*.....
# N.......
#
# ........
# ........
# ........
# ........
# ........
# .*......
# ..*.....
# N.......
