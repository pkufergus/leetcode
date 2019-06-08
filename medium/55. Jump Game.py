from model.util import *


class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) < 2:
            return True
        a=[0]*len(nums)
        for i, n in enumerate(nums):
            if i == 0:
                a[i] = n
            else:
                a[i] = max(i + n, a[i - 1])
            if a[i] == i:
                break
        if a[-1] == 0:
            return False
        return True


p(Solution().canJump([3,2,1,0,4]))