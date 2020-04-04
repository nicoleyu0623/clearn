'''
Problem

Given an integer array, output all the * *unique ** pairs that sum up to a specific value k.

So the input:

pair_sum([1,3,2,2],4)
would return 2 pairs:

 (1,3)
 (2,2)
NOTE: FOR TESTING PURPOSES CHANGE YOUR FUNCTION SO IT OUTPUTS THE NUMBER OF PAIRS
'''
from pprint import pprint as pp

# O(n^2)
def pair_sum_szi(arr,k):
    #keep only unique elements in arr
    urr=[]
    for e in arr:
        if e not in urr:
            urr.append(e)

    pairs=[]
    #do n * n/2 scan
    for i in range(0,len(urr)):
        for j in range(i,len(urr)):
            if urr[i] + urr[j] == k:
                pairs.append((urr[i],urr[j]))

    #return (pairs)
    return len(pairs)

############################################################
# solution with sets chars. Classic, expected solution
############################################################
def pair_sum(arr, k):
    if len(arr) < 2:
        return

    # Sets for tracking
    seen = set()
    output = set()

    # For every number in array
    for num in arr:

        # Set target difference
        target = k - num

        # Add it to set if target hasn't been seen
        if target not in seen:
            seen.add(num)
            #pp('deb num:{} target:{} adding num to seen..seen set:{}'.format(num,target,seen))

        else:
            # Add a tuple with the corresponding pair
            output.add((min(num, target), max(num, target)))
            #pp('deb num:{} target:{} adding to output..'.format(num, target))
    # FOR TESTING
    return len(output)

#test result
from nose.tools import assert_equal
class TestPair(object):

    def test(self, sol):
        assert_equal(sol([1, 9, 2, 8, 3, 7, 4, 6, 5, 5, 13, 14, 11, 13, -1], 10), 6)
        assert_equal(sol([1, 2, 3, 1], 3), 1)
        assert_equal(sol([1, 3, 2, 2], 4), 2)
        assert_equal(sol([0,1,2,3,3,4,5,6],6),4)
        print('ALL TEST CASES PASSED')

# Run tests
t = TestPair()
t.test(pair_sum_szi)
t.test(pair_sum)

