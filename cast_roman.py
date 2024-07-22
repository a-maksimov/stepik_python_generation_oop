from functools import total_ordering


@total_ordering
class RomanNumeral:
    _roman = {'I': 1, 'IV': 4, 'V': 5, 'IX': 9, 'X': 10, 'XL': 40, 'L': 50, 'XC': 90, 'C': 100, 'CD': 400, 'D': 500,
              'CM': 900, 'M': 1000}

    def __init__(self, number):
        self._number = number
        self._arab_number = self._to_arab()

    def __str__(self):
        return self._number

    def __int__(self):
        return self._arab_number

    def _to_arab(self):
        def _get_arab_number_from_slice(roman_slice, arab_number=0):
            for i in range(len(roman_slice)):
                new_arab_number = self._roman.get(roman_slice[i:])
                if not new_arab_number:
                    continue

                arab_number += new_arab_number
                new_roman_slice = roman_slice[:i]
                if not new_roman_slice:
                    return arab_number

                part_arab_number = _get_arab_number_from_slice(new_roman_slice, arab_number)
                return part_arab_number

        arab_number = _get_arab_number_from_slice(self._number)
        return arab_number

    def _to_roman(self, input_arab_number):
        _arab = {v: k for k, v in self._roman.items()}
        roman_number = _arab.get(input_arab_number)
        if roman_number:
            return roman_number

        def _find_closest_pair(number, roman_number=None):
            if new_roman_number := _arab.get(number):
                if roman_number:
                    roman_number += new_roman_number
                    return roman_number
                return new_roman_number

            filtered_roman = filter(lambda pair: pair[1] <= number, self._roman.items())
            closest_roman, closest_arab = min(filtered_roman, key=lambda pair: abs(pair[1] - number))
            new_roman_number = _find_closest_pair(
                number=number - closest_arab,
                roman_number=closest_roman
            )

            if roman_number:
                roman_number += new_roman_number
                return roman_number
            return new_roman_number

        roman_number = _find_closest_pair(input_arab_number)
        return roman_number

    def __add__(self, other):
        if not isinstance(other, self.__class__):
            return NotImplemented
        return RomanNumeral(self._to_roman(self._arab_number + other._arab_number))

    def __sub__(self, other):
        if not isinstance(other, self.__class__):
            return NotImplemented
        return RomanNumeral(self._to_roman(self._arab_number - other._arab_number))

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return NotImplemented

        return self._arab_number == other._arab_number

    def __lt__(self, other):
        if not isinstance(other, self.__class__):
            return NotImplemented

        return self._arab_number < other._arab_number


# TEST_5:
number = RomanNumeral('MXL') + RomanNumeral('MCDVIII') - RomanNumeral('I')

print(number)
print(int(number))

# TEST_5:
# MMCDXLVII
# 2447
