from copy import deepcopy


class AttrDict:
    def __init__(self, data=None):
        if not data:
            data = {}

        self._data = deepcopy(data)

        for key, value in self._data.items():
            self.__dict__[key] = value

    def __getitem__(self, key):
        return self._data[key]

    def __setitem__(self, key, value):
        self._data[key] = value
        self.__dict__[key] = value

    def __len__(self):
        return len(self._data)

    def __iter__(self):
        yield from self._data


# TEST_4:
d = AttrDict()
d.name = 'Leonardo da Vinci'

try:
    print(d['name'])
except KeyError:
    print('Ключ отсутствует')

# TEST_4:
# Ключ отсутствует