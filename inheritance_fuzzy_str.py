class FuzzyString(str):

    @staticmethod
    def _check_instance(other):
        if not isinstance(other, str):
            return False
        return True

    def __eq__(self, other):  # ==
        if not self._check_instance(other):
            return NotImplemented

        return self.lower() == other.lower()

    def __ne__(self, other):  # !=
        if not self._check_instance(other):
            return NotImplemented

        return self.lower() != other.lower()

    def __lt__(self, other):  # <
        if not self._check_instance(other):
            return NotImplemented

        return self.lower() < other.lower()

    def __gt__(self, other):  # >
        if not self._check_instance(other):
            return NotImplemented

        return self.lower() > other.lower()

    def __le__(self, other):  # <=
        if not self._check_instance(other):
            return NotImplemented

        return self.lower() <= other.lower()

    def __ge__(self, other):  # >=
        if not self._check_instance(other):
            return NotImplemented

        return self.lower() >= other.lower()

    def __contains__(self, other):  # other in self
        if not self._check_instance(other):
            return NotImplemented

        return other.lower() in self.lower()


s1 = FuzzyString('BeeGeek')
s2 = FuzzyString('beegeek')

print(s1 == s2)
print(s1 in s2)
print(s2 in s1)
print(s2 not in s1)
