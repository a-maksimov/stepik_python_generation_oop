import sys
from contextlib import contextmanager


@contextmanager
def reversed_print():
    standard_write = sys.stdout.write
    sys.stdout.write = lambda string: standard_write(string[::-1])
    yield
    sys.stdout.write = standard_write


print('Вывод вне блока with')

with reversed_print():
    print('Вывод внутри блока with')

print('Вывод вне блока with')

