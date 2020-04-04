
import os
import sys
from pprint import pprint as pp

pd=os.path.dirname(os.getcwd())
ppd=os.path.dirname(pd)
sys.path.extend([pd,ppd])
import util


#function decorator is defined as a closure
def escape_unicode(f):
    def wrap(*args, **kwargs):
        x = f(*args, **kwargs)  #covers any function signature
        return ascii(x)    #transforms output of f by applying ascii() on it

    return wrap


@escape_unicode
def northern_city1():
    return 'Tromsø'

@escape_unicode
def northern_city2():
    return 'Bergøya'

@escape_unicode
def european_city1():
    return 'Paris'


def demo_norther_cities():
    util.banner('a decorator transforms a func without modifying it')
    pp('decorated cities: {} {} {}'.format(northern_city1(),\
                                        northern_city2(),\
                                        european_city1()))



if __name__ == '__main__':
    demo_norther_cities()