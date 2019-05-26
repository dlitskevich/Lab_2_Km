import sys


class LoggerMCL(type):
    def __repr__(self):
        string = "Logs:\n"
        for log in self.logs:
            string += "{} Result: {} {}\n".format(log[0], log[1], log[2])
        return string


class LoggerTech(object, metaclass=LoggerMCL):
    logs = []

    @classmethod
    def log(cls, method):
        # better use wraps from functools
        def logging(*args, **kwargs):
            result = method(*args, **kwargs)
            cls.logs.append((method.__name__, result, (args, kwargs)))
            print(type(cls))

        return logging


class Logger:
    """
    print(sys._getframe().f_back.f_code)
    print(sys._getframe().f_code.co_names)
    print(sys._getframe().f_code.co_name)
    """

    def __getattribute__(self, item):
        method = super().__getattribute__(item)
        # types.MethodType
        if callable(method):
            setattr(self, item, LoggerTech.log(object.__getattribute__(self, item)))
        return method

    def __call__(self, *args, **kwargs):
        print(123)
        return 12

    # @LoggerTech.log
    def method1(self, arg=1):
        print(Logger.__subclasses__())
        return 1, 2


class Test(Logger):
    def recycle(self):
        return "recycled"


if __name__ == "__main__":
    a = Logger()
    print(a.__dict__)
    a.method1(2)
    print(a.__dict__)
    print()

    print(LoggerTech)
