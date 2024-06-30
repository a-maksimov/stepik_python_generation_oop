class WriteSpy:
    def __init__(self, file1, file2, to_close=False):
        self.file1 = file1
        self.file2 = file2
        self.to_close = to_close

    def write(self, text):
        if (
                any([self.file1.closed, self.file2.closed]) or
                not all([self.file1.writable(), self.file2.writable()])
        ):
            raise ValueError('Файл закрыт или недоступен для записи')
        self.file1.write(text)
        self.file2.write(text)

    def close(self):
        self.file1.close()
        self.file2.close()

    def writable(self):
        if (
                any([self.file1.closed, self.file2.closed]) or
                not all([self.file1.writable(), self.file2.writable()])
        ):
            return False
        return True

    def closed(self):
        return all([self.file1.closed, self.file2.closed])

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.to_close:
            self.file1.close()
            self.file2.close()
        return False


# TEST_5:
f1 = open('file1.txt', mode='r')
f2 = open('file2.txt', mode='w')

try:
    with WriteSpy(f1, f2, to_close=True) as combined:
        combined.write('No cost too great')
except ValueError as error:
    print(error)


# TEST_5:
# Файл закрыт или недоступен для записи

# TEST_6:
f1 = open('file1.txt', mode='w')
f2 = open('file2.txt', mode='w')
f1.close()

try:
    with WriteSpy(f1, f2, to_close=True) as combined:
        combined.write('No cost too great')
except ValueError as error:
    print(error)

# TEST_6:
# Файл закрыт или недоступен для записи
