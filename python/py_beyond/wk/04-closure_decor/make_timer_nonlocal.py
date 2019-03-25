
import os
import sys
from pprint import pprint as pp

pd=os.path.dirname(os.getcwd())
ppd=os.path.dirname(pd)
sys.path.extend([pd,ppd])
import util
import time

def make_timer():
    last_called = None

    def elapsed():
        nonlocal last_called
        now = time.time()
        if last_called is None:
            last_called  = now
            return None
        result = now - last_called
        last_called = now
        return result
    return elapsed


def demo_distinct_timers():
    util.banner('t1() and t2() are independent timers')
    t1 = make_timer()
    print('t1 elapsed first call {}'.format(t1()))
    t2 = make_timer()
    print('t2 elapsed 1st call {}'.format(t2()))
    print('t1 elapsed 2nd call {}'.format(t1()))
    time.sleep(1)
    print('t1 elapsed 3nd call {}'.format(t1()))
    time.sleep(2)
    print('t2 elapsed 2st call {}'.format(t2()))




if __name__ == '__main__':
    demo_distinct_timers()

