class SubscriberStorage:

    def __init__(self):
        self._counts = [0] * 24

    def update(self, hour: int, value: int):
        self._counts[hour - 1] += value

    def query(self, start: int, end: int) -> int:
        return sum(self._counts[start - 1:end])


if __name__ == '__main__':
    subs = SubscriberStorage()
    subs.update(1, 5)
    subs.update(2, 7)
    subs.update(3, 9)

    print(subs.query(2, 3))
