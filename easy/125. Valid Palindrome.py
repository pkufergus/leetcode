import sys

debug=1

def p(s):
    try:
        if debug == 1:
            print(s)
    except:
        pass

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        i, j = 0, len(s) - 1
        while i < j and j >= 0 and i < len(s):
            a = s[i]
            b = s[j]
            if a.isalnum() and b.isalnum():
                if a.lower() == b.lower():
                    i += 1
                    j -= 1
                    continue
                else:
                    return False
            else:
                if not a.isalnum():
                    i += 1
                if not b.isalnum():
                    j -= 1
        return True

p(Solution().isPalindrome("0P"))