from itertools import combinations


def inversions(sequence):
    return len(list(filter(lambda pair: pair[0] > pair[1], combinations(sequence, 2))))


print(inversions([1, 2, 3, 4, 5]))
