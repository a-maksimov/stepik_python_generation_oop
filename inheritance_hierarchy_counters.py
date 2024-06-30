class Counter:
    def __init__(self, start=0):
        self.start = start
        self.value = self.start

    def inc(self, n=1):
        self.value += n

    def dec(self, n=1):
        self.value -= n
        if self.value < 0:
            self.value = 0


class NonDecCounter(Counter):
    def inc(self, n=1):
        self.value += n

    def dec(self, n=1):
        ...


class LimitedCounter(Counter):
    def __init__(self, start=0, limit=10):
        super().__init__(start)

        self.limit = limit

    def inc(self, n=1):
        value = self.value + n
        self.value = min([value, self.limit])


counter = LimitedCounter()

print(counter.value)
counter.inc()
counter.inc(4)
print(counter.value)
counter.dec()
counter.dec(2)
print(counter.value)
counter.inc(20)
print(counter.value)

# 0
# 5
# 2
# 10