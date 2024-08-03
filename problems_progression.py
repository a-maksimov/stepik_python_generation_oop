class Progression:
    def __init__(self, start=0):
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        current = self.current
        self.current += 1
        return current


class ArithmeticProgression(Progression):
    def __init__(self, start=0, param=1):
        super().__init__(start)
        self.param = param

    def __next__(self):
        current = self.current
        self.current += self.param
        return current


class GeometricProgression(ArithmeticProgression):
    def __init__(self, start=0, param=1):
        super().__init__(start, param)

    def __next__(self):
        current = self.current
        self.current *= self.param
        return current


# TEST_1:
progression = ArithmeticProgression(0, 1)

for elem in progression:
    if elem > 10:
        break
    print(elem, end=' ')