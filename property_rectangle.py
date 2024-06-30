class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def get_perimeter(self):
        return self.width * 2 + self.length * 2

    def get_width(self):
        return self.width * self.length

    perimeter = property(get_perimeter)
    area = property(get_width)
