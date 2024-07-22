def limited_hash(left, right, hash_function=hash):
    def inside_function(obj):
        limit = list(range(left, right + 1))
        result = hash_function(obj)
        if result > right:
            return limit[(result - right) % len(limit) - 1]
        elif result < left:
            return limit[::-1][(left - result) % len(limit) - 1]
        else:
            return result

    return inside_function


hash_function = limited_hash(10, 15)

print(hash_function(9))
print(hash_function(8))
print(hash_function(4))
print(hash_function(3))
print(hash_function(2))
