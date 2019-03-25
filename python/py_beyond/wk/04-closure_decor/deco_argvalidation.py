import os
import sys
from pprint import pprint as pp

pd=os.path.dirname(os.getcwd())
ppd=os.path.dirname(pd)
sys.path.extend([pd,ppd])
import util


def check_non_negative(arg_index):
    def validator(f):
        def wrap(*args):
            if args[arg_index] < 0:
                raise ValueError(
                    'Argument {} expected to be non-negative'.format(arg_index))
            return f(*args)  #func execution
        return wrap
    return validator

@check_non_negative(1)  #1 is a 2nd argument in a decorated function
def create_list(value, size):
    return [value] * size


def demo_func_with_arg_validation_via_deco():
    util.banner('calling a function with 2nd arg validated through deco')
    l = create_list(0,5) # ok
    pp('called create_list ok  with result {}'.format(l))
    util.starprint('next call fails with an !!expected!! exception message from a decorator')
    #ll = create_list(0,-5) # nok
    pp('ll = create_list(0,-5)')


@check_non_negative(0)
@check_non_negative(1)
def dummy_func(par1, par2):
    print('par1: {}'.format(par1))
    print('par1: {}'.format(par2))

def demo_arg_valid_on_several_params():
    util.banner('multple args validation via chained decoratos')
    #dummy_func(-1,0) # expected raised exception
    #dummy_func(-1,-2) # expected raised exception
    #dummy_func(0,-2) # expected raised exception
    dummy_func(0,0) # expected no exception


if __name__ == '__main__':
    demo_func_with_arg_validation_via_deco()
    demo_arg_valid_on_several_params()