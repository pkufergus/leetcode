from model.util import *

class Solution(object):

    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        p, q = 0, len(matrix) - 1
        ln = -1
        if q < 0:
            return False
        if len(matrix[0]) < 1:
            return False
        while p <= q:
            m = (p + q) // 2

            mv = matrix[m][0]
            if mv <= target and matrix[m][-1] >= target:
                ln = m
                break
            elif mv > target:
                q = m - 1
            else:
                p = m + 1
        if ln < 0:
            return False

        p, q = 0, len(matrix[ln]) - 1
        while p <= q:
            m = (p + q) // 2
            mv = matrix[ln][m]
            if mv == target:
                return True
            if mv > target:
                q = m - 1
            else:
                p = m + 1
        return False

p(Solution().searchMatrix([
  [1],
], 1))