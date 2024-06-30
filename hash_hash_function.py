def hash_function(obj):
    obj = str(obj)
    length = len(obj)

    temp1 = 0
    for i in range(length // 2):
        temp1 += ord(obj[i]) * ord(obj[-i-1])

    if length % 2 != 0:
        temp1 += ord(obj[i + 1])

    temp2 = 0
    for i in range(length):
        if i % 2 == 0:
            temp2 += ord(obj[i]) * (i + 1)
        else:
            temp2 -= ord(obj[i]) * (i + 1)

    return (temp1 * temp2) % 123456791


print(hash_function('python'))
