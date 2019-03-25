import os
import sys
from pprint import pprint as pp

pd=os.path.dirname(os.getcwd())
ppd=os.path.dirname(pd)
sys.path.extend([pd,ppd])
## added parent 2 folders to import util
import util



def raise_to(exponenta):
    def raise_to_exp(x):
        return pow(x,exponenta)
    return raise_to_exp



def demo_factory_squares_cubes():

    util.banner('raise_to closure returning more specialized functions')
    square = raise_to(2)
    cube = raise_to(3)
    divisor = raise_to(-1)
    util.starprint('different calls of raise_to produce different functions')
    pp(square)
    pp(cube)

    pp('square of 3: {}'.format(square(3)))
    pp('cube of 3: {}'.format(cube(3)))
    pp('divisor of 3: {}'.format(divisor(3)))


if __name__ == '__main__':

    demo_factory_squares_cubes()
