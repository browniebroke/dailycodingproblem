from timeit import timeit


def mult_array_non_i_naive(array):
    multiplied_array = []
    for i, _ in enumerate(array):
        to_multiply = array[:i] + array[i + 1:]
        multiplied = 1
        for el in to_multiply:
            multiplied = multiplied * el
        multiplied_array.append(multiplied)
    return multiplied_array


def mult_array_non_i_with_division(array):
    total = 1
    for el in array:
        total = total * el
    multiplied_array = []
    for el in array:
        multiplied_array.append(total / el)
    return multiplied_array


def mult_array_non_i(array):
    product = 1
    product_below = []
    for i in range(0, len(array)):
        product_below.append(product)
        product = array[i] * product

    product = 1
    product_above = []
    for i in range(len(array), 0, -1):
        product_above.append(product)
        product = array[i - 1] * product
    product_above = list(reversed(product_above))

    multiplied_array = []
    for i in range(len(array)):
        multiplied_array.append(product_below[i] * product_above[i])
    return multiplied_array


if __name__ == '__main__':
    res = mult_array_non_i([3, 2, 1])
    assert res == [2, 3, 6]

    res = mult_array_non_i([1, 2, 3, 4, 5])
    assert res == [120, 60, 40, 30, 24]
    print(timeit("mult_array_non_i([1, 2, 3, 4, 5])", globals=globals()))
    # 3.6619 -> naive single function
    # 1.1407 -> with division
    # 4.4722 -> without division
