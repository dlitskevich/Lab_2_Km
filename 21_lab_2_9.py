
class Value(object):
    value = 0
    commission = 10

    def __get__(self, instance, owner):
        return self.value, self.commission

    def __set__(self, instance, init_value):
        self.value = init_value[0]
        self.commission = init_value[1]


class Account:
    amount = Value()

    def __init__(self, init_value=0, init_commission=10):
        self.amount = (init_value, init_commission)
        return

    def __call__(self, operation=None, amount=None):

        return self.amount


if __name__ == "__main__":
    test_account = Account(1, 1)
    test_an_account = Account(20, 3)

    print(test_account())
    print(test_an_account.__dict__)
    print(test_an_account())
