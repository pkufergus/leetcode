# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7

class Solution(object):
    def rand10(self):
        """
        :rtype: int
        """

        s  = 0
        for i in range(10):
            s += rand7()
        return s % 10 + 1