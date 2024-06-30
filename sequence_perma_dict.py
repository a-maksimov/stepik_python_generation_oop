from copy import deepcopy


class PermaDict:
    def __init__(self, data=None):
        if not data:
            data = {}

        self._data = deepcopy(data)

    def __getitem__(self, key):
        return self._data[key]

    def __setitem__(self, key, value):
        if key in self._data:
            raise KeyError('Изменение значения по ключу невозможно')
        self._data[key] = value

    def __len__(self):
        return len(self._data)

    def __iter__(self):
        yield from self._data

    def keys(self):
        return self._data.keys()

    def values(self):
        return self._data.values()

    def items(self):
        return self._data.items()

    def __delitem__(self, key):
        del self._data[key]
