class TypeChecked:
    def __init__(self, *types):
        self._types = types

    def __set_name__(self, owner, name):
        self._attr = name

    def __get__(self, obj, cls):
        if obj is None:
            return self
        if self._attr in obj.__dict__:
            return obj.__dict__[self._attr]
        else:
            raise AttributeError('Атрибут не найден')

    def __set__(self, obj, value):
        if isinstance(value, self._types):
            obj.__dict__[self._attr] = value
        else:
            raise TypeError('Некорректное значение')


class Student:
    name = LimitedTakes(3)


student = Student()
student.name = 'Gwen'

print(student.name)
print(student.name)
print(student.name)

try:
    print(student.name)
except MaxCallsException as e:
    print(e)
