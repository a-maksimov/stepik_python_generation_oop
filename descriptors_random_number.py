import random


class RandomNumber:
    def __init__(self, start, end, cache=False):
        self._range = start, end
        self._cache = cache
        self._first = None

    def __set_name__(self, owner, name):
        self._attr = name

    def __get__(self, obj, cls):
        if obj is None:
            return self
        if self._first is None:
            self._first = random.randint(self._range[0], self._range[1])
        if self._cache:
            return self._first
        return random.randint(self._range[0], self._range[1])

    def __set__(self, obj, value):
        raise AttributeError('Изменение невозможно')


class MagicPoint:
    x = RandomNumber(1, 5)
    y = RandomNumber(1, 5)
    z = RandomNumber(1, 5)

magicpoint = MagicPoint()

print(magicpoint.x in [1, 2, 3, 4, 5])
print(magicpoint.y in [1, 2, 3, 4, 5])
print(magicpoint.z in [1, 2, 3, 4, 5])