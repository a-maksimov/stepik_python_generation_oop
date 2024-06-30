from time import perf_counter


class AdvancedTimer:
    def __init__(self):
        self._start = None
        self._runs = None

    @property
    def runs(self):
        if self._runs is None:
            return []
        return self._runs

    @property
    def min(self):
        return min(self.runs, default=None)

    @property
    def max(self):
        return max(self.runs, default=None)

    @property
    def last_run(self):
        if not self._runs:
            return
        return self._runs[-1]

    def __enter__(self):
        self._start = perf_counter()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self._runs is None:
            self._runs = []
        self.runs.append(perf_counter() - self._start)
        return True


timer = AdvancedTimer()

print(timer.runs)
print(timer.last_run)
print(timer.min)
print(timer.max)


from time import sleep

timer = AdvancedTimer()

with timer:
    sleep(1.5)
print(round(timer.last_run, 1))

with timer:
    sleep(0.7)
print(round(timer.last_run, 1))

with timer:
    sleep(1)
print(round(timer.last_run, 1))