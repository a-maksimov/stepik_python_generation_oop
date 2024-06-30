class Color:
    def __init__(self, hexcode):
        self._hexcode = hexcode

        self.r, self.g, self.b = self._hex_to_dec()

    def _hex_to_dec(self):
        return [int(self._hexcode[i:i + 2], 16) for i in range(0, len(self._hexcode), 2)]

    @property
    def hexcode(self):
        return self._hexcode

    @hexcode.setter
    def hexcode(self, value):
        self._hexcode = value
        self.r, self.g, self.b = self._hex_to_dec()


color = Color('0000FF')

print(color.hexcode)
print(color.r)
print(color.g)
print(color.b)