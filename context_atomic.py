from copy import deepcopy


class Atomic:
    def __init__(self, data, deep=False):
        if deep:
            self._data_copy = deepcopy(data)
        else:
            self._data_copy = data.copy()
        self.data = data
        self.deep = deep

    def __enter__(self):
        return self.data

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            if type(self.data) is list:
                self.data[:] = self._data_copy
            elif type(self.data) is set:
                self.data.clear()
                self.data.update({item for item in self._data_copy})
            elif type(self.data) is dict:
                self.data.clear()
                self.data.update({k: v for k, v in self._data_copy.items()})

            return True


# numbers = [1, 2, 3, 4, 5]
#
# with Atomic(numbers) as atomic:
#     atomic.append(6)
#     atomic[2] = 0
#     del atomic[1]
#
# print(numbers)
#
# numbers = [1, 2, 3, 4, 5]
#
# with Atomic(numbers) as atomic:
#     atomic.append(6)
#     atomic[2] = 0
#     del atomic[100]           # обращение по несуществующему индексу
#
# print(numbers)


# TEST_5:
numbers = {1, 2, 3, 4, 5}

with Atomic(numbers) as atomic:
    atomic.add(6)
    atomic.append(7)           # добавление элемента с помощью несуществующего метода

print(sorted(numbers))

with Atomic(numbers) as atomic:
    atomic.add(6)

print(sorted(numbers))