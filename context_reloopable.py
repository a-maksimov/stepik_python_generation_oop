class Reloopable:
    def __init__(self, file):
        self.file = file
        self.data = None

    def __enter__(self):
        self.data = [line.strip() for line in self.file]
        return self.data

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()
        return False
