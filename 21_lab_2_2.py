import sys


def getancestor(self, item):
    """"""
    mro = self.__class__.__mro__
    for ancestor in mro:
        if item in ancestor.__dict__:
            return ancestor
    raise AttributeError


def instance_getattribute(self, item):
    """"""
    print()
    print("classGet", item, self)
    # ignore some magic
    if item.startswith("__"):
        return object.__getattribute__(self, item)
    ancestor = getancestor(self, item)

    # when we try to get access to private attr from any instance
    # if item in object.__getattribute__(ancestor, "__private__"):
    #    raise AttributeError("Trying to access private attribute")

    return object.__getattribute__(self, item)


class PPProtected(type):
    def __init__(cls, name, bases, dct):
        cls.__private__ = [] if not hasattr(cls, "__private__") else cls.__private__
        cls.__getattribute__ = instance_getattribute

        super().__init__(name, bases, dct)
    """
    def __getattribute__(self, item):
        print(self)
        print(object.__getattribute__(self, "__private__"), item)
        if item in object.__getattribute__(self, "__private__"):
            raise AttributeError("Trying to access private attribute")

        return object.__getattribute__(self, item)
    """
    def __getattribute__(self, item):
        if item == "attr_private":
            print(sys._getframe(1).f_globals)
            print(sys._getframe(1))
            print(sys._getframe(1).f_locals)
            print(sys._getframe(1).f_code.co_cellvars)
        return object.__getattribute__(self, item)


class SupClass(object):
    pass


class Class(SupClass, metaclass=PPProtected):
    __public__ = ["attr_public", "method_public"]
    __private__ = ["attr_private", "method_private"]
    __protected__ = ["attr_protected", "method_protected"]
    attr_public = "attr_public"
    attr_private = "attr_private"
    attr_protected = "attr_protected"

    def __init__(self):
        self.aa_test = 123

    def __getattribute__(self, item):
        print("lol", self)

        return object.__getattribute__(self, item)

    def method_public(self):
        print("method_public called")
        print(Class.attr_private)
        try:
            print(self.attr_private)
        except AttributeError as error:
            print(error, "inClass")

    def method_private(self):
        print("method_private called")

    def method_protected(self):
        print("method_protected called")


class SubClass(Class):
    pass


if __name__ == "__main__":
    instance = Class()

    # attributes tests
    print()
    Class.method_public(Class)
    print()
    print()
    print()
    print(instance.method_public.__self__)
    print()
    SubClass().method_public()
    print()
    try:
        print(Class.method_private(Class))
    except AttributeError as err:
        print(err)
    """
    try:
        print(instance.attr_private)
    except AttributeError as err:
        print(err)
    
    
    print()
    print(SubClass.mro())
    print(SubClass.attr_private)
    """
    """
    print()
    print(SubClass.attr_protected)
    """
    # methods tests
    """
    Test.method_public()
    Test.method_private()
    Test.method_protected()
    """
