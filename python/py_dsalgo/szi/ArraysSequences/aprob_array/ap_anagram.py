'''
Problem
Given two strings, check to see if they are anagrams. An anagram is when the two strings can be written using the exact same letters (so you can just rearrange the letters to get a different phrase or word).

For example:

"public relations" is an anagram of "crap built on lies."

"clint eastwood" is an anagram of "old west action"
Note: Ignore spaces and capitalization. So "d go" is an anagram of "God" and "dog" and "o d g".

szi initial though

count distinct chars in 2 strings  if 2 dictionaries are equal we have an anagram
'''
from pprint import pprint as pp


# solution 1 with sorting strings
def anagram1(s1, s2):
    #remove spaces and put put all charts to lowercase
    s1=s1.replace(' ', '').lower()
    s2=s2.replace(' ', '').lower()


    #we can compare sorted s1 and s2 and if they are same it's a solution
    return sorted(s1) == sorted(s2)

############################################################
# solution with counting chars. Classic, expected solution
############################################################
def anagram2(s1, s2):
    #remove spaces and put put all charts to lowercase
    s1=s1.replace(' ', '').lower()
    s2=s2.replace(' ', '').lower()

    #easy out
    if len(s1) != len(s2):
        return False
    #dictionary
    cnt = {}
    for c in range(len(s1)):
        if c in cnt:
            cnt[c] += 1
        else:
            cnt[c] = 1
    #check s2 with cnt, if the char is found decrease counter
    for c in range(len(s2)):
        if c in cnt:
            cnt[c] -= 1
        else:
            cnt[c] = 1
    #now check if all values in dictionary are at 0
    for k in cnt.keys():
        if cnt[k] != 0:
            return False

    return True

# solution which szi initially thoght
def anagram3(s1, s2):
    #remove spaces and put put all charts to lowercase
    s1=s1.replace(' ', '').lower()
    s2=s2.replace(' ', '').lower()


    #dictionary 1
    cnt1 = {}
    for c in range(len(s1)):
        if c in cnt1:
            cnt1[c] += 1
        else:
            cnt1[c] = 1

    #dictionary 2
    cnt2 = {}
    for c in range(len(s2)):
        if c in cnt2:
            cnt2[c] += 1
        else:
            cnt2[c] = 1

    #easy use-case returning false
    if len(cnt1) != len(cnt2):
        return False

    for k in cnt1.keys():
       if cnt1[k] != cnt2[k]:
           return False

    return True

## testing he solution
from nose.tools import assert_equal
class AnagramTest(object):
     def test(self,sol):
         assert_equal(sol('abc', 'cba'), True)
         assert_equal(sol('public relations','crap built on lies'), True)
         print('all tests Passed')

#run Tests
t = AnagramTest()
t.test(anagram1)
t.test(anagram2)
t.test(anagram3)