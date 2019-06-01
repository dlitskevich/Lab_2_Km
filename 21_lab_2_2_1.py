

"""
    This is an example of truly 'pythonic' style applied.
    The most common algorithm!
    Use of name mangling, though it isn't the only purpose of it.
    Why?
    Unpythonic is doing lots of type checking, or trying really hard to make
    something private/protected.
    By the way we're all consenting adults here...
"""


class Class:
    attr_public = "attr_public"
    __attr_private = "attr_private"
    _attr_protected = "attr_protected"

    def method_public(self):
        print("method_public called")
        print(self.__attr_private)
        # print(Class.__attr_private)

    def __method_private(self):
        print("method_private called")

    def _method_protected(self):
        print("method_protected called")


class SubClass(Class):

    def protected_test(self):
        self._method_protected()


if __name__ == "__main__":
    SubClass().protected_test()
