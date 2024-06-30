class Validator:
    def __init__(self, obj):
        self.obj = obj

    def is_valid(self):
        return


class NumberValidator(Validator):
    def is_valid(self):
        if isinstance(self.obj, (int, float)):
            return True
        return False

