class Range:
    start_number = 0
    before_number = 0
    step = 1

    def __init__(self):
        return

    def __call__(self, before_num):
        before_number = before_num
        return before_number

if __name__ == "__main__":
    print(dir(range))
    print(range.__call__(1, 6, 3))

    print(Range(1))
