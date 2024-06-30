class NonNegativeObject:
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            if isinstance(value, (int, float)):
                if value < 0:
                    self.__dict__[key] = -value
                else:
                    self.__dict__[key] = value
            else:
                self.__dict__[key] = value
