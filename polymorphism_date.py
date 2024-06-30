from datetime import date


class USADate:
    def __init__(self, year, month, day):
        self.date = date(year, month, day)

    def format(self):
        date_format = '%m-%d-%Y'
        return self.date.strftime(date_format)

    def iso_format(self):
        return self.date.isoformat()


class ItalianDate:
    def __init__(self, year, month, day):
        self.date = date(year, month, day)

    def format(self):
        date_format = '%d/%m/%Y'
        return self.date.strftime(date_format)

    def iso_format(self):
        return self.date.isoformat()
