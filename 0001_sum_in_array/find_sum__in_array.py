import random
from timeit import timeit


def main(array, sum_to_find):
    for i, a in enumerate(array):
        b = sum_to_find - a
        if b in array[i:]:
            return True
    return False


if __name__ == '__main__':
    # Correctness
    print(main([10, 2, 3, 4, 5, 11, 6, 7, 8, 9], 19)) # True
    print(main([10, 2, 3, 4, 5, 11, 6, 7, 8, 9], 40)) # False
    items = [random.choice(range(10_000)) for _ in range(10_000)]
    res1 = timeit("main(items, 17)", number=10, globals=globals())
    print(res1) # Duration
