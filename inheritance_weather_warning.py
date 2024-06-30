from datetime import date


class WeatherWarning:
    def rain(self):
        print('Ожидаются сильные дожди и ливни с грозой')

    def snow(self):
        print('Ожидается снег и усиление ветра')

    def low_temperature(self):
        print('Ожидается сильное понижение температуры')


class WeatherWarningWithDate(WeatherWarning):
    format = '%d.%m.%Y'

    def print_date(self, date):
        print(date.strftime(self.__class__.format))

    def rain(self, date):
        self.print_date(date)
        super().rain()

    def snow(self, date):
        self.print_date(date)
        super().snow()

    def low_temperature(self, date):
        self.print_date(date)
        super().low_temperature()


weatherwarning = WeatherWarningWithDate()
dt = date(2022, 12, 12)

weatherwarning.rain(dt)
weatherwarning.snow(dt)
weatherwarning.low_temperature(dt)


