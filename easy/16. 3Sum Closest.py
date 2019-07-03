from model.util import *

def sort_list_maopao(nums):
    N = len(nums)
    if N <= 1:
        return
    for i in range(N):
        flag = False
        for j in range(N - 1):
            if nums[j] > nums[j + 1]:
                nums[j + 1], nums[j] = nums[j], nums[j + 1]
                flag = True

        if not flag:
            return
class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        r = 0
        diff = 2**32
        # nums.sort()
        sort_list_maopao(nums)
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