from abc import ABC, abstractmethod


class Validator(ABC):
    def __set_name__(self, owner, name):
        self._attr = '_' + name

    def __get__(self, obj, cls):
        if obj is None:
            return self
        if self._attr in obj.__dict__:
            return obj.__dict__[self._attr]
        else:
            raise AttributeError('Атрибут не найден')

    @abstractmethod
    def validate(self, item):
        pass

    def __set__(self, obj, value):
        is_valid = self.validate(value)
        if is_valid:
            setattr(obj, self._attr, value)


class Number(Validator):
    def __init__(self, minvalue=None, maxvalue=None):
        self._minvalue = minvalue
        self._maxvalue = maxvalue

    def validate(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError('Устанавливаемое значение должно быть числом')
        if self._minvalue is not None and value < self._minvalue:
            raise ValueError(f'Устанавливаемое число должно быть больше или равно {self._minvalue}')
        if self._maxvalue is not None and value > self._maxvalue:
            raise ValueError(f'Устанавливаемое число должно быть меньше или равно {self._maxvalue}')
        return True


class String(Validator):
    def __init__(self, minsize=None, maxsize=None, predicate=None):
        self._minsize = minsize
        self._maxsize = maxsize
        self._predicate = predicate

    def validate(self, value):
        if not isinstance(value, str):
            raise TypeError('Устанавливаемое значение должно быть строкой')
        if self._minsize is not None and len(value) < self._minsize:
            raise ValueError(f'Длина устанавливаемой строки должна быть больше или равна {self._minsize}')
        if self._maxsize is not None and len(value) > self._maxsize:
            raise ValueError(f'Длина устанавливаемой строки должна быть меньше или равна {self._maxsize}')
        if self._predicate is not None and not self._predicate(value):
            raise ValueError(f'Устанавливаемая строка не удовлетворяет дополнительным условиям')
        return True


class Student:
    age = Number(18, 99)


student = Student()
student.age = 19
print(student.age)
