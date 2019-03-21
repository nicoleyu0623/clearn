import sys
from itertools import count, islice

def sequence():
    """Generate Recaman's sequence."""
    seen = set()
    a = 0
    for n in count(1):
        yield a           # a generator
        seen.add(a)
        c = a - n
        if c < 0 or c in seen:
           c = a + n
        a = c

def write_sequence(filename, num):
    """Write Recaman's sequence to a text file."""
    with open(filename, mode='wt', encoding='utf-8') as f: # with block allows
        f.writelines("{0}\n".format(r)                     #to avoid closing files explicitely
                     for r in islice(sequence(), num + 1))

    print("created file {}. sequence has {} elemnts.".format(filename,num))

if __name__ == '__main__':
    # write_sequence(filename=sys.argv[1],
    #                num=int(sys.argv[2]))
    write_sequence(filename="recaman_seq.dat", num=int(100))
