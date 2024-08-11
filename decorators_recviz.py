import functools


def recviz(func):
    func.counter = 0

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        args_string = ', '.join([f"'{arg}'" if isinstance(arg, str) else str(arg) for arg in args])
        kwargs_string = ', '.join(f'{k}={f"'{v}'" if isinstance(v, str) else v}' for k, v in kwargs.items())
        print('    ' * func.counter, end='')
        print('-> ' + f'{func.__name__}({args_string}{", " if kwargs_string else ""}{kwargs_string})')
        func.counter += 1
        value = func(*args, **kwargs)
        func.counter -= 1
        print('    ' * func.counter, end='')
        print('<- ' + f'{f"'{value}'" if isinstance(value, str) else str(value)}')

        return value

    return wrapper


@recviz
def add(a, b, c, d, e):
    return (a + b + c) * (d + e)


add('a', b='b', c='c', d=3, e=True)


@recviz
def fib(n):
    if n <= 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


fib(4)

# -> fib(4)
#     -> fib(3)
#         -> fib(2)
#         <- 1
#         -> fib(1)
#         <- 1
#     <- 2
#     -> fib(2)
#     <- 1
# <- 3
