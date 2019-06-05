from model.util import *


class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        flag = 0
        i, j = 0, len(nums) - 1
        if j < 0:
            return -1
        if j == 0:
            return j if nums[j] == target else -1
        while i < j:
            if target == nums[i]:
                return i
            if target == nums[j]:
                return j
            if i + 1 == j:
                return -1
            if nums[i] < nums[j]:
                flag = 0
            else:
                flag = 1
            mid = (i + j) // 2
            m = nums[mid]
            if m == target:
                return mid
            if m > nums[i]:
                if m > target:
                    if flag and target < nums[j]:
                        i = mid
                    else:
                        j = mid
                else:
                    i = mid
            else:
                if m > target:
                    j = mid
                else:
                    if flag and target < nums[j]:
                        i = mid
                    else:
                        j = mid
        return -1

p(Solution().search([2,3,4,5,6,7,8,9,1],3))




