'''
String Compression

Problem

Given a string in the form 'AAAABBBBCCCCCDDEEEE' compress it to become 'A4B4C5D2E4'. For this problem, you can falsely "compress" strings of single or double letters. For instance, it is okay for 'AAB' to return 'A2B1' even though this technically takes more space.

The function should also be case sensitive, so that a string 'AAAaaa' returns 'A3a3'.
'''

def compress_szi(s):
    if len(s) == 0:  #empty string case
        return ''
    cnt = {}
    for c in s:
        if c in cnt:
            cnt[c] +=1
        else:
            cnt[c] = 1
    comps=''
    for (k,v) in cnt.items():
        comps+=k
        comps+=str(v)
    return comps

###########
# author solution  does not use dictionaries
##################
def compress(s):
    r = ""
    l = len(s)

    if l == 0:
        return ''
    if l == 1:
        return s + '1'

    last = s[0]
    cnt = 1
    i = 1

    while i < l:
        if s[i] == s[i - 1]:
            cnt += 1
        else:
            r = r + s[i - 1] + str(cnt)
            cnt = 1
        i += 1
    r = r + s[i - 1] + str(cnt)
    return r
    pass

"""
RUN THIS CELL TO TEST YOUR SOLUTION
"""
from pprint import pprint as pp
from nose.tools import assert_equal

class TestCompress(object):

    def test(self, sol):
        assert_equal(sol(''), '')
        assert_equal(sol('AABBCC'), 'A2B2C2')
        assert_equal(sol('AAABCCDDDDD'), 'A3B1C2D5')
        assert_equal(sol('AAABCC  DDDDD'), 'A3B1C2 2D5')

        print('ALL TEST CASES PASSED')

# Run Tests
if __name__ == '__main__':
    t = TestCompress()
    t.test(compress_szi)
    t.test(compress)