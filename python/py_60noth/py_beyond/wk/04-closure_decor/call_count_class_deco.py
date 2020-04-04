
import os
import sys
from pprint import pprint as pp

pd=os.path.dirname(os.getcwd())
ppd=os.path.dirname(pd)
sys.path.extend([pd,ppd])
import util


class CallCount:
    def __init__(self, f):   #f is a func object
        self.f = f
        self.count = 0

    #__call__must be implemented
    def __call__(self, *args, **kwargs):
        self.count += 1  #each call this attribute gets updated
        return self.f(*args, **kwargs) #f attribute is called

@CallCount
def hello(name):
    pp('Hello, {}'.format(name))


def demo_counts_of_hello_calls():
    util.banner('shows the counts of a func call through class decorator')
    hello('Micha')
    hello('Sveta')
    hello('Petya')
    hello('Grisha')
    print('hello was called {} times '.format(hello.count))


if __name__ == '__main__':
    demo_counts_of_hello_calls()