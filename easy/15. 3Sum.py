from model.util import *


class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        ret_list = []
        map_list = {}

        for i, n in enumerate(nums):
            t = 0 - n

            p = 0
            q = i - 1
            while p < q and p < i and q >= 0:
                s = nums[p] + nums[q]
                if s == t:
                    r = [nums[p], nums[q], n]
                    r_str = "{},{},{}".format(r[0], r[1], r[2])
                    if not r_str in map_list:
                        ret_list.append([nums[p], nums[q], n])
                        map_list[r_str] = 1
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

p(Solution().threeSum([0,0,0,0]))
