def main(array, sum_to_find):
    for i, a in enumerate(array):
        for b in array[i:]:
            if a + b == sum_to_find:
                return True
    return False


if __name__ == '__main__':
    print(main([10, 23, 4, 6, 7, 2], 17))
    print(main([10, 23, 4, 6, 8, 2], 17))
