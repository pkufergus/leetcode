
import sys

debug=1

def p(s):
    try:
        if debug == 1:
            print(s)
    except:
        pass

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        node = max_node = 0
        for i, n in enumerate(nums):
            if i == 0:
                node = n
                max_node= node
                continue
            if n > node + n:
                node = n
            else:
                node = node + n
            if node > max_node:
                max_node = node

        return max_node

p(Solution().maxSubArray([-2,1,-3,4,- 1,2,1,-5,4]))