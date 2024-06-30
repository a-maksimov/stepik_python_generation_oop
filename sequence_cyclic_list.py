class CyclicList:
    def __init__(self, iterable=None):
        if iterable is None:
            iterable = []
        self.iterable = iterable.copy()

    def get_index(self, index):
        if index > len(self.iterable) - 1:
            return index % len(self.iterable)
        return index

    def append(self, item):
        self.iterable.append(item)

    def pop(self, index=None):
        if index is None:
            return self.iterable.pop()
        return self.iterable.pop(self.get_index(index))

    def __len__(self):
        return len(self.iterable)

    def __getitem__(self, index):
        return self.iterable[self.get_index(index)]


# TEST_6:
data = [1, 2, 3, 4, 5]
cycliclist = CyclicList(data)
data.extend([6, 7, 8, 9, 10])

count = 0
for item in cycliclist:
    if count == 10:
        break
    print(item, end=' ')
    count += 1

# 1 2 3 4 5 1 2 3 4 5
