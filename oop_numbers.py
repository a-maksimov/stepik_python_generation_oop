class Numbers:
    def __init__(self):
        self.number_list = []

    def add_number(self, number):
        self.number_list.append(number)

    def get_even(self):
        return [number for number in self.number_list if number % 2 == 0]

    def get_odd(self):
        return [number for number in self.number_list if number % 2 != 0]


numbers = Numbers()

numbers.add_number(1)
numbers.add_number(3)
numbers.add_number(1)

print(numbers.get_even())
print(numbers.get_odd())