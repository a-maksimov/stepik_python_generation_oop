from collections import OrderedDict


class Row:
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            object.__setattr__(self, key, value)

    def __setattr__(self, key, value):
        if self.__dict__.get(key):
            raise AttributeError('Изменение значения атрибута невозможно')
        raise AttributeError('Установка нового атрибута невозможна')

    def __delattr__(self, item):
        raise AttributeError('Удаление атрибута невозможно')

    def __repr__(self):
        string = ', '.join(
            [
                f"{key}={value}" if not isinstance(value, str) else f"{key}='{value}'"
                for key, value in self.__dict__.items()
            ]
        )
        return f"Row({string})"

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return OrderedDict(self.__dict__) == OrderedDict(other.__dict__)
        return NotImplemented

    def __hash__(self):
        return hash(str(self.__dict__))


row = Row(a='A', b='B', c='C')

print(row)
print(row.a, row.b, row.c)
#
# print()
#
# row1 = Row(a=1, b=2, c=3)
# row2 = Row(a=1, b=2, c=3)
# row3 = Row(b=2, c=3, a=1)
#
# print(row1 == row2)
# print(hash(row1) == hash(row2))
# print(row1 == row3)
# print(hash(row1) == hash(row3))
#
# print()
#
# row = Row(a=1, b=2, c=3)
#
# try:
#     row.d = 4
# except AttributeError as e:
#     print(e)

# Установка нового атрибута невозможна

print()

# TEST_6:
rows = {Row(a=1, b=2, c=3): 10, Row(d=4, e=5, f=6): 20}

print(rows)

# {Row(a=1, b=2, c=3): 10, Row(d=4, e=5, f=6): 20}
