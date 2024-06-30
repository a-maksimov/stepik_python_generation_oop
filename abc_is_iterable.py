from collections.abc import Iterable, Iterator


def is_iterable(obj):
    if isinstance(obj, Iterable):
        return True
    return False


def is_iterator(obj):
    if isinstance(obj, Iterator):
        return True
    return False
