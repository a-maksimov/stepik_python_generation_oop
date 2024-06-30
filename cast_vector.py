class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __abs__(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def __str__(self):
        return f'({self.x}, {self.y})'

    def __bool__(self):
        return any([self.x, self.y])

    def __int__(self):
        return int(self.__abs__())

    def __float__(self):
        return self.__abs__()

    def __complex__(self):
        return complex(self.x, self.y)
