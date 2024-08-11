from collections import UserDict


class MultiKeyDict(UserDict):
    def __init__(self, *args, **kwargs):
        self._aliases = {}
        super().__init__(*args, **kwargs)
        self._reverse_aliases = {k: [] for k in self.data}

    def alias(self, key, alias_key):
        self._aliases[alias_key] = key
        self._reverse_aliases[key].append(alias_key)

    def __getitem__(self, key):
        if key in self.data:
            return self.data.__getitem__(key)

        return self.data.__getitem__(self._aliases[key])

    def __setitem__(self, key, value):
        if key in self.data:
            self.data.__setitem__(key, value)
            return

        if self._aliases.get(key):
            self.data.__setitem__(self._aliases[key], value)
            return

        self.data.__setitem__(key, value)

    def __delitem__(self, key):
        if key in self.data:
            reverse_aliases = self._reverse_aliases.get(key, [])
            if reverse_aliases:
                new_key = next(iter(reverse_aliases))
                reverse_aliases.remove(new_key)
                self._reverse_aliases[new_key] = reverse_aliases
                del self._reverse_aliases[key]
                self.data[new_key] = self.data[key]
                self._aliases[new_key] = new_key
                for alias, value in self._aliases.items():
                    if value == key:
                        self._aliases[alias] = new_key

        self.data.__delitem__(key)


# TEST_8:
multikeydict = MultiKeyDict(x=100)

multikeydict.alias('x', 'z')
multikeydict.alias('x', 't')
del multikeydict['x']
multikeydict['z'] += 1
print(multikeydict['z'])
print(multikeydict['t'])


# # TEST_8:
# 101
# 101
