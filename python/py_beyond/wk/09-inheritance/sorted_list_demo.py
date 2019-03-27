# object
# |
# SimpleList -----|
# |               |
# SortedList    IntList
#        |        |
#       SortedIntList


import os
import sys
from pprint import pprint as pp
pd=os.path.dirname(os.getcwd())
ppd=os.path.dirname(pd)
sys.path.extend([pd,ppd])
from util import *
from sorted_list import *

def demo_sorted_list():
    banner('SortedList (derived from SimpleList)')
    sl=SortedList([4,3,78,1])
    pp('after initialization: sl=SortedList([4,3,78,1]) {}'.format(sl))
    starprint('add a value to the sorted list')
    sl.add(-42)
    pp('SortedList.add() calls SimpleList.add() with super().add()')
    pp('after adding -42, : {}'.format(sl))

    pp('isinstance(sl,SortedList):{}'.format(isinstance(sl,SortedList)))
    pp('isinstance(sl,SimpleList):{}'.format(isinstance(sl,SimpleList)))

def demo_int_list():
    banner('IntList (derived from SimpleList')
    starprint('il = IntList([1,-3,4,5])')
    il = IntList([1,-3,4,5])
    il.add(-9)
    pp('IntList.add() calls SimpleList.add() with super().add()')
    pp('after 1 ints added -9, IntList: {}'.format(il))
    pp('il.add("5") produces expected typeError exceptin')

def demo_multple_inheritance_list():
    banner('multiple iheritance SortedIntList')
    sil = SortedIntList([1,-1,0,5,9,-10])
    pp('sil = SortedIntList([1,-1,0,5,9,-10]) : {}'.format(sil))
    pp('sil = SortedIntList([1,-1.0] produces expected typeError exception')

    starprint('sil.add() maintains constraints from both parent classes')
    sil.add(-323)
    pp('sil.add(-323): {}'.format(sil))

    pp('SortedIntList.__bases__ : {}'.format(SortedIntList.__bases__))

    starprint('SortedIntList.__mro__',nstars=3,starchar='>')
    pp(SortedIntList.__mro__)

    starprint("observe that sequence in __mro__ is the same as in trace calls")
    pp('as add() is present in all 3 parent classes, it is called according to the __mro__ sequence.')

def demo_diamond_mro_basic():
    banner('mro with 4 classes, D has multiple inheritance')
    class A:
        def func(self):
            return 'A.func'
    class B(A):
        def func(self):
            return 'B.func'
    class C(A):
        def func(self):
            return 'C.func'
    class D(B,C):
        pass

    starprint('D.__mro__', nstars=3,starchar='>')
    pp(D.__mro__)

    starprint('resolving a D.func() which is not preent in D but in B, C,A')
    d=D()
    starprint('d.func()', nstars=3,starchar='>')
    pp(d.func())
    pp('according to D.__mro__ it is returned from B as B is a first in mro sequence where func() is present')


def demo_super_sortedInstList():
    banner('super() resolution ')
    sil = SortedIntList([1,-1,0,5])
    starprint('SortedIntList.__mro',nstars=3,starchar='>')
    pp(SortedIntList.__mro__)

    print('super(SortedList,sil).add(10) will call SimpleList.add as it is AFTER SortedList in mro sequence')
    starprint('SortedList, sil).add(10)',nstars=3,starchar='>')
    super(SortedList, sil).add(10)

    starprint('super() with no args in SortedInList method is the same as super(SortedIntList,sil).add() ')
    starprint('sil.add(9)', nstars=3,starchar='>')
    sil.add(9)
    pp(sil)
    starprint('it is the same call as below')
    starprint('SortedIntList, sil).add(9)', nstars=3,starchar='>')
    super(SortedIntList, sil).add(9)
    pp(sil)
    starprint('i.e. method is resolved in SortedIntList.__mro__ sequence AFTER SortedIntList entry')

def demo_object():
    banner('object is a base class for any other object')
    print(dir(object))
    banner('Python does not require type safety')
    starprint('any method can accept any type as arg')
    starprint('so inheritance is used for a code reuse and not for type hierarchies')


if __name__ == '__main__':
    demo_sorted_list()
    demo_int_list()
    demo_multple_inheritance_list()
    demo_diamond_mro_basic()
    demo_super_sortedInstList()
    demo_object()