from model.util import *


class Solution(object):
    def maximumGap(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        N = len(nums)
        if N <= 1:
            return 0
        max_n, min_n = nums[0], nums[0]

        for n in nums:
            max_n = max(max_n, n)
            min_n = min(min_n, n)
        for i in range(N):
            nums[i] = nums[i] - min_n
        max_n = max_n - min_n
        max_gap = 0
        step = max_n // N + 1
        b = [ [] for i in range(N)]
        for n in nums:
            k = n // step
            if not b[k]:
                b[k].append(n)
            elif len(b[k]) == 1:
                b[k].append(max(b[k][0], n))
                b[k][0] = min(b[k][0], n)
            else:
                b[k][0] = min(b[k][0], n)
                b[k][1] = max(b[k][1], n)
        left_n = 0
        left_n = b[0][1] if len(b[0]) == 2 else b[0][0]
        for k in range(1, N):
            if b[k]:
                if len(b[k]) == 1:
                    right_n = new_left_n = b[k][0]
                else:
                    right_n = b[k][0]
                    new_left_n = b[k][1]
                diff = right_n - left_n
                max_gap = max(max_gap, diff)
                left_n = new_left_n
        return max_gap

p(Solution().maximumGap([0,4,5,10,16]))


