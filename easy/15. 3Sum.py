from model.util import *


class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        ret_list = []

        for i, n in enumerate(nums):
            t = 0 - n

            p = 0
            q = i - 1
            while p < q and p < i and q >= 0:
                s = nums[p] + nums[q]
                if s == t:
                    ret_list.append([nums[p], nums[q], n])
                    while p + 1 < i and nums[p] == nums[p + 1]:
                        p += 1
                    p += 1
                    while q - 1 >= 0 and nums[q] == nums[q - 1]:
                        q -= 1
                    q -= 1
                elif s > t:
                    q -= 1
                else:
                    p += 1


        return ret_list

p(Solution().threeSum([-1, 0, 1, 2, -1, -4]))
