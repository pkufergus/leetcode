from model.util import *


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        N = len(prices)
        if N <= 1:
            return 0

        a = [0] * (N + 1)
        max_price = prices[N - 1]
        min_price = prices[N - 1]
        for i in range(N - 2, -1, -1):
            a[i] = max(a[i + 1], max_price - prices[i])
            max_price = max(max_price, prices[i])
        max_price = prices[0]
        min_price = prices[0]
        max_profit = 0
        p = 0
        for i in range(1, N):
            p = max(p, prices[i] - min_price)
            min_price = min(min_price, prices[i])
            max_profit = max(max_profit, p + a[i + 1])
        return max_profit

p(Solution().maxProfit( [3,3,5,0,0,3,1,4]))