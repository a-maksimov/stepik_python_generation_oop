from datetime import timedelta, datetime


class Lecture:
    __time_format = '%H:%M'

    def __init__(self, topic, start_time, duration):
        self.topic = topic
        self.start_time = datetime.strptime(start_time, self.__time_format)
        duration = datetime.strptime(duration, self.__time_format)
        self.duration = timedelta(hours=duration.hour, minutes=duration.minute)


class Conference:
    __time_format = '%H:%M'

    def __init__(self):
        self._lectures = []

    @property
    def lectures(self):
        if not self._lectures:
            return []
        return sorted(self._lectures, key=lambda x: x.start_time)

    def _check_schedule(self, lecture):
        if not self._lectures:
            return True

        first_lecture = self.lectures[0]
        if lecture.start_time + lecture.duration <= first_lecture.start_time:
            return True

        last_lecture = self.lectures[-1]
        if lecture.start_time >= last_lecture.start_time + last_lecture.duration:
            return True

        for i, item in enumerate(self.lectures):
            if item.start_time == lecture.start_time:
                return False
            end_time = item.start_time + item.duration
            if lecture.start_time < end_time:
                if lecture.start_time + lecture.duration <= item.start_time:
                    return True
                else:
                    return False
            if i + 1 == len(self.lectures):
                break
            next_lecture = self.lectures[i + 1]
            next_lecture_end_time = next_lecture.start_time + next_lecture.duration
            if lecture.start_time > next_lecture_end_time:
                continue
        return True

    def add(self, lecture):
        if not self._check_schedule(lecture):
            raise ValueError('Провести выступление в это время невозможно')
        self._lectures.append(lecture)

    def total(self):
        total = timedelta()
        for lecture in self._lectures:
            total += lecture.duration
        total = datetime(1, 1, 1) + total
        return total.strftime(self.__time_format)

    def longest_lecture(self):
        longest_duration = max(lecture.duration for lecture in self._lectures)
        longest_lecture = datetime(1, 1, 1) + longest_duration
        return longest_lecture.strftime(self.__time_format)

    def longest_break(self):
        longest_break_time = timedelta()
        for i, lecture in enumerate(self.lectures):
            if i + 1 == len(self.lectures):
                break
            end_time = lecture.start_time + lecture.duration
            next_lecture = self.lectures[i + 1]
            break_time = next_lecture.start_time - end_time
            if break_time > longest_break_time:
                longest_break_time = break_time
        longest_break = datetime(1, 1, 1) + longest_break_time
        return longest_break.strftime(self.__time_format)


# TEST_4:
# conference = Conference()
# conference.add(Lecture('Муравьиный алгоритм', '09:30', '02:00'))
# conference.add(Lecture('Жизнь после ChatGPT', '11:45', '04:00'))
# conference.add(Lecture('Простые числа', '08:00', '01:30'))
#
# print(conference.longest_lecture())
# print(conference.longest_break())

# TEST_4:
# 04:00
# 00:15

# TEST_5:
# conference = Conference()
# conference.add(Lecture('Введение в ООП', '09:30', '00:30'))
# conference.add(Lecture('Атрибуты объектов и классов', '08:00', '01:30'))
# conference.add(Lecture('Методы экземляра класса', '10:30', '02:00'))
#
# print(conference.longest_lecture())
# print(conference.longest_break())

# TEST_5:
# 02:00
# 00:30

# TEST_12:
conference = Conference()
conference.add(Lecture('Декораторы @classmethod и @staticmethod', '09:30', '00:30'))
conference.add(Lecture('Декоратор @singledispatchmethod', '09:00', '00:30'))
conference.add(Lecture('Создание, инициализация и очищение объектов', '11:00', '00:30'))
conference.add(Lecture('Унарные операторы и функции', '10:45', '00:15'))
conference.add(Lecture('Арифметические операции', '10:00', '00:30'))
conference.add(Lecture('Вызываемые объекты', '08:00', '01:00'))

print(conference.total())
print(conference.longest_lecture())
print(conference.longest_break())

# TEST_12:
# 03:15
# 01:00
# 00:15
