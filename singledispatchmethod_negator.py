from functools import singledispatchmethod


class Negator:

    @singledispatchmethod
    @staticmethod
    def neg(data):
        raise TypeError('Аргумент переданного типа не поддерживается')

    @neg.register(int)
    @staticmethod
    def neg_number_int(data):
        return -data

    @neg.register(float)
    @staticmethod
    def neg_from_float(data):
        return -data

    @neg.register(bool)
    @staticmethod
    def neg_from_bool(data):
        return not data
