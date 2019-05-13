

class Dict:
    def __get__(self, instance, owner):
        return instance.__dict__

    # def __set__(self, instance, value):
        # instance.__dict__[value] = {}


class RecursiveDict:
    dictionary = Dict()

    """
    def default_value(self):
        default_values = {
            int: 0,
            list: [],
            dict: {}
        }
        return default_values[self.type]
    """

    def __init__(self, default_type=int):
        # self.type = default_type
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
            print(self.dictionary)
            return self.dictionary[item]

    def __repr__(self):
        return "{}".format(self.dictionary)


if __name__ == "__main__":
    test_dict = RecursiveDict()
    test_dict["ab"] = "first"
    print(test_dict.__dict__)

    #test_dict["ac"]["bc"] = "second"
    #print(test_dict.__dict__)

    test_dict["a"]["b"]["c"] = 1
    print(test_dict["a"]["b"])
    print(test_dict.__dict__)

    print(test_dict["aff"]["b"])
    print(test_dict.__dict__)

    test_an_dict = RecursiveDict()
    print(test_dict.__dict__)
    print(test_an_dict.__dict__)
