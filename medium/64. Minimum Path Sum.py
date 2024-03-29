from model.util import *


class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        if m < 1:
            return 0
        n = len(grid[0])
        dp = [0] * n

        dp[0] = grid[0][0]
        for i in range(1, n):
            dp[i] = grid[0][i] + dp[i - 1]
        for i in range(1, m):
            dp[0] = grid[i][0] + dp[0]
            for j in range(1, n):
                dp[j] = grid[i][j] + min(dp[j], dp[j - 1])

        return dp[n - 1]

p(Solution().minPathSum([
  [1,3,1],
  [1,5,1],
  [4,2,1]
]))