def is_decimal(string):
    try:
        float(string)
        return True
    except ValueError:
        return False


print(is_decimal('.-95'))
print(is_decimal('-.95'))