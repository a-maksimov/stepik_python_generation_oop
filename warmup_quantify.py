def quantify(iterable, predicate):
    if not predicate:
        predicate = bool
    return sum(map(predicate, iterable))


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(quantify(numbers, lambda x: x % 2 == 0))