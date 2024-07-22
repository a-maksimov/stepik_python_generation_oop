import functools


class reverse_args:
    def __init__(self, func):
        functools.update_wrapper(self, func)
        self.func = func

    def __call__(self, *args, **kwargs):
        value = self.func(*args[::-1], **kwargs)
        return value


@reverse_args
def power(a, n):
    return a ** n


print(power(2, 3))
