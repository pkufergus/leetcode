from model.util import *

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if len(height) < 2:
            return 0
        area = 0
        i, j = 0, len(height) - 1
        while i < j:
            a = (j - i) * min(height[i], height[j])
            area = a if a > area else area
            if height[i] < height[j]:
                i += 1
                while i < j:
                    if height[i] > height[i - 1]:
                        break
                    i += 1
                a = (j - i) * min(height[i], height[j])
                area = a if a > area else area
            else:
                j -= 1
                while j > i:
                    if height[j] > height[j + 1]:
                        break
                    j -= 1
                a = (j - i) * min(height[i], height[j])
                area = a if a > area else area

        return area

p(Solution().maxArea([1,2,3,4,5,25,24,3,4]))