from model.util import *


class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        i, j = 0, len(numbers) - 1
        while i < j:
            s = numbers[i] + numbers[j]
            if s == target:
                break
            elif s > target:
                j -= 1
            else:
                i += 1
        return [i + 1, j + 1]

p(Solution().twoSum([-6, 2,7,11,15], 5))