from model.util import *


class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """

        if not matrix:
            return matrix
        m, n = len(matrix), len(matrix[0])
        flag = 2**32
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    for k in range(n):
                        if k != j and matrix[i][k] != 0:
                            matrix[i][k] = flag
                    for k in range(m):
                        if k != i and matrix[k][j] != 0:
                            matrix[k][j] = flag
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == flag:
                    matrix[i][j] = 0
        return None
