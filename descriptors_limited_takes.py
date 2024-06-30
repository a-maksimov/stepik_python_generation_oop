class MaxCallsException(Exception):
    pass


class LimitedTakes:
    def __init__(self, times):
        self._times = times + 1

    def __set_name__(self, owner, name):
        self._attr = name

    def __get__(self, obj, cls):
        if obj is None:
            return self
        if self._attr in obj.__dict__:
            self._times -= 1
            if self._times > 0:
                return obj.__dict__[self._attr]
            else:
                raise MaxCallsException('Превышено количество доступных обращений')
        else:
            raise AttributeError('Атрибут не найден')

    def __set__(self, obj, value):
        obj.__dict__[self._attr] = value


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
