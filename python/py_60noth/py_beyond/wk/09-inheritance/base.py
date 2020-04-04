

class Base:
    def __init__(self):
        print('Base initializer')

    def f(self):
        print('Base.f()')

    def bf(self):
        print('Base.bf()')

    def bbb(self):
        print('Base.bbb()')

class Sub(Base):
    def __init__(self):
        super().__init__()  #this will call __init__ in parent
        print('Sub initializer')

    def f(self):
        print('Sub.f()')

    def bbb(self):
        super().bbb()
        print('Sub.bbb()')

#================================
import os
import sys
from pprint import pprint as pp
pd=os.path.dirname(os.getcwd())
ppd=os.path.dirname(pd)
sys.path.extend([pd,ppd])
from util import *


def demo_Base_Sub():

    starprint('calling a base class. check its init')
    banner('basic single inheritance')
    starprint('b = Base()')
    b = Base()
    starprint('calling a derived class. check its init c=Sub()')
    c = Sub()

    starprint('c.bf() a method from derived which is only in base')
    c.bf()

    starprint('c.f() f method in derived which is also in super')
    c.f()

    starprint('c.bbb() a metho which like __init__ calls the same method in parent')
    c.bbb()

if __name__ == '__main__':
    demo_Base_Sub()
