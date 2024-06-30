class ValueDict(dict):

    def key_of(self, value):
        if self.keys_of(value):
            return self.keys_of(value)[0]

    def keys_of(self, value):
        values_to_keys = {}
        for key, v in self.items():
            values_to_keys.setdefault(v, []).append(key)
        return values_to_keys.get(value, [])


valuedict = ValueDict({'apple': 1, 'banana': 2, 'orange': 2})

print(valuedict.key_of(2))
print(*valuedict.keys_of(2))


# countries = {'Monaco': 'Monaco', 'Iceland': 'Reykjavik', 'Kenya': 'Nairobi', 'Kazakhstan': 'Nur-Sultan',
#              'Mali': 'Bamako', 'Colombia': 'Bogota', 'Finland': 'Helsinki', 'Costa Rica': 'San Jose',
#              'Cuba': 'Havana', 'France': 'Paris', 'Gabon': 'Libreville', 'Liberia': 'Monrovia',
#              'Angola': 'Luanda', 'India': 'New Delhi', 'Canada': 'Ottawa', 'Australia': 'Canberra'}
#
# valuedict = ValueDict(countries)
#
# print(valuedict.key_of('Moscow'))
# print(*valuedict.keys_of('Washington'))
