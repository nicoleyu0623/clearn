import os
import sys
from pprint import pprint as pp

pd=os.path.dirname(os.getcwd())
ppd=os.path.dirname(pd)
sys.path.extend([pd,ppd])
## added parent 2 folders to import util
import util



def demo_sorted():
    util.banner('demo how to sort on 2nd family name using lamba' + \
       'func as a key param of built-int sorted')
    scientist = ['Marie Curie', 'Albert Einsterin', 'Niels Bohr',
                 'Isaac Newton', 'Charles Darwin']
    pp(sorted(scientist, key=lambda name: name.split()[-1]))

if __name__ == '__main__':
    demo_sorted()