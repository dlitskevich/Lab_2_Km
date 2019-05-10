

class Dict:
    def __get__(self, instance, owner):
        return instance.__dict__

    # def __set__(self, instance, value):
        # instance.__dict__[value] = {}


class RecursiveDict:
    dictionary = Dict()

    def __init__(self):
        return

    def __setitem__(self, key, value):
        # print("set", key, value)
        self.dictionary[key] = value

    def __getitem__(self, item):
        # print("get", item)
        try:
            return self.dictionary[item]
        except KeyError:
            self.dictionary[item] = RecursiveDict()
            return self.dictionary[item]

    def __repr__(self):
        return "{}".format(self.dictionary)


if __name__ == "__main__":
    test_dict = RecursiveDict()
    test_dict["ab"] = "first"
    print(test_dict.__dict__)

    test_dict["ac"]["bc"] = "second"
    print(test_dict.__dict__)

    test_dict["a"]["b"]["c"] = 1
    print(test_dict["a"]["b"])
    print(test_dict.__dict__)

    print(test_dict["aff"]["b"])
    print(test_dict.__dict__)

    test_an_dict = RecursiveDict()
    print(test_dict.__dict__)
    print(test_an_dict.__dict__)
