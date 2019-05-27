

class FieldInitializer(type):
    # can be omitted
    def __new__(mcs, name, bases, dct):
        return super(FieldInitializer, mcs).__new__(mcs, name, bases, dct)

    def __init__(cls, name, bases, dct):
        for base in cls.mro():
            try:
                user_setattr = cls.__setattr__
            except AttributeError:
                user_setattr = base.__setattr__
                break

        def type_setattr(self, key, value):
            try:
                value_type = type(getattr(self, key))
                if isinstance(value, value_type):
                    user_setattr(self, key, value)
                else:
                    raise TypeError("Must be same type: {}"
                                    .format(value_type))
            except AttributeError:
                user_setattr(self, key, value)

        cls.__setattr__ = type_setattr
        super(FieldInitializer, cls).__init__(name, bases, dct)

    # The __call__ method will be called when you make instances of Class
    def __call__(cls, *args, **kwargs):
        # get expected kwargs (args, kwargs)
        quantity_arg = cls.__init__.__code__.co_argcount
        arguments = cls.__init__.__code__.co_varnames[quantity_arg:]

        # separate expected and unexpected kwargs
        unexpected_kwargs = {}
        for kwarg in list(kwargs):
            if kwarg not in arguments:
                unexpected_kwargs[kwarg] = kwargs.pop(kwarg)

        # create object
        created_object = super().__call__(*args, **kwargs)
        object_fields = list(created_object.__dict__.keys())

        # set attributes with unexpected kwargs
        for kwarg, value in unexpected_kwargs.items():
            if kwarg not in object_fields:
                setattr(created_object, kwarg, value)

        return created_object


class Foo(metaclass=FieldInitializer):
    bar = 'bip'

    def __init__(self, a, b=1, *args, test_value=2, an_test_value=32):
        self.car = a

    def lol(self):
        pass


class FooChild(Foo, metaclass=FieldInitializer):
    pass


if __name__ == "__main__":
    test = FooChild(1, 2, 3, 4, test_value=2, an_test_value=32, new_key=3)
    an_test = FooChild(10, test_value=20, an_test_value=32, new_key=3)

    print()
    print("         Tests")
    print(Foo)
    print(test.__dict__)
    print(an_test.__dict__)
    print()
    an_test.car = 100
    try:
        an_test.new_key = "d"
    except TypeError as e:
        print(e)
    print(an_test.car)
    print(test.__dict__)
    print(an_test.__dict__)
