

# make hooks and change 1)setitem 2)metaclass
class PPProtected(type):
    def __init__(cls, name, bases, dct):
        save = cls.__getattribute__
        print(save("attr_public"))

        def type_get(self, item):
            print(self, cls)
            return object.__getattribute__(self, item)

        cls.__getattribute__ = type_get
        super().__init__(name, bases, dct)
        pass

    def __getattribute__(self, item):
        print(self)
        print(type(self))

        return 1233321


def public(func):
    func.scope = "public"
    return func


def private(func):
    func.scope = "private"
    return func


def protected(func):
    func.scope = "protected"
    return func


class SupClass:
    pass


class Test(SupClass, metaclass=PPProtected):
    __public__ = ["attr_public"]
    __private__ = ["attr_private"]
    __protected__ = ["attr_protected"]
    attr_public = "attr_public"
    attr_private = "attr_private"
    attr_protected = "attr_protected"

    def __init__(self):
        self.aa_test = 123

    def __getattribute__(self, item):
        print(23)
        return lambda x: x

    @public
    def method_public(self):
        print("method_public called")

    @private
    def method_private(self):
        print("method_private called")

    @protected
    def method_protected(self):
        print("method_protected called")


class SubClass(Test):
    pass


if __name__ == "__main__":
    test = Test()

    # attributes tests
    print(Test.attr_public)
    print(test.attr_private)
    print(SubClass.attr_private)
    print(SubClass.attr_protected)
    # methods tests
    """
    Test.method_public()
    Test.method_private()
    Test.method_protected()
    """
