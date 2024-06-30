from copy import deepcopy


class HistoryDict:
    def __init__(self, data=None):
        if not data:
            data = {}

        self._data = deepcopy(data)

        self._history = {key: [value] for key, value in data.items()}

    def __getitem__(self, key):
        return self._data[key]

    def __setitem__(self, key, value):
        self._history[key] = self._history.get(key, []) + [value]
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
        del self._history[key]

    def history(self, key):
        return self._history.get(key, [])

    def all_history(self):
        return self._history

