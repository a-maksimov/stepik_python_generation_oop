class Scales:
    def __init__(self):
        self._left = 0
        self._right = 0

    def add_left(self, weight):
        self._left += weight

    def add_right(self, weight):
        self._right += weight

    def get_result(self):
        result = self._left - self._right
        if result > 0:
            return 'Левая чаша тяжелее'
        elif result < 0:
            return 'Правая чаша тяжелее'
        else:
            return 'Весы в равновесии'


scales = Scales()

scales.add_right(1)
scales.add_right(1)
scales.add_left(2)

print(scales.get_result())

