from itertools import groupby


class Grouper:
    def __init__(self, iterable, key):
        sorted_iterable = sorted(iterable, key=key)
        grouped_iterable = groupby(sorted_iterable, key=key)
        self._grouped_iterable = {}
        for group_key, group in grouped_iterable:
            self._grouped_iterable[group_key] = list(group)

        self._key = key

    def __len__(self):
        return len(self._grouped_iterable)

    def __contains__(self, key):
        return key in self._grouped_iterable

    def __getitem__(self, key):
        return self._grouped_iterable[key]

    def __iter__(self):
        yield from self._grouped_iterable.items()

    def add(self, item):
        key = self._key(item)
        self._grouped_iterable.setdefault(key, []).append(item)

    def group_for(self, item):
        return self._key(item)


grouper = Grouper(['bee', 'geek', 'one', 'two', 'five', 'hi'], key=len)

print(grouper[2])
print(grouper[3])
print(grouper[4])


grouper = Grouper(['bee', 'geek', 'one', 'two', 'five', 'hi'], key=len)

print(3 in grouper)
print('bee' in grouper)


grouper = Grouper(['hi'], key=lambda s: s[0])
print(len(grouper))

grouper.add('hello')
grouper.add('bee')
grouper.add('big')

print(len(grouper))

grouper.add('geek')
print(grouper['h'])
print(grouper['b'])
print(grouper['g'])

print(len(grouper))