class Money:
    def __init__(self, amount):
        self.amount = amount

    def __pos__(self):
        return self.__class__(abs(self.amount))

    def __neg__(self):
        return self.__class__(-abs(self.amount))

    def __str__(self):
        return f'{self.amount} руб.'


money = Money(100)

print(money)
print(+money)
print(-money)
