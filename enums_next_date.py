from enum import Enum
from datetime import timedelta


class Weekday(Enum):
    MONDAY = 0
    TUESDAY = 1
    WEDNESDAY = 2
    THURSDAY = 3
    FRIDAY = 4
    SATURDAY = 5
    SUNDAY = 6


class NextDate:
    def __init__(self, today, weekday, considering_today=False):
        self.today = today
        self.today_weekday = Weekday(self.today.weekday())
        self.weekday = weekday
        if self.today_weekday is self.weekday:
            if considering_today:
                self._next_date = self.today
                self._days_until = 0
            else:
                self._next_date = self.today + timedelta(days=7)
                self._days_until = 7
        else:
            self._days_until = self.weekday.value - self.today_weekday.value
            if self._days_until < 0:
                self._days_until = 7 + self._days_until
            self._next_date = self.today + timedelta(days=self._days_until)

    def date(self):
        return self._next_date

    def days_until(self):
        return self._days_until


# TEST_4:
from datetime import date

for weekday in Weekday:
    today = date(2023, 4, 27)                              # четверг
    next_date = NextDate(today, weekday)

    print(next_date.date())
    print(next_date.days_until())


# TEST_4:
# 2023-05-01
# 4
# 2023-05-02
# 5
# 2023-05-03
# 6
# 2023-05-04
# 7
# 2023-04-28
# 1
# 2023-04-29
# 2
# 2023-04-30
# 3