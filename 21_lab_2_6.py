

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
                    or self.current < self.stop <= 0:
                raise StopIteration
        else:
            if self.step > 0 \
                    or self.current < self.stop >= 0 \
                    or self.current > self.stop <= 0:
                raise StopIteration
        return self.current - self.step


class Range:
    def __init__(self, start, *args):
        quantity = len(args)
        if quantity > 2:
            raise TypeError("Range expected at most 3 arguments, got {}"
                            .format(quantity+1))
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


if __name__ == "__main__":
    print(range(200, -1))
    print(iter(range(1)))
    print(repr(range))
    print(repr(Range))
    print(range(1, ))
    print(Range(1, ))
    print(dir(iter(range(1))))
    print([x for x in range(49, 90)])
    print([x for x in Range(49, 90)])



