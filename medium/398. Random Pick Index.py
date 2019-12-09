import random
def bisec_left(nums, t):
    ret = -1
    if not nums:
        return ret
    p, q = 0, len(nums) - 1
    while p <= q:
        mid = (p + q) // 2
        if nums[mid][0] == t:
            ret = mid
            if mid == 0 or nums[mid - 1][0] < t:
                break
            q = mid - 1
        elif nums[mid][0] < t:
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
        if nums[mid][0] == t:
            ret = mid
            if mid == len(nums) - 1 or nums[mid + 1][0] > t:
                break
            p = mid + 1
        elif nums[mid][0] < t:
            p = mid + 1
        else:
            q = mid - 1
    return ret

class Solution(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = [(x, i) for i, x in enumerate(nums)]
        self.nums.sort(key=lambda x : x[0])

    def pick(self, target):
        """
        :type target: int
        :rtype: int
        """
        left = bisec_left(self.nums, target)
        right = bisec_right(self.nums, target)
        r = random.randint(left, right)
        return self.nums[r][1]


x = [0, 1, 2, 2, 2, 3]
r = bisec_left(x, 2)
print(r)
r = bisec_right(x, 2)
print(r)