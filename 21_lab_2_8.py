
def singleton_decorator(passed_class):

    class Singleton:
        def __init__(self, *args, **kwargs):
            if not self.instance:
                self.instance = passed_class(args, kwargs)
            else:
                print("Yep")

        def __getattr__(self, name):
            return getattr(self.wrapped, name)

    return Singleton


class Test:
    value = 1

    def __init__(self, number):
        self.value = number

    def __str__(self):
        return "{} : {}".format(object.__str__(self), self.value)

if __name__ == "__main__":
    a = Test(2)
    b = Test(3)
    c = Test(4)
    print(a)
    print(b)
    print(c)