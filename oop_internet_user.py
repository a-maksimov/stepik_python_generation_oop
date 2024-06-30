class User:
    def __init__(self, name, age):
        self._name = None
        self._age = None
        self.set_name(name)
        self.set_age(age)

    def get_name(self):
        return self._name

    def get_age(self):
        return self._age

    def set_name(self, new_name):
        if not isinstance(new_name, str) or not new_name.isalpha():
            raise ValueError('Некорректное имя')
        self._name = new_name

    def set_age(self, new_age):
        if not isinstance(new_age, int) or new_age not in list(range(1, 110)):
            raise ValueError('Некорректный возраст')
        self._age = new_age
