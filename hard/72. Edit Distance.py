from model.util import *


class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        M = len(word1) + 1
        N = len(word2) + 1
        if M == N and N == 1:
            return 0
        if M == N and M == 2 and word1[0] == word2[0]:
            return 0
        if M <= 2 or N <= 2:
            return 1
        mat = [[0] * N for i in range(M)]
        for i in range(M):
            mat[i][0] = i
        for i in range(N):
            mat[0][i] = i
        for i in range(1, M):
            for j in range(1, N):
                if word1[i - 1] == word2[j - 1]:
                    mat[i][j] = min(mat[i - 1][j - 1], mat[i][j - 1] + 1, mat[i - 1][j] + 1)
                else:
                    mat[i][j] = min(mat[i - 1][j - 1] + 1, mat[i][j - 1] + 1, mat[i - 1][j] + 1)

        return mat[M - 1][N - 1]

p(Solution().minDistance("intention", "execution"))
