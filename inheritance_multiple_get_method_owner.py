def get_method_owner(cls, method):
    for element in cls.mro():
        if method in element.__dict__:
            return element


