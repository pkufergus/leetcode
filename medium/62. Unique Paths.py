from model.util import *


class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        if m < 1 or n < 1:
            return 0
        a = [1] * n
        for i in range(1, m):
            for j in range(1, n):
                a[j] = a[j - 1] + a[j]
        return a[n - 1]

p(Solution().uniquePaths(7, 3))
