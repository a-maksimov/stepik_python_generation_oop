class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'Vector({self.x}, {self.y})'

    def __add__(self, other):
        if isinstance(other, self.__class__):
            return self.__class__(
                self.x + other.x,
                self.y + other.y,
            )
        return NotImplemented

    def __sub__(self, other):
        if isinstance(other, self.__class__):
            return self.__class__(
                self.x - other.x,
                self.y - other.y,
            )
        return NotImplemented

    def __mul__(self, other):
        if isinstance(other, (float, int)):
            return self.__class__(
                self.x * other,
                self.y * other,
            )
        return NotImplemented

    def __truediv__(self, other):
        if isinstance(other, (float, int)):
            return self.__class__(
                self.x / other,
                self.y / other
            )
        return NotImplemented

    def __rmul__(self, other):
        if isinstance(other, (float, int)):
            return self.__class__(
                other * self.x,
                other * self.y,
            )
        return NotImplemented

    def __rtruediv__(self, other):
        if isinstance(other, (float, int)):
            return self.__class__(
                other / self.x,
                other / self.y,
            )
        return NotImplemented

