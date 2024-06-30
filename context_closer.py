class Closer:
    def __init__(self, obj):
        self.obj = obj

    def __enter__(self):
        return self.obj

    def __exit__(self, exc_type, exc_val, exc_tb):
        if not hasattr(self.obj, 'close'):
            print('Незакрываемый объект')
            return True
        self.obj.close()
        return True
