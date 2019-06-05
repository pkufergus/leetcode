import sys

debug=1

def p(s):
    try:
        if debug == 1:
            print(s)
    except:
        pass

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) < 2:
            return 0
        max_profit = 0
        for i in range(1, len(prices)):
            last_item = prices[i - 1]
            if prices[i] > prices[i - 1]:
                max_profit += (prices[i] - prices[i - 1])
        return max_profit

p(Solution().maxProfit([7,6,4,3,1]))
