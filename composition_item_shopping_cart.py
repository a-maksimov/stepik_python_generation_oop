class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f'{self.name}, {self.price}$'


class ShoppingCart:
    def __init__(self, items=None):
        if not items:
            self.items = []
        else:
            self.items = items

    def add(self, item: Item):
        self.items.append(item)

    def total(self):
        return sum(map(lambda i: i.price, self.items))

    def remove(self, name: str):
        self.items = [item for item in self.items if not item.name == name]

    def __str__(self):
        return '\n'.join(map(lambda i: f'{i.name}, {i.price}$', self.items))


shopping_cart = ShoppingCart([Item('Yoga Mat', 130)])

shopping_cart.add(Item('Flannel Shirt', 22))
print(shopping_cart)
print(shopping_cart.total())