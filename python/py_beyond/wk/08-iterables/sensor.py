import datetime
import itertools
import random
import time

class Sensor:
    def __iter__(self):
        return self

    def __next__(self):
        return random.random()


import os
import sys
from pprint import pprint as pp

pd=os.path.dirname(os.getcwd())
ppd=os.path.dirname(pd)
sys.path.extend([pd,ppd])
from util import *


def demo_sensor():
    banner('dummy sensor')

    sensor = Sensor()

    ## inifinite sequence (None)
    timestamps = iter(datetime.datetime.now, None)

    #limit the zip output to 5 elements
    for stamp, value in itertools.islice(zip(timestamps, sensor), 5):
        print(stamp, value)
        time.sleep(1)

if __name__ == '__main__':
    demo_sensor()