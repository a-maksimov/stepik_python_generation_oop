from functools import singledispatchmethod
from datetime import datetime, timedelta
from datetime import date


class BirthInfo:
    def __init__(self, birth_date):
        self.birth_date = self._cast_birth_date(birth_date)
        self.age = self.current_age(self.birth_date, datetime.today().date())

    @staticmethod
    def current_age(birthday, today):
        age = today.year - birthday.year - 1
        age += (today.month, today.day) >= (birthday.month, birthday.day)
        return age

    @singledispatchmethod
    @staticmethod
    def _cast_birth_date(birth_date):
        raise TypeError('Аргумент переданного типа не поддерживается')

    @_cast_birth_date.register
    @staticmethod
    def _cast_from_date(birth_date: date):
        return birth_date

    @_cast_birth_date.register
    @staticmethod
    def _cast_from_iso(birth_date: str):
        try:
            return datetime.fromisoformat(birth_date).date()
        except ValueError:
            raise TypeError('Аргумент переданного типа не поддерживается')

    @_cast_birth_date.register
    @staticmethod
    def _cast_from_tuple(birth_date: tuple):
        try:
            return datetime(*birth_date).date()
        except TypeError:
            raise TypeError('Аргумент переданного типа не поддерживается')

    @_cast_birth_date.register
    @staticmethod
    def _cast_from_tuple(birth_date: list):
        try:
            return datetime(*birth_date).date()
        except TypeError:
            raise TypeError('Аргумент переданного типа не поддерживается')


# TEST_6:
today = date.today()
for day in range(10):
    birthday = (today + timedelta(days=day)).replace(year=2000)
    birthinfo = BirthInfo(birthday)
    true_age = current_age(birthday, today)
    print(birthinfo.age == true_age)

# TEST_6:
# True
# True
# True
# True
# True
# True
# True
# True
# True
# True
