from copy import deepcopy
from itertools import tee, islice


class SequenceZip:
    def __init__(self, *args):
        self._sequences = deepcopy(args)

    def __len__(self):
        self._sequences, sequences_copy = tee(self._sequences)
        return sum(1 for _ in zip(*sequences_copy))

    def __getitem__(self, index):
        self._sequences, sequences_copy = tee(self._sequences)
        return next(islice(zip(*sequences_copy), index, index + 1))

    def __iter__(self):
        self._sequences, sequences_copy = tee(self._sequences)
        yield from zip(*sequences_copy)


# TEST_4:
x, y, z = [1, 2, 3], [4, 5, 6], [7, 8, 9]
sequencezip = SequenceZip(x, y, z)

print(sequencezip[2])
x[-1], z[-1] = z[-1], x[-1]
print(sequencezip[2])

# TEST_4:
# (3, 6, 9)
# (3, 6, 9)

# TEST_5:
many_large_sequences = [range(100000) for _ in range(100)]
sequencezip = SequenceZip(*many_large_sequences)
print(sequencezip[99999])
