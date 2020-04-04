'''
Problem

Given an array of integers (positive and negative) find the largest continuous sum.

i.e. find subarray in array whos elements make a largest  sum

large_cont_sum([1,2,-1,3,4,10,10,-10,-1])   is 29
large_cont_sum[1,2,-1,3,4,-1]),9
'''
########################
# solution by jmportilla more intuitive
#########################
def large_cont_sum(arr):
    #edge case
    if len(arr)==0:
        return 0
    c_sum = arr[0]
    max_sum = c_sum
    for x in arr[1:]:  #loop from 2nd element
        c_sum = max(c_sum+x, x)  # current sum is the biggest from previous c_sum and curr element
        max_sum = max(max_sum, c_sum)  #keep track of the largest current sum
    return max_sum

import sys
def large_cont_sum_geek4geeksol(arr):
    max_so_far = -sys.maxsize
    max_ending_here = 0
    for x in arr:
        max_ending_here += x    #increment max_ending_here (c_sum)  by x
        if max_so_far < max_ending_here:
                max_so_far = max_ending_here  #keep track of largest sum
        if max_ending_here  < 0: #if large negative element puts c_sum into negative set it to zero
            max_ending_here = 0
    return max_so_far



from nose.tools import assert_equal

class LargeContTest(object):
    def test(self, sol):
        assert_equal(sol([1, 2, -1, 3, 4, -1]), 9)
        assert_equal(sol([-2,-3,4,-1,-2,1,5,-3]), 7)
        assert_equal(sol([1, 2, -1, 3, 4, 10, 10, -10, -1]), 29)
        assert_equal(sol([-1, 1]), 1)
        print('All tests passed')


# Run Test
if __name__ == '__main__':
    t = LargeContTest()
    t.test(large_cont_sum)
    t.test(large_cont_sum_geek4geeksol)
