from model.util import *


class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        N = len(ratings)
        if N <= 1:
            return N

        c = [0] * N
        for i in range(N):
            if i == 0:
                if ratings[i] <= ratings[i + 1]:
                    c[i] = 1
                continue
            if i == N - 1:
                if ratings[i] <= ratings[i - 1]:
                    c[i] = 1
                continue
            if ratings[i] <= ratings[i + 1] and ratings[i] <= ratings[i - 1]:
                c[i] = 1
        for i in range(1, N):
            if ratings[i] > ratings[i - 1]:
                c[i] = c[i - 1] + 1
                continue
        for i in range(N - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                c[i] = max(c[i], c[i + 1] + 1)

        return sum(c)
p(Solution().candy([1,2,2]))
