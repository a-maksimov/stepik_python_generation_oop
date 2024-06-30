class SuperInt(int):

    def repeat(self, n=2):
        return self.__class__(int(str(abs(self)) * n) * self // abs(self))

    def to_bin(self):
        return format(self, 'b')

    def next(self):
        return self.__class__(self + 1)

    def prev(self):
        return self.__class__(self - 1)

    def __iter__(self):
        yield from map(lambda x: self.__class__(x), str(self).strip('-'))


superint1 = SuperInt(1337)
superint2 = SuperInt(-2077)

print(*superint1)
print(*superint2)