class Father:
    def __init__(self, mood='neutral'):
        self.mood = mood

    def greet(self):
        return 'Hello!'

    def be_strict(self):
        self.mood = 'strict'


class Mother:
    def __init__(self, mood='neutral'):
        self.mood = mood

    def greet(self):
        return 'Hi, honey!'

    def be_kind(self):
        self.mood = 'kind'


class Daughter(Mother, Father):
    def __init__(self, mood='neutral'):
        super().__init__(mood)


class Son(Father, Mother):
    def __init__(self, mood='neutral'):
        super().__init__(mood)

