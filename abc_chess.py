from abc import ABC, abstractmethod


def char_to_int(char):
    return abs(ord(char) - ord('a'))


def int_to_char(num):
    return chr(ord('a') + num)


class ChessPiece(ABC):
    def __init__(self, horizontal, vertical):
        self.horizontal = horizontal
        self.vertical = vertical

    @abstractmethod
    def can_move(self, new_horizontal, new_vertical):
        pass

    @property
    def horizontal(self):
        return int_to_char(self._horizontal)

    @horizontal.setter
    def horizontal(self, value):
        self._horizontal = char_to_int(value)


class King(ChessPiece):
    def __init__(self, horizontal, vertical):
        super().__init__(horizontal, vertical)

    def can_move(self, new_horizontal, new_vertical):
        new_horizontal = char_to_int(new_horizontal) + 1
        if not all([abs(new_horizontal - (self._horizontal + 1)) <= 1, abs(self.vertical - new_vertical) <= 1]):
            return False
        if not any([abs(new_horizontal - (self._horizontal + 1)) > 0, abs(self.vertical - new_vertical) > 0]):
            return False
        return True


class Knight(ChessPiece):
    def __init__(self, horizontal, vertical):
        super().__init__(horizontal, vertical)

    def can_move(self, new_horizontal, new_vertical):
        new_horizontal = char_to_int(new_horizontal) + 1
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


# TEST_3:
king = King('e', 3)

print(king.can_move('e', 3))
print(king.can_move('e', 4))
print(king.can_move('b', 1))

# TEST_3:
# False
# True
# False