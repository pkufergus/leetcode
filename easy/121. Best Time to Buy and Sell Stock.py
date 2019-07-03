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

        min_p = prices[0]
        max_profit = 0
        for i in range(1, N):
            max_profit = max(max_profit, prices[i] - min_p)
            min_p = min(min_p, prices[i])

        return max_profit
p(Solution().maxProfit([7,6,4,3,1,10]))