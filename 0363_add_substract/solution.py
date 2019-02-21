from operator import add, sub


class add_subtract:
    def __init__(self, arg):
        self.total = arg
        self.next_op = add

    def __call__(self, new_number):
        self.total = self.next_op(self.total, new_number)
        self.next_op = sub if self.next_op == add else add
        return self

    def __eq__(self, other):
        return self.total == other


if __name__ == '__main__':
    assert add_subtract(7) == 7
    assert add_subtract(1)(2)(3) == 0
    assert add_subtract(-5)(10)(3)(9) == 11
