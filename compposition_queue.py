class Queue:
    def __init__(self, pairs=None):
        if pairs is None:
            self._pairs = {}
        else:
            if isinstance(pairs, list):
                self._pairs = {pair[0]: pair[1] for pair in pairs}
            else:
                self._pairs = pairs

    @property
    def pairs(self):
        return [tuple(pair) for pair in self._pairs.items()]

    def add(self, elem):
        if elem[0] in self._pairs:
            del self._pairs[elem[0]]
        self._pairs[elem[0]] = elem[1]

    def pop(self):
        if not self._pairs:
            raise KeyError('Очередь пуста')
        first_element = self.pairs[0]
        del self._pairs[first_element[0]]
        return first_element

    def __len__(self):
        return len(self._pairs)

    def __repr__(self):
        return f"{self.__class__.__name__}({self.pairs})"


queue = Queue([('one', 1)])

queue.add(('two', 2))
print(queue.pop())
print(queue.pop())
print(queue)