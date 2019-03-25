import os
import sys
from pprint import pprint as pp

pd=os.path.dirname(os.getcwd())
ppd=os.path.dirname(pd)
sys.path.extend([pd,ppd])
## added parent 2 folders to import util
import util

store = []

def sort_by_last_letter(strings):
    def last_letter(s):
        return s[-1]
    store.append(last_letter)  #simples caching
    print(last_letter)  #prints the adress of last_letter function
    return sorted(strings, key=last_letter)


g = 'global'
def outer(p='param'):
    l = 'local'
    def inner():
        print('accessing scopes {}, {}, {}'.format(g,p,l)) ##all 3 are accessible
    inner()

def demo_sort_by_last_let():
    util.banner('multiple calls to sort_by_last_letter redefine innner func')
    strparam= ['def', 'abc',  'ghi']
    r1 = sort_by_last_letter(strparam)
    r2 = sort_by_last_letter(strparam)
    print('intput param: {} sort by last letter resilt {}'.format(strparam,r2))

def demo_accessing_scopes_from_local_funcs():

    util.banner('scoping global params and local are accessible in local funcs')
    outer()

if __name__ == '__main__':
    demo_sort_by_last_let()
    demo_accessing_scopes_from_local_funcs()
