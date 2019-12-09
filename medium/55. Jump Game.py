from model.util import *


class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) < 2:
            return True
        k = 0
        for i, n in enumerate(nums):
            if k < i:
                return False
            if i == 0:
                k = n
            else:
                k = max(i + n, k)

        return True

p(Solution().canJump([2,0,0]))