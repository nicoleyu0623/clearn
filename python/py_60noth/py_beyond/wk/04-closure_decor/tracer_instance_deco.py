import os
import sys
from pprint import pprint as pp

pd=os.path.dirname(os.getcwd())
ppd=os.path.dirname(pd)
sys.path.extend([pd,ppd])
import util


class Trace:
    def __init__(self):
        self.enabled = True #easy switch off tracing in tracer instance

    def __call__(self, f):
        def wrap(*args, **kwargs):
            if self.enabled:
                print('Calling {}'.format(f))
            return f(*args, **kwargs)
        return wrap




def demo_decor_with_instance():
    util.banner('2 calls with tracing via an instance decorator')
    tracer = Trace()

    @tracer    # observe the use of tracer name  tracer is instance of Trace
    def rotate_list(l):
        return l[1:] + [l[0]]

    l = [1,2,3]
    lr = rotate_list(l)
    print('{} rotated {}'.format(l,lr))

    tracer.enabled = False
    util.starprint('switched off tracing before next call')
    lrr = rotate_list(lr)
    print('{} rotated {}'.format(lr,lrr))


if __name__ == '__main__':
    demo_decor_with_instance()