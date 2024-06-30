class AdvancedTuple(tuple):

    def __add__(self, other):
        if isinstance(other, dict):
            other = list(other.keys())
        return self.__class__(list(self) + list(other))

    def __radd__(self, other):
        if isinstance(other, dict):
            other = list(other.keys())
        return self.__class__(list(other) + list(self))


