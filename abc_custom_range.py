from collections.abc import Sequence


class CustomRange(Sequence):
    def __init__(self, *args):
        self._sequence = []
        for arg in args:
            if isinstance(arg, int):
                self._sequence.append(arg)
            elif isinstance(arg, str):
                _range = arg.split('-')
                for item in range(*map(int, _range)):
                    self._sequence.append(item)

    def __len__(self):
        return len(self._sequence)

    def __getitem__(self, index):
        return self._sequence[index]


