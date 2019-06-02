
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
        node = max_node = (0, 0, 0)
        for i, n in enumerate(nums):
            if i == 0:
                node = (n, 0, 0)
                max_node= node
                continue
            if n > node[0] + n:
                node = (n, i, i)
            else:
                node = (node[0] + n, node[1], i)
            if node[0] > max_node[0]:
                max_node = node

        return max_node[0]

p(Solution().maxSubArray([-2,1,-3,4,- 1,2,1,-5,4]))