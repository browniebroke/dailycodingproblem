def cons(a, b):
    return lambda f: f(a, b)


def car(func):
    return func(lambda a, b: a)


def cdr(func):
    return func(lambda a, b: b)


if __name__ == '__main__':
    assert car(cons(3, 4)) == 3
    assert cdr(cons(3, 4)) == 4
