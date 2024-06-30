from collections.abc import Sequence


class SortedList(Sequence):
    def __init__(self, iterable=None):
        if iterable is None:
            self._iterable = []
        else:
            self._iterable = sorted(iterable)

    def __repr__(self):
        return f"{self.__class__.__name__}({str(self._iterable)})"

    def __getattribute__(self, item):
        if item in ['append', 'insert', 'extend', 'reverse']:
            raise NotImplementedError
        return object.__getattribute__(self, item)

    def __reversed__(self):
        raise NotImplementedError

    def __len__(self):
        return len(self._iterable)

    def __getitem__(self, item):
        return self._iterable[item]

    def add(self, item):
        self._iterable.append(item)
        self._iterable.sort()

    def discard(self, item):
        new_iterable = []
        for element in self._iterable:
            if element == item:
                continue
            new_iterable.append(element)
        self._iterable = sorted(new_iterable)

    def update(self, iterable):
        self._iterable.extend(iterable)
        self._iterable.sort()

    def __delitem__(self, index):
        del self._iterable[index]
        self._iterable.sort()

    def __setitem__(self, key, value):
        raise NotImplementedError

    def __add__(self, other):
        if not isinstance(other, self.__class__):
            return NotImplemented

        return self.__class__(self._iterable + other._iterable)

    def __iadd__(self, other):
        if not isinstance(other, self.__class__):
            return NotImplemented

        self._iterable += other._iterable
        self._iterable.sort()

        return self

    def __mul__(self, n):
        if not isinstance(n, int):
            return NotImplemented
        return self.__class__(self._iterable * n)

    def __imul__(self, n):
        if not isinstance(n, int):
            return NotImplemented
        self._iterable *= n
        self._iterable.sort()
        return self


# TEST_11:
numbers1 = SortedList([1, 3, 5])
numbers2 = SortedList([2, 4])

id1_numbers1 = id(numbers1)
id1_numbers2 = id(numbers2)

numbers1 += numbers2
numbers2 *= 2

id2_numbers1 = id(numbers1)
id2_numbers2 = id(numbers2)

print(id1_numbers1 == id2_numbers1)
print(id1_numbers2 == id2_numbers2)
print(3 in numbers1)

# TEST_11:
# True
# True
# True