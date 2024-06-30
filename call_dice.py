from random import randint


class Dice:
    def __init__(self, sides):
        self.sides = sides

    def __call__(self):
        return randint(1, self.sides)


kingdice = Dice(6)

print(kingdice() in [1, 2, 3, 4, 5, 6])
print(kingdice() in [1, 2, 3, 4, 5, 6])
print(kingdice() in [7, 8, 9, 10])

print()

# TEST_3:
kingdice = Dice(1)

print(kingdice() == 1)
print(kingdice() in [1, 2])
print(kingdice() in [3, 4])
print(kingdice() in [7, 8, 9, 10])

# TEST_3:
# True
# True
# False
# False
