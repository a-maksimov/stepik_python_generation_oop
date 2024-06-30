def pluck(data, path, default=None):
    if data == default:
        return data
    if not isinstance(data, dict):
        return data
    if path == '':
        return data
    path = path.split('.')
    new_path = '.'.join(path[1:])
    return pluck(data.get(path[0], default), new_path, default)


d = {'a': {'b': {'c': {'d': {'e': 4}}}}}

print(pluck(d, 'a.c.c'))
