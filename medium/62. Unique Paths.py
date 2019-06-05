from model.util import *


class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        a = [[0]*n for i in range(m)]
        for i in range(n):
            a[0][i] = 1
        for i in range(m):
            a[i][0] = 1

        for i in range(1, m):
            for j in range(1, n):
                a[i][j] = a[i][j - 1] + a[i - 1][j]
        return a[m - 1][n - 1]

p(Solution().uniquePaths(7, 3))
