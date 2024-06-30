class SparseArray:
    def __init__(self, default=None):
        self.default = default
        self.sequence = {}

    def __getitem__(self, key):
        return self.sequence.get(key, self.default)

    def __setitem__(self, key, value):
        self.sequence[key] = value

