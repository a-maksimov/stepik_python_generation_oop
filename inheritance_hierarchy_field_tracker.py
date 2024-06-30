class FieldTracker:
    def __init__(self):
        self._initial_values = self.__dict__.copy()

    def base(self, name):
        return self._initial_values[name]

    def has_changed(self, name):
        if not getattr(self, name) == self._initial_values[name]:
            return True
        return False

    def changed(self):
        return {
            name: self._initial_values[name]
            for name in self.__class__.fields
            if self.has_changed(name)
        }

    def save(self):
        self._initial_values.update(
            {name: getattr(self, name) for name in self.__class__.fields}
        )


class Point(FieldTracker):
    fields = ('x', 'y', 'z')

    def __init__(self, x, y, z):
        self.x, self.y, self.z = x, y, z
        super().__init__()


point = Point(1, 2, 3)

print(point.base('x'))
print(point.has_changed('x'))
print(point.changed())