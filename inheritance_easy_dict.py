class EasyDict(dict):
    def __getattr__(self, item):
        return self.__getitem__(item)


easydict = EasyDict({'name': 'Timur', 'city': 'Moscow'})

print(easydict['name'])
print(easydict.city)