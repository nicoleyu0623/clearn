import os
import sys
from pprint import pprint as pp

pd=os.path.dirname(os.getcwd())
ppd=os.path.dirname(pd)
sys.path.extend([pd,ppd])
## added parent 2 folders to import util
from util import *

from shipping import *

def demo_BaseContainer():
    banner('base container can be instantiated')
    c1 = ShippingContainer("ESC", 50, "electronics")
    pp(c1)

    c2 = ShippingContainer("ESC", 55, ["electronics","batteries"])
    pp(c2)

    starprint('class methods can define specialized instance constructors')
    c3 = ShippingContainer.create_empty('EUR',40)
    pp(c3)
    c4 = ShippingContainer.create_with_items('EUB',30, ['milk', 'meat', 'wheat'])
    pp(c4)


def demo_DerivedRefrigiratedContainer():
    banner('derived  class RefrigiratedContainer')
    r1 = RefrigeratedShippingContainer('MAE', 60, 'iced fish', -2)
    pp(r1)

    starprint('class method create_empty is interited create_empty() create_with_items()')
    starprint('pay extra caution that args names are not misspelled!')
    r2 = RefrigeratedShippingContainer.create_empty(owner_code='SHA',
                                                    length_ft=60,
                                                    celsius=-1.0)
    pp(r2)

    r3 = RefrigeratedShippingContainer.create_with_items(owner_code='SHA',
                                                    length_ft=60,
                                                    items=['meat', 'choco'],
                                                    celsius=-1.5)

    pp(r3)
    starprint('gettting and setting properties')
    pp('r3 temp in fahrenheit: {}'.format(r3.fahrenheit))
    starprint('r3 modify fahrenheit property via setter, and see chainge in celcius property')
    r3.fahrenheit = 27
    pp('r3 fahrenheit after mod: {}, celcius: {}'.format(r3.fahrenheit,r3.celsius))


    starprint('property accessing parent property')
    pp('r3 volume is container volume minus fridging equipment volume: {}'.format(r3.volume_ft3))

def demo_DoubleDerivedHeatedRefrigeratedShippingContainer():
    banner('double derived HeatedRefrigiratorContainer')
    rh1 = HeatedRefrigeratedShippingContainer.create_empty('YML',length_ft=40,celsius=-18.0)
    pp(rh1)
    starprint('try to set modify temperature')
    #rh1.celsius = -21.0 #too cold will produce expected exception
    rh1.celsius = -17.0
    pp(rh1)

if __name__ == '__main__':
    demo_BaseContainer()
    demo_DerivedRefrigiratedContainer()
    demo_DoubleDerivedHeatedRefrigeratedShippingContainer()

