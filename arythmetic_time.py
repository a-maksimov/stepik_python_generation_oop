from datetime import datetime, timedelta


class Time:
    def __init__(self, hours, minutes):
        self._hours, self._minutes = self._parse_time(hours, minutes)
        self._time = datetime(
            year=1, month=1, day=1, hour=self._hours, minute=self._minutes
        )
        self._format = '%H:%M'

    @staticmethod
    def _parse_time(hours, minutes):
        hours = hours % 24
        hours_from_minutes = minutes // 60
        hours_from_minutes = hours_from_minutes % 24
        hours += hours_from_minutes
        minutes = minutes % 60

        return hours, minutes

    @property
    def time(self):
        return self._time.time()

    @property
    def hours(self):
        return self._time.hour

    @property
    def minutes(self):
        return self._time.minute

    def __add__(self, other):
        if not isinstance(other, self.__class__):
            return NotImplemented
        hours, minutes = self._parse_time(other.hours, other.minutes)
        add_time = self._time + timedelta(hours=hours, minutes=minutes)
        return self.__class__(add_time.hour, add_time.minute)

    def __iadd__(self, other):
        if not isinstance(other, self.__class__):
            return NotImplemented

        hours = self._hours + other.hours
        minutes = self._minutes + other.minutes
        self._hours, self._minutes = self._parse_time(hours, minutes)
        self._time = datetime(
            year=1, month=1, day=1, hour=self._hours, minute=self._minutes
        )
        return self

    def __str__(self):
        return self._time.strftime(self._format)


time1 = Time(2, 30)
time2 = Time(3, 10)

print(time1 + time2)
print(time2 + time1)

time1 = Time(2, 30)
time2 = Time(3, 10)

time1 += time2

print(time1)
print(time2)

# TEST_8:
t = Time(22, 0)
t += Time(3, 0)
print(t)