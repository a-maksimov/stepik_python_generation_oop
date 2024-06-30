import re


def is_fraction(string):
    pattern = r'-?\d+/(?!0*$)\d+'
    match = re.fullmatch(pattern, string)
    if match:
        return True
    return False


print(is_fraction('1000/1'))
print(is_fraction('71'))
print(is_fraction('1/0000'))
