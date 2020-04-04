'''
Problem¶

Given a string,determine if it is compreised of all unique characters.
 For example, the string 'abcde' has all unique characters and should return True.
  The string 'aabcde' contains duplicate characters and should return false.
'''


#O(n)
def uni_char_szi(s):
    if len(s) == 0:
        return True
    seen={}
    for c in s:
        if c not in seen:
            seen[c] = 1
        else:
            return False
    return True

#O(n^2) timeit  x 10 slower
def uni_char_szi_n2(s):
    if len(s) == 0:
        return True
    seen=[s[0]]
    for i in range(1,len(s)):
        for j in range(len(seen)):
            if s[i] == seen[j]:
                return False
        seen.append(s[i])
    return True


from nose.tools import assert_equal


class TestUnique(object):

    def test(self, sol):
        assert_equal(sol(''), True)
        assert_equal(sol('goo'), False)
        assert_equal(sol('abcdefg'), True)
        print('ALL TEST CASES PASSED')


# Run Tests
if __name__ == '__main__':
    t = TestUnique()
    t.test(uni_char_szi)
    t.test(uni_char_szi_n2)


