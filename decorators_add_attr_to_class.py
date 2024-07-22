def add_attr_to_class(**attrs):
    def decorator(cls):
        for attr, value in attrs.items():
            setattr(cls, attr, value)
        return cls

    return decorator


@add_attr_to_class(first_attr=1, second_attr=2)
class MyClass:
    pass

print(MyClass.first_attr)
print(MyClass.second_attr)