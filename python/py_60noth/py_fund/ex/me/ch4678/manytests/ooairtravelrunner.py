#!/usr/bin/env python3
"""Test running created objects

Usage:
    python3 ooairtravelrunner.py

"""


from ooairtravel import *


def banner(message, border="-"):
    line = border * len(message)
    print(line)
    print(message)
    print(line)

def main():
    banner("creating and booking two flights",border="*")
    f,g = make_flights()
    print("{0} available seats for aircraft {1} after passenger registration"
          .format(f.num_available_seats(), f.aircraft_model() ))
    banner("printing boards for the fist flight",border="*")
    f.make_boarding_cards(console_card_printer)


    banner("printing boards for the 2nd flight",border="*")
    g.make_boarding_cards(console_card_printer)

if __name__ == '__main__':
    main()