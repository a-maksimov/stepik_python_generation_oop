import json


def jsonattr(filename):
    def decorator(cls):
        with open(filename) as file:
            for field, value in json.load(file).items():
                setattr(cls, field, value)
        return cls

    return decorator