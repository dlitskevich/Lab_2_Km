

class Singleton:
    __first_instance = 1

    def __init__(self, passed_class):
        self.__passed_class = passed_class

    def __call__(self, *args):
        if self.__first_instance:
            self.__instance = self.__passed_class(*args)
            self.__first_instance = 0
            return self.__instance
        else:
            self.__instance.__dict__ = self.__passed_class(*args).__dict__
            return self.__instance
        

@Singleton
class Test:
    value = 1

    def __init__(self, number):
        self.value = number
        self.value2 = 12

    def __str__(self):
        return "{} : {}".format(object.__str__(self), self.value)


@Singleton
class TestAn:
    value = 1

    def __init__(self, number):
        self.value = number

    def __call__(self, *args, **kwargs):
        return 123

    def __repr__(self):
        return "{} : {}".format(object.__repr__(self), self.value)


if __name__ == "__main__":
    a = Test(2)
    print(a.__dict__)
    b = Test(3)
    print(a.value)
    print(b.value2)
    c = Test(4)
    print(a)
    print(b)
    print(c)
    d = Test(5)
    print(a)
    print(b)
    print(c)
    print(d)

    print()
    a = TestAn(2)
    print(a(1))
    b = TestAn(3)
    print(a)
    print(b)
    c = TestAn(4)
    print(a)
    print(b)
    print(c)
    d = TestAn(5)
    print(a)
    print(b)
    print(c)
    print(d)
