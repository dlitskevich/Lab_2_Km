import traceback
import inspect
import sys
import os


def exception_info(func):
    def test_func(*args, **kwargs):
        try:
            func(*args, **kwargs)
            return func(*args, **kwargs)

        except Exception:
            tb = sys.exc_info()[2]
            all_exceptions = traceback.extract_tb(tb)
            last_exception = all_exceptions[-1]
            print(tb.tb_frame.f_locals)
            print(last_exception)
            print(tb.tb_next.tb_next.tb_frame.f_locals)

            print()
            module = inspect.getmodule(tb.tb_frame.f_locals["func"])
            source = inspect.getsourcelines(module)
            row_before_exception = source[0][last_exception.lineno-2].strip()
            # print(inspect.getsourcelines(module_name))
            """
            

            f_locals = tb.tb_frame.f_locals
            name = tb.tb_frame.f_code.co_name

            all_exceptions = traceback.format_list(traceback.extract_tb(tb))
            last_exception = traceback.extract_tb(tb)[-1]
            print(all_exceptions)
            print(last_exception)
            print(last_exception)
            
            print(last_exception.f_code.co_consts)
            print(last_exception.f_code.co_varnames)
            print(last_exception.line)
            print(name)
            
            print()

            print(f_locals)
            print(f_locals.items())
            print(tb.tb_frame.f_code.co_consts)
            print(tb.tb_frame.f_code.co_varnames)
            # print(inspect.signature(name))
            print(traceback.extract_tb(tb))
            
            print(inspect.getsourcelines(last_exception.name))
            print(inspect.getsourcelines(test))
            
            
            """

            return row_before_exception, 1
    return test_func


def test(arg, *args, key=1):
    isinstance(arg, int)
    return arg/1000

@exception_info
def an_test(a, *args, key=1):
    a += [23]
    return test(a)


if __name__ == "__main__":
    b = [4]
    print(an_test(b, key=10))


