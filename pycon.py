import calendar
import datetime


def get_pycon_date(year, month):
    date_format = '%d.%m.%Y'
    year = int(year)
    month = int(month)
    cal = calendar.monthcalendar(year, month)
    cal = [week for week in cal if week[3] > 0]
    date = datetime.date(year, month, cal[3][3])

    return date.strftime(date_format)


print(get_pycon_date(input(), input()))
