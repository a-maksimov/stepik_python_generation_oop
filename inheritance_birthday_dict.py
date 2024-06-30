from collections import UserDict
from datetime import date


class BirthdayDict(UserDict):
    def __setitem__(self, key, value):
        if value in self.data.values():
            print(f'Хей, {key}, не только ты празднуешь день рождения в этот день!')
        self.data[key] = value


birthdaydict = BirthdayDict()

birthdaydict['Боб'] = date(1987, 6, 15)
birthdaydict['Том'] = date(1984, 7, 15)
birthdaydict['Мария'] = date(1987, 6, 15)