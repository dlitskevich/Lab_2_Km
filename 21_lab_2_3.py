

class LoggerMCS(type):
    logs = []

    @classmethod
    def log(mcs, method):
        # better use wraps from functools
        def logging(*args, **kwargs):
            result = method(*args, **kwargs)
            mcs.logs.append((method.__name__, result, (args, kwargs)))
            return result
        return logging

    def __new__(mcs, name, bases, dct):
        """
        if not hasattr(mcs, 'logs'):
            mcs.logs = []
        """
        newattrs = {}
        for attrname, attrvalue in dct.items():
            if callable(attrvalue):
                newattrs[attrname] = mcs.log(attrvalue)
            else:
                newattrs[attrname] = attrvalue

        return super().__new__(mcs, name, bases, newattrs)

    def __init__(cls, name, bases, dct):
        super().__init__(name, bases, dct)

    def __str__(self):
        string = "Logs:\n"
        for log in LoggerMCS.logs:
            string += "{} Result: {} {}\n".format(log[0], log[1], log[2])
        return string


class Logger(metaclass=LoggerMCS):

    def __call__(self, *args, **kwargs):
        print(123)
        return 12

    def method1(self, arg):
        print("method 1 called with {}".format(arg))
        return 1, 2, arg


def decorator(func):
    def change(*args, **kwargs):
        return func(*args, **kwargs) * 2

    return change


class Test(Logger):
    @decorator
    def recycle(self, arg=1):
        return "recycled" * arg


if __name__ == "__main__":
    a = Logger()
    print(a)
    a.method1(2)
    Logger.method1(Logger, 6)
    a.method1(3)
    Logger()()
    Test.recycle(Test, 1)
    print(Test.recycle)
    print()
    print(Logger)
