class MROHelper:

    @staticmethod
    def len(cls):
        return len(cls.mro())

    @staticmethod
    def class_by_index(cls, n=0):
        for i, elem in enumerate(cls.mro()):
            if i == n:
                return elem

    @staticmethod
    def index_by_class(child, parent):
        for i, elem in enumerate(child.mro()):
            if elem == parent:
                return i
