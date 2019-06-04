from model.util import *

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        d = {}
        p = 0
        q = 0
        size = 0
        for ch in s:
            if ch in d:
                pos = d[ch]
                if pos >= p:
                    p = pos + 1
                d[ch] = q
                q += 1
                size = q - p if (q - p) > size else size
            else:
                d[ch] = q
                q += 1
                size = q - p if (q - p) > size else size
        return size

p(Solution().lengthOfLongestSubstring("pwwkew"))
