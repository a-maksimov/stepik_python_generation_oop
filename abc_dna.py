from collections.abc import Sequence


class DNA(Sequence):
    complementarity = {
        "T": "A",
        "A": "T",
        "G": "C",
        "C": "G"
    }

    def __init__(self, chain):
        self._chain = chain
        self.chain = [(item, self.__class__.complementarity[item]) for item in chain]

    def __len__(self):
        return len(self.chain)

    def __getitem__(self, index):
        return self.chain[index]

    def __contains__(self, item):
        return item in self._chain

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return NotImplemented
        return self.chain == other.chain

    def __add__(self, other):
        if not isinstance(other, self.__class__):
            return NotImplemented
        return self.__class__(self._chain + other._chain)

    def __str__(self):
        return self._chain
    