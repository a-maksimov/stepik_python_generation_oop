class SuperString:
    def __init__(self, string):
        self.string = string

    def __str__(self):
        return self.string

    def __add__(self, other):
        if isinstance(other, self.__class__):
            new_string = self.string + other.string
            return self.__class__(new_string)
        else:
            return NotImplemented

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            new_string = self.string * other
            return self.__class__(new_string)
        else:
            return NotImplemented

    def __rmul__(self, other):
        if isinstance(other, (int, float)):
            new_string = other * self.string
            return self.__class__(new_string)
        else:
            return NotImplemented

    def __truediv__(self, other):
        if isinstance(other, int):
            m = len(self.string) // other
            new_string = self.string[:m]
            return self.__class__(new_string)
        else:
            return NotImplemented

    def __lshift__(self, other):
        if isinstance(other, int):
            if other >= len(self.string):
                return self.__class__('')
            new_string = self.string[:len(self.string) - other]
            return self.__class__(new_string)
        else:
            return NotImplemented

    def __rshift__(self, other):
        if isinstance(other, int):
            if other >= len(self.string):
                return self.__class__('')
            new_string = self.string[other:]
            return self.__class__(new_string)
        else:
            return NotImplemented


s = SuperString('beegeek')

print(s * 2)
print(3 * s)
print(s / 3)