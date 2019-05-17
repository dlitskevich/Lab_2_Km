

class SequenceIterator:
    def __init__(self, iterable):
        try:
            self.__iterator = iter(iterable)
            self.__iterable = iterable
        except TypeError:
            raise

    def __iter__(self):
        self.__iterator = iter(self.__iterable)
        return self

    def __next__(self):
        try:
            return next(self.__iterator)
        except StopIteration:
            self.__iterator = iter(self.__iterable)
            return next(self.__iterator)


class Sequence:
    def __init__(self, iterable):
        try:
            iter(iterable)
            self.__iterable = iterable
        except TypeError:
            raise

    def __iter__(self):
        return SequenceIterator(self.__iterable)

    def filter(self, function):
        filtered = []
        for item in self.__iterable:
            if function(item):
                filtered.append(item)

        return Sequence(filtered)


if __name__ == "__main__":
    test_sequence = Sequence(range(5, 40))
    test_an_sequence = Sequence(range(5, 9))
    test_filtered = test_sequence.filter(lambda x: 9 < x < 15)

    stop = 0
    for test_item in test_sequence:
        if stop > 10:
            break
        stop1 = 0
        for test_item1 in test_sequence:
            if stop1 > 10:
                break
            print(test_item, test_item1)
            stop1 += 1
        stop += 1
    a = iter(test_sequence)
    b = iter(test_sequence)
    print(a)
    print(b)
    print(iter(test_sequence))

