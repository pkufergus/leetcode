
from model.util import *


class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums_size = len(nums)
        i = 0
        while i < nums_size:
            n = nums[i]
            if n >= nums_size or n <= 0:
                i += 1
                continue
            if n == i + 1 or n == nums[n - 1]:
                i += 1
            else:
                nums[i], nums[n - 1] = nums[n - 1], n
        i = 0
        while i < nums_size:
            if i != nums[i] - 1:
                break
            i += 1
        return i + 1

p(Solution().firstMissingPositive([1, 1]))



