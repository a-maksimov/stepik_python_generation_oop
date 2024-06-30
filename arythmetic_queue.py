class Queue:
    def __init__(self, *args):
        self._queue = list(args)

    @property
    def queue(self):
        return tuple(self._queue)

    def add(self, *args):
        self._queue.extend(args)

    def pop(self):
        if not self.queue:
            return
        return self._queue.pop(0)

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return NotImplemented

        return self.queue == other.queue

    def __add__(self, other):
        if not isinstance(other, self.__class__):
            return NotImplemented

        args = self._queue + list(other.queue)
        return self.__class__(*args)

    def __iadd__(self, other):
        if not isinstance(other, Queue):
            return NotImplemented

        self._queue += list(other.queue)
        return self

    def __rshift__(self, other):
        if not isinstance(other, int):
            return NotImplemented

        if other > len(self._queue):
            return self.__class__(*[])

        args = self._queue.copy()
        for _ in range(other):
            args.pop(0)

        return self.__class__(*args)

    def __str__(self):
        queue = map(str, self._queue)
        return ' -> '.join(queue)


queue = Queue(1, 2)
queue.add(3)
queue.add(4, 5)

print(queue)
print(queue.pop())
print(queue)

print()

queue1 = Queue(1, 2, 3)
queue2 = Queue(1, 2)

print(queue1 == queue2)
queue2.add(3)
print(queue1 == queue2)

print()

queue1 = Queue(1, 2, 3)
queue2 = Queue(4, 5)

print(queue1 + queue2)

print()

queue = Queue(1, 2, 3, 4, 5)

print(queue >> 3)

print()

# TEST_7:
queue = Queue(*'beegeek')
for i in range(9):
    print(f'Queue >> {i} =', queue >> i)

# Queue >> 0 = b -> e -> e -> g -> e -> e -> k
# Queue >> 1 = e -> e -> g -> e -> e -> k
# Queue >> 2 = e -> g -> e -> e -> k
# Queue >> 3 = g -> e -> e -> k
# Queue >> 4 = e -> e -> k
# Queue >> 5 = e -> k
# Queue >> 6 = k
# Queue >> 7 =
# Queue >> 8 =