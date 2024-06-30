class ReversibleString:
    def __init__(self, string):
        self.string = string

    def __neg__(self):
        return ReversibleString(''.join(reversed(self.string)))

    def __str__(self):
        return self.string


string = ReversibleString('python')

print(string)
print(-string)
