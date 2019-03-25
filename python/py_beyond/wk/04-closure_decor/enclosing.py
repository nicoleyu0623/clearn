
import os
import sys
from pprint import pprint as pp

pd=os.path.dirname(os.getcwd())
ppd=os.path.dirname(pd)
sys.path.extend([pd,ppd])
import util


message = 'global'


def enclosing():
    message = 'enclosing'

    def local():
        nonlocal  message   #without nonlocal keyword local() func cannot modify
                            # message variable for higher scope
        message = 'local'

    print('before local() call enclosing message:', message)
    local()
    print('afer local()  call enclosing message:', message)


def demo_non_local_variable():
    print('before call global message:', message)
    enclosing()
    print('afer call global message:', message)



if __name__ == '__main__':
    demo_non_local_variable()