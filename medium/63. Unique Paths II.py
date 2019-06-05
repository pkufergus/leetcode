from model.util import *


class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        a = [[0] * n for i in range(m)]
        if obstacleGrid[0][0]:
            return 0
        a[0][0] = 1
        for i in range(1, n):
            a[0][i] = 0 if obstacleGrid[0][i] or a[0][i - 1] == 0 else 1
        for i in range(1, m):
            a[i][0] = 0 if obstacleGrid[i][0] or a[i - 1][0] == 0 else 1

        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j]:
                    a[i][j] = 0
                else:
                    a[i][j] = a[i][j - 1] + a[i - 1][j]

        return a[m - 1][n - 1]

# p(Solution().uniquePathsWithObstacles([[0,0,0],[0,1,0],[0,0,0]]))
p(Solution().uniquePathsWithObstacles([[0,0],[1,1],[0,0]]))
