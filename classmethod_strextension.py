class StrExtension:

    @staticmethod
    def remove_vowels(string):
        vowels = "aeiouy"
        for vowel in vowels:
            string = string.replace(vowel, '')
            string = string.replace(vowel.upper(), '')

        return string

    @staticmethod
    def leave_alpha(string):
        for symbol in string:
            if not symbol.isalpha():
                string = string.replace(symbol, '')

        return string

    @staticmethod
    def replace_all(string, chars, char):
        for symbol in string:
            if symbol in chars:
                string = string.replace(symbol, char)

        return string


print(StrExtension.remove_vowels('Python'))
print(StrExtension.remove_vowels('Stepik'))
print()

print(StrExtension.leave_alpha('Python111'))
print(StrExtension.leave_alpha('__Stepik__()'))
print()

print(StrExtension.replace_all('Python', 'Ptn', '-'))
print(StrExtension.replace_all('Stepik', 'stk', '#'))
print()


