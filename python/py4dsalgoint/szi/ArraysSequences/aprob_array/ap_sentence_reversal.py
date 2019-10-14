'''
Given a string of words, reverse all the words. For example:

Given:

'This is the best'
Return:

'best the is This'
As part of this exercise you should remove all leading and trailing whitespace. So that inputs such as:

'  space here'  and 'space here      '
both become:

'here space'
'''

#O(n)
def rev_word_szi(s):
    #clean preceeding white chars
    cnt = 0
    for i in range(len(s)):
        if s[i] == ' ':
            cnt +=1
        else:
            break #get out of loop on first non space char
    s = s[cnt:]  #subindex the string

    #clean last white chars
    cnt = 0
    for i in range(len(s)):
        if s[len(s)-i-1] == ' ':
            cnt+=1
        else:
            break  #get ot of loop on frist non space char from the end
    s = s[:(len(s)-cnt)]

    #now store words
    words = []
    cword = ''
    for i in range(len(s)):

        if s[i] == ' ':
            if len(cword) > 0:
                words.append(cword)
                cword=''
            else:
                continue
        else:
            cword += s[i]


        if i == len(s) -1: #last element
            words.append(cword)

    #pp('deb: words:{}'.format(words))
    #costruct reversed sentence
    reversed = ''
    for i in range(len(words)):
        reversed+=words[len(words)-i-1]
        if i != len(words)-1:
            reversed+=' '
    return reversed

#O(n)
###################
## sol by author  treats inner spaces longer than 1 space
#################
def rev_word3(s):
    """
    Manually doing the splits on the spaces.
    """

    words = []
    length = len(s)
    spaces = [' ']

    # Index Tracker
    i = 0

    # While index is less than length of string
    while i < length:

        # If element isn't a space
        if s[i] not in spaces:

            # The word starts at this index
            word_start = i

            while i < length and s[i] not in spaces:
                # Get index where word ends
                i += 1
            # Append that word to the list
            words.append(s[word_start:i])
        # Add to index
        i += 1

    # Join the reversed words
    return " ".join(reversed(words))

from pprint import pprint as pp
from nose.tools import assert_equal


class ReversalTest(object):

    def test(self, sol):
        assert_equal(sol('    space before'), 'before space')
        assert_equal(sol('space after     '), 'after space')
        assert_equal(sol('   Hello John  how are you   '), 'you are how John Hello')
        assert_equal(sol('1'), '1')
        print("ALL TEST CASES PASSED")


# Run and test
if __name__ == '__main__':
    t = ReversalTest()
    t.test(rev_word_szi)
    t.test(rev_word3)
