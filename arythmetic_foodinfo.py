class FoodInfo:
    def __init__(self, proteins, fats, carbohydrates):
        self.proteins = proteins
        self.fats = fats
        self.carbohydrates = carbohydrates

    def __repr__(self):
        return f'FoodInfo({self.proteins}, {self.fats}, {self.carbohydrates})'

    def __add__(self, other):
        if isinstance(other, self.__class__):
            return self.__class__(
                self.proteins + other.proteins,
                self.fats + other.fats,
                self.carbohydrates + other.carbohydrates
            )
        return NotImplemented

    def __mul__(self, other):
        if isinstance(other, (float, int)):
            return self.__class__(
                self.proteins * other,
                self.fats * other,
                self.carbohydrates * other
            )
        return NotImplemented

    def __truediv__(self, other):
        if isinstance(other, (float, int)):
            return self.__class__(
                self.proteins / other,
                self.fats / other,
                self.carbohydrates / other
            )
        return NotImplemented

    def __floordiv__(self, other):
        if isinstance(other, (int, float)):
            return self.__class__(
                self.proteins // other,
                self.fats // other,
                self.carbohydrates // other
            )
        return NotImplemented


# TEST_6:
food1 = FoodInfo(10, 20, 30)
food2 = FoodInfo(10, 20, 30)

not_supported = [food2, [], {}, set(), '', frozenset(), ()]

for item in not_supported:
    print(food1.__add__(item))
    print(food1.__floordiv__(item))
    print(food1.__mul__(item))
    print(food1.__truediv__(item))

