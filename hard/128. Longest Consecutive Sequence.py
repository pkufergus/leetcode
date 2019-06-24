from model.util import *

class Node():
    def __init__(self, a, b):
        self.s = a
        self.e = b

class Solution(object):


    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        N = len(nums)
        if N <= 1:
            return N

        m = {}
        for n in nums:
            if n in m:
                continue
            if not n + 1 in m and not n - 1 in m:
                m[n] = Node(n, n)
                continue
            if n + 1 in m and n - 1 in m:
                ls = m[n - 1].s
                le = m[n - 1].e
                rs = m[n + 1].s
                re = m[n + 1].e

                m[n - 1].e = re
                m[n + 1].s = ls
                m[ls] = m[re] = m[n] = m[n + 1]

                continue
            if n + 1 in m:
                m[n + 1].s = n
                m[n] = m[n + 1]
            if n - 1 in m:
                m[n - 1].e = n
                m[n] = m[n - 1]

        max_len = 0
        for k in m:
            max_len = max(max_len, m[k].e - m[k].s + 1)

        return max_len

p(Solution().longestConsecutive([0,3,7,2,5,8,4,6,0,1]))



