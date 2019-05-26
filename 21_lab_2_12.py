

class A(object):
    d = "as"

    def method(self, arg, *args, kwarg):
        print("A", self, self.d)


class B(object):
    def method(self):
        print("B")


class C(A, B):
    def method(self, arg, *args, kwarg):
        print("C")


class D(C):
    d = "dla"

    def method(self, arg, *args, kwarg):
        print("D")


class Super:
    __slots__ = ['__self__', '__self_class__', '__this_class__']

    def __init__(self, subclass, instance):
        if not isinstance(subclass, type):
            raise TypeError("Super() argument 1 must be type, not {}"
                            .format(subclass.__class__.__name__))
        if not isinstance(instance, subclass):
            raise TypeError("Super(type, obj): obj must be an instance "
                            "or subtype of type")
        self.__this_class__ = subclass
        self.__self__ = instance
        self.__self_class__ = instance.__class__

    def __repr__(self):
        return "<Super: <class '{}'>, <{} object>>"\
            .format(self.__this_class__.__name__,
                    self.__self__.__class__.__name__)

    def __get__(self, instance, owner):
        return self

    """
    def decorator(self, func):
        #@functools.wraps(func)
        def bound_func(*args, **kwargs):
            func(self.__self__, *args, **kwargs)

        return bound_func
    
    def decorator(self, func):
        return lambda *args, **kwargs: func(self.__self__, *args, **kwargs)
    """
    def __getattribute__(self, item):
        if item in object.__getattribute__(self, '__slots__') \
                or item == "decorator":
            return object.__getattribute__(self, item)
        mro = self.__this_class__.mro()[1:]

        for subclass in mro:
            try:
                attr = object.__getattribute__(subclass, item)
                # better through types MethodType
                if callable(attr):
                    # noinspection PyUnresolvedReferences
                    return attr.__get__(self.__self__, self.__this_class__)
                return attr
                # return self.decorator(object.__getattribute__(subclass, item))

            except AttributeError:
                continue
        raise AttributeError


if __name__ == "__main__":
    test_D = D()
    print(super(D))
    print(super(D, test_D))
    print()

    print(super(C, test_D).d)
    print(Super(C, test_D).d)
    print(Super(C, test_D).method)
    Super(C, test_D).method(1, kwarg=1)
    super(C, test_D).method(1, kwarg=1)
    print()

    # types
    """
        print(type(D.method))
        print(type(Super))
        print(type(super))
        print(type(Super(C, test_D)))
        print(type(super(A, test_D)))
    """
    # string representation
    print(Super(C, test_D))
    print(super(C, test_D))
    print()

    # super class members
    """
    print(dir(Super(C, test_D)))
    print(dir(super(C, test_D)))
    
    print(super(C, test_D).__get__(test_D, D).method())
    print(Super(C, test_D).__get__(test_D, D))
    
    print(super(C, test_D).__thisclass__)
    print(Super(C, test_D).__thisclass__)

    print(super(C, test_D).__self__)
    print(Super(C, test_D).__self__)
    print(super(C, test_D).__self_class__)
    print(Super(C, test_D).__self_class__)

    print(super.__self_class__)
    print(Super.__self_class__)
    print()
    

    # 1-st argument exception
    try:
        Super(test_D)
    except TypeError as err:
        print(err)
    try:
        super(test_D)
    except TypeError as err:
        print(err)
    print()

    # 2-nd argument exception
    try:
        Super(C, A())
    except TypeError as err:
        print(err)
    try:
        super(C, A())
    except TypeError as err:
        print(err)
    print()
    """
