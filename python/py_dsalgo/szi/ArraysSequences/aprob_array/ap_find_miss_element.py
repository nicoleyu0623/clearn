'''
Problem

Consider an array of non-negative integers. A second array is formed by shuffling the elements of the first array and deleting a random element. Given these two arrays, find which element is missing in the second array.

Here is an example input, the first array is shuffled and the number 5 is removed to construct the second array.

Input:

finder([1,2,3,4,5,6,7],[3,7,2,1,4,6])
Output:

5 is the missing number
'''

## O(n)
def finder_szi(arr1,arr2):
    if len(arr1)-len(arr2) != 1:
        return Exception('Difference between array 1 and array 2 is more than 1 element')

    #fill the counter
    cnt={}
    for x in arr1:
        if x in cnt:
            cnt[x] += 1
        else:
            cnt[x] = 1

    #unfill the counter
    for y in arr2:
        cnt[y] -= 1

    #find key with non-zero value
    for k in cnt.keys():
        if cnt[k] == 1:
            break
    return k


##################################
## also O(n)  ##proposed by author
import collections
def finder2(arr1, arr2):
    # Using default dict to avoid key errors
    d = collections.defaultdict(int)  #if a key does not exist, it is inserted automatically
    #d = {}
    # Add a count for every instance in Array 1
    for num in arr2:
        d[num] += 1

        # Check if num not in dictionary
    for num in arr1:
        if d[num] == 0:
            return num
            # Otherwise, subtract a count
        else:
            d[num] -= 1

"""
RUN THIS CELL TO TEST YOUR SOLUTION
"""
from nose.tools import assert_equal


class TestFinder(object):

    def test(self, sol):
        assert_equal(sol([5, 5, 7, 7], [5, 7, 7]), 5)
        assert_equal(sol([1, 2, 3, 4, 5, 6, 7], [3, 7, 2, 1, 4, 6]), 5)
        assert_equal(sol([9, 8, 7, 6, 5, 4, 3, 2, 1], [9, 8, 7, 5, 4, 3, 2, 1]), 6)
        print('ALL TEST CASES PASSED')


# Run test
t = TestFinder()
t.test(finder_szi)
t.test(finder2)






