from collections import UserList


class NumberList(UserList):
    def __init__(self, iterable=None):
        if iterable is None:
            iterable = []
        if not all([isinstance(item, (int, float)) for item in iterable]):
            raise TypeError('Элементами экземпляра класса NumberList должны быть числа')
        super().__init__(iterable)

    def _check_items(self, iterable):
        try:
            return self.__class__(iterable).data
        except TypeError:
            raise TypeError('Элементами экземпляра класса NumberList должны быть числа')

    def _check_item(self, item):
        if not isinstance(item, (int, float)):
            raise TypeError('Элементами экземпляра класса NumberList должны быть числа')
        return item

    def __iadd__(self, other):
        self.data += self._check_items(other)
        return NumberList(self.data)

    def __add__(self, other):
        return NumberList(self.data + self._check_items(other))

    def __radd__(self, other):
        return NumberList(self._check_items(other) + self.data)

    def append(self, item):
        self.data.append(self._check_item(item))

    def extend(self, iterable):
        self.data.extend(self._check_items(iterable))

    def insert(self, index, item):
        self.data.insert(index, self._check_item(item))

    def __setitem__(self, index, item):
        self.data[index] = self._check_item(item)


# TEST_5:
numberlist = NumberList([1, 2])

try:
    numberlist += [3, '4']
except TypeError as e:
    print(e)