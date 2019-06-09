from model.util import *


class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ret = [0] * 64
        r = 0
        for i in range(64):
            a = 0
            b = 0
            for n in nums:
                if n < 0:
                    n = -n
                x = n >> i
                x &= 1
                if x == 1:
                    a += 1
                else:
                    b += 1
            if a % 3 == 1:
                ret[i] = 1
        for i, bit in enumerate(ret):
            if bit == 1:
                r |= (bit << i)
        neg = 0
        for n in nums:
            if n < 0:
                neg += 1
        if neg % 3 == 1:
            return -r
        return r
p(Solution().singleNumber([-2,-2,1,1,-3,1,-3,-3,-4,-2]))


