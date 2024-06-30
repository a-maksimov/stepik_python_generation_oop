class AttrsNumberObject:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)
        self.attrs_num = len(self.__dict__) + 1

    def __getattribute__(self, name):
        if name == 'attrs_num':
            self.attrs_num = len(self.__dict__)
        return object.__getattribute__(self, name)


music_group = AttrsNumberObject(name='Silent Poets', genre='acid jazz')

print(music_group.attrs_num)