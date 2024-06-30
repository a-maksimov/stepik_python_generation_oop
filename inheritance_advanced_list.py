class AdvancedList(list):

    def join(self, sep=' '):
        return sep.join(map(str, self))

    def map(self, func):
        for i, item in enumerate(self):
            self[i] = func(item)

    def filter(self, func):
        length = len(self)
        for i in range(length):
            if func(self[i]):
                self.append(self[i])
        for _ in range(length):
            self.pop(0)


advancedlist = AdvancedList([1, 2, 3, 4, 5])
advancedlist.filter(lambda x: x % 2 == 0)

print(advancedlist)

# [2, 4]

