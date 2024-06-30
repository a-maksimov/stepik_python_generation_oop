class Animal:
    def sleep(self):
        ...

    def eat(self):
        ...


class Fish(Animal):
    def swim(self):
        ...


class Bird(Animal):
    def lay_eggs(self):
        ...


class FlyingBird(Bird):
    def fly(self):
        ...
