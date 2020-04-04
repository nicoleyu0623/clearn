"""Module for demonstrating files."""

import sys

fn = 'wasteland.txt'  #global var


def writeDummyFile():
    f = open(fn, mode='wt', encoding='utf-8')
    f.write('What are the roots that clutch,')
    f.write('What branches grow.\n')
    f.write('Out of this stony rubbish?\n')
    f.close()


def appendDummyFile():
    f = open(fn, mode='at', encoding='utf-8')
    f.write('I am out of this situation.')
    f.write('\n')
    f.close()

def read(filename):
    f = open(filename, mode='rt', encoding='utf-8')
    for line in f:              #f object is an iterator
        sys.stdout.write(line)
    f.close()

def _words_per_line(flo):
    return [ len(line.split()) for line in flo.readlines()  ]

def file_like_iterator():
    with open(fn, mode = 'rt', encoding='utf-8') as real_file:
        wpl = _words_per_line(real_file)
    print("for file: {} words per line: {}".format(fn, wpl))
    print(type(real_file))


def url_response_like_iterator():
    from urllib.request import urlopen
    urln = 'http://sixty-north.com/c/t.txt'
    with urlopen(urln) as web_file:
        wpl = _words_per_line(web_file)
    print("for web file: {} words per line: {}".format(urln, wpl))
    print(type(web_file))


def main():
    writeDummyFile()
    appendDummyFile()
    read(fn)
    file_like_iterator()  # files are iterables
    url_response_like_iterator() # web response is like a file



if __name__ == '__main__':
  main()
