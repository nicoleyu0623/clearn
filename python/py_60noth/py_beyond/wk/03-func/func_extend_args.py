import os
import sys
from pprint import pprint as pp

pd=os.path.dirname(os.getcwd())
ppd=os.path.dirname(pd)
sys.path.extend([pd,ppd])
## added parent 2 folders to import util
import util


def demo_position_extended_args():
    util.banner("hypervolume signature with 1 required an 2nd optional positional params")

    def hypervolume(length, *lengths):
        v = length
        for item in lengths:
            v *= item
        return v

    pp('line {}'.format(hypervolume(2)))
    pp('cube {}'.format(hypervolume(2,2,2)))
    pp('hupercube {}'.format(hypervolume(2,2,2,2)))
    pp('expected exception if hypervolume is called with no args: hypervolume()')


def demo_named_extended_args():
    util.banner('tag func  is called with a arbitrary number of attributes in  signature')

    def tag(name, **kargs):
        result = '<' + name
        for key, value in kargs.items():
            result += ' {k}="{v}"'.format(k=key, v=value)
        result += '>'
        return result

    pp(tag('img',src="monet.jpg", alt="Sunrise by C. Monet", border=1))


def demo_extened_call_syntax():
    util.banner('prepare a list of args in a tuple before passing it to a func')
    def print_args(arg1, arg2, *args):
        pp(arg1)
        pp(arg2)
        pp(args)

    t=(11,12,13,14,15)
    print_args(*t)  # NB! observe *t

def demo_trace():
    util.banner('trace func demo. trace does not know about signature of traced function')

    def trace(f, *args, **kwargs):
        print('args =', args)
        print('kwargs = ', kwargs)
        result = f(*args, **kwargs) #this covers a signature of any func
        print("result = ", result)
        return result

    trace(int, "ff", base=16)


def demo_zip_transposed():
    util.banner('zip transposing')

    util.starprint('zip initially')
    sunday = [12,14,15,15]
    monday = [13,14,14,14]
    tuesday = [10,11,11,10]
    for item in zip(sunday,monday,tuesday):
        pp(item)
    daily = [sunday,monday,tuesday] #list of list
    util.starprint('daily is a list of lists')
    pp(daily)

    util.starprint('zipping all sublists in daily')
    for item in zip(*daily):
        pp(item)

    util.starprint('now transposed compare it to daily')
    transposed = list(zip(*daily))
    pp(transposed)

if __name__ == '__main__':
    demo_position_extended_args()
    demo_named_extended_args()
    demo_extened_call_syntax()
    demo_trace()
    demo_zip_transposed()