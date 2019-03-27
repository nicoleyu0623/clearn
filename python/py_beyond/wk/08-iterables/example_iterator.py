
class MyBasicIterator:
    def __init__(self, data):
        self.index = 0
        self.data = data

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.data):
            raise StopIteration()

        rslt = self.data[self.index]
        self.index += 1 #update index
        return rslt

class ExampleIterable:
    def __init__(self):
        self.data = [1, 2, 3]

    def __iter__(self):
        return MyBasicIterator(self.data) #self.data is a indexable sequence


import os
import sys
from pprint import pprint as pp
from util import *

pd=os.path.dirname(os.getcwd())
ppd=os.path.dirname(pd)
sys.path.extend([pd,ppd])


def demo_ExampleIterator():
    banner('simplistic iterator demo')
    starprint('need to implement __iter__, __next__')
    it = MyBasicIterator(data=['a', 'b', 'c'])

    pp(next(it))
    pp(next(it))
    pp(next(it))
    pp('another call of next(it) will produce exception')
    pp('no more elements to iterate')

    starprint('iterator can be insie for statement')
    it =MyBasicIterator(data=['aa', 'bb', 'cc'])
    for el in it:
        pp(el)

def demo_ExampleIterable():
    banner('ExampleIterable has internal sequence of data ')
    for el in ExampleIterable():
        print(el)

    starprint('example usage in comprehension')
    ll = [ i * 3 for i in ExampleIterable()]
    pp('in comprehension each iterable element multipled  by 3: {}'
       .format(ll))


if __name__ == '__main__':
    demo_ExampleIterator()
    demo_ExampleIterable()
