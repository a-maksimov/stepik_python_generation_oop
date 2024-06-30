class LowerString(str):
    def __new__(cls, obj=''):
        instance = super().__new__(cls, str(obj).lower())
        return instance


s1 = LowerString('BEEGEEK')
s2 = LowerString('BeeGeek')

print(s1)
print(s2)
print(s1 == s2)
print(issubclass(LowerString, str))


print(LowerString(['Bee', 'Geek']))
print(LowerString({'A': 1, 'B': 2, 'C': 3}))
