from datetime import date
from functools import total_ordering


@total_ordering
class Month:
    def __init__(self, year, month):
        self.month = date(year, month, 1)

    def __repr__(self):
        return f"Month({self.month.year}, {self.month.month})"

    def __str__(self):
        date_format = '%Y-%#m'
        return self.month.strftime(date_format)

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.month == other.month
        elif isinstance(other, tuple) and len(other) == 2:
            return self.month.year == other[0] and self.month.month == other[1]
        else:
            return NotImplemented

    def __lt__(self, other):
        if isinstance(other, self.__class__):
            return self.month < other.month
        elif isinstance(other, tuple):
            return tuple([self.month.year, self.month.month]) < other
        else:
            return NotImplemented


print(Month(1999, 12) == Month(1999, 12))
print(Month(1999, 12) < Month(2000, 1))
print(Month(1999, 12) > Month(2000, 1))
print(Month(1999, 12) <= Month(1999, 12))
print(Month(1999, 12) >= Month(2000, 1))

print()

months = [Month(1998, 12), Month(2000, 1), Month(1999, 12)]

print(sorted(months))

print()

months = [Month(1998, 12), Month(2000, 1), Month(1999, 12)]

print(min(months))
print(max(months))

print()

# TEST_6:
print(Month(1999, 12) == (1999, 12))
print(Month(1999, 12) < (2000, 1))
print(Month(1999, 12) > (2000, 1))
print(Month(1999, 12) <= (1999, 12))
print(Month(1999, 12) >= (2000, 1))

# TEST_6:
# True
# True
# False
# True
# False
