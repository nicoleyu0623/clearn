#!/usr/bin/env python3
'''A modulefor demonstration exceptions'''

def banner(message, border="-"):
    line = border * len(message)
    print(line)
    print(message)
    print(line)


def starprint(message,stars=2):
        mstars = '*' * stars
        ending = ''
        if stars == 4:
                ending = '!'
        newline = ''
        if stars == 2:
                newline='\n'
        print(newline,mstars,message,ending)

def convert(s):
    '''Convert to an integer'''
    x = int(s)
    return x


def convertWithExcept(s):
    try:
        x = int(s)
        print("conversation ok x=", x)
    except ValueError:
            print("value error conversion nok for ", s)
            x = -1
    except TypeError:
            print("type error conversion nok for ",s)
            x = -1
    return x

def convertWithExceptCompact(s):
    x = -1 # default value
    try:
        x = int(s)
        print("conversation ok x=", x)
    except (ValueError, TypeError):
            print("Conversion failed")
    return x

import sys

def convertWithExceptionMessage(s):
    '''Convert to an integer'''
    try:
        return int(s)
    except (ValueError, TypeError) as e:
        print("Conversion error: {}".format(str(e)),
              file=sys.stderr )
        return -1

def convertWithExceptionRaise(s):
    '''Convert to an integer'''
    try:
        return int(s)
    except (ValueError, TypeError) as e:
        print("Conversion error: {}".format(str(e)),
              file=sys.stderr )
        raise    # allows to avoid returning an error code


def test_ch7_except_conversion():
    banner("test conversions")
    print(convert(34.5))  #ok
    print(convert("33")) # ok
    #print(convert('mama')) # nok
    print(convertWithExcept("mama"))
    print(convertWithExcept([1, 2, 3]))
    print("calling convertWithExceptCompact():",convertWithExceptCompact(['a','b']))

    print("calling convertWithExceptionMessage():",
          convertWithExceptionMessage('a'))

from math import log

def test_ch7_except_convert_return_error_code():
    banner("returning error code is bad")

    def string_log(s):
        v = convertWithExceptionMessage(s)
        return log(v)   # log(-1) is a math error

    def string_log_bis(s):
        v = convertWithExceptionRaise(s)
        return log(v)   # log(-1) is a math error



    #print( string_log('mama'))

    print( string_log_bis("mama"))  ## no error code is returned

import sys

def test_ch7_except_sqrt_heron():

    def sqrt(x):
        '''compute square roots using the method of Heron of Alexandria'''
        guess = x
        i = 0
        while  guess * guess != x and i < 20:
            guess = (guess + x / guess) / 2.0
            i += 1
        return guess

    try:
        x = sqrt(9)
        print("heron sqrt",x)
        x = sqrt(2)
        print("heron sqrt",x)
        badval = sqrt(-1)
        print('this is never printed')
    except ZeroDivisionError:    ## we need to know what exception happens here
        print('cannot compute a root of negative number')

    print('program execution continues normally here')

def test_ch7_except_sqrt_heron_value_error():
    """"lets add a negative arg check insde the sqrt func"""

    def sqrt(x):
        '''compute square roots using the method of Heron of Alexandria'''
        if x < 0:
                raise ValueError("Cannot compute square root of negative number {}".format(x))
        guess = x
        i = 0
        while  guess * guess != x and i < 20:
            guess = (guess + x / guess) / 2.0
            i += 1
        return guess

    try:
        x = sqrt(81)
        print(x)
        y = sqrt(-9)
        print('this is never printed')
    except ValueError as e:    # a much more generic exception which we know is raised in func
        print(e, file=sys.stderr)

    print('program execution continues normally here')


def test_ch7_except_api_exceptions():
    print('bad indexing')
    try:
        z = [1,2,3,4]
        z[4] = 5  #bad index
    except IndexError as e:
        print(e, file=sys.stderr)

    print('bad value type')
    try:
        x = int("0")
        y  = int("jim")
    except ValueError as e:
        print(e, file=sys.stderr)

    print('bad key')
    try:
        codes = dict(gb=44, us=1, no=47, ch=41)
        y  = codes['de']
    except KeyError as e:
        print(e, file=sys.stderr)

import os


def test_ch7_except_api_makedir():

    import os
    def make_at(path, dir_name):
        original_path = os.getcwd()
        try:
            os.chdir(path)
            os.mkdir(dir_name)
        except OSError as e:
            print(e, file=sys.stderr)
        finally:     #this block always execute regardless exception raised
            os.chdir(original_path)


    try:
        os.rmdir("/tmp/test1")  #make sure before test that the target folder does not exist
    except OSError as e:
        pass

    print("cur dir:", os.getcwd())
    make_at("/tmp", "test1")
    print("cur dir after 1 call:", os.getcwd())
    make_at("/tmp", "test1")  #except to get exception dir exists
    print("cur dir after 2nd call:", os.getcwd())


def test_ch7_except_api_WinUnixGetkey():
    """Platform-specific code. make a function work on windows and on unix"""
    from keypress import getkey as gk

    print("this is expected to work on both unix and windows")
    print("please press 1 key")
    captured_char = gk()
    print("captured char is:",captured_char)




def main():
    """ Run python exception tests
    """
    banner("exploring python exceptions",border="*")

    # ! execute one function by one for a meaningful output

    #test_ch7_except_conversion()
    #test_ch7_except_convert_return_error_code()
    #test_ch7_except_sqrt_heron()
    #test_ch7_except_sqrt_heron_value_error()   # clean way
    #test_ch7_except_api_exceptions()
    #test_ch7_except_api_makedir()
    #test_ch7_except_api_WinUnixGetkey() # this test do not run from inside pycharm but from cmd



if __name__ == '__main__':
    main()