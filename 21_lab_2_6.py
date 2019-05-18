class RangeIterator:
    def __init__(self, start, stop, step):
        self.stop = stop
        self.start = start
        self.step = step
        self.current = self.start

    def __iter__(self):
        return self

    def __next__(self):
        self.current += self.step
        if self.start < self.stop:
            if self.step < 0 \
                    or self.current > self.stop >= 0 \
                    or self.current > self.stop <= 0:
                raise StopIteration
        else:
            if self.step > 0 \
                    or self.current < self.stop >= 0 \
                    or self.current < self.stop <= 0:
                raise StopIteration
        return self.current - self.step

    def __length_hint__(self):
        if self.start > self.stop and self.step > 0 \
                or self.start < self.stop and self.step < 0:
            return 0
        return abs((self.start - self.stop) // self.step)


class Range:
    __slots__ = "start", "stop", "step"

    def __init__(self, start, *args):
        quantity = len(args)
        if quantity > 2:
            raise TypeError("Range expected at most 3 arguments, got {}"
                            .format(quantity + 1))
        if quantity == 0:
            self.stop = start
            self.start = 0
        else:
            self.stop = args[0]
            self.start = start
        if quantity == 1 or quantity == 0:
            self.step = 1
        else:
            self.step = args[1]
            if self.step == 0:
                raise ValueError("Range() arg 3 must not be zero")
        return

    def __iter__(self):
        return RangeIterator(self.start, self.stop, self.step)

    def __str__(self):
        if self.step == 1:
            return "Range({}, {})".format(self.start, self.stop)
        else:
            return "Range({}, {}, {})" \
                   "".format(self.start, self.stop, self.step)

    def __bool__(self):
        return True

    def __getitem__(self, order):
        quantity = abs((self.start - self.stop) // self.step)
        if order < 0:
            order = quantity + order
        current_index = 0
        for item in RangeIterator(self.start, self.stop, self.step):
            if current_index == order:
                return item
            current_index += 1
        raise IndexError("Range object index out of range")

    def __reversed__(self):
        return RangeIterator(self.stop - self.step,
                             self.start - self.step,
                             -self.step)

    def __contains__(self, item):
        return item in iter(self)

    def __len__(self):
        return RangeIterator(self.start, self.stop, self.step)\
            .__length_hint__()

    def index(self, value):
        if value not in iter(self):
            raise ValueError("{} is not in range".format(value))
        else:
            current_index = 0
            for item in RangeIterator(self.start, self.stop, self.step):
                if item == value:
                    return current_index
                current_index += 1

    def count(self, value):
        if value in iter(self):
            return 1
        return 0


if __name__ == "__main__":
    print(dir(range))
    print(dir(Range))
    print(dir(iter(range(1))))
    print(dir(iter(Range(1))))
    print(iter(range(1)))
    print(iter(Range(1)))
    print(repr(range))
    print(repr(Range))
    print(range(1, ))
    print(Range(1, ))
    print(iter(range(1, )))
    print(iter(Range(1, )))
    if range(1, 2):
        print(range(1, ))
    if Range(1):
        print(Range(1, ))
    print("{}".format(range.step))
    print("{}".format(Range.step))

    print(range(20)[12])
    print(Range(20)[12])

    print([x for x in reversed(range(-10, -20, -10))])
    print([x for x in reversed(Range(-10, -20, -10))])

    print(2 in range(4))
    print(-1 in Range(4))

    print(range(20, 400, 20).count(62))
    print(range(20, 400, 20).index(60))

    print(len(range(-10, 1)))
    print(len(Range(-10, 1)))

    print(range(100, 200, 10).count(100))
    print(Range(100, 200, 10).count(100))

    print(range(200, 100, -10).index(190))
    print(Range(200, 100, -10).index(190))

    print([x for x in range(49, 90)])
    print([x for x in Range(49, 90)])
    print([x for x in range(-9, -50, -1)])
    print([x for x in Range(-9, -50, -1)])
