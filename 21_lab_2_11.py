import inspect
import sys


def exception_info(func):
    def test_func(*args, **kwargs):
        try:
            func(*args, **kwargs)
            return func(*args, **kwargs)

        except Exception:
            tb = sys.exc_info()[2]
            # iterate to the last frame
            while tb.tb_next:
                tb = tb.tb_next
            last_frame = tb.tb_frame

            # getting row of code before exception occured
            source_func = inspect.getsourcelines(last_frame)
            lines, first_line = source_func
            exception_lineno = last_frame.f_lineno
            func_lineno = exception_lineno - first_line
            row_before_exception = lines[func_lineno-1].strip()

            # getting values and names of arguments ripped func called with
            *arg_names,  arg_locals = inspect.getargvalues(last_frame)
            arg_names = arg_names[0] + [arg for arg in arg_names[1:]
                                        if arg is not None]
            args_dict = {}
            for arg in arg_names:
                args_dict[arg] = arg_locals[arg]

            return row_before_exception, args_dict
    return test_func


def test(arg, *args, key=1, key2=12, **kwargs):
    test_const = 1
    isinstance(arg, int)
    return arg/1000


@exception_info
def an_test(arg, *args, **kwargs):
    return test(arg, *args, **kwargs)


if __name__ == "__main__":
    b = [4]
    print(an_test(1, key=10))
    print(an_test(b, key=10))
    print(an_test(b, 3, 4, 5, key14=23, key=10))
    print(an_test(b))
