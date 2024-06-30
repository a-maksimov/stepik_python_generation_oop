class Summator:

    def total(self, n, power=1):
        return sum(map(lambda x: x ** power, range(1, n + 1)))


class SquareSummator(Summator):

    def total(self, n):
        return super().total(n, 2)


class QubeSummator(Summator):

    def total(self, n):
        return super().total(n, 3)


class CustomSummator(Summator):
    def __init__(self, m):
        self.m = m

    def total(self, n):
        return super().total(n, self.m)
