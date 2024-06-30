from collections import UserList


class DefaultList(UserList):
    def __init__(self, iterable=None, default=None):
        if iterable is None:
            iterable = []
        self._default = default
        super().__init__(iterable)

    def __getitem__(self, index):
        try:
            return self.data[index]
        except IndexError:
            return self._default

