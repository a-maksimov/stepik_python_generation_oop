def auto_repr(args, kwargs):

    def decorator(cls):
        def _make_repr(self):
            repr_string = f'{self.__class__.__name__}('
            for arg in args:
                value = getattr(self, arg)
                if isinstance(value, str):
                    value = f"'{value}'"
                repr_string += f'{value}, '
            for kwarg in kwargs:
                value = getattr(self, kwarg)
                if isinstance(value, str):
                    value = f"'{value}'"
                repr_string += f'{kwarg}={value}, '
            repr_string = repr_string.strip(', ')
            repr_string += ')'
            return repr_string

        setattr(cls, '__repr__', _make_repr)
        return cls

    return decorator


# TEST_2:
@auto_repr(args=['name', 'surname'], kwargs=[])
class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname


person = Person('Gvido', 'van Rossum')

print(person)

# TEST_2:
# Person('Gvido', 'van Rossum')
