from model.util import *


class Solution(object):
    def findpos(self, nums, p, q, target):

        while p < q:
            m = (p + q) // 2
            m_n = nums[m]
            if m_n == target:
                return m
            if m_n > target:
                q = m
            else:
                p = m
            if p + 1 <= q and nums[p] < target and target < nums[p + 1]:
                return p
        return p

    def findkth(self, nums1, nums2, p1, q1, p2, q2, t):
        if t == 1:
            return nums1[p1] if nums1[p1] < nums2[p2] else nums2[p2]

        if nums2[p2] >= nums1[q1]:
            if t <= (q1 - p1) + 1:
                return nums1[p1 + t - 1]
            else:
                return nums2[p2 + t - ((q1 - p1) + 1) - 1]
        if nums1[p1] >= nums2[q2]:
            return self.findkth(nums2, nums1, p2, q2, p1, q1, t)

        if nums1[p1] <= nums2[p2]:
            pos = self.findpos(nums1, p1, q1, nums2[p2])
            if t <= (pos - p1) + 1:
                return nums1[p1 + t - 1]
            else:
                return self.findkth(nums1, nums2, pos + 1, q1, p2, q2, t - ((pos - p1) + 1))
        else:
            return self.findkth(nums2, nums1, p2, q2, p1, q1, t)


    def medium(self,nums):
        if len(nums) % 2 == 0:
            t = len(nums) // 2
            t1 = nums[t - 1]
            t2 = nums[t]
            return (t1 + t2)*1.0/2
        else:
            return nums[len(nums) // 2]

    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        if len(nums1) == 0:
            return self.medium(nums2)
        elif len(nums2) == 0:
            return self.medium(nums1)
        if (len(nums1) + len(nums2)) % 2 == 0:
            t = (len(nums1) + len(nums2)) // 2
            tval = self.findkth(nums1, nums2, 0, len(nums1) - 1, 0, len(nums2) - 1, t)
            tval2 = self.findkth(nums1, nums2, 0, len(nums1) - 1, 0, len(nums2) - 1, t + 1)
            return (tval + tval2) * 1.0/2
        else:
            t = (len(nums1) + len(nums2)) // 2 + 1
            tval = self.findkth(nums1, nums2,0, len(nums1) - 1, 0, len(nums2) - 1, t)
            return tval

# p(Solution().findMedianSortedArrays([1, 2, 9, 10, 11],[3, 4, 5, 6, 7, 8]))
p(Solution().findMedianSortedArrays([1, 2],[1, 2]))
# p(Solution().findMedianSortedArrays([4],[1,2,3,5,6]))
# p(Solution().findMedianSortedArrays([1, 2, 3],[4,5, 6,7,8,9]))
# p(Solution().findMedianSortedArrays([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22],[0, 6]))
