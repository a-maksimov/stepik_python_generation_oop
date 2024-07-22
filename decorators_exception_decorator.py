import functools


class exception_decorator:
    def __init__(self, func):
        functools.update_wrapper(self, func)
        self.func = func

    def __call__(self, *args, **kwargs):
        try:
            value = self.func(*args, **kwargs)
        except Exception as e:
            return None, type(e)

        return value, None


@exception_decorator
def func(x):
    return 2 * x + 1


print(func(1))
print(func('bee'))
