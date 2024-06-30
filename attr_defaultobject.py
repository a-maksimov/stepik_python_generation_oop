class DefaultObject:
    def __init__(self, default=None, **kwargs):
        self.default = default
        self.__dict__.update(
            {key: value for key, value in kwargs.items()}
        )

    def __getattr__(self, item):
        return self.default


god = DefaultObject(name='Ares', mythology='greek')

print(god.name)
print(god.mythology)
print(god.age)





