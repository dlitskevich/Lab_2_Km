

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
    """
    def __getattribute__(self, item):
        exception_list = [
            "_Singleton__first_instance",
            "_Singleton__passed_class",
            "_Singleton__instance"
        ]
        if item in exception_list:
            return object.__getattribute__(self, item)

        return object.__getattribute__(self.__instance, item)
    """
    
    def __getattr__(self, name):
        return getattr(self.__instance, name)


@Singleton
class Test:
    value = 1

    def __init__(self, number):
        self.value = number

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
