'''Read and print an integer series.'''

import sys

def read_series_simpl(filename):
    try:
        f = open(filename, mode='rt', econding='utf-8')
        series=[]
        for line in f:
            a = int(line.strip()) ## strip \n  from end of line, convert to int
            series.append(a)
    finally:
        f.close()
    return series

def read_series(filename):
    with open(filename, mode='rt', encoding='utf-8') as f:  #with block ensures file is closed
        return [int(line.strip()) for line in f]


def main(filename):
    series = read_series(filename)
    print(series)

if __name__ == '__main__':
    #main(sys.argv[1])
    main('recaman_seq.dat')
    print("\nchecking how exception handled when reading a file with a bad contents")
    # main('recaman_seq_bad.dat')  #exception is raised but the file is closed
