

class Sequence:
    def __init__(self, iterable):
        try:
            self.__iterable = iter(iterable)
            self.__iterable_saved = iterable
        except TypeError:
            raise

    def __iter__(self):
        self.__iterable = iter(self.__iterable_saved)
        return self

    def __next__(self):
        try:
            return next(self.__iterable)
        except StopIteration:
            self.__iterable = iter(self.__iterable_saved)
            return next(self.__iterable)

    def filter(self, function):
        filtered = []
        for item in self.__iterable_saved:
            if function(item):
                filtered.append(item)
        self.__iterable_saved = filtered
        self.__iterable = iter(self.__iterable_saved)
        return self


if __name__ == "__main__":
    test_sequence = Sequence(range(5, 40))
    test_an_sequence = Sequence(range(5, 9))
    print(test_sequence.filter(lambda a: 9 < a < 12))
    
    stop = 0
    for test_item in test_sequence:
        if stop > 100:
            break
        print(test_item)
        stop += 1

    print(iter(test_sequence))
