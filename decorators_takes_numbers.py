import functools
from itertools import chain


class takes_numbers:
    def __init__(self, func):
        functools.update_wrapper(self, func)
        self.func = func

    def __call__(self, *args, **kwargs):
        if any([not isinstance(arg, (int, float)) for arg in chain(args, kwargs.values())]):
            raise TypeError('Аргументы должны принадлежать типам int или float')
        value = self.func(*args, **kwargs)
        return value


@takes_numbers
def mul(a, b):
    return a * b


try:
    print(mul(1, '2'))
except TypeError as error:
    print(error)
