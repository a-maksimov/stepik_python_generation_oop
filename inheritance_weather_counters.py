class Counter:
    def __init__(self, start=0):
        self.start = start
        self.value = self.start

    def inc(self, n=1):
        self.value += n

    def dec(self, n=1):
        self.value = max([0, self.value - n])


class DoubledCounter(Counter):
    
    def inc(self, n=1):
        super().inc(n * 2)

    def dec(self, n=1):
        super().dec(n * 2)



