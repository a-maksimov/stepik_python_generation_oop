from functools import total_ordering


@total_ordering
class Vector:
    def __init__(self, *args):
        self.coordinates = args

    def __str__(self):
        return str(self.coordinates)

    @staticmethod
    def _check_length(v1, v2):
        if not len(v1.coordinates) == len(v2.coordinates):
            raise ValueError('Векторы должны иметь равную длину')

    def __add__(self, other):
        if not isinstance(other, self.__class__):
            return NotImplemented
        self._check_length(self, other)
        sum_vector = []
        for c1, c2 in zip(self.coordinates, other.coordinates):
            sum_vector.append(c1 + c2)
        return self.__class__(*sum_vector)

    def __sub__(self, other):
        if not isinstance(other, self.__class__):
            return NotImplemented
        self._check_length(self, other)
        sub_vector = []
        for c1, c2 in zip(self.coordinates, other.coordinates):
            sub_vector.append(c1 - c2)
        return self.__class__(*sub_vector)

    def __mul__(self, other):
        if not isinstance(other, self.__class__):
            return NotImplemented
        self._check_length(self, other)
        mul = 0
        for c1, c2 in zip(self.coordinates, other.coordinates):
            mul += c1 * c2
        return mul

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return NotImplemented
        self._check_length(self, other)
        return self.coordinates == other.coordinates

    def __lt__(self, other):
        if not isinstance(other, self.__class__):
            return NotImplemented
        self._check_length(self, other)
        return self.coordinates < other.coordinates

    def norm(self):
        return sum(map(lambda x: x**2, self.coordinates))**0.5


# TEST_1:
vector1 = Vector(1, 2, 3)
vector2 = Vector(3, 4, 5)
vector3 = Vector(5, 6, 7, 8)

print(vector1 + vector2)
print(vector1 - vector2)
print(vector1 * vector2)
print(vector3.norm())