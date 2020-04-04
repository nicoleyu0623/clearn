
import os
import sys
from pprint import pprint as pp

pd=os.path.dirname(os.getcwd())
ppd=os.path.dirname(pd)
sys.path.extend([pd,ppd])
## added parent 2 folders to import util
from util import *




class Point2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return '({}, {})'.format(self.x, self.y)

    def __repr__(self):
        return 'Point2D(x={}, y={})'.format(self.x, self.y)

    def __format__(self, f):
        if f == 'r':
            return 'Point2D(x={}, y={})'.format(self.y, self.x)
        else:
            return '{}, {}'.format(self.x, self.y)




def    demo_Point():
        banner('str(obj), repr(obj, format(obj')
        p = Point2D(1.0, 2.0)
        print(str(p))  #using str
        print(repr(p)) #using repr  unambigous string about obj
        print('print by default uses str(obj) print(p): {}'.format(p))

        starprint('expected non-pgogrammer oriented use of str()')
        print('The cercle is centered at {}.'.format(p))

        pp('format(obj) calls str(obj)')
        starprint('calling format with a param')
        print('extended format: {:r}.'.format(p))


def demo_asci_ord_chr():
    banner('asc() ord()  chr()')

    x = 'Hællo'
    y = ascii(x)
    pp(y)

    starprint('ord()')
    x='¾'
    pp('code for unicode 3/4: {}'.format(ord(x)))

    starprint('chr() is opposite of orc()')
    pp('chr(190) result: {}'.format(chr(190)))



if __name__ == '__main__':
    demo_Point()
    demo_asci_ord_chr()
