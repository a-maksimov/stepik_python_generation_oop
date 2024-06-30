class HourClock:
    def __init__(self, hour):
        self.hours = hour

    def set_hour(self, hour):
        if hour not in range(1, 13, 1):
            raise ValueError('Некорректное время')
        else:
            self._hours = hour

    def get_hour(self):
        return self._hours

    hours = property(get_hour, set_hour)
