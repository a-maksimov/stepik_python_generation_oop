class MinStat:
    def __init__(self, iterable=None):
        if not iterable:
            self.iterable = []
        else:
            self.iterable = iterable

    def add(self, n):
        self.iterable.append(n)

    def result(self):
        return min(self.iterable, default=None)

    def clear(self):
        self.iterable.clear()


class MaxStat:
    def __init__(self, iterable=None):
        if not iterable:
            self.iterable = []
        else:
            self.iterable = iterable

    def add(self, n):
        self.iterable.append(n)

    def result(self):
        return max(self.iterable, default=None)

    def clear(self):
        self.iterable.clear()


class AverageStat:
    def __init__(self, iterable=None):
        if not iterable:
            self.iterable = []
        else:
            self.iterable = iterable

    def add(self, n):
        self.iterable.append(n)

    def result(self):
        if not self.iterable:
            return
        return sum(self.iterable) / len(self.iterable)

    def clear(self):
        self.iterable.clear()


minstat = MinStat()
maxstat = MaxStat()
averagestat = AverageStat()

for i in range(1, 6):
    minstat.add(i)
    maxstat.add(i)
    averagestat.add(i)

print(minstat.result())
print(maxstat.result())
print(averagestat.result())