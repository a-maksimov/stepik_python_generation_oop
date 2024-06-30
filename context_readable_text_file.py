class ReadableTextFile:
    def __init__(self, filename):
        self.filename = filename
        self.file = None

    def __enter__(self):
        self.file = open(self.filename, 'r', encoding='utf-8')
        return [line.strip() for line in self.file]

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()
        return False
