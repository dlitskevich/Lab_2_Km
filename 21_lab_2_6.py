
def objectify(passed_class):
    """"""
    object_of_class = passed_class()
    return object_of_class


@objectify
class Range:
    def __init__(self, *args):
        return

    def __call__(self, start_number, before_number=None, step=1):
        if before_number is None:
            current_number = 0
            before_number = start_number
        else:
            current_number = start_number

        range_list = []
        while current_number < before_number:
            range_list.append(current_number)
            current_number += step
        return range_list


if __name__ == "__main__":
    print(Range(2, 100, 5))
    print(Range(2, 6))
    print(Range(2))
    print(1 in Range(2))

    print(next(iter(Range(2))))
    print()
    for item in Range(6, 65, 7):
        print(item)
