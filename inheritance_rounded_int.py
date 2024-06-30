class RoundedInt(int):
    def __new__(cls, num, even=True):
        if even and not num % 2 == 0:
            num += 1
        elif not even and not num % 2 != 0:
            num += 1
        instance = super().__new__(cls, num)
        return instance
