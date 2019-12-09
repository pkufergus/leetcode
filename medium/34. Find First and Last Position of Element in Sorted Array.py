
def bisec_left(nums, t):
    ret = -1
    if not nums:
        return ret
    p, q = 0, len(nums) - 1
    while p <= q:
        mid = (p + q) // 2
        if nums[mid] == t:
            ret = mid
            if mid == 0 or nums[mid - 1] < t:
                break
            q = mid - 1
        elif nums[mid] < t:
            p = mid + 1
        else:
            q = mid - 1
    return ret

def bisec_right(nums, t):
    ret = -1
    if not nums:
        return ret
    p, q = 0, len(nums) - 1
    while p <= q:
        mid = (p + q) // 2
        if nums[mid] == t:
            ret = mid
            if mid == len(nums) - 1 or nums[mid + 1] > t:
                break
            p = mid + 1
        elif nums[mid] < t:
            p = mid + 1
        else:
            q = mid - 1
    return ret

class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if not nums:
            return [-1, -1]
        left = bisec_left(nums, target)
        if left < 0:
            return [-1, -1]
        right = bisec_right(nums, target)
        return [left, right]