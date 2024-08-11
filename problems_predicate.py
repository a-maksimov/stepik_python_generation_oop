import functools


class predicate:
    def __init__(self, func):
        functools.update_wrapper(self, func)
        self.func = func

    def __call__(self, *args, **kwargs):
        value = self.func(*args, **kwargs)
        return value

    def __and__(self, other):
        return self.__class__(lambda *args, **kwargs: self(*args, **kwargs) and other(*args, **kwargs))

    def __or__(self, other):
        return self.__class__(lambda *args, **kwargs: self(*args, **kwargs) or other(*args, **kwargs))

    def __invert__(self):
        return self.__class__(lambda *args, **kwargs: not self(*args, **kwargs))


@predicate
def is_even(num):
    return num % 2 == 0


@predicate
def is_positive(num):
    return num > 0


print((is_even & is_positive)(4))  # True; равнозначно is_even(4) and is_positive(4)
