from model.util import *

class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        r = 0
        diff = 2**32
        nums.sort()
        for i, n in enumerate(nums):
            t = target - n

            p = 0
            q = i - 1
            while p < q and p < i and q >= 0:
                s = nums[p] + nums[q]
                d = abs(s - t)
                if d < diff:
                    r = nums[p] + nums[q] + n
                    diff = d
                if s == t:
                    return r
                elif s > t:
                    q -= 1
                else:
                    p += 1

        return r

p(Solution().threeSumClosest([-1, 2, 1, -4], 1))