from string import ascii_uppercase


def snake_case(attrs=False):
    def to_snake(string):
        if string[0] == '_' or string[0] in ascii_uppercase:
            word = string[1:]
        else:
            word = string
        for sym in word:
            if sym in ascii_uppercase:
                word = word.replace(sym, '_' + sym.lower())

        if string[0] == '_':
            if word[0] == '_':
                return word
            else:
                return string[0] + word
        elif string[0] in ascii_uppercase:
            return string[0].lower() + word

        return word

    def decorator(cls):
        for attr in list(cls.__dict__):
            if '__' not in attr and not callable(getattr(cls, attr)) == attrs:
                new_attr = to_snake(attr)
                setattr(cls, new_attr, getattr(cls, attr))
                delattr(cls, attr)
        return cls

    return decorator


@snake_case()
class MyClass:
    def FirstMethod(self):
        return 1

    def superSecondMethod(self):
        return 2


obj = MyClass()

print(obj.first_method())
print(obj.super_second_method())

# TEST_6:
# @snake_case()
# class MyClass:
#     def _FirstMethod(self):
#         return 1
#
#     def _superSecondMethod(self):
#         return 2
#
#
# obj = MyClass()
#
# print(obj._first_method())
# print(obj._super_second_method())

# TEST_6:
# 1
# 2


from functools import wraps
# from inflection import camelize, underscore
#
# def snake_case(attrs=False):
#     def decorator(cls):
#         for i,j in list(cls.__dict__.items()):
#             if i.count('_') < 4 and not callable(j) == attrs:
#                 attr = j
#                 delattr(cls,i)
#                 setattr(cls,underscore(i),attr)
#         return cls
#     return decorator