import sys

max_int = 2 ** 31 - 1


class Solution(object):

    def rev_positive(self, x):
        r = 0
        while x // 10 > 0:
            a = x % 10
            x = x // 10
            r = r * 10 + a
        r = r * 10 + x
        if r > max_int:
            r = 0
        return r

    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < 0:
            return -1 * self.rev_positive(-x)
        else:
            return self.rev_positive(x)

print(Solution().reverse(123))