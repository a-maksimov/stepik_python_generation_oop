from collections import UserString


class MutableString(UserString):
    def __init__(self, string=None):
        if not string:
            string = ''
        super().__init__(string)
        self._string = list(self.data)

    def __getitem__(self, index):
        return self.__class__(self._string[index])

    def __len__(self):
        return len(self._string)

    def __iter__(self):
        yield from self._string

    def __add__(self, other):
        if isinstance(other, self.__class__):
            return self.__class__(''.join(self._string + other._string))
        return NotImplemented

    def __delitem__(self, index):
        del self._string[index]

    def __setitem__(self, index, value):
        if isinstance(index, int):
            new_string = self._string[:index] + list(value)
            if len(new_string) < len(self._string):
                new_string += self._string[len(new_string):]
            self._string = new_string
            return
        self._string[index] = list(value)

    def lower(self):
        self._string = [item.lower() for item in self._string]

    def upper(self):
        self._string = [item.upper() for item in self._string]

    def sort(self, key=None, reverse=False):
        self._string = sorted(self._string, key=key, reverse=reverse)

    def __str__(self):
        return ''.join(self._string)


mutablestring = MutableString('Beegeek')

mutablestring.lower()
print(mutablestring)
mutablestring.upper()
print(mutablestring)
mutablestring.sort()
print(mutablestring)