
import os
import sys
from pprint import pprint as pp

pd=os.path.dirname(os.getcwd())
ppd=os.path.dirname(pd)
sys.path.extend([pd,ppd])
import util



def escape_unicode(f):
    def wrap(*args, **kwargs):
        x = f(*args, **kwargs)
        return ascii(x)

    return wrap


class Trace:
    def __init__(self):
        self.enabled = True

    def __call__(self, f):
        def wrap(*args, **kwargs):
            if self.enabled:
                print('Calling {}'.format(f))
            return f(*args, **kwargs)
        return wrap

tracer = Trace()  #define a global variable


def demo_chain_decorator():

    util.banner('decorators can be applied in chain (here tracer + escape_unicode')

    @tracer
    @escape_unicode
    def norwegian_island_maker(name):
        return name + 'øy'


    isl1 = norwegian_island_maker('Llama')
    isl2 = norwegian_island_maker('Troll')
    isl3 = norwegian_island_maker('Python')
    print("islands {} {} {}".format(isl1,isl2,isl3))


#create a class version of island_maker methods
class IslandMaker:
    def __init__(self, suffix):
        self.suffix = suffix

    @tracer
    def make_island(self, name):
        return name + self.suffix

def demo_decorator_on_class_method():
     util.banner('IslandMakers method make_island is decorated with tracer global variable')
     im = IslandMaker('øy')
     isl1 = im.make_island('Python')
     pp('made island {}'.format(isl1))


if __name__ == '__main__':
    demo_chain_decorator()
    demo_decorator_on_class_method()