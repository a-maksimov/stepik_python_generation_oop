from contextlib import contextmanager


@contextmanager
def safe_open(filename, mode='r'):
    try:
        with open(filename, mode) as file:
            yield file, None
    except Exception as e:
        yield None, e

