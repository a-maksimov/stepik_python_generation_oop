class MutableString :
    def __init__(self, string=None):
        if not string:
            string = []
        self._string = list(string)

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

    def __str__(self):
        return ''.join(self._string)

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.__str__()}')"


# TEST_5:
# mutablestring = MutableString('beegeek')
#
# s1 = mutablestring[2:]
# s2 = mutablestring[:5]
# s3 = mutablestring[2:5:2]
#
# print(s1, type(s1))
# print(s2, type(s2))
# print(s3, type(s3))

# # TEST_5:
# egeek <class '__main__.MutableString'>
# beege <class '__main__.MutableString'>
# ee <class '__main__.MutableString'>


# TEST_13:
mutablestring = MutableString('beegeek')

mutablestring[-1] = 'ee'
print(mutablestring)

mutablestring[-2:] = 'geek'
print(mutablestring)

# # TEST_13:
# beegeeee
# beegeegeek