from model.util import *


class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        i, j, k = 0, 0, len(nums) - 1
        if k < 1:
            return None
        while k >= 0 and nums[k] == 2:
            k -= 1
        while j <= len(nums) - 1 and nums[j] == 0:
            j += 1
        while i <= len(nums) - 1 and nums[i] == 0:
            i += 1
        while j < len(nums) and j <= k:
            if nums[j] == 0:
                if i == j:
                    i += 1
                    j += 1
                else:
                    nums[i], nums[j] = nums[j], nums[i]
                    i += 1
            elif nums[j] == 2:
                nums[k], nums[j] = nums[j], nums[k]
                k -= 1
                if nums[j] == 0:
                    if i == j:
                        i += 1
                        j += 1
                    else:
                        nums[i], nums[j] = nums[j], nums[i]
                        i += 1
            while k >= 0 and nums[k] == 2:
                k -= 1
            while j <= len(nums) - 1 and nums[j] == 1:
                j += 1
        return None

p(Solution().sortColors([2, 0, 0]))

