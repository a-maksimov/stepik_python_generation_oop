import functools


def singleton(cls):
    cls._instance = None
    old_new = cls.__new__

    @functools.wraps(old_new)
    def new_new(cls, *args, **kwargs):
        old_new(cls)
        if cls._instance is None:
            cls._instance = object.__new__(cls)
        return cls._instance

    cls.__new__ = new_new
    return cls


@singleton
class Person:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f'Person({self.name!r})'


instances = [Person('John Doe') for _ in range(1000)]
person = Person('Doe John')
print(person)
print(instances[389])
print(all(instance is person for instance in instances))