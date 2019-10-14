'''
Problem Statement

Given a string of opening and closing parentheses, check whether it’s balanced.
We have 3 types of parentheses: round brackets: (), square brackets: [], and curly brackets: {}.
Assume that the string doesn’t contain any other character than these, no spaces words or numbers.
As a reminder, balanced parentheses require every opening parenthesis to be closed in
the reverse order opened. For example ‘([])’ is balanced but ‘([)]’ is not.

You can assume the input string has no spaces.
'''

##################
# author solution
##################

def balance_check(s):
    # Check is even number of brackets
    if len(s) % 2 != 0:
        return False

    # Set of opening brackets
    opening = set('([{')

    # Matching Pairs
    matches = set([('(', ')'), ('[', ']'), ('{', '}')])

    # Use a list as a "Stack"
    stack = []

    # Check every parenthesis in string
    for cc in s:

        # If its an opening, append it to list
        if cc in opening:
            stack.append(cc)  #stack contains only opening brackets

        else:

            #here we check only closing brackets
            if len(stack) == 0:  #edge case if string contains only closing brackets
                return False

            # Check the last open parenthesis
            last_open = stack.pop()  #get the top from stack

            # Check if it has a closing match
            if (last_open, cc) not in matches:    #this ensures that [()] matches and [)(] does not
                return False

    return len(stack) == 0


from nose.tools import assert_equal


class TestBalanceCheck(object):

    def test(self, sol):
        assert_equal(sol('({})'),True)
        assert_equal(sol('[{(})]'),False)
        assert_equal(sol('[](){([[[]]])}('), False)
        assert_equal(sol('[{{{(())}}}]((()))'), True)
        assert_equal(sol('[[[]])]'), False)
        assert_equal(sol('}{'), False)
        print('ALL TEST CASES PASSED')


# Run Tests
if __name__ == '__main__':
    t = TestBalanceCheck()
    t.test(balance_check)