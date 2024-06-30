import re
from string import ascii_uppercase


class CaseHelper:
    def __init__(self):
        pass

    @staticmethod
    def is_snake(string):
        pattern = r'_{2,}'
        match = re.search(pattern, string)
        if (
                string.lower() == string and
                all([string[0].isalpha(), string[-1].isalpha()]) and
                not match
        ):
            return True
        return False

    @staticmethod
    def is_upper_camel(string):
        if (
                string.lower() == string or
                '_' in string or
                string[0] not in ascii_uppercase
        ):
            return False
        return True

    @staticmethod
    def to_snake(string):
        word = string[1:]
        for sym in word:
            if sym in ascii_uppercase:
                word = word.replace(sym, '_' + sym.lower())

        string = string[0] + word
        string = string.lower()
        return string

    @staticmethod
    def to_upper_camel(string):
        pattern = r'_\w'
        matches = re.findall(pattern, string)
        for match in set(matches):
            sym = match[-1].upper()
            string = string.replace(match, sym)
        string = string[0].upper() + string[1:]
        return string


# print(CaseHelper.is_snake('beegeek'))
# print(CaseHelper.is_snake('bee_geek'))
# print(CaseHelper.is_snake('Beegeek'))
# print(CaseHelper.is_snake('BeeGeek'))
#
# print()
#
# print(CaseHelper.is_upper_camel('beegeek'))
# print(CaseHelper.is_upper_camel('bee_geek'))
# print(CaseHelper.is_upper_camel('Beegeek'))
# print(CaseHelper.is_upper_camel('BeeGeek'))
#
# print()
#
# print(CaseHelper.to_snake('Beegeek'))
# print(CaseHelper.to_snake('BeeGeek'))


# TEST_5:
# cases = ['assert_equal', 'tear_down', '__init__', 'assertEqual', 'setUp', 'tearDown', 'run', 'exit', 'setup']
#
# for case in cases:
#     print(CaseHelper.is_snake(case))

# TEST_5:
# True
# True
# False
# False
# False
# False
# True
# True
# True

# TEST_6:
# cases = ['assert_equal', 'tear_down', '__init__', 'assertEqual', 'setUp', 'tearDown', 'run', 'exit', 'setup', 'AssertEqual', 'SetUp']
#
# for case in cases:
#     print(CaseHelper.is_upper_camel(case))

# TEST_6:
# False
# False
# False
# False
# False
# False
# False
# False
# False
# True
# True

# TEST_7:
cases = ['AssertEqual', 'SetUp', 'TearDown', 'AddModuleCleanup', 'AssertRaisesRegex', 'AssertAlmostEqual', 'AssertNotAlmostEqual']

for case in cases:
    print(CaseHelper.to_snake(case))

# TEST_7:
# assert_equal
# set_up
# tear_down
# add_module_cleanup
# assert_raises_regex
# assert_almost_equal
# assert_not_almost_equal

# print(CaseHelper.to_snake('Beegeek'))
# print(CaseHelper.to_snake('BeeGeek'))
#
# print()

# print(CaseHelper.to_upper_camel('beegeek'))
# print(CaseHelper.to_upper_camel('bee_geek'))


