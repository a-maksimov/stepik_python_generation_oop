class NonNegativeInteger:
    def __init__(self, name, default=None):
        self._name = name
        self._default = default

    def __get__(self, obj, cls):
        if obj is None:
            return self
        if self._name in obj.__dict__:
            return obj.__dict__[self._name]
        elif self._default is not None:
            return self._default
        else:
            raise AttributeError('Атрибут не найден')

    def __set__(self, obj, value):
        if isinstance(value, int) and value >= 0:
            obj.__dict__[self._name] = value
        else:
            raise ValueError('Некорректное значение')


class Student:
    score = NonNegativeInteger('score', 0)


student = Student()

print(student.score)
student.score = 0
print(student.score)
