

def cached(f):
    """
    main task function
    memoizing values with given params of ANY type
    :param f:
    :return:
    """
    memo = {}

    def helper(*args, **kwargs):
        frozen_arguments = frozen_unhashable((args, kwargs.items()))
        if frozen_arguments not in memo:
            print("Value added to cache {} {}".format(args, kwargs))
            memo[frozen_arguments] = f(*args, **kwargs)
        else:
            print("Value from cache {0} {1}".format(args, kwargs))
        return memo[frozen_arguments]
    return helper


def frozen_unhashable(argument):
    """
    frozenset applied to almost everything unhashable
    :param argument:
    :return:
    """
    # to prevent iteration through string as array of chars
    if isinstance(argument, str):
        return argument

    frozen_arguments = []
    try:
        for arg in argument:
            frozen_arguments.append(frozen_unhashable(arg))
    except TypeError:
        # for leaves
        try:
            hash(argument)
            return argument
        except TypeError:
            return frozenset(argument)
    # no matter what iterable object it was
    return frozenset(frozen_arguments)


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
    # print(hash({1:2}))

    print("{}\n".format(recursive_fibonacci(fibonacci_order)))

    print("{}".format(fibonacci_tail_recursion(fibonacci_order)))
    print("{}\n".format(fibonacci_tail_recursion(fibonacci_order)))

    print("{}".format(test(12, 345, key={1: {2: {3: [1, 2]}}}, key2=2)))
    print("{}".format(test(12, 345, key2=2, key={1: {2: {3: [1, 2]}}}, )))
