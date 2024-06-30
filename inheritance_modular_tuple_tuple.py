class ModularTuple(tuple):
    def __new__(cls, iterable=tuple(), size=100):
        iterable = [item % size for item in iterable]
        instance = super().__new__(cls, iterable)
        return instance


modulartuple = ModularTuple([101, 102, 103, 104, 105])

print(modulartuple)
print(type(modulartuple))


