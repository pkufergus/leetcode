from model.util import *

class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        N = len(heights)
        if N < 1:
            return 0
        if N == 1:
            return heights[0]
        max_area = heights[0]
        last_w = 1
        for i in range(1, N):
            a = heights[i]
            b = heights[i - 1]
            if a < b:
                last_w = last_w + 1
                area = a * last_w
                max_area = max(max_area, area)
            else:


        return area

p(Solution().largestRectangleArea([2,1,5,6,2,3,2,2,2,3,3]))