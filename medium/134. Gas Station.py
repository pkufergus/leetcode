from model.util import *

class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        sum = 0
        left = 0
        label = 0
        next = 0
        for i in range(len(gas)):
            d = gas[i] - cost[i]
            if d >= 0:
                if i == 0 or next == 1:
                    label = i
                    left = d
                    next = 0
                    continue
            left += d
            if left < 0:
                next = 1
                sum += left
                left = 0
        if sum + left >= 0:
            return label
        else:
            return -1
# p(Solution().canCompleteCircuit([1,2,3,4,5], [3,4,5,1,2]))
p(Solution().canCompleteCircuit([2,3,4], [3,4,3]))
