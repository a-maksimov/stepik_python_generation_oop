import functools


class type_check:
    def __init__(self, types):
        self._types = types

    def __call__(self, func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for arg, _type in zip(args, self._types):
                if not isinstance(arg, _type):
                    raise TypeError
            return func(*args, **kwargs)

        return wrapper


@type_check([int, int, str, list])
def add(a, b):
    """sum a and b"""
    return a + b

print(add.__name__)
print(add.__doc__)
print(add(1, 2))