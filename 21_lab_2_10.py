

class FieldInitializer(type):
    # can be omitted
    def __new__(mcs, name, bases, dct):
        return super(FieldInitializer, mcs).__new__(mcs, name, bases, dct)

    def __init__(cls, name, bases, dct):
        for base in cls.mro():
            try:
                user_setattr = dct.__setattr
            except AttributeError:
                user_setattr = base.__setattr__
                break

        def type_setattr(self, key, value):
            try:
                value_type = type(getattr(self, key))
                if isinstance(value, value_type):
                    user_setattr(self, key, value)
                else:
                    raise TypeError("Must be same type: {}".format(value_type))
            except AttributeError:
                user_setattr(self, key, value)

        cls.__setattr__ = type_setattr
        super(FieldInitializer, cls).__init__(name, bases, dct)

    # The __call__ method will be called when you make instances of Class
    def __call__(cls, *args, **kwargs):
        print(kwargs)
        created_object = super().__call__(*args, **kwargs)
        object_fields = list(created_object.__dict__.keys())

        for kwarg, value in kwargs.items():
            if kwarg not in object_fields:
                setattr(created_object, kwarg, value)

        return created_object


class Foo(metaclass=FieldInitializer):
    bar = 'bip'

    def __init__(self, a, *args, test_value=2, an_test_value=32, **kwargs):
        self.car = a

    def lol(self):
        pass


class FooChild(Foo, metaclass=FieldInitializer):
    pass


if __name__ == "__main__":
    test = FooChild(1, test_value=2, an_test_value=32, new_key=3)
    an_test = FooChild(10, test_value=20, an_test_value=32)

    print(Foo)
    print(test.__dict__)
    print(an_test.__dict__)
    print()
    an_test.car = 100
    try:
        an_test.test_value = "d"
    except TypeError as e:
        print(e)
    print(an_test.car)
    print(test.__dict__)
    print(an_test.__dict__)
