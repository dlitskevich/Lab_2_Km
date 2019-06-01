
class Value(object):
    def __get__(self, instance, owner):
        return instance.value, instance.commission

    def __set__(self, instance, init_value):
        instance.value = init_value[0]
        instance.commission = init_value[1]


class Account:
    balance = Value()

    def __init__(self, init_value=0, init_commission=10):
        self.balance = (init_value, init_commission)
        return

    def __call__(self, operation=None, amount=0):
        operations = {
            None: ("None", str(self)),
            "add":  ["self.add(amount)",
                     "Balance change: +{} Commission was {}"
                     "".format(amount, (self.balance[1]/100*amount))],
            "subtract": ["self.add(-amount)",
                         "Balance change: -{} Commission was {}"
                         "".format(amount, (self.balance[1]/100*amount))],
            "commission": ["self.change_commission(amount)",
                           "Commission changed to {}%".format(amount)]
        }
        if operation in operations:
            eval(operations[operation][0])
            return operations[operation][1]
        else:
            return "No operation's been found"

    def __str__(self):
        return "Account's balance: {} Account's commission: {}%".format(
            self.balance[0], self.balance[1]
        )

    def add(self, amount):
        balance = self.balance[0]
        commission = self.balance[1]
        changed_balance = balance+amount-abs(amount)*commission/100
        self.balance = (changed_balance, commission)
        return

    def change_commission(self, commission):
        self.balance = (self.balance[0], commission)
        return


if __name__ == "__main__":
    test_account = Account(1, 1)
    test_an_account = Account(20, 3)

    print(test_account())
    print(test_account("commission", 10))
    print(test_account)
    print(test_account("add", 10))
    print(test_account)
    print(test_account("subtract", 10))
    print(test_account)

    print()
    print(test_an_account.__dict__)
    print(test_an_account())
    print(test_account())
