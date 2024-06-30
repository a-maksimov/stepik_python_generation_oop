class OrderedSet:
    def __init__(self, iterable=None):
        if not iterable:
            iterable = []

        self._iterable = []
        for item in iterable:
            if item in self._iterable:
                continue
            self._iterable.append(item)

    def add(self, item):
        if item not in self._iterable:
            self._iterable.append(item)

    def discard(self, item):
        if item in self._iterable:
            self._iterable.remove(item)

    def __len__(self):
        return len(self._iterable)

    def __iter__(self):
        yield from self._iterable

    def __contains__(self, item):
        return item in self._iterable

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self._iterable == other._iterable
        elif isinstance(other, set):
            return set(self._iterable) == other
        else:
            return NotImplemented
