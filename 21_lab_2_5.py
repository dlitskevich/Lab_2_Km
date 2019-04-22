

def cached(f):
    memo = {}

    def helper(*args, **kwargs):
        if (args, frozenset(kwargs.items())) not in memo:
            print("Value added to cache {} {}".format(args, kwargs))
            memo[(args, frozenset(kwargs.items()))] = f(*args, **kwargs)
        else:
            print("Value from cache {0} {1}".format(args, kwargs))
        return memo[(args, frozenset(kwargs.items()))]
    return helper


@cached
def recursive_fibonacci(member_order):
    """ Computes n-th fibonacci number
        Arguments:
        member_order -- order
        Returns:
        n-th fibonacci number
    """

    if member_order in (1, 2):
        return 1
    else:
        return recursive_fibonacci(member_order - 1) \
               + recursive_fibonacci(member_order - 2)


@cached
def get_fibonacci(current_order, answer, following):
    """
    compute fibonacci using tail recursion
    :param current_order: iterator
    :param answer:
    :param following:
    :return:
    """
    if current_order == 0:
        return answer
    return get_fibonacci(current_order - 1, following, answer + following)


@cached
def test(*args, **kwargs):
    return args, kwargs


def fibonacci_tail_recursion(member_order):
    """ Computes n-th fibonacci number
        Arguments:
        member_order -- order
        Returns:
        n-th fibonacci number
    """

    return get_fibonacci(member_order, 0, 1)


if __name__ == "__main__":
    # DO NOT use numbers over ~900 as RecursionError can occur
    fibonacci_order = 13
    # for demonstration only
    print("{}\n".format(recursive_fibonacci(fibonacci_order)))

    print("{}".format(fibonacci_tail_recursion(fibonacci_order)))
    print("{}\n".format(fibonacci_tail_recursion(fibonacci_order)))

    print("{}".format(test(12, 345, key=1, key2=2)))
    print("{}".format(test(12, 345, key2=2, key=1, )))
