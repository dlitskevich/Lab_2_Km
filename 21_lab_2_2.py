import sys


def getancestor(self, item):
    """"""
    mro = self.__class__.__mro__
    if item == "getattribute":
        return None.__class__
    for ancestor in mro:
        if item in ancestor.__dict__:
            return ancestor
    raise AttributeError


def get_start_frame(frame):
    """"""
    current_frame = frame
    not_last = True
    while not_last:
        next_frame = current_frame.f_back
        if next_frame is None or next_frame.f_code.co_name == "<module>":
            return current_frame
        current_frame = next_frame

    return current_frame


def PPProtected(cls):
    def getattribute(self, item):
        # pass everything magic
        if item.endswith("__"):
            return object.__getattribute__(self, item)

        # check 'privatness' of attribute
        if item.startswith('__'):
            raise AttributeError("Trying to access private not from class")

        # check 'protectness' of attribute
        if item.startswith('_') and\
                not item[1:].startswith(self.__class__.__name__[4:]):
            invoker_name = get_start_frame(sys._getframe(0)).f_code.co_name
            invoker = getancestor(self, invoker_name)
            owner = getancestor(self, item)
            # print(invoker, owner, issubclass(invoker, owner))
            if not issubclass(invoker, owner):
                raise AttributeError("Trying to access protected "
                                     "not from children")

        return object.__getattribute__(self, item)

    wrapper = type("PPP_{}".format(cls.__name__), (cls,), dict())
    wrapper.__getattribute__ = getattribute
    return wrapper


class SupClass(object):
    def test_protected(self):
        Class()._method_protected()
        print(Class()._attr_protected)


@PPProtected
class Class(SupClass):
    attr_public = "attr_public"
    __attr_private = "attr_private"
    _attr_protected = "attr_protected"

    def __init__(self):
        self.aa_test = 123

    def method_public(self):
        print("method_public called")
        print(self.__attr_private)
        print(self._attr_protected)
        self.__method_private()

    def __method_private(self):
        print("method_private called")

    def _method_protected(self):
        print("method_protected called")


class SubClass(Class):
    def test_protected(self):
        self._method_protected()
        print(self._attr_protected)


if __name__ == "__main__":
    instance = Class()

    # attributes tests
    print("     1-st")
    instance.method_public()
    print("     2-nd")
    try:
        print(instance.__method_private)
    except AttributeError as err:
        print(err)
    print("     3-rd")
    try:
        SupClass().test_protected()
    except AttributeError as err:
        print(err)

    print("     4-th")
    SubClass().test_protected()
    print("     5-th")
    try:
        instance._method_protected()
    except AttributeError as err:
        print(err)
