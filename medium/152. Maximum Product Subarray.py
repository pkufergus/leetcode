from model.util import *


class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        ret = nums[0]
        neg_ret = nums[0]
        max_ret = ret
        for i in range(1, n):
            last_ret = ret
            ret = max(nums[i], nums[i] * ret, nums[i] * neg_ret)
            neg_ret = min(nums[i], nums[i] * last_ret, nums[i] * neg_ret)
            max_ret = max(max_ret, ret)
        return max_ret

p(Solution().maxProduct([2,3,-2,4, -3, -4]))


