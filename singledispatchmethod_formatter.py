from functools import singledispatchmethod
from itertools import starmap


class Formatter:

    @singledispatchmethod
    @staticmethod
    def format(data):
        raise TypeError('Аргумент переданного типа не поддерживается')


    @format.register(int)
    @staticmethod
    def format_int(data):
        print(f'Целое число: {data}')


    @format.register(float)
    @staticmethod
    def format_float(data):
        print(f'Вещественное число: {data}')


    @format.register(list)
    @staticmethod
    def format_list(data):
        data = map(str, data)
        print(f'Элементы списка: {", ".join(data)}')


    @format.register(tuple)
    @staticmethod
    def format_tuple(data):
        data = map(str, data)
        print(f'Элементы кортежа: {", ".join(data)}')


    @format.register(dict)
    @staticmethod
    def format_dict(data):

        def format_item(item):
            if isinstance(item, str):
                return f"'{item}'"
            return str(item)

        data = starmap(lambda i, j: f'({format_item(i)}, {format_item(j)})', map(tuple, data.items()))
        print(f'Пары словаря: {", ".join(data)}')


Formatter.format(1337)
Formatter.format(20.77)

print()

Formatter.format([10, 20, 30, 40, 50])
Formatter.format(([1, 3], [2, 4, 6]))

print()

Formatter.format({'Cuphead': 1, 'Mugman': 3})
Formatter.format({1: 'one', 2: 'two'})
Formatter.format({1: True, 0: False})
