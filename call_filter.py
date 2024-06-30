class Filter:
    def __init__(self, predicate):
        self.predicate = predicate

    def __call__(self, iterable):
        if self.predicate is None:
            self.predicate = bool
        return [
            item for item in iterable
            if self.predicate(item) is True
        ]


leave_even = Filter(lambda x: x % 2 == 0)
numbers = [1, 2, 3, 4, 5, 6]

print(leave_even(numbers))
