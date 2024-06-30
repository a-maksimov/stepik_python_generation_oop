class AnyClass:
    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            self.__dict__[k] = v

        self._attributes = ", ". join([f'{k}={self._format_item(v)}'
                                       for k, v in self.__dict__.items()])

    @staticmethod
    def _format_item(item):
        if isinstance(item, str):
            return "'" + f'{item}' + "'"
        return item

    def __repr__(self):
        return f"AnyClass({self._attributes})"

    def __str__(self):
        return f"AnyClass: {self._attributes}"


obj = AnyClass(attr1=10, attr2='beegeek', attr3=True, attr4=[1, 2, 3], attr5=('one', 'two'), attr6=None)

print(str(obj))
print(repr(obj))