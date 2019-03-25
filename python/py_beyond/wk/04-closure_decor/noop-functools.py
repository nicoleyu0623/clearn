import os
import sys
from pprint import pprint as pp

pd=os.path.dirname(os.getcwd())
ppd=os.path.dirname(pd)
sys.path.extend([pd,ppd])
import util
import functools


def hello():
    "Print a well-known message."
    print('Hello, world!')



def noop(f):
    def noop_wrapper(*args, **kwargs):
        return f(*args, **kwargs)
    return noop_wrapper

@noop
def hello2():
    "Print a 2nd well-known message."
    print('Hello, world 2!')


def noopfixed(f):
    @functools.wraps(f)   #use a functools.wraps()
    def noop_wrapper(*args, **kwargs):
        return f(*args, **kwargs)
    return noop_wrapper

@noopfixed
def hello3():
    "Print a 3nd well-known message."
    print('Hello, world 3!')

def demo_method_attributes():

    util.banner('decorators can change __name__ and __doc__')
    print('non-decorated hello func dunder name: {}'.format(hello.__name__))
    print('hello-decorated func dunder doc: {}'.format(hello.__doc__))

    util.starprint('hello2 with noop deco,')
    print('hello2 func dunder name: {}'.format(hello2.__name__))
    print('hello2 func dunder doc: {}'.format(hello2.__doc__))

    util.starprint('hello3 with noopfixed deco,')
    print('hello3 func dunder name: {}'.format(hello3.__name__))
    print('hello3 func dunder doc: {}'.format(hello3.__doc__))



if __name__ == '__main__':
        demo_method_attributes()