from contextlib import contextmanager


@contextmanager
def safe_write(filename):
    try:
        with open('tempfile', 'w') as t:
            yield t
        with open(filename, 'w') as file, open('tempfile', 'r') as t:
            file.writelines(t.readlines())

    except Exception as error:
        print(f'Во время записи в файл было возбуждено исключение {error.__class__.__name__}')

