class Item:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def __getattribute__(self, attr):
        if attr == 'name':
            return object.__getattribute__(self, attr).title()
        return object.__getattribute__(self, attr)

    def __getattr__(self, attr):
        if attr == 'total':
            return self.price * self.quantity
        raise AttributeError


fruit = Item('banana', 15, 5)

print(fruit.price)
print(fruit.quantity)