from collections import OrderedDict


def limiter(limit, unique, lookup):
    __instances = OrderedDict()

    def decorator(cls):
        def add_instance(*args, **kwargs):
            obj = cls(*args, **kwargs)
            ID = getattr(obj, unique)
            if len(__instances) == limit:
                if ID not in __instances:
                    if lookup == 'FIRST':
                        obj = list(__instances.items())[0][1]
                    else:
                        obj = list(__instances.items())[-1][1]
                    return obj
                else:
                    obj = __instances[ID]
                    return obj
            else:
                __instances[ID] = obj
                return obj

        return add_instance

    return decorator


@limiter(3, 'ID', 'LAST')
class MyClass:
    def __init__(self, ID, value):
        self.ID = ID
        self.value = value


obj1 = MyClass(1, 5)  # создается экземпляр класса с идентификатором 1
obj2 = MyClass(2, 8)  # создается экземпляр класса с идентификатором 2
obj3 = MyClass(3, 10)  # создается экземпляр класса с идентификатором 3

obj4 = MyClass(4, 0)  # превышено ограничение limit, возвращается последний созданный экземпляр
obj5 = MyClass(2, 20)  # возвращается obj2, так как экземпляр с идентификатором 2 уже есть

print(obj4.value)
print(obj5.value)
