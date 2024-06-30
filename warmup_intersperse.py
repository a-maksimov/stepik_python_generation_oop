from itertools import product, chain


def intersperse(iterable, delimiter):
    iterable = iter(iterable)
    full_chain = chain.from_iterable(product(iterable, [delimiter]))
    try:
        prev = next(full_chain)
    except StopIteration:
        return
    for item in full_chain:
        yield prev
        prev = item


print(*intersperse([1, 2, 3], 0))

iterable = iter('Beegeek')
print(*intersperse(iterable, '+'))


# def intersperse(iterable, delimiter):
#     first = True
#     for item in iterable:
#         if not first:
#             yield delimiter
#         first = False
#         yield item
