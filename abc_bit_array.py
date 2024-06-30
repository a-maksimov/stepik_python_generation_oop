from collections.abc import Sequence


class BitArray(Sequence):
    def __init__(self, iterable=None):
        if iterable is None:
            self.iterable = []
        else:
            self.iterable = iterable.copy()

    def __len__(self):
        return len(self.iterable)

    def __getitem__(self, index):
        return self.iterable[index]

    def __str__(self):
        return str(self.iterable)

    def __invert__(self):
        return self.__class__([int(not item) for item in self.iterable])

    def __and__(self, other):
        if not isinstance(other, BitArray):
            return NotImplemented

        if not len(other) == len(self):
            return NotImplemented

        return self.__class__([a & b for a, b in zip(self, other)])

    def __or__(self, other):
        if not isinstance(other, BitArray):
            return NotImplemented

        if not len(other) == len(self):
            return NotImplemented

        return self.__class__([a | b for a, b in zip(self, other)])


data1 = [0, 1, 1, 0, 0, 1]
data2 = [1, 1, 1, 1, 1]

bitarray1 = BitArray(data1)
bitarray2 = BitArray(data2)

try:
    print(bitarray1 | bitarray2)
except TypeError:
    print('Списки должны быть равной длины')

try:
    print(bitarray1 & bitarray2)
except TypeError:
    print('Списки должны быть равной длины')
