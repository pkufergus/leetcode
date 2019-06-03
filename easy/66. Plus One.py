import sys

debug=1

def p(s):
    try:
        if debug == 1:
            if isinstance(s, str):
                print(s)
            elif isinstance(s, list):
                print(map(str, s))
    except:
        pass

class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] + 1 < 10:
                digits[i] = digits[i] + 1
                return digits
            else:
                digits[i] = 0
        digits[0] = 1
        digits.append(0)
        return digits

p(Solution().plusOne([0]))
p(Solution().plusOne([9]))
