

class Singleton:
    first_instance = 1

    def __init__(self, passed_class):
        self.passed_class = passed_class

    def __call__(self, *args):
        if self.first_instance:
            self.instance = self.passed_class(*args)
            self.first_instance = 0
            return self
        else:
            self.instance.__dict__ = self.passed_class(*args).__dict__
            return self

    def __getattr__(self, name):
        return getattr(self.instance, name)


@Singleton
class Test:
    value = 1

    def __init__(self, number):
        self.value = number

    def __str__(self):
        return "{} : {}".format(repr(self), self.value)


if __name__ == "__main__":
    a = Test(2)
    print(a)
    b = Test(3)
    print(a)
    print(b)
    c = Test(4)
    print(a)
    print(b)
    print(c)
    d = Test(5)
    print(a)
    print(b)
    print(c)
    print(d)
